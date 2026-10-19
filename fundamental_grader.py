#!/usr/bin/env python3
"""finance-research skill - Fundamental grading per sektor (A+ s/d F)

Diporting dari repo `Automated-Fundamental-Analysis` (stockgrader.py), yang
ASLINYA scraping ~8300 ticker dari Finviz.com memakai proxy rotation (lihat
`getProxies()` di source asli, dan file `useragents.txt`). Scraping seperti
itu:
  - Kemungkinan besar DIBLOKIR oleh network allowlist sandbox ini (Finviz
    bukan API resmi, dan traffic lewat proxy acak pasti ditolak).
  - Berisiko melanggar Terms of Service Finviz.

Yang diporting di sini HANYA metodologi grading-nya (persentil metrik
terhadap sektor -> skor A+ s/d F -> skor gabungan 0-100), bukan sumber
datanya. Sumber data diganti ke `yfinance` (gratis, tanpa API key, dan lewat
API resmi Yahoo Finance bukan scraping HTML).

Metodologi grading (dipertahankan dari repo asli):
  1. Untuk tiap metrik, hitung distribusi metrik itu di seluruh universe
     (dibatasi ke sektor yang sama untuk keadilan perbandingan).
  2. Buang outlier (IQR), hitung std dev dari sisa data, bagi 3 -> 'unit
     langkah' grade.
  3. Hitung z-like distance dari persentil acuan (persentil 90 untuk metrik
     "semakin tinggi semakin baik", persentil 10 untuk metrik "semakin
     rendah semakin baik" seperti P/E, P/S, P/FCF) dibagi unit langkah ->
     mapping ke grade huruf A+ ... F.
  4. Rata-rata skor per kategori (Valuation/Profitability/Growth/Performance)
     -> skor gabungan 0-100.

PENTING - batasan yang harus didisclose ke user:
  - Universe saham dibatasi ke daftar ticker yang diberikan user (bukan
    seluruh 8300+ saham AS seperti versi asli) karena menarik fundamental
    ribuan ticker dari yfinance satu per satu lambat dan rawan rate-limit.
    Untuk screening skala besar, pertimbangkan FinanceDatabase (lookup
    universe ticker per sektor) dikombinasikan dengan data provider
    berbayar/bulk.
  - Field yfinance tidak selalu 1:1 sama dengan field Finviz; mapping di
    bawah adalah pendekatan terbaik, bukan replikasi exact.

Pemakaian:
    python fundamental_grader.py --tickers AAPL,MSFT,GOOGL,NVDA,AMD --out grades.csv
"""
import argparse
import sys
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# metrik "semakin tinggi semakin baik" vs "semakin rendah semakin baik"
HIGHER_IS_BETTER = {
    "profitMargins": True, "operatingMargins": True, "grossMargins": True,
    "returnOnEquity": True, "returnOnAssets": True,
    "earningsGrowth": True, "revenueGrowth": True,
    "trailingPegRatio": False,
    "forwardPE": False, "priceToSalesTrailing12Months": False, "priceToBook": False,
}

CATEGORY_METRICS = {
    "Valuation": ["forwardPE", "trailingPegRatio", "priceToSalesTrailing12Months", "priceToBook"],
    "Profitability": ["profitMargins", "operatingMargins", "grossMargins", "returnOnEquity", "returnOnAssets"],
    "Growth": ["earningsGrowth", "revenueGrowth"],
}

GRADE_BINS = ["F", "D", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]


def fetch_metrics(tickers):
    import yfinance as yf
    rows = []
    for t in tickers:
        try:
            info = yf.Ticker(t).info
        except Exception as e:
            print(f"[peringatan] gagal ambil data {t}: {e}", file=sys.stderr)
            continue
        row = {"ticker": t, "sector": info.get("sector", "Unknown")}
        for metrics in CATEGORY_METRICS.values():
            for m in metrics:
                row[m] = info.get(m)
        rows.append(row)
    return pd.DataFrame(rows).set_index("ticker")


def grade_metric(series: pd.Series, higher_is_better: bool) -> pd.Series:
    """Grading ala repo asli: persentil acuan +- std/3 sebagai unit langkah."""
    s = series.dropna().astype(float)
    if len(s) < 3:
        return pd.Series(index=series.index, dtype=object)
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    clean = s[(s >= q1 - 1.5 * iqr) & (s <= q3 + 1.5 * iqr)]
    if len(clean) < 2:
        clean = s
    step = clean.std() / 3 if clean.std() else 1e-9
    anchor = clean.quantile(0.90) if higher_is_better else clean.quantile(0.10)

    def to_grade(x):
        if pd.isna(x):
            return None
        z = (x - anchor) / step if higher_is_better else (anchor - x) / step
        idx = int(np.clip(round(z) + 5, 0, len(GRADE_BINS) - 1))  # z=0 -> tengah bin (B-)
        return GRADE_BINS[idx]

    return series.apply(to_grade)


GRADE_TO_SCORE = {g: i / (len(GRADE_BINS) - 1) * 100 for i, g in enumerate(GRADE_BINS)}


def run(tickers, out_path):
    df = fetch_metrics(tickers)
    if df.empty:
        print("[error] tidak ada data yang berhasil diambil", file=sys.stderr)
        sys.exit(2)

    grade_cols = {}
    for metrics in CATEGORY_METRICS.values():
        for m in metrics:
            if m not in df.columns:
                continue
            higher = HIGHER_IS_BETTER.get(m, True)
            # Grading relatif terhadap SEKTOR YANG SAMA, sesuai metodologi asli.
            graded = df.groupby("sector")[m].transform(
                lambda s: grade_metric(s, higher)
            )
            grade_cols[f"{m}_grade"] = graded

    grades_df = pd.DataFrame(grade_cols, index=df.index)
    for cat, metrics in CATEGORY_METRICS.items():
        cols = [f"{m}_grade" for m in metrics if f"{m}_grade" in grades_df.columns]
        if cols:
            scores = grades_df[cols].apply(lambda col: col.map(GRADE_TO_SCORE))
            grades_df[f"{cat}_score"] = scores.mean(axis=1)

    score_cols = [f"{c}_score" for c in CATEGORY_METRICS if f"{c}_score" in grades_df.columns]
    grades_df["overall_score_0_100"] = grades_df[score_cols].mean(axis=1)

    result = df[["sector"]].join(grades_df).sort_values("overall_score_0_100", ascending=False)
    print(result.round(1).to_string())
    if out_path:
        result.to_csv(out_path)
        print(f"\nTersimpan ke {out_path}")
    return result


def main():
    ap = argparse.ArgumentParser(description="Grading fundamental A+ s/d F relatif terhadap sektor (via yfinance)")
    ap.add_argument("--tickers", required=True, help="Daftar ticker dipisah koma, mis. AAPL,MSFT,GOOGL")
    ap.add_argument("--out", default=None, help="Path CSV output (opsional)")
    args = ap.parse_args()
    tickers = [t.strip().upper() for t in args.tickers.split(",") if t.strip()]
    run(tickers, args.out)


if __name__ == "__main__":
    main()
