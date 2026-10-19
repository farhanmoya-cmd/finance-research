# Manual Operasional Pasar Non-AS: Saham A China / Saham Hong Kong / Dual Listing A+H

Kondisi penerapan: saham target listing di Shanghai Stock Exchange (SSE), Shenzhen Stock Exchange (SZSE), atau Hong Kong Stock Exchange (HKEX). Saham AS tetap mengikuti manual utama di `data-sources.md`; file ini hanya menulis item-item yang berbeda. **Saham dengan dual listing (A/H) secara default harus dibandingkan dari kedua sisi dan diberi kesimpulan per pasar**, kecuali pengguna secara eksplisit hanya meminta satu sisi.

Daftar isi:
1. Validasi kode saham, pasar, dan sumber harga
2. Sumber pengungkapan primer
3. Morningstar dan data pihak ketiga
4. Tahun fiskal dan basis akuntansi
5. Modul analisis premium A/H (wajib untuk dual listing)
6. Item perbedaan pasar dalam valuasi dan kesimpulan
7. Daftar jebakan umum

---

## 1. Validasi Kode Saham, Pasar, dan Sumber Harga

**Aturan kode saham**: saham A China terdiri dari 6 digit angka (600xxx/601xxx/603xxx = papan utama Shanghai, 000xxx/001xxx = papan utama Shenzhen, 002xxx = papan SME lama, 300xxx = ChiNext/papan pertumbuhan, 688xxx = STAR Market/papan inovasi sains-teknologi); saham Hong Kong terdiri dari 4–5 digit angka (misalnya 0700, 2050, 9988). Perusahaan yang sama dengan listing A/H memiliki kode yang berbeda di kedua pasar (contoh: Sanhua Intelligent Controls 002050.SZ dan 2050.HK), sehingga kedua sisi harus dikonfirmasi secara terpisah untuk listing utama, mata uang, jumlah saham, dan harga pasarnya — jangan berasumsi satu query dapat menguraikan keduanya secara bersamaan.

**Prioritas sumber harga pasar**: bursa dan platform pengungkapan statutori > terminal/data profesional berizin > konektor broker yang tersedia > cross-check dua halaman harga pasar publik. Saham A China dapat dicek di SSE, SZSE, Beijing Stock Exchange, dan platform data profesional utama; saham Hong Kong dapat dicek di HKEX, platform data profesional, dan halaman harga pasar publik. Semua harga wajib mencantumkan waktu, mata uang, status intraday/closing, dan status delay.

Jika menggunakan konektor IBKR atau broker lain, lakukan validasi sesuai aturan berikut:
- Saham Hong Kong/H-share: `country_code` adalah `HK` (atau deskripsi mengandung HKEX/SEHK), `exchange` umumnya `SEHK`, mata uang HKD.
- Saham A China (via rekening internasional melalui Stock Connect Shanghai/Shenzhen-Hong Kong arah northbound): `exchange` sering berbentuk kode channel Connect seperti `SEHKNTL` (Shanghai Connect) / `SEHKSZSE` (Shenzhen Connect), dll. — **mengikuti hasil return dari `search_contracts`, jangan hardcode berdasarkan ingatan**; mata uang CNH/CNY.
- Jebakan yang sama seperti saham AS: perusahaan berbeda dengan nama sama, listing ganda GDR/ADR (sebagian perusahaan saham A memiliki GDR di Swiss/London, ADR di AS), serta produk leverage di sekitar saham yang populer. Rasio konversi ADR terhadap saham induk (misalnya 1 ADR = n saham) wajib dikonversi secara eksplisit saat membandingkan harga.
- Jika konektor tidak dapat menguraikan kontrak saham A atau akun tidak memiliki izin northbound, langsung beralih ke bursa, platform data profesional, atau halaman harga pasar publik; tidak mengharuskan pengguna menginstal IBKR, dan tidak berhenti karena tidak ada koneksi broker.

**Basis perhitungan harga pasar**: saham A China memiliki limit naik/turun harian ±10%/±20% dan settlement T+1; saham Hong Kong tidak memiliki limit naik/turun dan settlement T+0 dengan penyelesaian T+2; perhatikan perbedaan sistem ini saat membandingkan volatilitas intraday dan likuiditas. Nilai transaksi (turnover value) dikonversi ke mata uang yang sama saat dibandingkan.

## 2. Sumber Pengungkapan Primer

| Pasar | Platform Pengungkapan Statutori | Dokumen Kunci |
|---|---|---|
| Saham A China | Cninfo (巨潮资讯网, cninfo.com.cn — ditetapkan secara resmi sebagai platform wajib); situs resmi bursa sse.com.cn / szse.cn | Laporan tahunan/semesteran/kuartalan, pre-announcement/flash report laba, prospektus, tanggapan atas surat pertanyaan bursa, insentif saham karyawan, pengumuman pengurangan kepemilikan saham |
| Saham Hong Kong | HKEXnews (披露易, hkexnews.hk) | Laporan tahunan/tengah tahunan, profit warning, circular, disclosure of interests (DI), prospektus |

Poin perbedaan:
- Saham A China memiliki sistem **pre-announcement/flash report laba** (sinyal leading penting sebelum laporan resmi keluar, tidak ada mekanisme serupa di saham AS); saham Hong Kong memiliki sistem **profit warning**. Keduanya wajib dicek di bab katalis.
- Segmen dan konsentrasi pelanggan: untuk saham A China lihat bagian "Diskusi dan Analisis Kondisi Operasional" di laporan tahunan + catatan atas laporan audit; saham Hong Kong menggunakan catatan atas segmen berdasarkan HKFRS/IFRS pada laporan tahunan. Granularitas pengungkapan laporan tengah tahun saham Hong Kong umumnya lebih rendah dibanding laporan tahunan.
- Pemegang saham dan governance: saham A China melihat sepuluh pemegang saham utama/pemegang saham free-float (setiap kuartal), pengumuman gadai saham (share pledge); saham Hong Kong melihat disclosure of interests di HKEXnews (ambang 5%) dan perubahan kepemilikan saham direksi (peran yang setara dengan Form 4 di saham AS).
- Earnings call: sebagian besar saham A China tidak memiliki transkrip bahasa Inggris, cari dengan kata kunci "业绩说明会 纪要/实录" (ringkasan/transkrip earnings briefing); perusahaan kapitalisasi besar saham Hong Kong umumnya memiliki materi earnings call bilingual Mandarin-Inggris (halaman IR perusahaan).

## 3. Morningstar dan Data Pihak Ketiga

- Segmen URL bursa pada Morningstar menggunakan kode MIC: saham Hong Kong `xhkg`, Shanghai `xshg`, Shenzhen `xshe`. Contoh: `morningstar.com/stocks/xhkg/00700/quote`.
- **Peringatan cakupan**: cakupan analis Morningstar untuk saham A China/Hong Kong jauh lebih jarang dibanding saham AS, banyak saham hanya memiliki Quantitative Rating, bukan fair value dari analis — keduanya memiliki makna berbeda, laporan wajib menandai mana yang digunakan; jika keduanya tidak ada, tulis "tidak diperoleh" untuk jangkar fair value yang hilang, dan gunakan metode lain untuk mengisinya, jangan dipaksakan.
- Konsensus analis diutamakan dari FactSet, LSEG, Bloomberg, S&P Capital IQ, Visible Alpha, Wind, Choice, dan platform lain yang dapat menampilkan jumlah cakupan dan tanggal statistik; jika tidak memiliki akses, saham A China dapat menggunakan agregasi Eastmoney (东方财富)/THS iFinD (同花顺), saham Hong Kong dapat menggunakan aastocks, halaman publik Futu (富途), atau etnet (经济通). Basis perhitungan agregator minimal dicek ulang di dua tempat.
- Data keuangan untuk cross-check dapat menggunakan Wind, Choice, THS iFinD, Lixinger (理杏仁), Eastmoney, aastocks, Futu, dll.; **tetap mengutamakan pengajuan asli dari Cninfo/bursa/HKEXnews sebagai acuan**.

## 4. Tahun Fiskal dan Basis Akuntansi

- Saham A China: regulasi mengharuskan tahun kalender (tutup tahun 31 Desember), tidak ada jebakan pergeseran tahun fiskal seperti saham AS; tetapi perhatikan bahwa **laporan kuartalan tidak diaudit, laporan semesteran umumnya juga tidak diaudit**, sehingga kredibilitas datanya berjenjang.
- Saham Hong Kong: tidak ada tanggal tutup tahun yang diwajibkan. 31 Desember paling umum, **31 Maret juga sering digunakan** (contoh: Lenovo Group); Hang Seng/HSBC dan lainnya masing-masing memiliki konvensi sendiri. Wajib cek dahulu tanggal tutup tahun sebelum melakukan perbandingan YoY dan anualisasi valuasi.
- Standar akuntansi: saham A China menggunakan CAS (Chinese Accounting Standards, sangat konvergen dengan IFRS tetapi ada perbedaan, misalnya instrumen keuangan dan penyajian subsidi pemerintah); saham Hong Kong menggunakan HKFRS/IFRS. Laporan A-share dan H-share dari perusahaan yang sama pada dasarnya memiliki basis konsolidasi yang sama karena berada dalam kerangka standar yang sama, tetapi **granularitas pengungkapan dan pembagian segmen antara laporan A-share dan H-share bisa berbeda**; saat rekonsiliasi, jadikan laporan yang lebih detail sebagai acuan.
- Mata uang: laporan saham A China dalam CNY; perusahaan daratan China yang listing di Hong Kong umumnya tetap melaporkan dalam CNY tetapi bertransaksi dalam HKD — konversi valuasi menggunakan kurs pada tanggal laporan dan wajib dicantumkan.

## 5. Modul Analisis Premium A/H (Wajib untuk Dual Listing)

**Definisi tingkat premium**: `Premium A/H = Harga Saham A × (kurs CNY→HKD) ÷ Harga Saham H − 1`. Angka positif berarti saham A lebih mahal.

Empat hal wajib dilakukan:
1. **Premium saat ini + persentil historis**: hitung tingkat premium saat ini, bandingkan dengan distribusi persentil premium saham tersebut sejak listing; untuk level pasar secara keseluruhan gunakan **Hang Seng Stock Connect AH Premium Index (HSAHP)** sebagai acuan, untuk menilai apakah premium saham individual disebabkan "faktor spesifik saham" atau "level pasar secara umum".
2. **Atribusi penyebab struktural**: perbedaan likuiditas (rata-rata nilai transaksi harian kedua pasar), struktur investor (proporsi investor ritel saham A vs institusi/dana southbound saham Hong Kong), kontrol modal (arbitrase tidak dapat dieksekusi secara penuh, premium dapat bertahan dalam jangka panjang — **jangan menganggap premium sebagai peluang arbitrase yang pasti akan konvergen**), apakah masuk dalam Stock Connect Hong Kong (setelah masuk, dana southbound umumnya menekan premium).
3. **Koreksi pajak dividen**: investor individu daratan China yang memegang H-share via Stock Connect Hong Kong dikenakan pajak dividen 20% (red chip memiliki basis perhitungan berbeda); non-resident yang memegang H-share secara langsung umumnya dikenakan 10%. Untuk saham dividen tinggi, lakukan perbandingan dividend yield setelah pajak — "kemurahan" H-share akan sebagian terkikis oleh pajak ini, wajib dikuantifikasi secara eksplisit.
4. **Kesimpulan per pasar**: kesimpulan Bab IX wajib dipisah per pasar (contoh: "H-share undervalued → beli; A-share karena premium X% berada di level historis tertinggi → hindari, pemegang saham yang sudah punya dapat mempertimbangkan konversi A ke H"). Dilarang memberikan kesimpulan umum seperti "perusahaan ini undervalued" tanpa pemisahan pasar.

Kerangka tabel perbandingan A/H (ditempatkan di akhir Bab VI laporan):

| Item | Saham A | Saham H | Catatan |
|---|---|---|---|
| Kode / Bursa | | | |
| Harga Saat Ini (mata uang lokal) | | | Cantumkan timestamp |
| Tingkat Premium Terkonversi | (A terhadap H: ___%) | — | Cantumkan kurs dan waktu pengambilan |
| Persentil Historis Premium | | — | Basis sejak listing/5 tahun terakhir |
| Rata-Rata Nilai Transaksi Harian (dikonversi ke mata uang yang sama) | | | Perbedaan likuiditas |
| Apakah Termasuk Saham Stock Connect Hong Kong | — | | |
| Dividend Yield Setelah Pajak | | | Termasuk koreksi pajak dividen |
| **Kesimpulan Per Pasar** | | | |

## 6. Item Perbedaan Pasar dalam Valuasi dan Kesimpulan

- Pembanding relative valuation diambil secara terpisah: saham A dibandingkan dengan median seluruh saham A/industri sejenis klasifikasi CSRC/CITIC, saham Hong Kong dibandingkan dengan Hang Seng Index/industri dan peer internasional — median multiple kedua pasar secara jangka panjang berbeda, **mencampur pembanding adalah kesalahan umum**.
- Parameter DCF: tingkat diskonto menggunakan basis lokasi operasional utama saham tersebut (bisnis daratan China menggunakan risk-free rate CNY + ERP China), untuk A/H gunakan satu set enterprise-level DCF yang sama untuk mendapatkan enterprise value, **lalu konversikan ke nilai per saham sesuai masing-masing pasar untuk dibandingkan dengan harga kedua pasar** — satu nilai intrinsik untuk keseluruhan, dua harga untuk masing-masing pasar.
- Diskon likuiditas saham Hong Kong: saham Hong Kong berkapitalisasi kecil/volume transaksi rendah umumnya mengalami diskon struktural, dalam kesimpulan valuasi jadikan ini sebagai item risiko, bukan langsung menurunkan fair value (kecuali likuiditasnya memang buruk sampai mempengaruhi kemampuan exit).
- Target harga sell-side: cakupan broker asing untuk saham Hong Kong luas dan target harganya cukup dapat diperbandingkan; proporsi rating "beli" dari sell-side saham A China sangat tinggi, distribusi ratingnya memiliki informasi yang rendah, fokus utama sebaiknya pada arah revisi proyeksi laba, bukan pada rating itu sendiri.

## 7. Daftar Jebakan Umum

- Memperlakukan H-share sebagai "versi dolar dari saham A" dan membandingkan P/E secara langsung: mata uang, pajak dividen, struktur investor semuanya belum disamakan.
- Pencarian di Cninfo gagal karena perubahan nama singkat perusahaan/nama lama yang digunakan sebelumnya: gunakan kode saham sebagai pencarian cadangan.
- Risiko "saham bandit lama" (老千股) di saham Hong Kong dengan frekuensi tinggi rights issue/reverse stock split: bab governance wajib memeriksa riwayat aksi korporasi permodalan (rights issue, reverse split, private placement dengan rasio besar).
- Data proporsi kepemilikan northbound/southbound keliru dianggap sebagai keseluruhan "sikap investor asing/domestik": itu hanya bagian yang terlihat.
- Goodwill dan ritme impairment saham A China, laba/rugi revaluasi properti saham Hong Kong: item non-recurring ini mencemari basis perhitungan "laba operasional", tabel tren lima tahun harus dikecualikan item ini sebelum dianalisis.

## 8. Risiko Struktural Saham China Konsep (China Concepts Stock): VIE / ADR (Wajib untuk Saham Berbasis China yang Listing di AS/Hong Kong)

Sebelum valuasi, periksa dahulu hambatan struktural — risiko struktural adalah koefisien yang dikalikan ke seluruh valuasi, bukan sekadar satu baris dalam daftar risiko.

**Lima item wajib periksa**:
1. **Struktur VIE**: pemegang saham sebenarnya memegang **kontrol kontraktual (contractual control)** atas VIE melalui shell company Cayman, bukan kepemilikan saham langsung. Periksa: bisnis/laba mana yang mengalir melalui VIE (bisnis berbasis lisensi biasanya seluruhnya), keterlaksanaan kontrak belum pernah diuji secara penuh oleh pengadilan China, bandingkan perubahan nada bicara di bagian khusus VIE dalam bab risiko 10-K/laporan tahunan dari tahun ke tahun.
2. **Jalur kas**: laba dari entitas domestik → WFOE (wholly foreign-owned enterprise) → Cayman → pemegang saham di setiap tahap (biaya transfer jasa, pajak dividen, kontrol valuta asing); pengungkapan berjenjang tentang "kas berada di entitas mana, mata uang apa, dapat keluar atau tidak" — kas konsolidasi grup ≠ kas yang dapat digunakan untuk buyback/dividen.
3. **Delisting dan regulasi**: status pemeriksaan kertas kerja audit HFCAA, kepatuhan inspeksi PCAOB; apakah dual primary listing (saham Hong Kong) sudah selesai (konvertibilitas = hedge terhadap delisting); eksposur bisnis terhadap keamanan data China dan tinjauan go-abroad.
4. **Governance**: struktur saham dual-class, selisih antara kontrol pendiri vs kepemilikan ekonomis, lemahnya perlindungan pemegang saham minoritas di perusahaan Cayman secara praktik.
5. **Item mekanis ADR**: rasio ADR, biaya kustodian, selisih harga dan friksi konversi dengan saham induk di Hong Kong.

**Aturan penanganan**: risiko struktural wajib di-pricing secara eksplisit menggunakan **probabilitas skenario** (misalnya "kegagalan kontrol kontraktual/delisting yang tidak dapat di-hedge" diberi probabilitas sebagai skenario tail), atau diberikan diskon eksplisit pada rentang gabungan dengan persentase dan dasar yang ditulis jelas; dilarang hanya menyebutkannya sekali di bab risiko sementara valuasi diberikan penuh tanpa potongan. Saham yang sudah menyelesaikan dual primary listing di Hong Kong + sebagian besar kas berada di entitas yang dapat didistribusikan, diskonnya dapat menyempit signifikan — tetap wajib menulis alasannya.
