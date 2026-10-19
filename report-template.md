# Template Laporan: Struktur Sembilan Bab (v2)

Output harus mengikuti urutan bab berikut secara ketat. **Baca `references/output-format.md` sebelum menulis** (kotak kesimpulan/Tearsheet/poin utama bab/standar penulisan angka/cara membuat football field semuanya ada di sana). Jika data tidak tersedia, tulis "tidak diperoleh" atau "Not obtained" sesuai bahasa laporan, jangan membiarkan header tabel kosong tanpa isi.

Konvensi format: judul dibuat sesuai bahasa laporan; untuk bahasa Indonesia gunakan `# Nama Perusahaan (Kode) Laporan Riset Investasi Saham Individual`, untuk bahasa Inggris gunakan `# Company (Ticker) Equity Research Report`. Subjudul mencantumkan "Tanggal penulisan / Data cutoff / Mata uang laporan" atau padanan bahasa Inggrisnya `"Report date / Data cutoff / Reporting currency"`, baris berikutnya mendeklarasikan `Lampiran industri: <slug utama>[, <slug sekunder>]` atau `Industry appendix: <primary slug>[, <secondary slug>]`. Untuk saham dual listing A/H, akhir Bab VI dilampiri perbandingan kedua pasar, Bab I/IX diberi kesimpulan per pasar.

---

## I. Ringkasan Satu Halaman (Executive Summary)

Berurutan berisi:

1. **Kotak kesimpulan** (blockquote): trikotomi keputusan (penilaian nilai intrinsik / arah perdagangan pasar 1–3 bulan ke depan / aksi investasi) + grade kredibilitas laporan keuangan + tingkat keyakinan + tesis satu kalimat + rentang gabungan dan implied upside/downside + risiko terbesar.
2. **Tabel snapshot Tearsheet**: harga saat ini/kapitalisasi pasar/52 minggu/multiple kunci/moat/kredibilitas/katalis Top1/penggugur upside Top1/penggugur downside Top1 (setiap baris dengan sumber+timestamp).
3. **Tabel Expectations Gap** (alur analisis utama template ini, kerangkanya lihat `expectations-investing.md`): implied pasar vs ekspektasi saya vs persentil base rate, arah net expectations gap.
4. Masing-masing 3 argumen inti bullish-bearish (ringkas, dapat digugurkan/falsifiable).

Laporan berbahasa Inggris menggunakan judul bahasa Inggris dengan struktur sembilan bab yang sama: Executive Summary; Business Overview; Business and Competitive Analysis; Management, Governance, and Capital Allocation; Financial Analysis and Earnings Quality; Valuation; Analyst View Summary; Recent News and Catalysts; Investment Conclusion, Counter-Case, and Position Sizing. Field tabel, penanda data hilang, dan disclaimer secara serentak diubah ke bahasa Inggris.

## II. Detail Bisnis

Poin utama bab didahulukan. Uraian model bisnis, struktur pendapatan (lini bisnis/wilayah/pelanggan, tabel proporsi+pertumbuhan), konsentrasi, posisi dalam rantai industri.

| Lini Bisnis/Segmen | Pendapatan Terbaru | Proporsi | YoY | Catatan |
|---|---|---|---|---|

## III. Analisis Bisnis dan Kompetisi

Ruang industri dan posisi siklus; lanskap kompetisi dan tren market share; **tabel skor moat** (aset tak berwujud/switching cost/network effect/keunggulan biaya/skala, masing-masing diberi ada/tidak+kekuatan+dasar, kesimpulan gabungan tidak ada/sempit/luas) — wajib disilangkan dengan verifikasi finansial dari EPV/aset bersih dan EVA di Bab VI, bagian yang tidak konsisten wajib dijelaskan secara eksplisit; engine pertumbuhan dan titik penggugurnya.

## IV. Manajemen, Governance, dan Scorecard Alokasi Modal

Latar belakang eksekutif dan riwayat jabatan, kepemilikan saham internal dan konsistensi insentif, red flag governance. **Scorecard alokasi modal** (ditingkatkan jadi kuantitatif):

| Dimensi | Riwayat 5 Tahun Terakhir | Skor (Baik/Sedang/Buruk) | Dasar |
|---|---|---|---|
| Buyback | Harga buyback vs estimasi nilai intrinsik periode yang sama | | Membeli saat undervalued itu baik, membeli saat overvalued itu buruk |
| M&A | Riwayat impairment goodwill, ROIC lanjutan dari target akuisisi | | |
| Reinvestasi | ROIIC dari investasi inkremental | | Bersumber sama dengan modul EVA di Bab VI |
| Dividen | Rasio cakupan dan stabilitas | | |
| Dilusi Saham | SBC/pendapatan, net dilution rate | | |
| **Gabungan** | | | Penilaian buruk masuk pertimbangan item veto |

## V. Analisis Keuangan dan Kualitas Laporan Keuangan

**5.1 Tren Keuangan**: tabel 5 tahun pendapatan/margin kotor/margin operasi/FCF/ROIC/ROE + kesehatan balance sheet + tabel perbandingan perusahaan sejenis (mengikuti kerangka asli).

**5.2 Kualitas Laporan Keuangan (forensic, wajib)**: dieksekusi sesuai `forensic-accounting.md` — rasio akrual dan tren konversi kas, Beneish M-Score (hitung jika bisa), divergensi DSO/deferred, kebijakan kapitalisasi, sinyal governance; output **grade kredibilitas laporan keuangan A/B/C/D** dan tabel bukti per item:

| Item Pemeriksaan | Hasil | Penilaian | Bukti/Sumber |
|---|---|---|---|
| Rasio Akrual / Konversi Kas | | | |
| Beneish M-Score | | | |
| Red Flag Pengakuan Pendapatan | | | |
| Kapitalisasi Biaya | | | |
| Sinyal Governance/Audit | | | |
| **Grade Kredibilitas** | A/B/C/D | | Terhubung ke item veto Bab IX |

## VI. Valuasi (Validasi Silang Multi-Metode)

Dieksekusi sesuai `valuation-methods.md`, **minimal tiga metode**, urutan yang disarankan:

1. **Reverse DCF + PVGO** (pembuka: apa yang diimplikasikan harga saat ini, dibandingkan dengan base rates).
2. DCF tertimbang probabilitas tiga skenario (+ opsional distribusi Monte Carlo).
3. Three-factor/EPV (termasuk verifikasi finansial moat).
4. EVA/residual income (termasuk uji konsistensi g = RR×ROIIC).
5. Relative valuation (disiplin warranted multiple)/SOTP/metode khusus industri.

Output: tabel asumsi masing-masing metode (dilampiri persentil base rate dan kekuatan bukti saat ini) → **tabel ringkasan valuasi + grafik football field versi teks** → sensitivitas WACC×g (sel di atas harga saat ini ditebalkan) → rentang gabungan. Probabilitas tiga skenario wajib menjelaskan kekuatan bukti saat ini untuk bull/base/bear; jika salah satu skenario non-baseline sudah memiliki bukti menengah-kuat/kuat, tidak boleh hanya diperlakukan sebagai skenario tail kecuali dijelaskan secara eksplisit alasannya. Semua angka bersumber dari `scripts/dcf.py`, JSON asumsi disimpan sebagai dokumentasi.

## VII. Ringkasan Pandangan Analis

Distribusi rating/rentang dan median target harga/revisi terbaru; **titik perbedaan konsensus vs pandangan saya** (selaras dengan tabel Gap di Bab I — ini adalah bagian paling berharga dari laporan).

## VIII. Berita Terbaru dan Katalis

Peristiwa penting 1–3 bulan terakhir; jadwal katalis 6–12 bulan ke depan (bedakan jadwal yang sudah dikonfirmasi/target manajemen/ekspektasi pasar), tandai arah bullish/bearish dan logika dampaknya.

| Waktu | Peristiwa | Bullish/Bearish | Logika Dampak | Status Konfirmasi |
|---|---|---|---|---|

**8.1 Registrasi Proyeksi dan Verifikasi (Wajib)**: pecah tesis inti menjadi proyeksi operasional, katalis, dan valuasi yang dapat diverifikasi jatuh temponya. Simpan proyeksi asli beserta timestamp-nya, update selanjutnya hanya menambahkan hasil dan atribusi error, tidak boleh menulis ulang proyeksi asli.

| Objek Proyeksi | Nilai Baseline/Tanggal Cutoff | Rentang atau Arah Proyeksi | Tanggal Verifikasi | Indikator Leading dan Ambang | Kondisi Penggugur Upside/Downside | Status |
|---|---|---|---|---|---|---|

Laporan berbahasa Inggris menggunakan field setara: Forecast; Baseline/data cutoff; Range or direction; Validation date; Leading indicators and thresholds; Upside/downside invalidation; Status.

## IX. Kesimpulan Investasi, Argumen Counter-Case, dan Posisi

**9.1 Kesimpulan**: ulangi trikotomi keputusan dari Bab I (penilaian nilai intrinsik / arah perdagangan pasar 1–3 bulan ke depan / aksi investasi), dan jelaskan mengapa ketiganya bisa berbeda; jawab "jika ini adalah uang tunai hari ini, apakah saya akan membelinya? Mengapa?"

**9.2 Argumen Counter-Case / Pre-mortem Risiko (Wajib)**: beralih ke posisi counter-case, tulis "jika investasi ini gagal setahun dari sekarang, 3 alasan paling mungkin"; untuk setiap alasan berikan kekuatan bukti saat ini dan sinyal pemantauan. Argumen counter-case bukan basa-basi disclaimer — minimal satu harus merupakan serangan langsung terhadap tesis inti laporan; jika kekuatan bukti saat ini menengah-kuat/kuat, wajib jelaskan bagaimana itu mengubah arah perdagangan pasar, probabilitas skenario, atau aksi investasi di Bab I.

| Skenario Kegagalan | Mekanisme Pemicu | Kekuatan Bukti Saat Ini | Sinyal Pemantauan | Titik Waktu Penggugur |
|---|---|---|---|---|

Jika terdapat laporan versi sebelumnya atau proyeksi yang sudah jatuh tempo, lampirkan dahulu **tabel review proyeksi** di bagian ini. KPI operasional, jalur katalis, multiple valuasi, dan total return dinilai secara terpisah; perubahan harga saham tidak dapat sendirian membuktikan tesis operasional benar.

| Proyeksi Asli dan Timestamp | Hasil Aktual | Status Hit | Atribusi Error | Penulisan Ulang Model/Probabilitas |
|---|---|---|---|---|

**9.3 Pemikiran Posisi**: expected value (EV), rasio asimetri upside/downside, P(loss), orde besaran Kelly-lite (posisi kecil/menengah/standar; bukan rekomendasi alokasi).

**9.4 Checklist Pemantauan**: 3–5 indikator pemantauan berkelanjutan (KPI/jangkar valuasi/sinyal penggugur), masing-masing diberi ambang perhatian; minimal mencakup satu penggugur upside dan satu penggugur downside, arahnya tidak boleh tercampur.

**9.5 Tabel Evaluasi Diri Tingkat Keyakinan** (kerangka lihat Bagian 7 di `output-format.md`).

---

## Lampiran (Wajib)

1. **Daftar sumber data dan timestamp**: | Item Data | Sumber | Waktu |
2. **Ringkasan asumsi kunci valuasi** dan ringkasan hasil pemeriksaan `check_research_output.py` (JSON dan output mentah skrip adalah file dokumentasi internal, tidak diserahkan bersama laporan; diberikan jika pengguna meminta).
3. Disclaimer: bukan penasihat investasi berlisensi, tidak merupakan rekomendasi investasi.

Lampiran laporan berbahasa Inggris menggunakan judul setara: **Sources and timestamps**, **Key valuation assumptions and checker summary**, **Disclaimer: not investment advice**.
