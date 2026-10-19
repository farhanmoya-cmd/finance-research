# Lampiran Riset Mendalam Industri Internet/Platform

Berlaku untuk perusahaan platform seperti search engine, e-commerce, media sosial, periklanan, local life service (jasa lokal), streaming, dan sharing economy. Karakteristik inti: efek jaringan + biaya marginal menurun + inkubasi multi-bisnis, kesulitan valuasi ada pada "gabungan cash cow matang + optionality bakar uang". Jika perusahaan memiliki segmen cloud/infrastruktur, segmen itu dimodelkan terpisah (lihat `industries/saas.md`), tidak digabung menggunakan multiple yang sama dengan bisnis iklan.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Platform
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Identifikasi dulu tipe bisnisnya**, baru pilih KPI:
  - **Platform iklan** (search/feed/sosial): waktu penggunaan pengguna × tingkat monetisasi (ad load, eCPM), ROI pengiklan, sensitivitas terhadap siklus iklan makro.
  - **E-commerce/marketplace**: GMV, take rate, rasio biaya fulfillment, mix kategori (frekuensi tinggi margin rendah vs frekuensi rendah margin tinggi).
  - **Subscription/streaming**: net addition pelanggan, ARPU, churn rate, kebijakan amortisasi biaya konten (gap antara kas keluar dan amortisasi).
  - **Local life service/sharing economy**: volume pesanan, ekonomi per order, biaya pasokan rider/driver, intensitas subsidi.
  - **Segmen cloud/infrastruktur**: dimodelkan terpisah, lihat lampiran SaaS.
- **Mayoritas platform adalah target SOTP**: bisnis matang menggunakan DCF/multiple, bisnis baru menggunakan option pricing atau unit economics, **dilarang menggunakan satu P/E untuk membungkus semuanya**.
- Pertumbuhan pendapatan harus diurai menjadi **volume dan harga**. Jika iklan hanya melaporkan pendapatan tanpa memisahkan impressions dan eCPM, sama dengan menyembunyikan siklikalitas.
- Pada fase ekspansi AI/cloud/data center, harus dibedakan **maintenance capex dan growth capex**: yang pertama adalah biaya untuk menjaga kapabilitas pendapatan saat ini, yang kedua adalah kapasitas pendapatan masa depan. **Tidak boleh secara mekanis menurunkan penilaian kualitas hanya karena FCF margin ditekan growth capex.**
- SBC (stock-based compensation) adalah biaya riil perusahaan platform. Selalu gunakan FCF setelah SBC dan jumlah saham setelah dilusi.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Laporan keuangan dan catatan segmen 10-K**: pendapatan segmen, laba operasi, capex, definisi indikator pengguna. **Dokumen litigasi antitrust sering mengungkap data internal**, merupakan sumber bernilai tinggi.
2. **Data operasional yang dilaporkan sendiri oleh platform**: MAU/DAU, GMV, volume pesanan, jumlah pelanggan. **Perhatikan perubahan basis dan definisi "aktif"**.
3. **Pengukuran pihak ketiga**: Sensor Tower, data.ai, Similarweb, eMarketer (pangsa iklan), Nielsen. Harus dicantumkan metode sampel dan bias cakupan.
4. **Survei pengiklan/merchant, channel checks**: hanya sebagai petunjuk, perlu diverifikasi silang dengan pengungkapan perusahaan.
5. **Teks asli regulasi dan kebijakan**: kebijakan privasi (seperti ATT), keputusan antitrust, regulasi konten, legislasi tanggung jawab platform.

### Mekanisme Kewajaran

- **Perubahan basis harus dicantumkan**: perubahan definisi MAU, DAU, GMV, "pengguna aktif" dapat menciptakan pertumbuhan semu. Harus dicantumkan apakah data historis direstatement.
- **Basis GMV**: apakah termasuk retur, pembatalan, first-party vs third-party, cross-border, pajak. GMV dengan basis berbeda tidak dapat dibandingkan.
- **Volume dan harga harus dipisahkan**: pendapatan iklan harus diurai impressions (volume) dan eCPM (harga); e-commerce harus diurai GMV dan take rate.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "AI meningkatkan efisiensi iklan" harus dikaitkan dengan tren eCPM, retensi pengiklan, atau data konversi — bukan hanya mengutip narasi manajemen.
- **Bedakan siklus dan struktural**: penurunan pendapatan iklan bisa jadi siklus iklan makro, bisa juga kehilangan pangsa pasar atau kanibalisasi format baru. Harus dibedakan dengan data pangsa dan volume-harga.
- **Hindari survivorship bias**: peer set harus mencakup platform yang sudah kehilangan pangsa pasar dan perusahaan yang terdisrupsi bentuk baru.

## 3. Pohon Penggerak Nilai Platform

Pilih pohon penggerak berdasarkan tipe bisnis:

```text
Nilai iklan = jumlah pengguna × waktu penggunaan × ad load × harga (eCPM) × retensi pengiklan
Nilai e-commerce = GMV × take rate − fulfillment/subsidi − biaya akuisisi pelanggan
Nilai subscription = jumlah pelanggan × ARPU × masa retensi − biaya konten/jasa
Nilai local life service = volume pesanan × GMV per order × take rate − subsidi fulfillment

Enterprise Value =
  Σ bisnis matang (laba steady state × keberlanjutannya)
  + Σ bisnis baru (probabilitas unit economics menjadi positif × batas atas skala)
  + net cash dan investasi
  − dilusi SBC
  − sanksi regulasi dan risiko struktural (probabilitas skenario)
  − risiko growth capex tidak terkonversi
```

Laporan minimal harus menjawab:

- Apakah pertumbuhan pendapatan berasal dari pertumbuhan pengguna, pertumbuhan waktu penggunaan, peningkatan tingkat monetisasi, atau harga? Berapa kontribusi masing-masing?
- Berapa ruang kenaikan lagi tingkat monetisasi? Apakah ad load sudah mendekati batas atas pengalaman pengguna?
- Apakah unit economics bisnis baru memiliki jalur yang jelas menjadi positif? Atau hanya didukung narasi TAM?
- Apa jalur konversi pendapatan dari growth capex (terutama AI/data center)? Bagaimana utilisasi dan ROIIC?
- Apakah risiko regulasi berupa denda, atau bisa memaksa spin-off atau mengubah model bisnis?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Bisnis | Jebakan Umum |
|---|---|---|---|
| MAU / DAU | Pengguna aktif bulanan/harian | Semua platform | **Perubahan basis adalah teknik pemolesan paling umum** |
| DAU/MAU | Rasio stickiness pengguna | Sosial, konten | Rasio tinggi mewakili penggunaan frekuensi tinggi |
| Waktu penggunaan | Rata-rata waktu penggunaan per pengguna | Platform iklan | Pertumbuhan waktu dari konten kualitas rendah akan merusak nilai iklan |
| Ad load | Tingkat pemuatan iklan | Platform iklan | Peningkatan ad load adalah bonus satu kali, ada batas atas pengalaman |
| Impressions | Volume tayangan iklan | Platform iklan | Pertumbuhan volume perlu dipisahkan dari harga |
| eCPM / harga per unit | Pendapatan per seribu tayangan | Platform iklan | Penurunan harga sering ditutupi pertumbuhan volume tayangan |
| Jumlah/konsentrasi pengiklan | Pengiklan aktif dan konsentrasinya | Platform iklan | Risiko kehilangan pengiklan besar |
| GMV | Gross merchandise value platform | E-commerce, local life | **Harus dicantumkan apakah termasuk retur pembatalan; rawan inflasi angka** |
| Take rate | Pendapatan platform / GMV | E-commerce, local life | Menaikkan take rate bisa merusak retensi merchant |
| Rasio biaya fulfillment | Biaya fulfillment / GMV atau pendapatan | E-commerce | Menentukan profitabilitas riil e-commerce |
| Unit economics (UE) | Laba kontribusi per order/per pengguna | Bisnis baru | **Tidak bisa menggunakan TAM untuk mengganti argumentasi UE** |
| Net addition pelanggan | Baru − churn | Subscription, streaming | Kualitas pelanggan masa promosi buruk, churn tinggi |
| ARPU | Pendapatan per pengguna | Semua platform | Perlu dibedakan dampak perubahan struktur regional |
| Churn | Tingkat churn | Subscription | Churn setelah konversi free trial perlu dilihat tersendiri |
| Biaya konten dan amortisasi | Kas keluar vs amortisasi | Streaming | **Gap antara kas dan amortisasi adalah kunci**; liabilitas konten off-balance-sheet perlu diperiksa di catatan |
| Intensitas subsidi | Subsidi / GMV atau order | Bisnis baru, local life | Pertumbuhan yang didorong subsidi memiliki retensi buruk |
| Biaya akuisisi pelanggan | Biaya marketing / pengguna baru | Semua platform | Perlu dibandingkan dengan lifetime value pengguna |
| SBC / revenue | Porsi kompensasi berbasis saham | Semua platform | **Dilarang menggunakan multiple FCF yang mengeluarkan SBC** |
| Maintenance vs growth capex | Pemisahan capex | Bisnis cloud/AI | Jika tidak dipisah, harus dicantumkan dan ditangani dengan rentang |
| RPO / backlog | Kontrak di tangan segmen cloud | Segmen cloud | Mengukur kecepatan konsumsi growth capex |
| ROIIC | Return on incremental invested capital | Semua platform | Memverifikasi apakah reinvestasi menciptakan nilai |

8 indikator yang wajib diungkap duluan: skala dan stickiness pengguna, waktu penggunaan atau frekuensi, pemisahan volume-harga tingkat monetisasi (eCPM atau take rate), basis GMV, unit economics bisnis baru, SBC/revenue, pemisahan maintenance dan growth capex, margin laba operasi per segmen.

## 5. Struktur Model Keuangan

### Model Pendapatan

Dimodelkan per segmen bisnis, dilarang digabung dalam proyeksi:

1. **Iklan**: `jumlah pengguna × waktu penggunaan × ad load × eCPM`, permintaan diurai per regional dan vertikal industri (e-commerce/game/finansial/otomotif).
2. **E-commerce**: `GMV × take rate`, GMV diurai jumlah pembeli × frekuensi × average order value; first-party dan third-party dipisah.
3. **Subscription/streaming**: `pelanggan awal periode + penambahan − churn = pelanggan akhir periode`, dikali ARPU; dilapiskan per regional (ARPU berbeda signifikan).
4. **Segmen cloud**: lihat lampiran SaaS, didorong RPO/backlog dan pertumbuhan konsumsi.
5. **Bisnis baru**: dimodelkan dengan unit economics × jalur skala, dengan titik waktu menjadi positif dan skala yang diperlukan yang jelas.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, dirinci per segmen, tidak boleh hanya CAGR pendapatan konsolidasi.
- Pendapatan iklan harus memberikan proyeksi terpisah volume (impressions) dan harga (eCPM).
- Pertumbuhan organik dan M&A dipisah tersendiri; jika tidak bisa dipisah tulis "pemisahan tidak diperoleh" dan turunkan tingkat keyakinan.

### Model Biaya, Capex, dan Margin

- **Margin per segmen**: setiap segmen dimodelkan terpisah. Margin tinggi bisnis matang tidak boleh digunakan untuk menutupi kerugian berkelanjutan bisnis baru.
- **Biaya fulfillment dan konten**: rasio biaya fulfillment e-commerce, kebijakan amortisasi konten streaming harus dibahas tersendiri. **Streaming perlu membandingkan kas keluar konten dengan biaya amortisasi** — gap yang terus negatif berarti laba dipercantik oleh kebijakan amortisasi.
- **Bridge growth capex**: saat infrastruktur AI, biaya training/inference, atau investasi data center signifikan, harus diberikan: maintenance capex, growth capex, tren biaya inference per unit, utilisasi, RPO/backlog, dan hubungan konversi ke pendapatan tambahan.
- **SBC**: masuk sekaligus ke pembahasan dilusi saham dan biaya ekonomi riil. Margin Non-GAAP tidak dapat menggantikan FCF setelah SBC.
- **Modal kerja**: periode utang usaha e-commerce, siklus settlement merchant platform akan mempengaruhi arus kas secara signifikan, perlu dirinci tersendiri.

### Batasan Asumsi Steady State

- Peningkatan tingkat monetisasi iklan memiliki batas atas: ad load dibatasi pengalaman pengguna, eCPM dibatasi ROI pengiklan. **Pasar iklan global secara umum sekitar 1–1.5% dari GDP, pangsa memiliki plafon**, reverse DCF harus memverifikasi kewajaran implied share.
- Jika pertumbuhan pengguna stagnan, waktu penggunaan menurun, eCPM tertekan, tidak boleh sekaligus memberi pertumbuhan pendapatan tinggi dan margin tinggi.
- Bisnis baru tidak boleh default semua berhasil. Harus diberikan probabilitas menjadi positif, atau diberi bobot skenario.
- Jika growth capex terus diinvestasikan tapi konversi pendapatan dan utilisasi tidak membaik, perlu turunkan ROIIC dan re-estimasi nilai investasi.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **SOTP sebagai framework utama**: bisnis inti menggunakan DCF tiga tahap; bisnis baru yang merugi menggunakan "skenario × unit economics" atau benchmark valuasi private equity (dengan diskon); **net cash dipisah tersendiri**.
2. **Reverse DCF**: sangat bermanfaat terutama untuk raksasa platform — dari harga saat ini, dibalik untuk mendapatkan implied pangsa pasar iklan, skala GMV, atau tingkat monetisasi pengguna, dan **diverifikasi apakah mungkin relatif terhadap plafon pasar**.
3. **Multiple FCF setelah SBC**: dihitung berdasarkan saham setelah dilusi, dilarang menggunakan basis yang mengeluarkan SBC.
4. **Bridge owner earnings** (saat capex AI/cloud signifikan): `arus kas operasi − maintenance capex = FCF pemeliharaan`; growth capex dikaitkan tersendiri dengan konversi pendapatan, utilisasi, RPO/backlog, margin per segmen, dan ROIIC. Jika tidak bisa dipisah, tulis "pemisahan maintenance/growth capex tidak diperoleh", dan tangani dengan rentang atau skenario.

### Opsional

- **Metode multiple per segmen**: bisnis iklan matang menggunakan EV/EBIT, cloud menggunakan EV/Revenue, e-commerce menggunakan EV/GMV atau EV/EBITDA.
- **Option pricing**: bisnis baru fase awal bisa menggunakan framework real option, tetapi harus dijelaskan kerawanan asumsinya.
- **Metode nilai per pengguna**: `nilai per pengguna × jumlah pengguna` sebagai referensi cross-check, bukan valuasi utama.

**Diskon regulasi harus dieksplisitkan**: denda antitrust, spin-off wajib, batasan model bisnis ditangani dengan **probabilitas skenario**, **jangan disembunyikan dalam WACC**.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Model monetisasi: iklan, komisi, subscription, transaksi, tidak boleh dicampur.
- Tipe efek jaringan: cross-side network (marketplace), same-side network (sosial), tanpa efek jaringan (konten).
- Fase pertumbuhan: cash cow matang, fase monetisasi pertumbuhan tinggi, fase ekspansi bakar uang.
- Regional dan regulasi: tingkat dampak kebijakan privasi, antitrust, dan regulasi konten.
- Intensitas modal: platform aset ringan dan platform aset berat (data center, logistik) berbeda.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi model monetisasi atau intensitas modal jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan segmen, laba operasi, EPS, guidance capex relatif terhadap konsensus? |
| Volume-harga iklan | Berapa kontribusi masing-masing impressions dan eCPM terhadap pertumbuhan pendapatan? Apakah eCPM turun YoY? |
| Permintaan vertikal | Bagaimana divergensi kondisi masing-masing industri pengiklan (e-commerce/game/finansial/otomotif)? |
| Dampak format baru | Seberapa besar kanibalisasi short video, AI search, dan format baru lainnya terhadap slot iklan existing? |
| E-commerce | Apakah GMV dan pendapatan berdivergensi? Alasan perubahan take rate? Tren rasio biaya fulfillment? |
| Subscription/konten | Bagaimana kualitas net addition? Apakah gap kas konten dan amortisasi melebar? |
| Segmen cloud | Bagaimana pertumbuhan relatif terhadap raksasa sejenis kuartal ini? Ramp-up margin operasi? Kecepatan konsumsi RPO/backlog? |
| Capex | Berapa besar perubahan guidance capex? Bagaimana pemisahan maintenance dan growth? Bagaimana utilisasi? |
| Bisnis baru | Apakah jalur penyempitan kerugian terealisasi? Apakah unit economics membaik? |
| SBC | Bagaimana tren SBC/revenue? Apakah dilusi benar-benar dikompensasi sepenuhnya oleh buyback? |
| Alokasi modal | Apakah nada bicara manajemen tentang capex, buyback, pengurangan kerugian bisnis baru berubah? |
| Regulasi | Dampak riil litigasi, denda, perubahan kebijakan terhadap model bisnis? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan monetisasi AI, siklus iklan, return capex, atau hasil regulasi? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 9% tapi sektor internet naik 5% di hari yang sama, reaksi spesifik perusahaan sekitar +4%.

## 8. Moat & Penilaian Kompetitif

Inti moat platform adalah **efek jaringan**, tetapi efek jaringan memiliki batas dan juga bisa memudar. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Efek jaringan cross-side | Pembeli dan penjual saling menarik, keunggulan skala memperkuat diri sendiri | Multi-homing umum, pengguna bisa menggunakan beberapa platform sekaligus |
| Efek jaringan same-side | Semakin banyak pengguna, semakin tinggi nilai sosial, migrasi butuh tindakan kolektif | Graf sosial bisa direplikasi, pengguna muda beralih ke platform baru |
| Flywheel data dan algoritma | Skala data terkonversi menjadi keunggulan efisiensi rekomendasi/iklan yang terukur | Data bisa disubstitusi, gap algoritma menyempit |
| Ekosistem dan biaya peralihan | Akun, pembayaran, konten, perangkat membentuk lock-in ekosistem | Layanan titik tunggal, biaya peralihan rendah |
| Efisiensi monetisasi | eCPM atau take rate lebih tinggi dari sejenis dan stabil | Peningkatan tingkat monetisasi langsung memicu churn pengguna atau merchant |
| Barrier sisi supply | Konten eksklusif, merchant eksklusif, supply langka | Daya tawar pihak supply kuat, biaya terus naik |
| Pintu distribusi | Menguasai sistem operasi, browser, atau pintu default | Bergantung pada distribusi pihak ketiga, dibatasi kebijakan platform |
| Return reinvestasi | ROIIC bisnis baru lebih tinggi dari cost of capital | Terus bakar uang jangka panjang tapi unit economics tidak membaik |

Verifikasi keuangan: gunakan tiga hal — **stabilitas pangsa pasar + daya tawar harga (tren eCPM/take rate) + ROIIC**. Jika diklaim "efek jaringan kuat", tapi pangsa menurun, eCPM turun, ROIIC bisnis baru negatif, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- Perubahan basis MAU/DAU/GMV, dan data historis tidak direstatement.
- Selisih GMV dan pendapatan terus melebar (GMV naik tapi monetisasi menurun).
- "Pendapatan lain" atau pendapatan yang tidak disegmentasi berkembang cepat, menutupi kelemahan bisnis utama.
- Pertumbuhan pendapatan iklan sepenuhnya mengandalkan impressions, eCPM terus turun.
- Ad load sudah mendekati atau melebihi batas atas industri, tapi masih mengasumsikan tingkat monetisasi terus naik.
- Bisnis baru menggunakan narasi TAM untuk mengganti argumentasi unit economics, dan kerugian terus melebar.
- Kas keluar konten streaming signifikan lebih tinggi dari amortisasi, dan liabilitas konten off-balance-sheet berkembang cepat.
- Sanksi regulasi menjadi normal, atau model bisnis inti menghadapi batasan struktural.
- SBC sangat tinggi dan buyback hanya mampu mengompensasi dilusi, pemegang saham tidak mendapat return riil.
- Founder/eksekutif terus melakukan divestasi besar, iramanya berdivergensi dengan fundamental.
- Growth capex naik signifikan tapi utilisasi, RPO, atau konversi pendapatan tidak membaik sepadan.

### Daftar Bukti Sanggahan

Setiap laporan platform minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- DAU/MAU atau waktu penggunaan pengguna turun N kuartal berturut-turut.
- eCPM atau take rate jatuh di bawah ambang tertentu.
- Selisih pertumbuhan GMV dan pendapatan melebihi persentase tertentu.
- Unit economics bisnis baru belum menjadi positif pada titik waktu yang dijanjikan.
- Utilisasi atau pertumbuhan RPO segmen cloud/AI jatuh di bawah ambang, growth capex tidak terkonsumsi.
- Keputusan antitrust mengharuskan divestasi bisnis inti atau mengubah distribusi default.

### Kesalahpahaman Umum

- Menggunakan satu P/E tunggal untuk menilai platform multi-bisnis, menutupi kerugian bisnis baru atau kemunduran bisnis matang.
- Menganggap pertumbuhan GMV sebagai pertumbuhan pendapatan, mengabaikan perubahan take rate.
- Menganggap pertumbuhan pengguna sebagai pertumbuhan nilai, mengabaikan kapabilitas monetisasi pengguna baru (ARPU pasar berkembang sangat rendah).
- Menggunakan multiple FCF yang mengeluarkan SBC, secara sistematis melebih-lebihkan nilai.
- Menganggap FCF yang ditekan growth capex sebagai pemburukan kualitas, atau sebaliknya menganggap semua capex sebagai investasi pertumbuhan.
- Menggunakan TAM untuk mengargumentasikan nilai bisnis baru, mengabaikan unit economics yang belum pernah menjadi positif.
- Memasukkan risiko regulasi ke dalam WACC, bukan dimodelkan secara eksplisit dengan probabilitas skenario.
- Mengabaikan efek pemercantik laba dari kebijakan amortisasi konten streaming.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan platform selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tiga Tabel Pendapatan-Laba-Valuasi per Segmen (harus cocok dengan rekapitulasi SOTP)

| Segmen | Pendapatan | Pertumbuhan | Laba Operasi | Margin | Metode Valuasi | Valuasi |
|---|---:|---:|---:|---:|---|---:|

### Tabel KPI Inti

| Indikator | Nilai Terbaru | YoY/QoQ | Tren 8 Kuartal Terakhir | Posisi vs Sejenis | Sumber & Basis |
|---|---:|---:|---|---|---|
| MAU / DAU (dengan basis) | | | | | |
| Waktu penggunaan per kapita / frekuensi | | | | | |
| Impressions (volume) | | | | | |
| eCPM (harga) | | | | | |
| GMV (dengan basis) | | | | | |
| Take rate | | | | | |
| Net addition pelanggan / ARPU / churn | | | | | |
| SBC / revenue | | | | | |

### Tabel Unit Economics Bisnis Baru

| Bisnis | UE Saat Ini | Jalur Menjadi Positif | Skala yang Diperlukan | Burn Rate | Probabilitas Menjadi Positif |
|---|---:|---|---:|---:|---:|

### Bridge Return AI / Capex

| Item | Nominal | Keterangan |
|---|---:|---|
| Arus kas operasi | | |
| Maintenance capex | | |
| FCF pemeliharaan | | |
| Growth capex | | |
| Pendapatan tambahan terkait / RPO | | |
| Utilisasi | | |
| ROIIC inkremental | | |

### Tabel Skenario Regulasi

| Skenario | Probabilitas | Dampak terhadap Pendapatan/Laba | Dampak terhadap Valuasi |
|---|---:|---|---|

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada pendapatan iklan kuartal ini, melainkan apakah tingkat monetisasi dapat terus naik dalam N tahun ke depan, dan apakah ROIIC investasi bisnis baru/AI dapat lebih tinggi dari cost of capital."
- "Pangsa pasar iklan atau skala GMV yang terimplikasi harga saat ini adalah ……; dibandingkan dengan plafon pasar, implikasi ini wajar/agresif/konservatif."
- "Jika salah satu indikator inti berikut — waktu penggunaan / eCPM / take rate / UE bisnis baru / return capex — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
