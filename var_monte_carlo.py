#!/usr/bin/env python3
"""finance-research skill - Value at Risk (VaR) & Monte Carlo portofolio

Implementasi mandiri dari metodologi VaR standar industri (RiskMetrics-style
variance-covariance, historical simulation, dan Monte Carlo simulation) -
ditulis dari rumus buku teks/akademik, BUKAN turunan dari source code
proyek atau vendor manapun.

Modul yang tersedia:
  1. Historical VaR & Expected Shortfall (CVaR) dari return historis.
  2. Parametric (variance-covariance) VaR dengan asumsi distribusi normal.
  3. Monte Carlo VaR: simulasi return portofolio dari distribusi multivariat
     (korelasi antar aset dipertahankan via decomposisi Cholesky).
  4. Backtesting sederhana (Kupiec POF test) untuk mengecek apakah jumlah
     breach historis konsisten dengan confidence level yang diklaim.

Batasan yang harus didisclose ke user:
  - Return diasumsikan i.i.d. dan (untuk parametric/Monte Carlo) mengikuti
    distribusi normal multivariat - asumsi ini melemah di ekor distribusi
    (fat tails, volatility clustering), yang umum terjadi pada return aset
    finansial riil.
  - Perlu data harga historis (CSV atau DataFrame), tidak melakukan scraping
    sendiri.

Pemakaian:
    python var_monte_carlo.py --prices prices.csv --weights 0.4,0.3,0.3 \
        --confidence 0.95,0.99 --horizon 1 --notional 1000000 \
        --mc-sims 20000 --seed 42

    prices.csv: kolom pertama 'date', kolom-kolom berikutnya ticker dengan
    harga close historis (urut tanggal naik).
"""
import argparse
import sys

import numpy as np
import pandas as pd


def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Log return harian dari matriks harga (kolom = aset)."""
    return np.log(prices / prices.shift(1)).dropna()


def portfolio_returns(returns: pd.DataFrame, weights: np.ndarray) -> pd.Series:
    weights = np.asarray(weights, dtype=float)
    if not np.isclose(weights.sum(), 1.0):
        print(f"[peringatan] bobot portofolio berjumlah {weights.sum():.4f}, bukan 1.0 - "
              f"dinormalisasi otomatis.", file=sys.stderr)
        weights = weights / weights.sum()
    return returns.dot(weights)


def historical_var(port_returns: pd.Series, confidence: float, horizon: int, notional: float):
    """VaR historis: kuantil empiris dari distribusi return realized."""
    alpha = 1 - confidence
    q = port_returns.quantile(alpha)
    var_1d = -q * notional
    var_h = var_1d * np.sqrt(horizon)
    tail = port_returns[port_returns <= q]
    es_1d = -tail.mean() * notional if len(tail) else float("nan")
    es_h = es_1d * np.sqrt(horizon)
    return {"method": "historical", "confidence": confidence, "var": var_h, "es_cvar": es_h}


def parametric_var(port_returns: pd.Series, confidence: float, horizon: int, notional: float):
    """VaR parametrik (variance-covariance) dengan asumsi return normal."""
    from scipy.stats import norm
    mu, sigma = port_returns.mean(), port_returns.std()
    z = norm.ppf(1 - confidence)
    var_1d = -(mu + z * sigma) * notional
    var_h = -(mu * horizon + z * sigma * np.sqrt(horizon)) * notional
    # Expected shortfall normal: ES = sigma * phi(z) / (1-confidence) - mu
    es_1d = (sigma * norm.pdf(z) / (1 - confidence) - mu) * notional
    es_h = es_1d * np.sqrt(horizon)
    return {"method": "parametric_normal", "confidence": confidence, "var": var_h, "es_cvar": es_h}


def monte_carlo_var(returns: pd.DataFrame, weights: np.ndarray, confidence: float,
                     horizon: int, notional: float, n_sims: int, seed: int):
    """Monte Carlo VaR: sampling return multivariat normal (korelasi via Cholesky)."""
    weights = np.asarray(weights, dtype=float)
    weights = weights / weights.sum()
    mu = returns.mean().values
    cov = returns.cov().values
    rng = np.random.default_rng(seed)
    try:
        L = np.linalg.cholesky(cov)
    except np.linalg.LinAlgError:
        # Kovarians tidak positive-definite (sering karena aset terlalu sedikit
        # histori atau kolinear) -> regularisasi ringan sebelum Cholesky.
        cov = cov + np.eye(cov.shape[0]) * 1e-10
        L = np.linalg.cholesky(cov)
    z = rng.standard_normal((n_sims, len(mu)))
    simulated_daily = mu + z @ L.T  # (n_sims, n_assets)
    port_daily = simulated_daily @ weights  # return portofolio per simulasi
    port_h = port_daily * horizon  # pendekatan kasar: skala linear ke horizon
    pnl = port_h * notional
    alpha = 1 - confidence
    var_h = -np.quantile(pnl, alpha)
    tail = pnl[pnl <= -var_h]
    es_h = -tail.mean() if len(tail) else float("nan")
    return {"method": "monte_carlo", "confidence": confidence, "var": var_h, "es_cvar": es_h,
            "n_sims": n_sims}


def kupiec_pof_test(port_returns: pd.Series, var_series: pd.Series, confidence: float):
    """Kupiec Proportion-of-Failures test: breach historis vs breach yang diharapkan.

    var_series: VaR (positif = kerugian) yang berlaku pada tanggal yang sama
    dengan port_returns (misalnya rolling VaR). Jika hanya punya satu angka
    VaR statis, broadcast ke semua tanggal sebelum memanggil fungsi ini.
    """
    losses = -port_returns
    breaches = (losses > var_series).sum()
    n = len(port_returns)
    p = 1 - confidence
    p_hat = breaches / n if n else float("nan")
    # Likelihood ratio statistic (chi-square, 1 df)
    if 0 < p_hat < 1:
        lr = -2 * (
            (n - breaches) * np.log(1 - p) + breaches * np.log(p)
            - (n - breaches) * np.log(1 - p_hat) - breaches * np.log(p_hat)
        )
    else:
        lr = float("nan")
    from scipy.stats import chi2
    p_value = 1 - chi2.cdf(lr, df=1) if not np.isnan(lr) else float("nan")
    verdict = "model konsisten (gagal tolak H0)" if (not np.isnan(p_value) and p_value > 0.05) \
        else "model DIPERTANYAKAN (tolak H0 pada 5%)" if not np.isnan(p_value) else "tidak dapat dihitung"
    return {"n_obs": n, "breaches": breaches, "expected_breaches": n * p,
            "p_hat": p_hat, "lr_stat": lr, "p_value": p_value, "verdict": verdict}


def main():
    ap = argparse.ArgumentParser(description="VaR historis/parametrik/Monte Carlo untuk portofolio")
    ap.add_argument("--prices", required=True, help="CSV harga historis (kolom: date, TICKER1, TICKER2, ...)")
    ap.add_argument("--weights", required=True, help="Bobot portofolio dipisah koma, urut sama dengan kolom harga, mis. 0.4,0.3,0.3")
    ap.add_argument("--confidence", default="0.95,0.99", help="Daftar confidence level dipisah koma")
    ap.add_argument("--horizon", type=int, default=1, help="Horizon VaR dalam hari (skala akar-waktu)")
    ap.add_argument("--notional", type=float, default=1_000_000.0, help="Nilai portofolio (mata uang laporan)")
    ap.add_argument("--mc-sims", type=int, default=20000, help="Jumlah simulasi Monte Carlo")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    prices = pd.read_csv(args.prices, parse_dates=["date"]).set_index("date").sort_index()
    weights = [float(w) for w in args.weights.split(",")]
    if len(weights) != prices.shape[1]:
        print(f"[error konfigurasi] jumlah bobot ({len(weights)}) harus sama dengan jumlah "
              f"kolom harga ({prices.shape[1]})", file=sys.stderr)
        sys.exit(2)
    confidences = [float(c) for c in args.confidence.split(",")]

    returns = compute_returns(prices)
    port_ret = portfolio_returns(returns, weights)

    print(f"=== Input === {prices.shape[1]} aset | {len(returns)} observasi harian | "
          f"notional {args.notional:,.0f} | horizon {args.horizon}d")
    print(f"Return harian portofolio: mean={port_ret.mean():.4%}  std={port_ret.std():.4%}")

    for conf in confidences:
        print(f"\n--- Confidence {conf:.0%} ---")
        h = historical_var(port_ret, conf, args.horizon, args.notional)
        print(f"  Historical   VaR={h['var']:,.0f}   ES/CVaR={h['es_cvar']:,.0f}")
        p = parametric_var(port_ret, conf, args.horizon, args.notional)
        print(f"  Parametric   VaR={p['var']:,.0f}   ES/CVaR={p['es_cvar']:,.0f}  (asumsi normal)")
        m = monte_carlo_var(returns, weights, conf, args.horizon, args.notional, args.mc_sims, args.seed)
        print(f"  Monte Carlo  VaR={m['var']:,.0f}   ES/CVaR={m['es_cvar']:,.0f}  (n_sims={m['n_sims']})")

        # Backtest sederhana: pakai VaR historis sebagai ambang statis di seluruh sample.
        var_series = pd.Series(h["var"] / args.notional, index=port_ret.index)  # dalam basis return
        bt = kupiec_pof_test(port_ret, var_series, conf)
        print(f"  Backtest Kupiec: breach={bt['breaches']} (ekspektasi {bt['expected_breaches']:.1f}) "
              f"p-value={bt['p_value']:.3f} -> {bt['verdict']}")

    print("\n[catatan] Hasil parametrik & Monte Carlo mengasumsikan return normal multivariat. "
          "Untuk aset dengan ekor gemuk (crypto, saham volatile, krisis likuiditas), VaR historis "
          "dan ES biasanya lebih dipercaya sebagai sanity check.")


if __name__ == "__main__":
    main()
