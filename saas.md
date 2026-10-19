# Lampiran Riset Mendalam Industri SaaS

Ruang lingkup: software subscription, software aplikasi cloud-native, software B2B berbasis platform, SaaS vertikal, software subscription konsumen, dan perusahaan software hybrid yang berbasis pendapatan subscription. Jika perusahaan juga memiliki bisnis hardware, jasa, iklan, komisi transaksi, atau infrastruktur cloud, pisahkan dulu pendapatan dan margin kotor, baru gunakan lampiran ini hanya untuk bagian subscription/software.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai SaaS
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- Pastikan dulu apakah perusahaan ini benar-benar SaaS: pendapatan harus didominasi subscription yang bisa diperpanjang, subscription berbasis usage, atau kontrak software jangka panjang. Pendapatan license satu kali, konsultasi implementasi, atau bundling hardware tidak bisa langsung menggunakan multiple SaaS.
- Jangan hanya melihat tingkat pertumbuhan pendapatan. Inti riset SaaS adalah "kualitas pertumbuhan": retensi, ekspansi, efisiensi akuisisi pelanggan, margin kotor, arus kas, dilusi SBC, dan intensitas kompetisi bersama-sama menentukan nilai.
- Bedakan enterprise, SMB, developer tools, SaaS vertikal, subscription konsumen, dan SaaS berbasis platform. Churn, siklus penjualan, margin kotor, efisiensi S&M, dan median valuasi berbeda-beda sesuai basis pelanggan.
- Semua KPI yang didefinisikan sendiri oleh perusahaan harus dikembalikan ke definisi asli dalam pengungkapan, tidak boleh memaksakan perbandingan antar perusahaan dengan basis berbeda.
- Pisahkan reported growth menjadi kontribusi organic growth, M&A, nilai tukar, harga, seat expansion, usage expansion, dan churn.
- Untuk SaaS dengan valuasi tinggi, bagian valuasi harus memprioritaskan reverse DCF untuk menjelaskan implied ARR, FCF margin, Rule of 40, dan pangsa pasar akhir yang terimplikasi harga saat ini.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Pengajuan regulasi**: 10-K/10-Q/20-F/S-1/F-1/laporan tahunan. Digunakan untuk mengonfirmasi pengakuan pendapatan, RPO, deferred revenue, konsentrasi pelanggan, faktor risiko, SBC, M&A, dan basis segmen.
2. **Materi laporan keuangan perusahaan**: earnings release, shareholder letter, investor presentation, supplemental metrics. Digunakan untuk mendapatkan ARR, NRR, RPO, jumlah pelanggan, ACV, guidance, dan basis dari manajemen.
3. **Transkrip earnings call**: digunakan untuk melacak perubahan nada manajemen tentang demand, pipeline, seat expansion, monetisasi AI, pricing, churn, dan headwind makro.
4. **Pengungkapan perusahaan sejenis**: digunakan untuk membangun peer set dan rentang kewajaran KPI. Prioritaskan perusahaan dengan basis pelanggan, model penjualan, kategori produk, dan fase pertumbuhan yang sama.
5. **Riset pihak ketiga dan sell-side**: hanya bisa sebagai pelengkap opini, tidak boleh menggantikan pengungkapan primer. Saat mengutip, cantumkan tanggal dan basisnya.

### Mekanisme Kewajaran

- **Definisi diutamakan**: setiap KPI saat pertama kali muncul harus dicantumkan definisi perusahaan. Jika perusahaan tidak mengungkap definisinya, tulis "definisi perusahaan tidak diperoleh", jangan menggunakan definisi kebiasaan industri untuk menggantikan fakta.
- **Samakan basis sebelum membandingkan dengan sejenis**: sebelum membandingkan NRR, ARR, RPO, billings, FCF margin lintas perusahaan, jelaskan perbedaan basis dan item yang tidak dapat dibandingkan.
- **Pertumbuhan dan kualitas disandingkan**: setiap kesimpulan "pertumbuhan tinggi" harus sekaligus memberikan batasan kualitas berupa retensi, efisiensi akuisisi pelanggan, margin kotor, FCF, atau dilusi SBC.
- **Bukti sanggahan harus dimasukkan lebih dulu**: setiap argumen bullish harus memberikan bukti yang bisa membatalkannya. Misalnya "ekspansi yang didorong AI" harus dikaitkan dengan AI attach rate, ARPU, gross retention, atau pertumbuhan usage — bukan hanya mengutip narasi manajemen.
- **Hindari survivorship bias**: saat memilih perusahaan pembanding, sertakan sekaligus perusahaan berkualitas, pertumbuhan tinggi, matang, dan yang tertekan, tidak hanya memilih sejenis dengan multiple tinggi.
- **Bedakan siklus dan struktural**: pembekuan budget, siklus penjualan yang memanjang, seat contraction bisa jadi siklus makro, bisa juga penurunan daya saing produk. Harus dinilai dengan bukti perpanjangan, ekspansi, pipeline conversion, dan cohort pelanggan.

## 3. Pohon Penggerak Nilai SaaS

Nilai intrinsik SaaS dapat diurai menjadi:

```text
Enterprise Value =
  skala total addressable market
  × pangsa yang dapat diraih jangka panjang
  × kapabilitas pricing / ARPU
  × kualitas retensi dan ekspansi
  × margin kotor steady state
  × efisiensi sales & marketing steady state
  × leverage biaya R&D dan administrasi
  × tingkat konversi FCF setelah pajak
  ÷ discount rate risiko
  − erosi dilusi dan alokasi modal
```

Laporan minimal harus menjawab:

- Apakah pertumbuhan berasal dari pelanggan baru, ekspansi pelanggan existing, harga, usage, attach modul, atau M&A?
- Apakah pertumbuhan memerlukan investasi S&M tinggi yang terus-menerus untuk dipertahankan?
- Apakah retensi pelanggan cukup membuktikan produk adalah workflow system of record, bukan alat yang bisa disubstitusi?
- Apakah margin kotor dan FCF margin sudah mendekati level perusahaan software matang, atau masih ditekan oleh biaya infrastruktur, support, jasa, atau inference AI?
- Apakah SBC dan dilusi saham menggerus nilai free cash flow?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Kegunaan Riset | Jebakan Umum |
|---|---|---|---|
| ARR | Annualized recurring revenue; mengacu pada definisi perusahaan | Basis pendapatan subscription dan indikator leading forward revenue | Ada perusahaan menggunakan ending ARR, ada yang menggunakan run-rate revenue; ARR dari M&A harus dikeluarkan |
| Revenue growth | reported / organic / constant currency | Kecepatan pertumbuhan top-line | Terkontaminasi M&A, nilai tukar, harga, pendapatan migrasi satu kali |
| NRR / DBNRR | Retensi dan ekspansi pendapatan dari cohort pelanggan awal periode pada akhir periode | Ekspansi pelanggan existing dan stickiness produk | Perlu diperiksa apakah termasuk churn, downgrade, harga, pelanggan M&A, ekspansi pelanggan sangat besar |
| Gross retention | Retensi pendapatan setelah dikeluarkan expansion | Ketidaktergantikan produk | Jika hanya mengungkap NRR tanpa gross retention, bisa jadi upsell menutupi churn |
| Churn | Tingkat churn pelanggan atau pendapatan | Resiliensi permintaan dan tekanan kompetisi | Logo churn dan revenue churn maknanya berbeda |
| RPO / cRPO | Remaining performance obligation dan porsi yang bisa diakui dalam 12 bulan | Kontrak yang sudah ditandatangani dan visibilitas pendapatan | Kontrak besar multi-tahun, perubahan tenor kontrak, kontrak berbasis usage bisa mendistorsi |
| Billings | revenue + perubahan deferred revenue | Tren pesanan/penerimaan kas | Perubahan pembayaran tahunan/bulanan, tenor kontrak, uang muka berpengaruh |
| Customer count | Jumlah pelanggan berbayar, sering dipisah per tier ACV | Akuisisi pelanggan dan ruang upside | Pertumbuhan pelanggan bernilai rendah tidak sama dengan ARR berkualitas tinggi |
| ACV / ARPA | Annual contract value / pendapatan per akun | Kualitas pelanggan dan ruang upside | Perubahan mix pelanggan enterprise bisa mendongkrak tapi menurunkan pertumbuhan jumlah pelanggan |
| Net new ARR | ARR tambahan bersih | Momentum pertumbuhan | Musiman kuat, perlu dilihat 4Q rolling |
| CAC payback | Bulan pengembalian biaya akuisisi pelanggan | Efisiensi S&M | Menggunakan gross margin-adjusted ARR lebih konservatif |
| Magic number | Net new ARR × 4 × gross margin / S&M kuartal sebelumnya | Efisiensi penjualan | Sensitif terhadap musiman, kontrak besar enterprise, dan penyesuaian harga |
| Rule of 40 | Tingkat pertumbuhan pendapatan + FCF margin atau operating margin | Keseimbangan pertumbuhan dan laba | Basisnya harus disamakan, jangan mencampur non-GAAP operating margin dengan unlevered FCF |
| Gross margin | gross profit / revenue | Ekonomi software | Professional services, hosting, biaya inference AI bisa menekan |
| S&M / Revenue | Rasio biaya penjualan dan marketing | Intensitas investasi pertumbuhan | Rasio biaya tinggi di fase pertumbuhan tinggi tidak selalu buruk, perlu dilihat bersama net new ARR |
| R&D / Revenue | Rasio biaya R&D | Reinvestasi produk | Kapitalisasi software, SBC, dan migrasi platform harus dipisah |
| SBC / Revenue | Kompensasi berbasis saham / revenue | Dilusi pemegang saham | Non-GAAP profit sering mengeluarkan SBC, tapi valuasi tidak boleh mengabaikannya |
| FCF margin | FCF / revenue | Kapabilitas generasi kas | Uang muka subscription tahunan, PHK, capex, sewa, dan siklus penagihan bisa mengganggu |

8 indikator yang wajib diungkap duluan: ARR atau pendapatan subscription, revenue growth, NRR atau gross retention, RPO/cRPO, gross margin, efisiensi S&M, FCF margin, SBC/revenue.

## 5. Struktur Model Keuangan

### Model Pendapatan

Pilih penggerak dari data yang tersedia, dari paling detail ke paling umum:

1. `ARR awal periode + ARR baru + ARR ekspansi - ARR churned = ARR akhir periode`
2. `jumlah pelanggan × ARPA`
3. `jumlah seat × harga per seat × attach rate`
4. `volume usage × harga per unit`
5. Jika pengungkapan terbatas, proyeksikan terpisah pendapatan subscription dan pendapatan jasa, tidak boleh hanya CAGR total pendapatan.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, tingkat pertumbuhan pendapatan menurun bertahap tahun demi tahun ke level matang.
- Pisahkan tersendiri pendapatan subscription, pendapatan professional services/implementasi, dan pendapatan hardware atau non-subscription lainnya.
- Pisahkan tersendiri organic growth dan dampak M&A; jika tidak bisa dipisah, tulis "pemisahan tidak diperoleh", dan turunkan tingkat keyakinan kesimpulan.

### Model Biaya dan Margin

- Gross margin: margin kotor subscription dan margin kotor jasa dipisah. Jika biaya inference AI, hosting cloud, payment channel, atau data pihak ketiga signifikan, bahas tersendiri tekanan steady state-nya.
- S&M: digerakkan oleh efisiensi penjualan, jangan secara mekanis menurunkannya sebagai rasio terhadap pendapatan. SaaS enterprise perlu mempertimbangkan siklus penjualan dan kapasitas quota.
- R&D: perusahaan pertumbuhan tinggi tidak boleh terlalu dini mengasumsikan margin matang. Jika sedang fase rekonstruksi platform atau investasi produk AI, leverage R&D harus dilepas lebih lambat.
- G&A: bisa menurun seiring skala, tetapi biaya kepatuhan perusahaan publik, integrasi M&A, dan internasionalisasi menetapkan batas bawah.
- SBC: masuk sekaligus ke pembahasan diluted shares dan biaya ekonomi riil; Non-GAAP margin tidak dapat menggantikan FCF.
- FCF: dijelaskan dari arus kas operasi, capex, capitalized software, sewa, dan perubahan deferred revenue, jangan hanya menempelkan satu angka margin. Ketika inference AI, training model, data center, atau migrasi platform menyebabkan capex/software terkapitalisasi naik, harus dipisah maintenance capex dan growth capex; FCF pemeliharaan dan jalur return investasi pertumbuhan dinilai terpisah.

### Batasan Asumsi Steady State

- SaaS matang berkualitas bisa memiliki margin kotor tinggi dan FCF margin tinggi, tetapi harus didukung retensi, pricing power, churn rendah, dan leverage biaya.
- Jika NRR menurun, gross retention rendah, CAC payback memanjang, tidak boleh sekaligus memberi tingkat pertumbuhan tinggi, margin steady state tinggi, dan discount rate rendah.
- Jika SBC/revenue tinggi dalam jangka panjang dan buyback hanya mengompensasi dilusi, harus menurunkan nilai ekuitas atau secara eksplisit menambahkan dilusi saham.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **Reverse DCF**: dari harga saat ini, dibalik untuk mendapatkan ARR/revenue steady state yang diperlukan, FCF margin, jumlah tahun pertumbuhan, dan pangsa pasar akhir. Digunakan untuk menjawab "apa yang sudah di-price in pasar".
2. **DCF tiga skenario**: bear/base/bull masing-masing menetapkan tingkat pertumbuhan pendapatan, FCF margin, tingkat dilusi, dan nilai terminal; probabilitas berjumlah 1, dan lakukan stress test probabilitas yang tidak menguntungkan.
3. **Valuasi relatif**: EV/Revenue, EV/ARR, EV/FCF atau P/FCF. Fase pertumbuhan tinggi yang merugi bisa menggunakan EV/Revenue, tetapi harus dikoreksi dengan Rule of 40 dan kualitas pertumbuhan.
4. **Bridge growth capex / biaya AI**: ketika infrastruktur AI, biaya training/inference, atau investasi software terkapitalisasi signifikan, berikan FCF pemeliharaan, investasi pertumbuhan, tren biaya inference per unit, dan hubungan konversi ke ARR/usage baru; jangan hanya menggunakan penurunan FCF margin jangka pendek untuk membatalkan kualitas pertumbuhan.

### Opsional

- **SOTP**: digunakan untuk perusahaan platform, lini produk yang sangat berbeda, atau yang memiliki marketplace cloud, data, iklan, pembayaran, professional services sekaligus.
- **EPV**: bisa digunakan untuk SaaS matang yang profitable, tetapi tidak cocok sebagai valuasi utama untuk perusahaan fase awal yang merugi, SBC tinggi, atau reinvestasi tinggi. Jika menggunakan EPV, laba ternormalisasi harus mengurangi SBC riil atau mencerminkannya melalui dilusi.
- **Valuasi unit economics**: jika pengungkapan cukup, gunakan LTV/CAC, gross retention, CAC payback untuk cross-check FCF margin jangka panjang.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Kategori produk: CRM, ERP, security, observability, data, collaboration, SaaS vertikal, dll.
- Basis pelanggan: enterprise, mid-market, SMB, developer, consumer.
- Model penjualan: sales-led, PLG (product-led growth), channel-led, marketplace-led.
- Fase pertumbuhan: pertumbuhan tinggi merugi, seimbang Rule of 40, cash cow matang, tertekan dalam transformasi.
- Geografi dan nilai tukar: porsi pendapatan AS, Eropa, Tiongkok, global.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi model bisnis, struktur margin kotor, basis pelanggan, atau fase pertumbuhan jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

Mode laporan keuangan harus menjawab "apa yang berubah dari laporan ini", bukan hanya mendaftar beat/miss.

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan, ARR, billings, cRPO, operating margin, FCF relatif terhadap konsensus dan guidance perusahaan? |
| Kualitas pertumbuhan | Beat berasal dari pelanggan baru, ekspansi, harga, usage, pengakuan dini, M&A, atau nilai tukar? |
| Retensi | Apakah NRR/gross retention/churn membaik? Jika tidak diungkap, apakah bahasa manajemen berubah? |
| RPO/cRPO | Apakah kontrak baru dan perpanjangan mendukung pendapatan 12 bulan ke depan? Apakah perubahan tenor kontrak mendistorsi? |
| Efisiensi penjualan | Apakah investasi S&M sepadan dengan net new ARR? Apakah CAC payback membaik atau pertumbuhan dikorbankan demi laba? |
| Margin | Margin kotor, S&M, R&D, G&A, SBC, dan FCF margin mana yang mendorong perubahan laba? |
| Guidance | Apakah guidance revenue, operating margin, FCF, RPO, atau ARR mengubah model jangka panjang? |
| Earnings call | Apakah nada bicara tentang demand, pipeline, budget scrutiny, monetisasi AI, pricing, seat expansion, churn menguat atau melemah? |
| Bridge valuasi | Bagaimana laporan keuangan baru mengubah jalur pendapatan masa depan, FCF margin steady state, tingkat dilusi, WACC, atau probabilitas skenario? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan monetisasi AI, pertumbuhan usage, RPO/cRPO, perbaikan margin, atau tekanan FCF/capex? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 8% tapi basket peer SaaS naik 5% di hari yang sama, reaksi spesifik perusahaan sekitar +3%.

## 8. Moat & Penilaian Kompetitif

Moat SaaS tidak bisa hanya ditulis "biaya peralihan tinggi". Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Workflow depth | Menjadi sistem proses bisnis inti, penghentian penggunaan akan mempengaruhi pendapatan, kepatuhan, atau produksi | Hanya dashboard, plugin, atau alat yang bisa disubstitusi |
| Data moat | Data pelanggan, workflow historis, feedback model membentuk keunggulan kumulatif | Data mudah diekspor, biaya peralihan ke kompetitor rendah |
| Ecosystem | API, marketplace, partner, developer membentuk ekosistem | Pendapatan ekosistem lemah, integrasi hanya sales pitch |
| Multi-product expansion | Attach multi-modul mendorong kenaikan NRR dan ARPA | Hanya bergantung satu produk unggulan, bukti cross-sell tidak memadai |
| Scale efficiency | Efisiensi S&M membaik seiring skala, gross retention stabil | Pertumbuhan seluruhnya dipaksakan dengan penjualan |
| Pricing power | Setelah beberapa tahun kenaikan harga churn masih rendah, NRR stabil | Kenaikan harga menyebabkan downgrade, seat contraction, atau logo churn |
| AI defensibility | Fitur AI meningkatkan retensi, ARPU, efisiensi, atau barrier data | AI hanya menyamakan fitur, menekan harga atau meningkatkan biaya inference |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "moat kuat", tapi gross retention rendah, NRR menurun, CAC payback memanjang, SBC tinggi, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- NRR terus menurun dan perusahaan berhenti mengungkap atau mengubah basisnya.
- ARR dan revenue growth berdivergensi, dan tidak dapat dijelaskan dengan tenor kontrak, M&A, atau nilai tukar.
- Pertumbuhan RPO didorong perpanjangan tenor kontrak, sementara cRPO atau billings melemah.
- Porsi pendapatan jasa naik, margin kotor subscription menurun, menunjukkan tingkat software-nya mungkin lebih rendah dari narasi.
- Efisiensi S&M memburuk tapi manajemen tetap mempertahankan guidance pertumbuhan tinggi jangka panjang.
- Non-GAAP profit terlihat bagus, tapi SBC/revenue tinggi dan dilusi saham terus berlanjut.
- Perbaikan FCF utamanya dari siklus penagihan, PHK, atau penundaan capex, bukan dari operating leverage.
- "Produk AI" hanya meningkatkan narasi, tanpa bukti attach rate, ARPU, retensi, atau gross margin.
- M&A berkontribusi terhadap pertumbuhan tapi organic growth tidak diungkap atau jelas melambat.
- Konsentrasi pelanggan besar, eksposur budget pemerintah/industri tunggal tinggi, tapi menggunakan multiple SaaS biasa.

### Daftar Bukti Sanggahan

Setiap laporan SaaS minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- NRR di bawah ambang tertentu atau menurun N kuartal berturut-turut.
- Pertumbuhan cRPO / billings jatuh di bawah revenue growth.
- CAC payback memanjang melebihi rentang yang wajar.
- FCF margin membaik tapi SBC/revenue tidak menurun.
- AI/produk baru belum terkonversi menjadi ARPU, attach rate, atau retensi.
- Perang harga atau substitusi produk dari peer utama menyebabkan win rate menurun.

### Kesalahpahaman Umum

- Menganggap EV/Revenue rendah sebagai murah, mengabaikan retensi rendah, margin kotor rendah, atau kualitas pertumbuhan rendah.
- Menganggap pencapaian Rule of 40 sebagai kondisi cukup, mengabaikan apakah margin masih bisa terus naik setelah pertumbuhan melambat.
- Menganggap NRR tinggi sebagai ekspansi perpetual, mengabaikan ekspansi awal pelanggan sangat besar yang tidak berkelanjutan.
- Menganggap pertumbuhan deferred revenue sebagai demand kuat, mengabaikan perubahan siklus penagihan dan uang muka.
- Menganggap perbaikan margin setelah PHK sebagai operating leverage, mengabaikan investasi produk dan penjualan yang kurang memadai.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan SaaS selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel KPI SaaS

| Indikator | Nilai Terbaru | YoY/QoQ | Tren 8 Kuartal Terakhir | Posisi vs Sejenis | Sumber & Basis |
|---|---:|---:|---|---|---|
| ARR / pendapatan subscription | | | | | |
| Revenue growth | | | | | |
| NRR / gross retention | | | | | |
| RPO / cRPO | | | | | |
| Gross margin | | | | | |
| Efisiensi S&M / CAC payback | | | | | |
| Rule of 40 | | | | | |
| FCF margin | | | | | |
| SBC / revenue | | | | | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| CAGR pendapatan 5 tahun | | | | |
| FCF margin steady state | | | | |
| Dilusi saham tahunan | | | | |
| EV/FCF terminal atau exit multiple | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada pendapatan kuartal ini, melainkan apakah dapat menjaga pertumbuhan sekitar X% dalam N tahun ke depan dan menaikkan FCF margin ke Y%."
- "Jika salah satu indikator inti berikut — NRR / cRPO / CAC payback / SBC — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
- "ARR, FCF margin, dan pangsa akhir yang terimplikasi harga saham saat ini adalah ……; saya menilai implikasi ini wajar/agresif/konservatif, dengan alasan ……"
</content>
