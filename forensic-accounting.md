# Pemeriksaan Kualitas Laporan Keuangan (Forensic Accounting)

Tujuan: menjawab pertanyaan yang lebih fundamental sebelum melakukan valuasi — **apakah laba ini benar-benar nyata**. Modul ini menghasilkan "grade kredibilitas laporan keuangan (A/B/C/D)" yang langsung terhubung ke item veto di Bagian 8 `valuation-methods.md`: untuk grade C, aksi maksimum hanya sampai "wait and see"; untuk grade D selalu "avoid/hindari" dan wajib diberi peringatan eksplisit di bab pertama.

Disiplin eksekusi: semua metrik yang dapat dihitung direview ulang secara otomatis oleh `scripts/check_research_output.py --financials` (persyaratan nama kolom lihat Bagian 7); item yang datanya tidak dapat diperoleh ditulis "tidak diperoleh", tidak boleh memberi nilai berdasarkan kesan semata.

## 1. Kualitas Akrual (Accruals, Anomali Sloan)

Laba = kas + akrual. Semakin tinggi proporsi akrual, semakin rendah kualitas laba dan semakin buruk return masa depan (Sloan, 1996).

- **Rasio Total Akrual = (Net Income − Arus Kas Operasi) ÷ Rata-Rata Total Aset**. Acuan empiris: < 0 (laba kas melebihi laba buku) tergolong baik; 0–5% normal; **> 10% red flag**.
- **Rasio Konversi Kas = CFO ÷ Net Income**, lihat tren 3–5 tahun. Jika secara jangka panjang < 80% dan terus menurun wajib dijelaskan; laba tumbuh tetapi konversi kas memburuk adalah risiko inti, bukan catatan kaki.
- Dekomposisi akrual: berapa kontribusi perubahan piutang, inventori, utang usaha, dan deferred masing-masing; akrual besar yang bersifat one-off (seperti akuisisi) dicantumkan tersendiri agar tidak mencemari tren.

## 2. Beneish M-Score (Probabilitas Manipulasi Laba)

Model delapan variabel, membandingkan tahun ini (t) dengan tahun sebelumnya (t-1):

```text
M = −4,84 + 0,92·DSRI + 0,528·GMI + 0,404·AQI + 0,892·SGI
    + 0,115·DEPI − 0,172·SGAI + 4,679·TATA − 0,327·LVGI
```

| Variabel | Makna | Perhitungan | Arah Berbahaya |
|---|---|---|---|
| DSRI | Indeks Piutang/Pendapatan | (Piutang_t/Pendapatan_t) ÷ (Piutang_t-1/Pendapatan_t-1) | ↑ pengakuan pendapatan dipercepat |
| GMI | Indeks Margin Kotor | Margin Kotor_t-1 ÷ Margin Kotor_t | ↑ margin kotor memburuk memicu manipulasi |
| AQI | Indeks Kualitas Aset | Rasio aset non-lancar non-PP&E | ↑ kapitalisasi biaya |
| SGI | Indeks Pertumbuhan Pendapatan | Pendapatan_t ÷ Pendapatan_t-1 | ↑ perusahaan growth tinggi lebih bermotif |
| DEPI | Indeks Tarif Depresiasi | Tarif Depresiasi_t-1 ÷ Tarif Depresiasi_t | ↑ memperlambat depresiasi |
| SGAI | Indeks Rasio Biaya | Rasio SGA_t ÷ Rasio SGA_t-1 | ↑ efisiensi memburuk |
| TATA | Total Akrual/Total Aset | (Net Income − CFO) ÷ Total Aset | ↑ bobot terbesar |
| LVGI | Indeks Leverage | Leverage_t ÷ Leverage_t-1 | ↑ tekanan default |

Interpretasi: **M > −1,78 → masuk zona "kemungkinan manipulasi"** (ambang model asli). Ini bukan putusan bersalah, melainkan memasukkan perusahaan tersebut ke dalam daftar "pemeriksaan manual item per item". Tidak berlaku untuk saham finansial (struktur aset-liabilitasnya berbeda), gunakan item pengganti industri di Bagian 6.

## 3. Red Flag Pengakuan Pendapatan

- **Divergensi DSO**: pertumbuhan piutang terus-menerus > pertumbuhan pendapatan (DSO naik 2 tahun berturut-turut atau lebih) → channel stuffing / pelonggaran kredit / pengakuan dini.
- **Divergensi deferred revenue/contract liability** (item fatal untuk bisnis subscription): pendapatan berakselerasi sementara deferred revenue melambat atau bahkan turun → pertumbuhan menguras masa depan.
- Kontrak jangka panjang (metode percentage of completion/POC), bill-and-hold, channel stuffing ke distributor, transaksi berulang dengan pihak terafiliasi, pengiriman mendadak di akhir kuartal (proporsi Q4 yang anomali).
- Restatement historis, pergantian kebijakan pengakuan pendapatan, reklasifikasi segmen yang membuat tidak dapat diperbandingkan → wajib dijembatani (bridge); jika jembatan tidak seimbang, itu adalah red flag.

## 4. Kapitalisasi Biaya dan Perataan Laba (Earnings Smoothing)

- Proporsi dan tren kapitalisasi biaya pengembangan/software/biaya akuisisi pelanggan; **capex secara jangka panjang > 2× depresiasi-amortisasi** sementara rasio perputaran aset tidak meningkat sepadan → kemungkinan biaya disembunyikan ke dalam balance sheet.
- Rincian inventori: divergensi pertumbuhan bahan baku vs barang jadi (penumpukan barang jadi = indikator leading pelemahan demand).
- Ritme impairment: tidak melakukan write-down saat bull market, melakukan "big bath" bersamaan saat pergantian CEO; apakah tingkat provisi (bad debt/garansi/retur) berfluktuasi countercyclical (alat perataan laba).
- "Laba/rugi non-recurring" yang muncul 3 tahun berturut-turut atau lebih → reklasifikasi sebagai recurring, langsung sesuaikan ke laba ternormalisasi.

## 5. Sinyal Struktur dan Governance (Non-Kuantitatif, tetapi Berbobot Tinggi)

- Auditor: bukan Big Four/pergantian auditor yang sering/biaya audit yang anomali rendah, defisiensi material pada internal control (SOX 302/404), opini non-standar.
- SDM: CFO/ketua komite audit mengundurkan diri secara mendadak; publikasi laporan keuangan yang ditunda.
- Regulasi: tema dan frekuensi SEC comment letter/surat pertanyaan bursa; tuduhan inti dari laporan short-seller dan kualitas tanggapan perusahaan.
- Transaksi pihak terafiliasi: kewajaran harga, sirkulasi dana di luar pembukuan (supplier/customer yang terafiliasi dengan pengendali aktual); untuk saham A China, cek tambahan rasio gadai saham (share pledge) dan penggunaan dana oleh pihak terkait (lihat `markets-cn-hk.md`).
- Struktur insentif: menggunakan metrik adjusted (terutama Non-GAAP EPS yang mengecualikan SBC) sebagai basis penilaian kinerja → motif manipulasi sudah terbangun secara struktural.

## 6. Item Pengganti Industri

Keuangan/asuransi tidak menggunakan akrual dan M-Score, melainkan memeriksa: migrasi klasifikasi pinjaman dan pinjaman yang direstrukturisasi, perubahan countercyclical pada provision coverage ratio, proporsi aset keuangan Level 3, kontribusi pelepasan reserve terhadap laba (asuransi), pengaturan reasuransi. REIT memeriksa item penyesuaian AFFO dan bunga yang dikapitalisasi. Energi memeriksa restatement cadangan (reserve) dan basis perhitungan DD&A.

## 7. Integrasi dengan Checker (Konvensi Nama Kolom)

`check_research_output.py --financials` secara otomatis menghitung dan mengeluarkan isu P1/P2 ketika CSV memuat kolom-kolom berikut:

- Wajib (rasio akrual): `net_income`, `cfo`, `total_assets`
- M-Score membutuhkan tambahan: `revenue`, `receivables`, `gross_profit`, `ppe`, `current_assets`, `depreciation`, `sga`, `total_liabilities`
- Divergensi DSO/deferred membutuhkan tambahan: `receivables`, `deferred_revenue` (opsional)

## 8. Rating Kredibilitas Laporan Keuangan (Pra-Registrasi)

| Grade | Kriteria Penentuan | Dampak Wajib terhadap Kesimpulan |
|---|---|---|
| A | Tidak ada red flag; konversi kas ≥ 90%; akrual < 5%; governance bersih | Tidak ada batasan |
| B | 1–2 red flag ringan (misalnya akrual tinggi pada satu tahun saja) dengan penjelasan yang wajar | Tidak ada batasan, tetapi masuk daftar pemantauan |
| C | M-Score melampaui ambang, divergensi DSO/deferred yang persisten, "non-recurring" yang berulang, 1 red flag governance yang serius | **Aksi maksimum "wait and see"**, bab pertama laporan wajib memberi peringatan |
| D | Beberapa red flag serius menumpuk / ada indikasi bukti kecurangan / opini audit non-standar | **Avoid/hindari**, bab valuasi diubah menjadi "valuasi tidak bermakna sampai kredibilitas pulih" |

Rating dan bukti per item ditulis di sub-bab "Kualitas Laporan Keuangan" pada Bab V laporan; untuk grade C/D, dilarang menggunakan "valuasi murah" sebagai penyeimbang — murah adalah kedok paling umum dari kecurangan.
