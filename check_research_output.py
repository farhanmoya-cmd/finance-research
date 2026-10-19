#!/usr/bin/env python3
"""finance-research skill - Checker Konsistensi Laporan Keuangan/Valuasi

Diterjemahkan & diadaptasi dari modul `scripts/check_research_output.py`
milik skill equity-research-skill (bahasa Mandarin asli). Logika dan aturan
pengecekan TIDAK diubah - hanya string/marker bahasa yang diterjemahkan ke
Indonesia, dan marker deteksi dibuat menerima tiga bahasa (Indonesia,
Inggris, dan Mandarin asli) supaya laporan lama berbahasa apapun masih bisa
dicek.

Pemakaian:
    python check_research_output.py --report report.md --assumptions valuation.json
    python check_research_output.py --financials financials.csv
    python check_research_output.py --demo

Semua input bersifat opsional; script hanya mengecek hal yang bisa
dihitung ulang dari file yang tersedia. Hanya memakai Python standard
library.
"""

import argparse
import csv
import json
import math
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


SEVERITY_RANK = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
LABELS = ["Sangat Undervalued", "Undervalued", "Wajar", "Overvalued", "Sangat Overvalued"]
LABEL_ALIASES = {
    "Sangat Undervalued": ["sangat undervalued", "显著低估", "significantly undervalued", "deeply undervalued"],
    "Undervalued": ["undervalued", "低估"],
    "Wajar": ["wajar", "合理", "fairly valued", "fair value", "fairly priced"],
    "Overvalued": ["overvalued", "高估"],
    "Sangat Overvalued": ["sangat overvalued", "显著高估", "significantly overvalued", "deeply overvalued"],
}
MISSING_DATA_MARKERS = ["tidak diperoleh", "未获取到", "not obtained", "not available", "unavailable", "not disclosed", "not found"]
JUDGMENT_MARKERS = ["penilaian saya", "我的判断", "my view", "my judgment", "my assessment", "assessment:"]
SOURCE_MARKERS = ["sumber data", "数据来源", "来源", "sources and timestamps", "data sources", "sources", "source:"]
INDUSTRY_RULES_PATH = os.path.join(os.path.dirname(__file__), "..", "references", "industry-rules.json")
ID_TEMPLATE_MARKERS = ["poin utama bab ini", "penilaian saya", "tidak diperoleh", "sumber data dan timestamp", "kalimat kesimpulan wajib", "tabel asumsi valuasi"]
EN_TEMPLATE_MARKERS = ["key takeaways:", "my view:", "not obtained", "sources and timestamps", "disclaimer: not investment advice"]
ZH_TEMPLATE_MARKERS = ["本章要点", "我的判断", "未获取到", "数据来源与时间戳", "必写结论句", "估值假设表"]


@dataclass
class Issue:
    severity: str
    code: str
    message: str
    detail: str = ""
    file: str = ""

    def line(self) -> str:
        loc = f" [{self.file}]" if self.file else ""
        detail = f"\n    {self.detail}" if self.detail else ""
        return f"[{self.severity}] {self.code}{loc}: {self.message}{detail}"


def add(issues: List[Issue], severity: str, code: str, message: str, detail: str = "", file: str = "") -> None:
    issues.append(Issue(severity, code, message, detail, file))


def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def norm_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.strip().lower())


def parse_number(value) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return None
        return float(value)
    s = str(value).strip()
    if not s or s in {"-", "—", "N/A", "NA", "n/a", "未获取到", "not obtained", "not available", "tidak diperoleh"}:
        return None
    mult = 1.0
    if s.endswith("%"):
        mult = 0.01
        s = s[:-1]
    s = s.replace(",", "").replace("$", "").replace("￥", "").replace("¥", "").replace("Rp", "")
    s = s.replace("倍", "").replace("x", "").replace("X", "")
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    if not m:
        return None
    return float(m.group(0)) * mult


def pct(value: float) -> str:
    return f"{value:.1%}"


def close_enough(a: float, b: float, rel_tol: float = 0.015, abs_tol: float = 0.02) -> bool:
    return abs(a - b) <= max(abs_tol, rel_tol * max(abs(a), abs(b), 1.0))


def detect_labels(text: str) -> List[str]:
    """Alias lebih panjang dicocokkan dulu, supaya 'Sangat Undervalued' tidak
    ikut terhitung sebagai 'Undervalued'; label Mandarin/Inggris lama dipetakan
    balik ke label kanonik Indonesia."""
    found: List[str] = []
    masked = text.lower()
    aliases = []
    for canonical, values in LABEL_ALIASES.items():
        for alias in values:
            aliases.append((canonical, alias.lower()))
    for canonical, alias in sorted(aliases, key=lambda item: len(item[1]), reverse=True):
        if alias in masked and canonical not in found:
            found.append(canonical)
            masked = masked.replace(alias, "■" * len(alias))
    return found


def has_any(text: str, patterns: Sequence[str]) -> bool:
    lower = text.lower()
    return any(pattern.lower() in lower for pattern in patterns)


def load_industry_rules() -> Dict[str, Dict]:
    with open(INDUSTRY_RULES_PATH, "r", encoding="utf-8") as f:
        payload = json.load(f)
    return payload["industries"]


def normalize_industry_args(values: Optional[Sequence[str]]) -> List[str]:
    industries: List[str] = []
    for value in values or []:
        for item in value.split(","):
            slug = item.strip().lower()
            if slug and slug not in industries:
                industries.append(slug)
    return industries


def detect_declared_industries(text: str, rules: Dict[str, Dict]) -> List[str]:
    matches = re.findall(r"(?:lampiran industri|行业附录|industry append(?:ix|ices))\s*[:：]\s*([^\n]+)", text, flags=re.I)
    declared = " ".join(matches).lower()
    if not declared:
        return []
    declared_words = re.sub(r"[^a-z0-9一-鿿]+", " ", declared)
    declared_compact = declared_words.replace(" ", "")
    found: List[str] = []
    for slug, rule in rules.items():
        candidates = [slug, rule.get("name_id", rule.get("name_zh", "")), rule.get("name_en", "")] + rule.get("aliases", [])
        normalized = [re.sub(r"[^a-z0-9一-鿿]+", " ", candidate.lower()).strip() for candidate in candidates if candidate]
        if any(candidate in declared_words or candidate.replace(" ", "") in declared_compact for candidate in normalized):
            found.append(slug)
    return found


def detect_report_language(text: str) -> Optional[str]:
    if re.search(r"^# .+Equity Research Report\s*$", text, flags=re.I | re.M):
        return "en"
    if re.search(r"^# .+(个股投资研究报告|财报深度分析)\s*$", text, flags=re.M):
        return "zh"
    if re.search(r"^# .+(Laporan Riset Investasi Saham|Analisis Mendalam Laporan Keuangan)\s*$", text, flags=re.I | re.M):
        return "id"
    return None


def check_language_consistency(text: str, language: str, path: str, issues: List[Issue]) -> None:
    resolved = detect_report_language(text) if language == "auto" else language
    if not resolved:
        add(issues, "P2", "REPORT_LANGUAGE_UNDETERMINED", "Bahasa laporan tidak dapat ditentukan dari judul; gunakan --language id, --language zh, atau --language en.", file=path)
        return
    conflicting_map = {"id": [], "en": ID_TEMPLATE_MARKERS + ZH_TEMPLATE_MARKERS, "zh": ID_TEMPLATE_MARKERS + EN_TEMPLATE_MARKERS}
    conflicting = conflicting_map.get(resolved, EN_TEMPLATE_MARKERS)
    found = [marker for marker in conflicting if marker.lower() in text.lower()]
    if found:
        add(
            issues,
            "P1",
            "REPORT_LANGUAGE_MIXED",
            "Laporan mengandung marker template dari bahasa lain selain bahasa target.",
            detail=f"language={resolved}; conflicting_markers={', '.join(found)}",
            file=path,
        )


def check_industry_requirements(
    text: str,
    requested: Optional[Sequence[str]],
    path: str,
    issues: List[Issue],
) -> None:
    rules = load_industry_rules()
    table_text = "\n".join(line for line in text.splitlines() if "|" in line)
    slugs = normalize_industry_args(requested)
    if "auto" in slugs:
        slugs = [slug for slug in slugs if slug != "auto"] + detect_declared_industries(text, rules)
    if not slugs:
        slugs = detect_declared_industries(text, rules)
    if not slugs:
        add(
            issues,
            "P2",
            "REPORT_NO_INDUSTRY_DECLARATION",
            "Laporan tidak mendeklarasikan lampiran industri utama/sekunder, sehingga pengecekan KPI spesifik-industri tidak bisa dijalankan.",
            detail="Tulis 'Lampiran industri: saas' di laporan, atau jalankan checker dengan --industry saas.",
            file=path,
        )
        return
    for slug in dict.fromkeys(slugs):
        rule = rules.get(slug)
        if not rule:
            add(issues, "P1", "REPORT_UNKNOWN_INDUSTRY", f"Aturan industri tidak dikenal: {slug}.", file=path)
            continue
        for group in rule.get("required_groups", []):
            if not has_any(table_text, group.get("terms", [])):
                name = rule.get('name_id', rule.get('name_zh', slug))
                add(
                    issues,
                    "P1",
                    "REPORT_INDUSTRY_KPI_MISSING",
                    f"Laporan sektor {name} kehilangan grup KPI wajib: {group['label']}.",
                    detail=f"accepted_terms={', '.join(group.get('terms', []))}",
                    file=path,
                )


def text_mentions_ai_capex(text: str) -> bool:
    lower = text.lower()
    return ("ai" in lower or "人工智能" in text or "cloud" in lower or "云" in text) and (
        "capex" in lower or "资本开支" in text or "数据中心" in text or "belanja modal" in lower
    )


def calibrate(price: float, lo: float, hi: float) -> str:
    if price < lo * 0.50:
        return "Sangat Undervalued"
    if price < lo * 0.85:
        return "Undervalued"
    if price <= hi * 1.15:
        return "Wajar"
    if price <= hi * 1.50:
        return "Overvalued"
    return "Sangat Overvalued"


def load_csv(path: str) -> Tuple[List[Dict[str, str]], Dict[str, str]]:
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    aliases = {norm_key(k): k for k in (reader.fieldnames or [])}
    return rows, aliases


def pick(aliases: Dict[str, str], names: Sequence[str]) -> Optional[str]:
    for name in names:
        key = norm_key(name)
        if key in aliases:
            return aliases[key]
    return None


def row_num(row: Dict[str, str], col: Optional[str]) -> Optional[float]:
    return parse_number(row.get(col)) if col else None


def check_report(
    path: str,
    assumptions: Optional[Dict],
    issues: List[Issue],
    industries: Optional[Sequence[str]] = None,
    language: str = "auto",
) -> None:
    text = load_text(path)
    lower = text.lower()

    check_language_consistency(text, language, path, issues)
    check_industry_requirements(text, industries, path, issues)

    if not has_any(text, SOURCE_MARKERS):
        add(issues, "P1", "REPORT_NO_SOURCE_SECTION", "Laporan tidak memiliki daftar/keterangan sumber data.", file=path)
    if not re.search(r"20\d{2}[-年/.]\d{1,2}", text):
        add(issues, "P2", "REPORT_NO_TIMESTAMP", "Laporan tidak memiliki tanggal atau timestamp yang jelas.", file=path)
    if not has_any(text, MISSING_DATA_MARKERS):
        add(issues, "P3", "REPORT_NO_MISSING_DATA_MARKER", "Laporan tidak memiliki marker data hilang (misalnya 'Tidak diperoleh' atau 'Not obtained'); abaikan jika memang tidak ada data yang hilang.", file=path)
    if not has_any(text, JUDGMENT_MARKERS):
        add(issues, "P2", "REPORT_NO_JUDGMENT_MARKER", "Laporan tidak memiliki marker penilaian eksplisit (misalnya 'Penilaian saya' atau 'My view'); fakta dan penilaian mungkin tercampur.", file=path)
    if "scripts/dcf.py" not in text and "dcf.py" not in lower:
        add(issues, "P2", "REPORT_NO_DCF_SCRIPT_EVIDENCE", "Laporan tidak menjelaskan bahwa DCF/EPV dijalankan lewat script.", file=path)
    if "reverse dcf" not in lower and "dcf terbalik" not in lower and "反向 dcf" not in lower and "反向DCF" not in text:
        add(issues, "P2", "REPORT_NO_REVERSE_DCF", "Laporan tidak memiliki kerangka reverse DCF.", file=path)
    if "skenario" not in lower and "情景" not in text and "scenario" not in lower:
        add(issues, "P2", "REPORT_NO_SCENARIO_VALUATION", "Laporan tidak memiliki valuasi skenario atau pembahasan pembobotan probabilitas.", file=path)
    if "epv" not in lower and "earnings power value" not in lower and "盈利能力价值" not in text and "三要素" not in text:
        add(issues, "P2", "REPORT_NO_EPV", "Laporan tidak memiliki verifikasi silang valuasi EPV/metode tiga lapis.", file=path)
    if not has_any(text, ["registrasi prediksi", "pencatatan prediksi", "预测登记", "预测与验证", "forecast register", "forecast tracking"]):
        add(issues, "P2", "REPORT_NO_FORECAST_REGISTER", "Laporan tidak memiliki registrasi prediksi dengan tenggat verifikasi.", file=path)
    if not has_any(text, ["tanggal verifikasi", "验证日期", "验证时点", "validation date", "review date"]):
        add(issues, "P2", "REPORT_NO_FORECAST_REVIEW_DATE", "Prediksi dalam laporan tidak memiliki tanggal verifikasi yang jelas.", file=path)

    has_decision_triad = (
        has_any(text, ["penilaian nilai intrinsik", "内在价值判断", "intrinsic value view", "intrinsic value judgment"])
        and has_any(text, ["arah perdagangan pasar 1-3 bulan", "未来 1–3 个月市场交易方向", "1-3 month market trading direction", "1–3 month market trading direction"])
        and has_any(text, ["tindakan investasi", "投资动作", "action:", "investment action"])
    )
    if not has_decision_triad:
        add(
            issues,
            "P2",
            "REPORT_NO_DECISION_TRIAD",
            "Laporan tidak memiliki trias keputusan: penilaian nilai intrinsik / arah perdagangan pasar 1-3 bulan / tindakan investasi.",
            file=path,
        )

    has_upside = has_any(text, ["falsifikasi upside", "sinyal upside", "上行证伪", "踏空", "上修证伪", "upside invalidation", "upside disconfirmation", "upside risk"])
    has_downside = has_any(text, ["falsifikasi downside", "sinyal downside", "下行证伪", "下修证伪", "破坏本报告乐观", "downside invalidation", "downside disconfirmation", "downside risk"])
    if has_any(text, ["sinyal falsifikasi", "证伪信号", "invalidation signal", "disconfirmation signal"]) and not (has_upside and has_downside):
        add(
            issues,
            "P2",
            "REPORT_DISCONFIRMATION_DIRECTION_AMBIGUOUS",
            "Laporan menyebut 'sinyal falsifikasi' tapi tidak membedakan falsifikasi upside dan downside secara terpisah.",
            file=path,
        )
    if has_any(text, ["tunggu dan amati", "observasi", "观望", "wait and see", "hold off", "watch"]) and not has_upside:
        add(
            issues,
            "P2",
            "REPORT_WAIT_NO_UPSIDE_DISCONFIRMATION",
            "Laporan memiliki tindakan 'tunggu dan amati' tapi tidak memiliki kondisi falsifikasi upside/risiko tertinggal rally.",
            file=path,
        )

    if has_any(text, ["arah perdagangan pasar 1-3 bulan", "未来 1–3 个月市场交易方向", "1-3 month market trading direction", "1–3 month market trading direction"]) and not has_any(text, ["pasar paling mungkin", "akan trading dulu", "repricing", "reprice", "市场最可能", "先交易", "再定价", "重定价", "market is most likely", "trade first", "re-rating"]):
        add(
            issues,
            "P3",
            "REPORT_MARKET_PATH_UNEXPLAINED",
            "Laporan menulis arah perdagangan pasar 1-3 bulan tapi tidak menjelaskan variabel apa yang paling mungkin ditradingkan pasar lebih dulu.",
            file=path,
        )

    if text_mentions_ai_capex(text) and not (
        "capex pemeliharaan" in lower
        or "belanja modal pemeliharaan" in lower
        or "capex pertumbuhan" in lower
        or "belanja modal pertumbuhan" in lower
        or "维护性 capex" in lower
        or "维护性资本开支" in text
        or "成长性 capex" in lower
        or "成长性资本开支" in text
        or "维护性/成长" in text
    ):
        add(
            issues,
            "P2",
            "REPORT_AI_CAPEX_NOT_SPLIT",
            "Laporan membahas capex AI/cloud/data center tapi tidak memisahkan capex pemeliharaan vs capex pertumbuhan, atau tidak menjelaskan bahwa pemisahan itu tidak bisa diperoleh.",
            file=path,
        )

    if assumptions:
        price = parse_number(assumptions.get("price"))
        lo = parse_number(assumptions.get("range_low"))
        hi = parse_number(assumptions.get("range_high"))
        if price is not None and lo is not None and hi is not None and hi >= lo:
            expected = calibrate(price, lo, hi)
            found_labels = detect_labels(text)
            if expected not in found_labels:
                add(
                    issues,
                    "P1",
                    "REPORT_VALUATION_LABEL_MISMATCH",
                    f"Kesimpulan laporan tidak mengandung label valuasi yang seharusnya muncul menurut aturan: {expected}.",
                    f"price={price}, range=[{lo}, {hi}], report_labels={found_labels or 'none'}",
                    path,
                )


def check_assumptions(path: str, issues: List[Issue]) -> Dict:
    cfg = load_json(path)
    price = parse_number(cfg.get("price"))
    shares = parse_number(cfg.get("shares"))
    wacc = parse_number(cfg.get("wacc"))
    g = parse_number(cfg.get("terminal_g"))
    lo = parse_number(cfg.get("range_low"))
    hi = parse_number(cfg.get("range_high"))

    for key, value in [("price", price), ("shares", shares), ("wacc", wacc), ("terminal_g", g)]:
        if value is None:
            add(issues, "P2", "ASSUMPTION_MISSING_CORE_FIELD", f"Asumsi valuasi tidak memiliki field wajib `{key}`.", file=path)

    if wacc is not None and g is not None:
        if wacc <= g:
            add(issues, "P0", "DCF_WACC_NOT_ABOVE_G", "WACC harus lebih besar dari tingkat pertumbuhan perpetual g.", f"wacc={wacc}, terminal_g={g}", path)
        if not 0.03 <= wacc <= 0.20:
            add(issues, "P2", "DCF_WACC_UNUSUAL", "WACC di luar rentang umum, pastikan basis perhitungannya.", f"wacc={pct(wacc)}", path)
        if not -0.02 <= g <= 0.05:
            add(issues, "P2", "DCF_TERMINAL_G_UNUSUAL", "Tingkat pertumbuhan perpetual g di luar rentang umum, pastikan acuan pertumbuhan nominal jangka panjangnya.", f"g={pct(g)}", path)

    if shares is not None and shares <= 0:
        add(issues, "P0", "SHARES_NON_POSITIVE", "Jumlah saham harus bernilai positif.", f"shares={shares}", path)
    if lo is not None and hi is not None:
        if lo > hi:
            add(issues, "P0", "VALUATION_RANGE_INVERTED", "Batas bawah rentang valuasi gabungan lebih tinggi dari batas atas.", f"range_low={lo}, range_high={hi}", path)

    scenarios = cfg.get("scenarios") or []
    if not scenarios:
        add(issues, "P1", "DCF_NO_SCENARIOS", "Asumsi valuasi tidak memiliki scenarios, pengecekan DCF tiga-skenario tertimbang probabilitas tidak bisa dilakukan.", file=path)
    else:
        prob_sum = 0.0
        seen = set()
        for idx, sc in enumerate(scenarios):
            name = str(sc.get("name") or f"scenario_{idx}")
            name_key = norm_key(name)
            if name in seen:
                add(issues, "P2", "DCF_DUPLICATE_SCENARIO", "Nama skenario duplikat.", name, path)
            seen.add(name)
            prob = parse_number(sc.get("prob"))
            if prob is None:
                add(issues, "P1", "DCF_SCENARIO_MISSING_PROB", "Skenario tidak memiliki probabilitas.", name, path)
            else:
                prob_sum += prob
                if prob < 0 or prob > 1:
                    add(issues, "P0", "DCF_SCENARIO_PROB_OUT_OF_RANGE", "Probabilitas skenario harus di antara 0 dan 1.", f"{name}: prob={prob}", path)
            evidence = str(sc.get("evidence_strength") or sc.get("evidence") or "").strip()
            if not evidence:
                add(issues, "P3", "DCF_SCENARIO_NO_EVIDENCE_STRENGTH", "Skenario tidak menandai kekuatan bukti saat ini (lemah/sedang/cukup kuat/kuat).", name, path)
            elif prob is not None and ("bull" in name_key or "bear" in name_key or "牛" in name or "熊" in name):
                strong_evidence = evidence in {"中强", "强", "cukup kuat", "kuat", "medium-high", "high", "strong"}
                if strong_evidence and prob < 0.25:
                    add(
                        issues,
                        "P2",
                        "DCF_STRONG_EVIDENCE_LOW_PROBABILITY",
                        "Skenario non-basis sudah memiliki bukti cukup kuat/kuat, tapi probabilitasnya masih di bawah 25%; perlu dinaikkan atau dijelaskan mengapa tetap jadi skenario ekor.",
                        f"{name}: prob={prob}, evidence_strength={evidence}",
                        path,
                    )
            if "fcf" not in sc:
                revenue = sc.get("revenue")
                margin = sc.get("fcf_margin")
                if not isinstance(revenue, list) or not isinstance(margin, list):
                    add(issues, "P1", "DCF_SCENARIO_NO_FCF_OR_DRIVERS", "Skenario harus menyediakan fcf, atau revenue + fcf_margin.", name, path)
                elif len(revenue) != len(margin):
                    add(issues, "P0", "DCF_DRIVER_LENGTH_MISMATCH", "Panjang revenue dan fcf_margin tidak sama.", f"{name}: revenue={len(revenue)}, fcf_margin={len(margin)}", path)
            dilution = parse_number(sc.get("annual_dilution", 0))
            if dilution is not None and (dilution < -0.20 or dilution > 0.20):
                add(issues, "P2", "DCF_DILUTION_UNUSUAL", "Perubahan saham tahunan di luar rentang umum, pastikan kembali.", f"{name}: annual_dilution={pct(dilution)}", path)
        if abs(prob_sum - 1.0) > 0.005:
            add(issues, "P1", "DCF_PROBABILITY_SUM_NOT_ONE", "Jumlah probabilitas skenario tidak sama dengan 1.", f"prob_sum={prob_sum:.4f}", path)

    epv = cfg.get("epv")
    if epv:
        e = parse_number(epv.get("normalized_earnings"))
        coc = parse_number(epv.get("coc"))
        epv_shares = parse_number(epv.get("shares"))
        if e is None or coc is None or epv_shares is None:
            add(issues, "P1", "EPV_MISSING_CORE_FIELD", "Blok EPV tidak memiliki normalized_earnings / coc / shares.", file=path)
        if coc is not None and coc <= 0:
            add(issues, "P0", "EPV_COC_NON_POSITIVE", "Cost of capital EPV harus positif.", f"coc={coc}", path)
        growth = epv.get("growth") or {}
        gg = parse_number(growth.get("g"))
        roiic = parse_number(growth.get("roiic"))
        if gg is not None and coc is not None and gg >= coc:
            add(issues, "P1", "EPV_G_NOT_BELOW_COC", "Formula pertumbuhan franchise mensyaratkan g < cost of capital; jika tidak, jelaskan penggunaan formula fallback sederhana.", f"g={gg}, coc={coc}", path)
        if roiic is not None and coc is not None and roiic < coc:
            add(issues, "P2", "EPV_ROIIC_BELOW_COC", "ROIIC di bawah cost of capital, pertumbuhan berpotensi menghancurkan nilai.", f"roiic={pct(roiic)}, coc={pct(coc)}", path)
    else:
        add(issues, "P2", "EPV_BLOCK_MISSING", "Asumsi valuasi tidak memiliki blok epv, valuasi EPV/metode tiga lapis sulit diverifikasi ulang.", file=path)

    return cfg


def check_ratio(
    issues: List[Issue],
    path: str,
    row_label: str,
    row: Dict[str, str],
    numerator_col: Optional[str],
    denominator_col: Optional[str],
    provided_col: Optional[str],
    code: str,
    name: str,
    tolerance: float = 0.006,
) -> None:
    if not numerator_col or not denominator_col or not provided_col:
        return
    num = row_num(row, numerator_col)
    den = row_num(row, denominator_col)
    provided = row_num(row, provided_col)
    if num is None or den in (None, 0) or provided is None:
        return
    expected = num / den
    if abs(expected - provided) > tolerance:
        add(
            issues,
            "P1",
            code,
            f"{name} pada {row_label} tidak konsisten dengan nilai mentahnya.",
            f"expected={pct(expected)}, provided={pct(provided)}, numerator={num}, denominator={den}",
            path,
        )


def check_growth(
    issues: List[Issue],
    path: str,
    rows: List[Dict[str, str]],
    period_col: Optional[str],
    value_col: Optional[str],
    provided_col: Optional[str],
    lag: int,
    code: str,
    name: str,
) -> None:
    if not value_col or not provided_col or len(rows) <= lag:
        return
    for idx in range(lag, len(rows)):
        cur = row_num(rows[idx], value_col)
        prev = row_num(rows[idx - lag], value_col)
        provided = row_num(rows[idx], provided_col)
        label = rows[idx].get(period_col, f"row {idx + 2}") if period_col else f"row {idx + 2}"
        if cur is None or prev in (None, 0) or provided is None:
            continue
        expected = cur / prev - 1
        if abs(expected - provided) > 0.015:
            add(
                issues,
                "P1",
                code,
                f"{name} pada {label} tidak konsisten dengan perhitungan seri data.",
                f"expected={pct(expected)}, provided={pct(provided)}, current={cur}, prior={prev}",
                path,
            )


def growth_rate(cur, prev):
    if cur is None or prev in (None, 0):
        return None
    return cur / prev - 1


def check_forensics(rows, aliases, path, issues) -> None:
    """Pengecekan kualitas laporan keuangan (forensic accounting): kualitas
    akrual / konversi kas / divergensi DSO & pendapatan ditangguhkan / Beneish
    M-Score. Nama kolom yang dibutuhkan ada di
    references/forensic-accounting.md §7; kolom yang tidak ada otomatis
    dilewati."""
    ni = pick(aliases, ["net_income", "netincome", "laba_bersih", "净利润"])
    cfo = pick(aliases, ["cfo", "operating_cash_flow", "cash_from_operations", "arus_kas_operasi", "经营现金流"])
    ta = pick(aliases, ["total_assets", "totalassets", "total_aset", "总资产"])
    rev = pick(aliases, ["revenue", "sales", "pendapatan", "收入", "营收"])
    rec = pick(aliases, ["receivables", "accounts_receivable", "piutang", "应收账款", "应收"])
    dfr = pick(aliases, ["deferred_revenue", "contract_liabilities", "pendapatan_ditangguhkan", "递延收入", "合同负债"])
    gp = pick(aliases, ["gross_profit", "grossprofit", "laba_kotor", "毛利"])
    ppe = pick(aliases, ["ppe", "net_ppe", "aset_tetap", "固定资产"])
    ca = pick(aliases, ["current_assets", "aset_lancar", "流动资产"])
    dep = pick(aliases, ["depreciation", "depresiasi", "折旧"])
    sga = pick(aliases, ["sga", "sg_a", "beban_penjualan_administrasi", "销售管理费用"])
    tl = pick(aliases, ["total_liabilities", "totalliabilities", "total_liabilitas", "总负债"])

    # -- Rasio akrual & konversi kas (per baris + tren) --
    conv_series = []
    for idx, row in enumerate(rows):
        label = row.get(pick(aliases, ["period", "fiscal_period", "date", "periode", "财期", "期间"]) or "", f"row {idx + 2}")
        ni_v, cfo_v, ta_v = row_num(row, ni), row_num(row, cfo), row_num(row, ta)
        if ni_v is not None and cfo_v is not None and ta_v not in (None, 0):
            accr = (ni_v - cfo_v) / ta_v
            if accr > 0.10:
                add(issues, "P1", "FORENSIC_HIGH_ACCRUALS", f"Rasio akrual total {label} sebesar {accr:.1%} > 10%, sinyal kualitas laba (red flag).",
                    f"net_income={ni_v}, cfo={cfo_v}, total_assets={ta_v}", path)
            elif accr > 0.05:
                add(issues, "P2", "FORENSIC_ELEVATED_ACCRUALS", f"Rasio akrual total {label} sebesar {accr:.1%} cukup tinggi (5-10%).", "", path)
        if ni_v not in (None, 0) and cfo_v is not None and ni_v > 0:
            conv_series.append((label, cfo_v / ni_v))
    if len(conv_series) >= 3:
        last = conv_series[-1][1]
        declining = all(conv_series[i][1] >= conv_series[i + 1][1] for i in range(len(conv_series) - 3, len(conv_series) - 1))
        if last < 0.8 and declining:
            add(issues, "P2", "FORENSIC_CASH_CONVERSION_DECLINING",
                f"Rasio konversi kas turun ke {last:.0%} (<80% dan terus menurun), laba dan kas mulai terdivergensi.",
                ", ".join(f"{l}={v:.0%}" for l, v in conv_series[-3:]), path)

    # -- Divergensi DSO / pendapatan ditangguhkan vs pertumbuhan revenue (dua baris terakhir) --
    if len(rows) >= 2 and rev:
        r_g = growth_rate(row_num(rows[-1], rev), row_num(rows[-2], rev))
        if rec:
            rec_g = growth_rate(row_num(rows[-1], rec), row_num(rows[-2], rec))
            if r_g is not None and rec_g is not None and rec_g - r_g > 0.15:
                add(issues, "P2", "FORENSIC_DSO_DIVERGENCE",
                    f"Pertumbuhan piutang {rec_g:.0%} melampaui pertumbuhan revenue {r_g:.0%} lebih dari 15pp, waspadai channel stuffing/pelonggaran kredit/pengakuan revenue dini.", "", path)
        if dfr:
            d_g = growth_rate(row_num(rows[-1], dfr), row_num(rows[-2], dfr))
            if r_g is not None and d_g is not None and r_g > 0 and d_g < 0:
                add(issues, "P2", "FORENSIC_DEFERRED_DIVERGENCE",
                    f"Revenue tumbuh {r_g:.0%} sementara pendapatan ditangguhkan turun {d_g:.0%}; untuk perusahaan subscription ini sinyal 'memakan masa depan'.", "", path)

    # -- Beneish M-Score (dua baris terakhir, perlu semua kolom) --
    needed = [rev, rec, gp, ppe, ca, dep, sga, tl, ta, ni, cfo]
    if len(rows) >= 2 and all(needed):
        t, p = rows[-1], rows[-2]
        try:
            def v(row, col):
                x = row_num(row, col)
                if x is None:
                    raise ValueError(col)
                return x
            dsri = (v(t, rec) / v(t, rev)) / (v(p, rec) / v(p, rev))
            gmi = (v(p, gp) / v(p, rev)) / (v(t, gp) / v(t, rev))
            aqi_t = 1 - (v(t, ca) + v(t, ppe)) / v(t, ta)
            aqi_p = 1 - (v(p, ca) + v(p, ppe)) / v(p, ta)
            aqi = aqi_t / aqi_p if aqi_p else 1.0
            sgi = v(t, rev) / v(p, rev)
            depi = (v(p, dep) / (v(p, dep) + v(p, ppe))) / (v(t, dep) / (v(t, dep) + v(t, ppe)))
            sgai = (v(t, sga) / v(t, rev)) / (v(p, sga) / v(p, rev))
            tata = (v(t, ni) - v(t, cfo)) / v(t, ta)
            lvgi = (v(t, tl) / v(t, ta)) / (v(p, tl) / v(p, ta))
            m = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
                 + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
            detail = (f"M={m:.2f} | DSRI={dsri:.2f} GMI={gmi:.2f} AQI={aqi:.2f} SGI={sgi:.2f} "
                      f"DEPI={depi:.2f} SGAI={sgai:.2f} TATA={tata:.3f} LVGI={lvgi:.2f}")
            if m > -1.78:
                add(issues, "P1", "FORENSIC_MSCORE_FLAG",
                    f"Beneish M-Score = {m:.2f} > -1.78, masuk zona dicurigai manipulasi laba, perlu pengecekan manual per komponen.", detail, path)
            else:
                add(issues, "P3", "FORENSIC_MSCORE_INFO", f"Beneish M-Score = {m:.2f} (ambang -1.78, tidak terlampaui).", detail, path)
        except (ValueError, ZeroDivisionError):
            add(issues, "P3", "FORENSIC_MSCORE_SKIPPED", "Kolom yang dibutuhkan M-Score ada tapi mengandung nilai hilang/nol, perhitungan dilewati.", "", path)


def check_financials(path: str, issues: List[Issue]) -> None:
    rows, aliases = load_csv(path)
    if not rows:
        add(issues, "P1", "FINANCIALS_EMPTY", "CSV data keuangan tidak memiliki baris data.", file=path)
        return

    period = pick(aliases, ["period", "fiscal_period", "date", "periode", "财期", "期间"])
    revenue = pick(aliases, ["revenue", "sales", "pendapatan", "收入", "营收"])
    gross_profit = pick(aliases, ["gross_profit", "grossprofit", "laba_kotor", "毛利"])
    operating_income = pick(aliases, ["operating_income", "operatingincome", "ebit", "laba_operasi", "营业利润", "经营利润"])
    net_income = pick(aliases, ["net_income", "netincome", "laba_bersih", "净利润"])
    cfo = pick(aliases, ["cfo", "operating_cash_flow", "cash_from_operations", "arus_kas_operasi", "经营现金流"])
    capex = pick(aliases, ["capex", "capital_expenditure", "capitalexpenditure", "belanja_modal", "资本开支"])
    fcf = pick(aliases, ["fcf", "free_cash_flow", "freecashflow", "arus_kas_bebas", "自由现金流"])
    shares = pick(aliases, ["shares", "diluted_shares", "share_count", "jumlah_saham", "saham_terdilusi", "股本", "稀释股数"])
    eps = pick(aliases, ["eps", "diluted_eps", "laba_per_saham", "每股收益"])
    cash_begin = pick(aliases, ["cash_begin", "beginning_cash", "kas_awal", "期初现金"])
    cash_end = pick(aliases, ["cash_end", "ending_cash", "kas_akhir", "期末现金"])
    cfi = pick(aliases, ["cfi", "investing_cash_flow", "arus_kas_investasi", "投资现金流"])
    cff = pick(aliases, ["cff", "financing_cash_flow", "arus_kas_pendanaan", "融资现金流"])
    gross_margin = pick(aliases, ["gross_margin", "grossmargin", "margin_kotor", "毛利率"])
    operating_margin = pick(aliases, ["operating_margin", "operatingmargin", "margin_operasi", "营业利润率", "经营利润率"])
    net_margin = pick(aliases, ["net_margin", "netmargin", "margin_bersih", "净利率"])
    fcf_margin = pick(aliases, ["fcf_margin", "fcfmargin", "margin_fcf", "自由现金流率"])
    yoy_revenue = pick(aliases, ["revenue_yoy", "yoy_revenue", "revenue_yoy_pct", "营收同比"])
    qoq_revenue = pick(aliases, ["revenue_qoq", "qoq_revenue", "revenue_qoq_pct", "营收环比"])

    if not period:
        add(issues, "P2", "FINANCIALS_NO_PERIOD_COLUMN", "CSV data keuangan tidak memiliki kolom periode.", file=path)
    if not revenue:
        add(issues, "P1", "FINANCIALS_NO_REVENUE_COLUMN", "CSV data keuangan tidak memiliki kolom revenue, banyak rasio tidak bisa diverifikasi ulang.", file=path)

    for idx, row in enumerate(rows):
        label = row.get(period, f"row {idx + 2}") if period else f"row {idx + 2}"
        check_ratio(issues, path, label, row, gross_profit, revenue, gross_margin, "GROSS_MARGIN_MISMATCH", "Margin kotor")
        check_ratio(issues, path, label, row, operating_income, revenue, operating_margin, "OPERATING_MARGIN_MISMATCH", "Margin operasi")
        check_ratio(issues, path, label, row, net_income, revenue, net_margin, "NET_MARGIN_MISMATCH", "Margin bersih")
        check_ratio(issues, path, label, row, fcf, revenue, fcf_margin, "FCF_MARGIN_MISMATCH", "Margin FCF")

        cfo_v = row_num(row, cfo)
        capex_v = row_num(row, capex)
        fcf_v = row_num(row, fcf)
        if cfo_v is not None and capex_v is not None and fcf_v is not None:
            expected = cfo_v - abs(capex_v) if capex_v >= 0 else cfo_v + capex_v
            if not close_enough(expected, fcf_v):
                add(issues, "P1", "FCF_RECONCILIATION_MISMATCH", f"FCF pada {label} tidak konsisten dengan CFO/Capex.", f"expected={expected}, provided={fcf_v}, cfo={cfo_v}, capex={capex_v}", path)

        net_income_v = row_num(row, net_income)
        shares_v = row_num(row, shares)
        eps_v = row_num(row, eps)
        if net_income_v is not None and shares_v not in (None, 0) and eps_v is not None:
            expected = net_income_v / shares_v
            if not close_enough(expected, eps_v, rel_tol=0.025, abs_tol=0.03):
                add(issues, "P2", "EPS_RECONCILIATION_MISMATCH", f"EPS pada {label} tidak konsisten dengan laba bersih/jumlah saham, periksa satuannya.", f"expected={expected}, provided={eps_v}, net_income={net_income_v}, shares={shares_v}", path)

        if cash_begin and cash_end and cfo and cfi and cff:
            cb = row_num(row, cash_begin)
            ce = row_num(row, cash_end)
            cfo_v = row_num(row, cfo)
            cfi_v = row_num(row, cfi)
            cff_v = row_num(row, cff)
            if None not in (cb, ce, cfo_v, cfi_v, cff_v):
                expected = cb + cfo_v + cfi_v + cff_v
                if not close_enough(expected, ce):
                    add(issues, "P1", "CASH_FLOW_ROLL_FORWARD_MISMATCH", f"Laporan arus kas pada {label} tidak konsisten secara perhitungan roll-forward.", f"expected_ending_cash={expected}, provided={ce}", path)

    check_growth(issues, path, rows, period, revenue, yoy_revenue, 4, "REVENUE_YOY_MISMATCH", "Revenue YoY")
    check_growth(issues, path, rows, period, revenue, qoq_revenue, 1, "REVENUE_QOQ_MISMATCH", "Revenue QoQ")

    check_forensics(rows, aliases, path, issues)


def sort_issues(issues: Iterable[Issue]) -> List[Issue]:
    return sorted(issues, key=lambda x: (SEVERITY_RANK.get(x.severity, 9), x.code, x.file))


def print_report(issues: List[Issue], as_json: bool = False) -> None:
    ordered = sort_issues(issues)
    if as_json:
        print(json.dumps([issue.__dict__ for issue in ordered], ensure_ascii=False, indent=2))
        return
    if not ordered:
        print("Pengecekan konsistensi keuangan/valuasi LOLOS: tidak ditemukan anomali yang bisa dihitung ulang.")
        return
    counts = {}
    for issue in ordered:
        counts[issue.severity] = counts.get(issue.severity, 0) + 1
    summary = " ".join(f"{sev}={counts.get(sev, 0)}" for sev in ["P0", "P1", "P2", "P3"])
    print(f"Pengecekan konsistensi keuangan/valuasi menemukan {len(ordered)} isu: {summary}\n")
    for issue in ordered:
        print(issue.line())


def run(args) -> int:
    issues: List[Issue] = []
    assumptions = None
    if args.assumptions:
        assumptions = check_assumptions(args.assumptions, issues)
    if args.report:
        check_report(args.report, assumptions, issues, args.industry, args.language)
    if args.financials:
        check_financials(args.financials, issues)
    if not any([args.report, args.assumptions, args.financials]):
        add(issues, "P1", "NO_INPUT", "Berikan minimal salah satu dari --report, --assumptions, atau --financials.")
    print_report(issues, args.json)
    fail_levels = {"P0", "P1"} if not args.strict else {"P0", "P1", "P2"}
    return 1 if any(issue.severity in fail_levels for issue in issues) else 0


def write_demo_files(tmp: str) -> Tuple[str, str, str]:
    report = os.path.join(tmp, "demo_report.md")
    assumptions = os.path.join(tmp, "demo_assumptions.json")
    financials = os.path.join(tmp, "demo_financials.csv")
    with open(report, "w", encoding="utf-8") as f:
        f.write(
            "# Demo (DEMO) Laporan Riset Investasi Saham\n\n"
            "Per 2026-07-21, sumber Demo. Penilaian saya: perusahaan dinilai wajar.\n\n"
            "Lampiran industri: saas.\n\n"
            "| NRR | RPO | Rule of 40 |\n|---:|---:|---:|\n| 110% | 100 | 35% |\n\n"
            "> Penilaian nilai intrinsik: Wajar | Arah perdagangan pasar 1-3 bulan: netral | Tindakan investasi: tunggu dan amati.\n"
            "> Pasar paling mungkin akan trading dulu pertumbuhan revenue dan recovery FCF; falsifikasi upside: pertumbuhan akselerasi signifikan; falsifikasi downside: FCF terus memburuk.\n\n"
            "Valuasi dijalankan lewat scripts/dcf.py, mencakup reverse DCF, DCF skenario, EPV / earnings power value.\n\n"
            "Registrasi prediksi: pertumbuhan revenue 10%-15%, tanggal verifikasi 2026-10-31.\n\n"
            "Sumber data dan timestamp: Demo 2026-07-21. Tidak diperoleh: tidak ada.\n"
        )
    with open(assumptions, "w", encoding="utf-8") as f:
        json.dump(
            {
                "price": 100.0,
                "shares": 10.0,
                "net_debt": 5.0,
                "wacc": 0.09,
                "terminal_g": 0.03,
                "range_low": 80.0,
                "range_high": 110.0,
                "scenarios": [
                    {"name": "bear", "prob": 0.3, "evidence_strength": "sedang", "revenue": [100, 105], "fcf_margin": [0.10, 0.11]},
                    {"name": "base", "prob": 0.5, "evidence_strength": "sedang", "revenue": [100, 115], "fcf_margin": [0.12, 0.14]},
                    {"name": "bull", "prob": 0.2, "evidence_strength": "lemah", "revenue": [100, 130], "fcf_margin": [0.15, 0.18]},
                ],
                "epv": {
                    "earnings_basis": "NOPAT",
                    "normalized_earnings": 12.0,
                    "coc": 0.09,
                    "shares": 10.0,
                    "net_debt": 5.0,
                    "growth": {"g": 0.03, "roiic": 0.18},
                },
            },
            f,
            ensure_ascii=False,
            indent=2,
        )
    with open(financials, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["period", "revenue", "gross_profit", "gross_margin", "cfo", "capex", "fcf", "fcf_margin"])
        writer.writerow(["Q1", "100", "60", "60%", "30", "10", "20", "20%"])
        writer.writerow(["Q2", "110", "66", "60%", "33", "11", "22", "20%"])
    return report, assumptions, financials


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", help="Path laporan Markdown")
    ap.add_argument("--assumptions", help="Path JSON asumsi valuasi, disarankan pakai config dari dcf.py")
    ap.add_argument("--financials", help="Path CSV data keuangan historis/prediksi")
    ap.add_argument("--industry", action="append", help="Slug aturan industri, bisa diulang atau dipisah koma; isi 'auto' untuk membaca deklarasi lampiran industri dari laporan")
    ap.add_argument("--language", choices=["auto", "id", "zh", "en"], default="auto", help="Bahasa laporan; auto menentukan dari judul standar")
    ap.add_argument("--list-industries", action="store_true", help="Tampilkan slug industri yang tersedia lalu keluar")
    ap.add_argument("--json", action="store_true", help="Tampilkan hasil pengecekan dalam format JSON")
    ap.add_argument("--strict", action="store_true", help="P2 juga mengembalikan exit code non-zero")
    ap.add_argument("--demo", action="store_true", help="Jalankan contoh bawaan")
    args = ap.parse_args()
    if args.list_industries:
        for slug, rule in load_industry_rules().items():
            print(f"{slug}\t{rule.get('name_id', rule.get('name_zh', ''))}\t{rule['appendix']}")
        return
    if args.demo:
        with tempfile.TemporaryDirectory() as tmp:
            report, assumptions, financials = write_demo_files(tmp)
            args.report, args.assumptions, args.financials = report, assumptions, financials
            sys.exit(run(args))
    sys.exit(run(args))


if __name__ == "__main__":
    main()
