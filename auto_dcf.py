#!/usr/bin/env python3
"""finance-research skill - DCF otomatis via yfinance (quick-pull, bukan pengganti dcf.py)

Diporting & diadaptasi dari repo `Stock-Valuation` (DCFModel.py). Berbeda
dari `dcf.py` (yang menuntut asumsi eksplisit lewat JSON, disiplin ala
institutional research dan tidak boleh "hitung di kepala"), script ini
menarik fundamental otomatis dari yfinance dan langsung menghasilkan satu
angka implied price. Gunakan ini HANYA untuk:
  - Sanity check cepat / first pass sebelum riset mendalam.
  - Membandingkan "apa kata data mentah otomatis" vs model manual di dcf.py.

JANGAN gunakan output script ini sebagai valuasi final dalam laporan
equity-research - workflow `equity-research` di SKILL.md ini mewajibkan
semua angka DCF dihitung lewat dcf.py dengan asumsi yang didokumentasikan,
bukan black-box otomatis.

Peringatan keterbatasan (diwarisi dari desain asli, dipertahankan apa
adanya):
  - Memakai nama baris laporan keuangan yfinance yang hardcoded
    ("Total Revenue", "EBIT", "Tax Provision", dst). Baris ini bisa tidak
    ada atau bernama lain untuk ticker tertentu (bank, asuransi, REIT,
    perusahaan non-AS) - script akan error di ticker semacam itu, itu
    normal, bukan bug yang harus diperbaiki diam-diam.
  - WACC dihitung dari cost of debt = interest expense / total debt (bukan
    yield to maturity aktual) dan cost of equity dari CAPM dengan beta
    yfinance (noisy untuk saham individual).
  - Terminal value hanya memakai metode perpetual growth, tidak ada metode
    exit-multiple maupun sensitivity table.
  - Data yfinance bisa telat/tidak lengkap; selalu silang-cek dengan sumber
    Tier 1 (laporan keuangan resmi) sebelum mengandalkan angka ini.

Pemakaian:
    python auto_dcf.py --ticker KO
    python auto_dcf.py --ticker NVDA --tgr 0.02 --riskfree ^FVX --market VT
"""
import warnings
from argparse import ArgumentParser

import numpy as np
import pandas as pd


class AutoDCFModel:
    def __init__(self, ticker, terminal_growth_rate=0.03, riskfree_ticker="^TNX", market_ticker="VTI"):
        import yfinance as yf
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        self.income = self.stock.income_stmt
        self.balance = self.stock.balance_sheet
        self.cashflow = self.stock.cash_flow
        self.terminal_growth_rate = terminal_growth_rate
        self.weights = np.array([0.4, 0.3, 0.2, 0.1])
        self.tax_weights = np.array([0.5, 0.3, 0.2])

        info = self.stock.info
        self.market_cap = info["marketCap"]
        self.debt = info["totalDebt"]
        self.cash = info["totalCash"]
        self.shares = info["sharesOutstanding"]
        self.beta = info["beta"]
        self.interest = self.income.loc["Interest Expense"].iloc[0]
        self.riskfree = yf.Ticker(riskfree_ticker).info["previousClose"] / 100
        self.market_return = yf.Ticker(market_ticker).info["threeYearAverageReturn"]
        self.price = info["previousClose"]

        self.revenue = None
        self.ebit = None
        self.tax_rate = None
        self.future_revenue = self._future_revenue()
        self.future_ebit = self._future_ebit()
        self.future_tax = self._future_tax()
        self.ebiat = self.future_ebit - self.future_tax
        self.future_da = self._future_da()
        self.future_capex = self._future_capex()
        self.future_nwc = self._future_nwc()
        self.future_fcf = self.ebiat + self.future_da - self.future_capex - self.future_nwc
        self.wacc = self._wacc()
        self.terminal_value = self._terminal_value()
        self.enterprise_value = self._discounted_cash_flow()
        self.implied_price = self._implied_share_price()
        self.margin_of_safety = (self.implied_price - self.price) / self.price

    def _future_revenue(self):
        self.revenue = self.income.loc["Total Revenue"].iloc[:-1]
        rev_ttm = self.stock.revenue_estimate.loc["0y", "avg"]
        rev_growth = 1 + self.stock.revenue_estimate.loc["+1y", "growth"]
        return pd.Series(rev_ttm * (rev_growth ** i) for i in range(5))

    def _future_ebit(self):
        self.ebit = self.income.loc["EBIT"].iloc[:-1]
        margin = np.average(self.ebit / self.revenue, weights=self.weights)
        return self.future_revenue * margin

    def _future_tax(self):
        tax = self.income.loc["Tax Provision"].iloc[:-1]
        self.tax_rate = np.average((tax / self.ebit)[:3], weights=self.tax_weights)
        return self.future_ebit * self.tax_rate

    def _future_da(self):
        da = abs(self.cashflow.loc["Depreciation And Amortization"].iloc[:-1])
        margin = np.average(da / self.revenue, weights=self.weights)
        return self.future_revenue * margin

    def _future_capex(self):
        capex = abs(self.cashflow.loc["Capital Expenditure"].iloc[:-1])
        margin = np.average(capex / self.revenue, weights=self.weights)
        return self.future_revenue * margin

    def _future_nwc(self):
        nwc = self.cashflow.loc["Change In Working Capital"].iloc[:-1]
        margin = np.average(nwc / self.revenue, weights=self.weights)
        return self.future_revenue * margin

    def _wacc(self):
        w_debt = self.debt / (self.debt + self.market_cap)
        w_equity = self.market_cap / (self.debt + self.market_cap)
        cost_debt = self.interest / self.debt
        cost_equity = self.riskfree + self.beta * (self.market_return - self.riskfree)
        return w_debt * cost_debt * (1 - self.tax_rate) + w_equity * cost_equity

    def _terminal_value(self):
        return (self.future_fcf.iloc[4] * (1 + self.terminal_growth_rate)) / (self.wacc - self.terminal_growth_rate)

    def _discounted_cash_flow(self):
        discounted_fcf = sum(
            pd.Series(fcf / ((1 + self.wacc) ** (0.5 + i)) for i, fcf in enumerate(self.future_fcf))
        )
        discounted_tv = self.terminal_value / ((1 + self.wacc) ** 5)
        return discounted_fcf + discounted_tv

    def _implied_share_price(self):
        equity_value = self.enterprise_value - self.debt + self.cash
        return equity_value / self.shares

    def implied_growth_rate(self, tolerance=0.01, max_iterations=100):
        """Bisection: cari growth rate yang membuat implied price = harga pasar saat ini."""
        def price_at(growth_rate):
            self.future_revenue = pd.Series(self.revenue.iloc[0] * ((1 + growth_rate) ** i) for i in range(5))
            self.future_ebit = self._future_ebit()
            self.future_tax = self._future_tax()
            self.ebiat = self.future_ebit - self.future_tax
            self.future_da = self._future_da()
            self.future_capex = self._future_capex()
            self.future_nwc = self._future_nwc()
            self.future_fcf = self.ebiat + self.future_da - self.future_capex - self.future_nwc
            self.terminal_value = self._terminal_value()
            self.enterprise_value = self._discounted_cash_flow()
            return self._implied_share_price()

        lower, upper = -0.5, 0.5
        for _ in range(max_iterations):
            mid = (lower + upper) / 2
            calculated = price_at(mid)
            if abs(calculated - self.price) < tolerance:
                return mid
            if calculated > self.price:
                upper = mid
            else:
                lower = mid
        raise ValueError("Implied growth rate tidak konvergen dalam batas iterasi")


def main():
    warnings.filterwarnings("ignore")
    ap = ArgumentParser(description="DCF otomatis cepat via yfinance (quick-pull, lihat disclaimer di docstring)")
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--tgr", type=float, default=0.03, help="Terminal growth rate (default 0.03)")
    ap.add_argument("--riskfree", default="^TNX", help="Ticker yield risk-free (default ^TNX)")
    ap.add_argument("--market", default="VTI", help="Ticker proxy market return (default VTI)")
    args = ap.parse_args()

    model = AutoDCFModel(args.ticker.upper(), args.tgr, args.riskfree, args.market)
    print(f"=== DCF otomatis cepat: {args.ticker.upper()} ===")
    print(f"Harga saat ini      : {model.price:.2f}")
    print(f"Implied share price : {model.implied_price:.2f}")
    print(f"Margin of safety    : {model.margin_of_safety:.2%}")
    print(f"WACC terpakai       : {model.wacc:.2%}")
    try:
        igr = model.implied_growth_rate()
        print(f"Implied growth rate : {igr:.2%}  (growth rate yang membuat model=harga pasar)")
    except ValueError as e:
        print(f"[peringatan] {e}")
    print("\n[catatan] Ini quick-pull otomatis, BUKAN pengganti valuasi dcf.py yang memakai "
          "asumsi terdokumentasi. Silang-cek angka fundamental di atas dengan laporan "
          "keuangan resmi sebelum dipakai dalam kesimpulan riset.")


if __name__ == "__main__":
    main()
