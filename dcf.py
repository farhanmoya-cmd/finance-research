#!/usr/bin/env python3
"""finance-research skill - Kalkulator Valuasi v2 (pengganti hitung di kepala)

Diterjemahkan & diadaptasi dari modul `scripts/dcf.py` milik skill
equity-research-skill (bahasa Mandarin asli) - logika matematisnya TIDAK
diubah, hanya semua string output dan nama label diterjemahkan ke
Bahasa Indonesia.

Pemakaian:
    python dcf.py --config assumptions.json   # jalankan penuh dari file JSON
    python dcf.py --demo                      # jalankan contoh bawaan untuk self-check

Modul yang tersedia: DCF tiga-fase per skenario, pembobotan probabilitas,
sensitivitas WACC x g, DCF terbalik (reverse DCF), EPV/metode tiga lapis
(Greenwald), EVA/residual income, dekomposisi PVGO, Monte Carlo, kerangka
sizing posisi (EV/rasio asimetri/Kelly-lite), dan label standar sesuai
aturan kalibrasi pra-registrasi.

Field level atas JSON config: price, shares, net_debt, wacc, terminal_g,
scenarios[], sensitivity{}, reverse{}, epv{}, eva{}, pvgo{}, montecarlo{},
range_low, range_high
"""
import argparse, json, math, random, sys

LABELS = ["Sangat Undervalued", "Undervalued", "Wajar", "Overvalued", "Sangat Overvalued"]

def die(msg):
    raise ValueError(f"[Error konfigurasi] {msg}")

def need(d, key, ctx):
    if key not in d:
        die(f"{ctx} tidak memiliki field wajib `{key}`")
    return d[key]

# ---------- Perhitungan inti ----------

def scenario_fcfs(sc, terminal_g):
    """Urutan FCF lengkap periode eksplisit + periode fade, plus revenue tahun terakhir."""
    name = sc.get("name", "?")
    if "fcf" in sc:
        if not isinstance(sc["fcf"], list) or not sc["fcf"]:
            die(f"Skenario {name}: fcf harus berupa array yang tidak kosong")
        fcfs = list(sc["fcf"]); rev = None
    else:
        rev_path, m = need(sc, "revenue", f"Skenario {name}"), need(sc, "fcf_margin", f"Skenario {name}")
        if len(rev_path) != len(m):
            die(f"Skenario {name}: panjang revenue({len(rev_path)}) dan fcf_margin({len(m)}) tidak sama")
        fcfs = [r * mm for r, mm in zip(rev_path, m)]
        rev = rev_path[-1]
    fade, g0 = sc.get("fade_years", 0), sc.get("fade_g_start", terminal_g)
    mm_last = sc["fcf_margin"][-1] if "fcf_margin" in sc else None
    for k in range(fade):
        gr = g0 + (terminal_g - g0) * (k + 1) / fade
        if rev is not None:
            rev *= (1 + gr); fcfs.append(rev * mm_last)
        else:
            fcfs.append(fcfs[-1] * (1 + gr))
    return fcfs, rev

def dcf_value(sc, wacc, g, shares, net_debt):
    if wacc <= g:
        die(f"WACC({wacc}) harus lebih besar dari pertumbuhan perpetual g({g})")
    if shares <= 0:
        die(f"Jumlah saham harus positif (shares={shares})")
    fcfs, _ = scenario_fcfs(sc, g)
    n = len(fcfs)
    pv = sum(f / (1 + wacc) ** (i + 1) for i, f in enumerate(fcfs))
    tv = fcfs[-1] * (1 + g) / (wacc - g)
    ev = pv + tv / (1 + wacc) ** n
    explicit_years = len(sc.get("fcf", sc.get("revenue", [])))
    sh = shares * (1 + sc.get("annual_dilution", 0.0)) ** explicit_years
    tv_share = (tv / (1 + wacc) ** n) / ev if ev else float("nan")
    return {"ev": ev, "equity": ev - net_debt, "per_share": (ev - net_debt) / sh,
            "shares_end": sh, "terminal_fcf": fcfs[-1],
            "exit_pfcf": tv / fcfs[-1] if fcfs[-1] else float("nan"),
            "tv_share": tv_share}

def reverse_dcf(price, shares, net_debt, wacc, g, interim_fcf, steady_margins, base_revenue):
    if wacc <= g:
        die(f"Reverse DCF: WACC({wacc}) harus lebih besar dari g({g})")
    ev = price * shares + net_debt
    n = len(interim_fcf)
    pv_interim = sum(f / (1 + wacc) ** (i + 1) for i, f in enumerate(interim_fcf))
    tv_needed = (ev - pv_interim) * (1 + wacc) ** n
    fcf_req = tv_needed * (wacc - g)
    rows = []
    for m in steady_margins:
        if m <= 0:
            die(f"Reverse DCF: steady_margin harus positif ({m})")
        rev_req = fcf_req / m
        cagr = (rev_req / base_revenue) ** (1 / n) - 1 if base_revenue else None
        rows.append({"margin": m, "revenue_required": rev_req, "implied_cagr": cagr})
    return {"ev": ev, "pv_interim": pv_interim, "fcf_required": fcf_req, "rows": rows}

def calibrate(price, lo, hi):
    """Kalibrasi pra-registrasi (harus identik dengan check_research_output.py
    dan references/valuation-methods.md §9)."""
    if lo > hi:
        die(f"Kalibrasi: range_low({lo}) > range_high({hi})")
    if price < lo * 0.50: return "Sangat Undervalued"
    if price < lo * 0.85: return "Undervalued"
    if price <= hi * 1.15: return "Wajar"
    if price <= hi * 1.50: return "Overvalued"
    return "Sangat Overvalued"

# ---------- EPV / Metode Tiga Lapis (Greenwald) ----------

def epv_value(e, coc, basis='NOPAT', net_debt=0.0, excess_cash=0.0):
    if coc <= 0:
        die("EPV: coc harus positif")
    ev = e / coc
    if basis.upper() == 'NOPAT':
        return {'ev': ev, 'equity': ev - net_debt + excess_cash}
    return {'ev': None, 'equity': ev}

def franchise_growth_value(e, coc, g, roiic, basis='NOPAT', net_debt=0.0, excess_cash=0.0):
    if roiic is None or roiic <= 0 or not (coc > g):
        return None
    v = e * (1 - g / roiic) / (coc - g)
    if basis.upper() == 'NOPAT':
        return {'ev': v, 'equity': v - net_debt + excess_cash}
    return {'ev': None, 'equity': v}

def moat_verdict(ratio):
    if ratio < 1.0:  return 'EPV<nilai aset bersih -> nilai dihancurkan (ROIC<cost of capital), hindari'
    if ratio <= 1.3: return 'EPV~=nilai aset bersih -> bisnis tanpa/lemah moat, kerja keras margin tipis'
    return 'EPV>>nilai aset bersih -> ukuran finansial dari moat (selisih = nilai franchise)'

def run_epv(c):
    basis = c.get('earnings_basis', 'NOPAT')
    e, coc = need(c, 'normalized_earnings', 'epv'), need(c, 'coc', 'epv')
    nd, xc = c.get('net_debt', 0.0), c.get('excess_cash', 0.0)
    sh, av, price = need(c, 'shares', 'epv'), c.get('asset_value'), c.get('price')
    print(f"\n=== Earnings Power Value (EPV) === basis {basis} | laba ternormalisasi {e} | cost of capital(=WACC) {coc:.2%}")
    if basis.upper() != 'NOPAT':
        print("  [catatan] jatuh ke basis laba bersih (coc diperlakukan sebagai cost of equity)")
    ep = epv_value(e, coc, basis, nd, xc)
    epv_ps = ep['equity'] / sh
    print(f"  Nilai ekuitas EPV {ep['equity']:,.1f} | per saham {epv_ps:,.2f}")
    if av:
        ratio = ep['equity'] / av
        print(f"  Verifikasi moat: EPV/nilai aset bersih = {ratio:.2f}x -> {moat_verdict(ratio)}")
    if c.get('asset_series'):
        print("  Tren EPV/nilai aset bersih multi-tahun:")
        for yr, ee, aa in c['asset_series']:
            print(f"    {yr}: {(ee/coc)/aa:.2f}x")
    growth_ps = None
    g = c.get('growth')
    if g:
        gg, roiic, mode = need(g, 'g', 'epv.growth'), g.get('roiic'), g.get('mode', 'franchise')
        fg = franchise_growth_value(e, coc, gg, roiic, basis, nd, xc) if mode == 'franchise' else None
        if fg is None:
            growth_ps = ep['equity'] * (1 + gg) / sh
            print(f"  Nilai pertumbuhan (formula fallback sederhana, g={gg:.1%}): per saham {growth_ps:,.2f}")
        else:
            growth_ps = fg['equity'] / sh
            warn = ' PERINGATAN: ROIIC<coc, pertumbuhan menghancurkan nilai' if roiic < coc else ''
            print(f"  Nilai pertumbuhan (formula franchise ketat, g={gg:.1%}, ROIIC={roiic:.1%}): per saham {growth_ps:,.2f}{warn}")
    if av and price:
        asset_ps = av / sh
        print(f"  Tangga titik beli: nilai lantai {asset_ps:,.2f} | EPV {epv_ps:,.2f}" +
              (f" | penyesuaian pertumbuhan {growth_ps:,.2f}" if growth_ps else ""))
    return {"epv_ps": epv_ps, "growth_ps": growth_ps}

# ---------- EVA / Residual Income ----------

def run_eva(c, top):
    ic = need(c, 'invested_capital', 'eva')
    nopat = need(c, 'nopat', 'eva')
    wacc = c.get('wacc', top.get('wacc'))
    sh = c.get('shares', top.get('shares'))
    nd = c.get('net_debt', top.get('net_debt', 0.0))
    fade = c.get('fade_years', 10)
    growth = c.get('nopat_growth', 0.0)
    rr, roiic = c.get('reinvestment_rate'), c.get('roiic')
    if wacc is None or wacc <= 0: die("eva: wacc tidak valid atau tidak ada")
    if ic <= 0: die("eva: invested_capital harus positif")
    roic = nopat / ic
    spread0 = roic - wacc
    print(f"\n=== EVA / Residual Income === NOPAT {nopat} | Modal diinvestasikan {ic} | ROIC {roic:.1%} | WACC {wacc:.2%} | Excess spread {spread0:+.1%}")
    if rr is not None and roiic is not None:
        g_implied = rr * roiic
        print(f"  Cek konsistensi: g = reinvestment rate {rr:.0%} x ROIIC {roiic:.1%} = {g_implied:.1%}"
              f" (jika pertumbuhan yang diasumsikan di DCF lebih tinggi dari ini, berarti butuh modal eksternal atau asumsi tidak konsisten)")
    pv_eva, ic_t, nopat_t = 0.0, ic, nopat
    for t in range(1, fade + 1):
        spread_t = spread0 * (1 - t / fade)          # excess return meluruh linear ke 0
        nopat_t = nopat_t * (1 + growth)
        ic_t = nopat_t / (wacc + spread_t) if (wacc + spread_t) > 0 else ic_t
        eva_t = spread_t * ic_t
        pv_eva += eva_t / (1 + wacc) ** t
    value = ic + pv_eva
    equity = value - nd
    print(f"  Nilai residual income: Modal diinvestasikan {ic:,.1f} + PV(EVA, peluruhan {fade} tahun) {pv_eva:,.1f} = EV {value:,.1f}")
    if sh:
        print(f"  Ekuitas {equity:,.1f} | per saham {equity/sh:,.2f}")
    if spread0 < 0:
        print("  PERINGATAN: EVA saat ini negatif - perusahaan belum menutup cost of capital, asumsi pertumbuhan apapun hanya memperbesar penghancuran nilai")
    return {"per_share": equity / sh if sh else None}

# ---------- Dekomposisi PVGO ----------

def run_pvgo(c, top):
    e = need(c, 'earnings_ps', 'pvgo')          # laba ternormalisasi per saham (atau FCF/saham)
    r = c.get('r', top.get('wacc'))
    price = c.get('price', top.get('price'))
    if r is None or r <= 0: die("pvgo: discount rate r tidak valid atau tidak ada")
    if not price: die("pvgo: price tidak ada")
    zg = e / r
    pvgo = price - zg
    pct = pvgo / price
    print(f"\n=== Dekomposisi PVGO === laba per saham {e} / r {r:.2%} = nilai zero-growth {zg:,.2f}/saham")
    print(f"  Harga saat ini {price} = zero-growth {zg:,.2f} + opsi pertumbuhan PVGO {pvgo:,.2f} -> **{pct:.0%} dari harga saat ini membayar untuk pertumbuhan masa depan**")
    if pct > 0.5:
        print("  PERINGATAN: PVGO>50% - laporan harus menjawab 'pertumbuhan ini datang dari mana, siapa yang membayarnya' (bandingkan dengan base-rates)")
    return {"pvgo_pct": pct}

# ---------- Monte Carlo ----------

def run_montecarlo(c, top):
    n = c.get('n', 2000)
    rng = random.Random(c.get('seed', 42))
    years = c.get('years', 5)
    rev0 = need(c, 'base_revenue', 'montecarlo')
    gm, gs = need(c, 'growth_mean', 'montecarlo'), need(c, 'growth_std', 'montecarlo')
    ml, mm, mh = need(c, 'margin_low', 'montecarlo'), need(c, 'margin_mode', 'montecarlo'), need(c, 'margin_high', 'montecarlo')
    wl, wh = c.get('wacc_low', top['wacc'] - 0.01), c.get('wacc_high', top['wacc'] + 0.01)
    g = c.get('terminal_g', top.get('terminal_g', 0.03))
    fade = c.get('fade_years', 5)
    shares, nd, price = top.get('shares'), top.get('net_debt', 0.0), top.get('price')
    if not shares: die("montecarlo: shares tidak ada di level atas")
    vals = []
    for _ in range(n):
        gr = max(min(rng.gauss(gm, gs), gm + 3 * gs), gm - 3 * gs)   # normal terpotong (truncated)
        mg = rng.triangular(ml, mh, mm)
        wc = rng.uniform(wl, wh)
        if wc <= g: wc = g + 0.005
        rev, fcfs = rev0, []
        for _t in range(years):
            rev *= (1 + gr); fcfs.append(rev * mg)
        for k in range(fade):
            gr_f = gr + (g - gr) * (k + 1) / fade
            rev *= (1 + gr_f); fcfs.append(rev * mg)
        pv = sum(f / (1 + wc) ** (i + 1) for i, f in enumerate(fcfs))
        tv = fcfs[-1] * (1 + g) / (wc - g)
        ev = pv + tv / (1 + wc) ** len(fcfs)
        vals.append((ev - nd) / shares)
    vals.sort()
    q = lambda p: vals[min(int(p * n), n - 1)]
    mean = sum(vals) / n
    print(f"\n=== Monte Carlo (n={n}) === Distribusi fair value (per saham)")
    print(f"  P10 {q(.10):,.1f} | P25 {q(.25):,.1f} | P50 {q(.50):,.1f} | P75 {q(.75):,.1f} | P90 {q(.90):,.1f} | Mean {mean:,.1f}")
    out = {"p50": q(.50), "mean": mean}
    if price:
        p_loss = sum(1 for v in vals if v < price) / n
        out["p_loss"] = p_loss
        print(f"  P(intrinsic value < harga saat ini {price}) = {p_loss:.0%}  <- probabilitas model bahwa 'membeli di harga sekarang adalah keputusan salah'")
    return out

# ---------- Kerangka sizing posisi ----------

def run_position(results, cfg):
    price = cfg.get('price')
    scs = cfg.get('scenarios') or []
    if not price or not results or not scs:
        return
    pairs = [(sc.get('prob', 0.0), results[sc['name']]['per_share']) for sc in scs if sc['name'] in results]
    if not pairs: return
    ev_ret = sum(p * (v / price - 1) for p, v in pairs)
    ups = [(p, v / price - 1) for p, v in pairs if v > price]
    downs = [(p, 1 - v / price) for p, v in pairs if v <= price]
    up_mag = max((v for _, v in ups), default=0.0)
    down_mag = max((v for _, v in downs), default=0.0)
    asym = up_mag / down_mag if down_mag > 0 else float('inf')
    print(f"\n=== Kerangka sizing posisi === Expected value (EV) tertimbang probabilitas = {ev_ret:+.0%}")
    print(f"  Magnitude upside (bull) {up_mag:+.0%} | Magnitude downside (bear) {-down_mag:.0%} | Rasio asimetri {asym:.1f}"
          + (" (<1.5: struktur risk/reward tidak mendukung posisi besar)" if asym < 1.5 else ""))
    p_up = sum(p for p, _ in ups); p_dn = sum(p for p, _ in downs)
    b = sum(p * v for p, v in ups) / p_up if p_up else 0.0
    a = sum(p * v for p, v in downs) / p_dn if p_dn else 0.0
    if a > 0 and b > 0:
        kelly = (p_up * b - p_dn * a) / (a * b)
        lite = max(0.0, min(kelly / 4, 0.15))
        size = "standar" if lite >= 0.08 else ("menengah" if lite >= 0.04 else ("kecil" if lite > 0 else "nol"))
        print(f"  Kelly-lite (1/4 Kelly, cap 15%) ~= {lite:.0%} -> struktur risk/reward ini mendukung posisi **{size}** (referensi magnitude, bukan saran alokasi)")

# ---------- Alur utama ----------

def run(cfg):
    shares = need(cfg, "shares", "level atas")
    nd = cfg.get("net_debt", 0.0)
    wacc, g = need(cfg, "wacc", "level atas"), need(cfg, "terminal_g", "level atas")
    price = cfg.get("price")
    if shares <= 0: die("shares harus positif")
    if not (0 < wacc < 0.5): die(f"wacc={wacc} di luar rentang wajar (0, 0.5)")

    print(f"=== Input === Saham {shares} | Net debt {nd} | WACC {wacc:.2%} | g {g:.2%}"
          + (f" | Harga saat ini {price}" if price else ""))

    weighted, probs, results = 0.0, 0.0, {}
    if cfg.get("scenarios"):
        print("\n=== Skenario DCF ===")
        for sc in cfg["scenarios"]:
            r = dcf_value(sc, wacc, g, shares, nd)
            results[sc["name"]] = r
            p = sc.get("prob", 0.0); probs += p; weighted += p * r["per_share"]
            tv_warn = " PERINGATAN: TV>80%" if r["tv_share"] > 0.80 else ""
            print(f"  {sc['name']:<8} p={p:.0%}  EV {r['ev']:>9,.0f} | per saham {r['per_share']:>7,.1f} "
                  f"| Exit P/FCF {r['exit_pfcf']:.1f}x | %TV {r['tv_share']:.0%}{tv_warn} "
                  f"| Saham akhir {r['shares_end']:.2f}")
        if abs(probs - 1.0) > 1e-6:
            print(f"  [PERINGATAN] Jumlah probabilitas = {probs:.2f} != 1, nilai tertimbang tidak valid")
        else:
            print(f"  -- Fair value tertimbang probabilitas: {weighted:,.1f}/saham"
                  + (f" (vs harga saat ini {(weighted/price-1):+.0%})" if price else ""))

    sens = cfg.get("sensitivity")
    if sens and cfg.get("scenarios"):
        sc = next((s for s in cfg["scenarios"] if s["name"] == sens["scenario"]), None)
        if sc is None: die(f"sensitivity.scenario `{sens['scenario']}` tidak ada di scenarios")
        print(f"\n=== Sensitivitas ({sens['scenario']}, per saham) ===")
        print("            " + "".join(f"g={gg:.1%}  " for gg in sens["g"]))
        for w in sens["wacc"]:
            cells = "".join(f"{dcf_value(sc, w, gg, shares, nd)['per_share']:>7,.1f} " for gg in sens["g"])
            print(f"  WACC {w:.1%} {cells}")

    rev = cfg.get("reverse")
    if rev and price:
        r = reverse_dcf(price, shares, nd, wacc, g, need(rev, "interim_fcf", "reverse"),
                        need(rev, "steady_margins", "reverse"), rev.get("base_revenue"))
        print(f"\n=== Reverse DCF ===  EV {r['ev']:,.0f} | PV FCF periode transisi {r['pv_interim']:,.0f}")
        print(f"  Harga saat ini mengimplikasikan FCF tahun pertama steady-state: {r['fcf_required']:,.0f}/tahun")
        for row in r["rows"]:
            cagr = f", mengimplikasikan CAGR revenue {row['implied_cagr']:.0%}" if row["implied_cagr"] is not None else ""
            print(f"    @FCF margin {row['margin']:.0%} -> butuh revenue {row['revenue_required']:,.0f}{cagr}")

    if cfg.get("pvgo"):        run_pvgo(cfg["pvgo"], cfg)
    if cfg.get("epv"):         run_epv(cfg["epv"])
    if cfg.get("eva"):         run_eva(cfg["eva"], cfg)
    if cfg.get("montecarlo"):  run_montecarlo(cfg["montecarlo"], cfg)
    run_position(results, cfg)

    if price and cfg.get("range_low") and cfg.get("range_high"):
        lo, hi = cfg["range_low"], cfg["range_high"]
        print(f"\n=== Kalibrasi === Rentang gabungan [{lo}, {hi}] x Harga saat ini {price} -> **{calibrate(price, lo, hi)}**")
        print("  (Pemetaan aksi dan kondisi veto ada di valuation-methods.md §9, dieksekusi analis berdasarkan ketidakpastian dan grade kredibilitas laporan keuangan)")
    return results

DEMO = {
    "price": 100.0, "shares": 1.0, "net_debt": 5.0, "wacc": 0.09, "terminal_g": 0.03,
    "scenarios": [
        {"name": "bear", "prob": 0.3, "revenue": [10, 11, 12, 13, 14],
         "fcf_margin": [0.10, 0.12, 0.14, 0.15, 0.16], "fade_years": 3,
         "fade_g_start": 0.05, "annual_dilution": 0.01},
        {"name": "base", "prob": 0.5, "revenue": [10, 12, 14, 17, 20],
         "fcf_margin": [0.12, 0.15, 0.18, 0.20, 0.22], "fade_years": 5,
         "fade_g_start": 0.10, "annual_dilution": 0.01},
        {"name": "bull", "prob": 0.2, "revenue": [10, 13, 17, 22, 28],
         "fcf_margin": [0.14, 0.18, 0.22, 0.25, 0.28], "fade_years": 5,
         "fade_g_start": 0.14, "annual_dilution": 0.02}],
    "sensitivity": {"scenario": "base", "wacc": [0.08, 0.09, 0.10], "g": [0.02, 0.03, 0.04]},
    "reverse": {"interim_fcf": [1.2, 1.8, 2.5, 3.4, 4.4],
                "steady_margins": [0.20, 0.25], "base_revenue": 10},
    "range_low": 45, "range_high": 75,
    "pvgo": {"earnings_ps": 5.5},
    "epv": {"earnings_basis": "NOPAT", "normalized_earnings": 6.0, "coc": 0.09,
            "net_debt": 5.0, "shares": 1.0, "asset_value": 30.0, "price": 100.0,
            "growth": {"g": 0.04, "roiic": 0.20, "mode": "franchise"},
            "asset_series": [["FY-2", 4.5, 26], ["FY-1", 5.2, 28], ["Terbaru", 6.0, 30]]},
    "eva": {"invested_capital": 40.0, "nopat": 6.0, "fade_years": 10,
            "reinvestment_rate": 0.4, "roiic": 0.20},
    "montecarlo": {"n": 2000, "base_revenue": 10, "years": 5,
                   "growth_mean": 0.14, "growth_std": 0.06,
                   "margin_low": 0.10, "margin_mode": 0.18, "margin_high": 0.26},
}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", help="Path file JSON asumsi")
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()
    try:
        if a.demo:
            run(DEMO)
        elif a.config:
            with open(a.config) as f:
                run(json.load(f))
        else:
            ap.print_help(); sys.exit(1)
    except ValueError as e:
        print(str(e), file=sys.stderr); sys.exit(2)
