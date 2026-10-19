# Standar Format Output dan Keterbacaan

Tujuan: kedalaman tidak berarti harus sulit dibaca. Keterbacaan riset institusional berasal dari **kesimpulan di awal, informasi berjenjang, standar penulisan angka, dan jangkar visual**. Wajib membaca file ini sebelum menulis isi laporan.

## 1. Header Laporan (Tiga Komponen)

Berurutan: kotak kesimpulan → Tearsheet → tabel Expectations Gap. Pembaca harus memperoleh informasi keputusan yang lengkap dalam 60 detik.

**Bahasa laporan**: default menggunakan bahasa permintaan pengguna; jika pengguna tidak menyebutkan secara eksplisit, gunakan bahasa komunikasi umum antara pengguna dan Agent dalam percakapan saat ini. Jika pengguna menentukan bahasa secara eksplisit, ikuti itu. Judul, nama bab, penanda data yang hilang, penanda fakta/penilaian, disclaimer, dan keterangan grafik harus konsisten menggunakan satu bahasa; laporan berbahasa Inggris menggunakan penanda setara seperti `My view` / `Not obtained` / `Sources and timestamps`.

**Kotak kesimpulan** (blockquote, ditempatkan di layar pertama setelah judul):

> **Penilaian nilai intrinsik: Undervalued**｜**Arah perdagangan pasar 1–3 bulan ke depan: Bias naik**｜**Aksi investasi: Beli secara bertahap (dollar-cost)**
> (Label valuasi dihasilkan oleh aturan kalibrasi｜Kredibilitas laporan keuangan A｜Tingkat keyakinan: Menengah-tinggi)
> Tesis satu kalimat: Pasar memberi harga pada X seolah Y, tetapi bukti Z menunjukkan……
> Rentang valuasi gabungan $L–$H (harga saat ini $P, implied upside +a% ~ +b%)｜Penggugur upside: ……｜Penggugur downside: ……

**Tearsheet** (tabel ringkasan satu halaman): harga saat ini/kapitalisasi pasar/rentang 52 minggu/multiple kunci/moat/kredibilitas laporan keuangan/katalis Top1/penggugur upside Top1/penggugur downside Top1, setiap baris disertai sumber+timestamp.

**Disiplin pemisahan arah**: penilaian nilai intrinsik menjawab "berapa nilainya", arah perdagangan pasar menjawab "variabel apa yang paling mungkin diperdagangkan pasar dalam 1–3 bulan ke depan", aksi investasi menjawab "bagaimana bertindak dengan odds dan ketidakpastian saat ini". Ketiganya bisa berbeda, tetapi tidak boleh dicampur menjadi satu kesimpulan tunggal.

Laporan berbahasa Inggris dapat menggunakan header setara:

> **Intrinsic value view: Undervalued** | **1-3 month market trading direction: Upward bias** | **Action: Accumulate in tranches**
> (Valuation label from the calibration rule | Earnings credibility A | Confidence: Medium-high)
> One-sentence thesis: The market prices X as Y, but evidence Z suggests...
> Fair value range $L-$H (current price $P, implied upside +a% to +b%) | Upside invalidation: ... | Downside invalidation: ...

## 2. Cara Penulisan Bab

- Baris pertama setiap bab: **"Poin utama bab ini:" + kesimpulan ≤2 kalimat**. Berikan jawaban dulu baru argumentasinya, agar pembaca bisa membaca cepat hanya dari poin utama.
- Laporan berbahasa Inggris, baris pertama setiap bab menggunakan **"Key takeaways:"**; laporan berbahasa Indonesia menggunakan **"Poin utama bab ini:"**.
- Paragraf ≤5 baris; jika lebih, pecah atau ubah menjadi tabel. Waspadai 3 paragraf berturut-turut tanpa angka — biasanya itu basa-basi kosong.
- "Fakta" dan "penilaian saya" dipisahkan secara eksplisit dengan penanda; kalimat penilaian wajib disertai nomor acuan atau data pendukung.
- Prinsip kedekatan tabel-teks: tabel ditempatkan langsung setelah argumen yang mengutipnya, jangan dikumpulkan di akhir bab.

## 3. Standar Penulisan Angka

- Gunakan separator ribuan; simbol mata uang + satuan dideklarasikan sekali ("berikut ini tanpa keterangan lain berarti $B"); persentase dibulatkan 1 desimal, nilai per saham dibulatkan ke bilangan bulat atau 1 desimal.
- **Presisi harus sesuai tingkat ketidakpastian**: output DCF ditulis "$185–$240" bukan "$212,47" — berpura-pura presisi adalah kepalsuan yang berlagak ilmiah.
- YoY/QoQ menggunakan tanda +/−; angka negatif tidak menggunakan tanda kurung (dalam konteks laporan bahasa Indonesia).
- Setiap tabel mencantumkan kolom "sumber/waktu" atau catatan kaki tabel.

## 4. Elemen Visual (Dirender sebagai Teks, Terbaca Langsung di Markdown)

**Grafik Valuasi Football Field** (wajib di bab ringkasan valuasi):

```text
Reverse DCF (penggugur)   │────implied pasar────│
DCF tertimbang skenario       ▓▓▓▓▓▓▓▓▓ 170———225
Three-factor/EPV            ▓▓▓▓▓▓ 150———195
Relative valuation             ▓▓▓▓▓▓▓▓ 165———215
EVA/residual income          ▓▓▓▓▓▓▓ 160———205
Rentang gabungan [L———————H]        harga saat ini P ▼
```

Gambar menggunakan blok kode monospace + karakter ▓/─ secara proporsional; harga saat ini ditandai dengan ▼. Jika output berupa .docx/.xlsx, dapat diganti dengan grafik sungguhan.

**Anotasi heatmap sensitivitas**: pada tabel 3×3, tebalkan sel yang nilainya di atas harga saat ini, agar "pada asumsi apa harga saat ini masuk akal" terlihat sekali pandang.

**Tabel jembatan (bridge table)** (revenue bridge/fair value bridge): titik awal → masing-masing item driver (+/−) → titik akhir, satu baris per driver.

## 5. Daftar Barang yang Diserahkan (Deliverables)

**Prinsip: hanya file laporan itu sendiri yang diserahkan ke pengguna**; semua produk antara (JSON, output skrip, CSV) adalah dokumentasi internal, tidak masuk dalam daftar penyerahan.

| Produk | Peran | Keterangan |
|---|---|---|
| Laporan sembilan bab **PDF** | **Deliverable (default)** | Jika pengguna tidak menentukan format, selalu diserahkan sebagai PDF; dikonversi dari sumber .md (skill pdf atau toolchain md→PDF), pastikan font dan rendering tabel sesuai bahasa laporan |
| Laporan .md / .docx / workbook .xlsx | Deliverable (hanya jika diminta pengguna) | Workbook xlsx memuat empat halaman: asumsi/DCF/skenario/output (skill xlsx) |
| Tearsheet | Deliverable (tertanam) | Tertanam di header laporan, bukan file terpisah |
| JSON asumsi valuasi | Dokumentasi internal | Config `dcf.py`, disimpan di working directory untuk dihitung ulang; asumsi kunci ditulis sebagai ringkasan di lampiran laporan |
| Output checker | Dokumentasi internal | Ringkasan hasil ditulis di lampiran laporan |
| CSV keuangan / output mentah skrip | Dokumentasi internal | Diberikan hanya jika pengguna memintanya |

## 6. Disiplin Panjang dan Densitas

- Kedalaman = densitas informasi × kelengkapan cakupan, bukan jumlah kata. Setiap bab wajib diperiksa sendiri: "paragraf mana yang jika dihapus tidak merugikan pembaca?" Jika bisa dihapus, hapus.
- Acuan orde besaran: badan laporan mode lengkap 6.000–12.000 kata + 15–25 tabel; mode laporan keuangan 4.000–8.000 kata. Melebihi batas ini biasanya berarti mengulang data, bukan menganalisis.
- Lampiran menyimpan tabel data mentah yang panjang; badan laporan hanya memuat angka yang benar-benar digunakan dalam argumentasi.

## 7. Evaluasi Diri Tingkat Keyakinan (Wajib Dilampirkan di Akhir Bab IX)

| Dimensi | Skor (Tinggi/Menengah/Rendah) | Keterangan |
|---|---|---|
| Kelengkapan Data | | Proporsi data kunci yang berhasil diperoleh, rasio cakupan Tier 1 |
| Konvergensi Valuasi | | Tingkat overlap rentang dari berbagai metode |
| Kejelasan Expectations Gap | | Apakah variant view dapat digugurkan (falsifiable) |
| Kredibilitas Laporan Keuangan | A/B/C/D | Output dari modul forensic |
| **Tingkat Keyakinan Gabungan** | | Tingkat keyakinan rendah + label bagus ≠ posisi besar |

## 8. Keterlacakan Proyeksi (Forecast Traceability)

- Setiap proyeksi inti menggunakan rentang dan tanggal verifikasi yang jelas, jangan gunakan kalimat yang tidak dapat ditentukan jatuh temponya seperti "berprospek baik dalam jangka panjang".
- KPI operasional, jalur katalis, multiple valuasi, dan harga saham/total return dicatat secara terpisah; arah harga saham yang salah tidak otomatis berarti penilaian operasional salah, dan sebaliknya.
- Saat memperbarui laporan, pertahankan proyeksi lama dan timestamp aslinya, hanya tambahkan hasil aktual, status hit, atribusi error, dan penulisan ulang model.
- Status hit hanya menggunakan: hit, partial hit, miss, tidak dapat diverifikasi; "tidak dapat diverifikasi" wajib menjelaskan data yang hilang atau peristiwa yang tertunda.
- Laporan berbahasa Inggris menggunakan field setara seperti `Forecast register`, `Validation date`, `Hit / Partial hit / Miss / Not verifiable`.
