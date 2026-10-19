# Lampiran Riset Mendalam Industri Semikonduktor

Berlaku untuk desain chip, wafer foundry, IDM, memory, equipment, material, EDA/IP, packaging testing, dan perusahaan sistem semikonduktor. Pisahkan dulu berdasarkan value chain dan kategori produk; segmen yang berbeda tidak bisa menggunakan satu set indikator siklus atau multiple valuasi yang sama. Jika perusahaan juga memiliki bisnis sistem, software, atau jasa, pisahkan dulu pendapatan dan margin kotor, baru gunakan lampiran ini untuk masing-masing segmen.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Semikonduktor
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Identifikasi dulu posisi di value chain**, baru pilih KPI dan metode valuasi. Di bawah label "semikonduktor" yang sama, penggerak siklus perusahaan equipment dan perusahaan memory hampir tidak memiliki persinggungan.
  - **Fabless / akselerator / CPU**: performa produk, ekosistem software, content value sistem, design win, pasokan foundry dan advanced packaging.
  - **Foundry / IDM**: node proses, yield, utilisasi kapasitas, wafer ASP, intensitas modal, dan siklus depresiasi.
  - **Memory**: bit shipment, bit growth, ASP, inventori, disiplin supply, dan biaya per unit, **tidak bisa hanya melihat pertumbuhan pendapatan YoY**.
  - **Equipment / Material / EDA / IP**: backlog, pesanan, capex pelanggan, pendapatan jasa, basis instalasi, kontrol ekspor, dan konsentrasi pelanggan.
  - **OSAT / testing**: porsi advanced packaging, utilisasi, content value per mesin, yield, dan sertifikasi pelanggan.
- Semikonduktor adalah **industri siklikal**. Setiap kesimpulan pertumbuhan harus sekaligus menjelaskan posisi saat ini dalam siklus inventori, siklus kapasitas, dan siklus harga.
- Siklus terminal AI, otomotif, industrial, handphone, PC berbeda-beda; dimodelkan per terminal, regional, pelanggan, dan produk, **jangan langsung menerapkan pertumbuhan total industri ke perusahaan**.
- Pertumbuhan pendapatan harus diurai menjadi kontribusi units, ASP, mix produk, pangsa, dan nilai tukar. Pertumbuhan yang didorong harga dan pertumbuhan yang didorong pangsa memiliki nilai yang sama sekali berbeda.
- Geopolitik adalah variabel struktural industri ini, bukan catatan kaki peringatan risiko. Kontrol ekspor, subsidi industri, dan regionalisasi rantai pasok harus masuk ke model.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Pengajuan regulasi dan pengungkapan perusahaan**: 10-K/10-Q/20-F/laporan tahunan, presentasi laporan keuangan, pengungkapan primer pemasok dan pelanggan. Digunakan untuk mengonfirmasi pendapatan segmen, konsentrasi pelanggan, komitmen pembelian, inventori, dan perencanaan kapasitas.
2. **Lembaga statistik industri**: statistik penjualan, unit, dan ASP dari WSTS/SIA; data equipment dan fab dari SEMI/SEAJ; data material dari bea cukai masing-masing negara dan USGS.
3. **Teks asli regulasi dan kebijakan**: untuk kontrol ekspor gunakan teks asli BIS Entity List, Uni Eropa, Jepang, dan regulator lokal lainnya, jangan mengutip parafrase sekunder.
4. **Riset komersial**: Gartner, Omdia, TechInsights, TrendForce, Counterpoint, IDC, Yole dapat melengkapi pangsa dan harga, tetapi **harus dicantumkan sampel, basis, dan tanggal publikasi**.
5. **Teardown, saluran, dan informasi rantai pasok**: hanya sebagai petunjuk; harus diverifikasi silang dengan data perusahaan, pelanggan, atau industri baru bisa ditulis di laporan.

### Mekanisme Kewajaran

- **Denominator harus dicantumkan jelas**: setiap pangsa dan TAM harus mencantumkan definisi denominator (berdasarkan nominal atau unit, termasuk atau tidak memory, termasuk atau tidak transaksi internal).
- **Peringatan basis**: data bulanan WSTS mungkin menggunakan moving average; pesanan mungkin double-counted, dibatalkan, atau lintas periode; definisi "AI revenue" yang didefinisikan sendiri oleh perusahaan berbeda-beda, harus dicantumkan definisi perusahaan saat pertama kali muncul.
- **Pisahkan siklus dan struktural**: pertumbuhan pendapatan harus menjawab apakah dari restocking, peningkatan pangsa, kenaikan content, atau kenaikan harga. Keempatnya memiliki keberlanjutan yang sama sekali berbeda.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "permintaan AI kuat" harus dikaitkan dengan pesanan, booking kapasitas, guidance capex pelanggan, atau kuota HBM/advanced packaging — bukan hanya mengutip narasi manajemen.
- **Hindari survivorship bias**: peer set harus mencakup perusahaan di puncak siklus, perusahaan yang tertekan, dan perusahaan yang sudah kehilangan kepemimpinan node.
- **Verifikasi tiga lapis inventori**: hari inventori perusahaan, inventori pelanggan/saluran, dan shipments/ASP industri harus diverifikasi silang satu sama lain, hanya melihat inventori perusahaan akan sangat lagging.

## 3. Pohon Penggerak Nilai Semikonduktor

Nilai intrinsik semikonduktor dapat diurai menjadi:

```text
Enterprise Value =
  total permintaan terminal (dimodelkan terpisah per pasar terminal)
  × content per unit/sistem
  × pangsa pasar
  × ASP dan posisi siklus harga
  × margin kotor steady state (yield, mix, kurva biaya)
  × efisiensi return R&D dan intensitas modal
  × ROIC lintas siklus
  ÷ discount rate risiko (termasuk premium geopolitik)
  − kerugian mismatch inventori/kapasitas
  − risiko konsentrasi pelanggan dan foundry
  − kerugian akses pasar dari kontrol ekspor
```

Laporan minimal harus menjawab:

- Apakah pertumbuhan berasal dari permintaan terminal, kenaikan content, perolehan pangsa, kenaikan harga, atau restocking?
- Apakah keunggulan teknologi sudah tercermin sebagai pangsa, ASP, margin kotor, atau return modal? Jika belum, apakah keunggulan itu hanya narasi?
- Di mana posisi saat ini dalam siklus inventori? Apakah inventori di tiga lapis (perusahaan, pelanggan, saluran) konsisten?
- Apa jalur return capex? Apakah titik waktu penambahan kapasitas sesuai dengan titik waktu permintaan?
- Apakah kerugian pendapatan akibat kontrol ekspor bersifat permanen, atau akan disubstitusi oleh regional/pelanggan lain?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Segmen | Jebakan Umum |
|---|---|---|---|
| Units / shipments | Volume pengiriman | Fabless, IDM | Perlu dibedakan dari penjualan terminal (sell-through), saluran bisa menumpuk stok |
| ASP | Harga jual rata-rata | Semua segmen | Perubahan mix bisa menutupi pricing riil; kenaikan porsi high-end mendongkrak ASP |
| Content per unit | Nilai semikonduktor per mesin | Fabless | Kenaikan content adalah penggerak struktural jangka panjang, perlu dipisah dari pangsa |
| Design win | Kemenangan desain | Fabless | **Design win yang diumumkan belum sama dengan pendapatan terealisasi**, perlu lihat titik waktu produksi massal |
| Market share | Pangsa (berdasarkan nominal atau unit) | Semua segmen | Definisi denominator berbeda bisa membalik kesimpulan |
| Wafer shipments | Volume pengiriman wafer | Foundry, IDM | Perlu dikaitkan dengan mix node, harga per unit node advanced sangat berbeda |
| Utilization | Utilisasi kapasitas | Foundry, IDM, OSAT | **Full load tidak sama dengan return tinggi**, bergantung pada node dan pricing |
| Node mix | Struktur node proses | Foundry | Porsi node advanced menentukan margin kotor dan premium teknologi |
| Yield | Yield produksi | Foundry, IDM, OSAT | Ramp-up yield node awal langsung menentukan titik waktu profitabilitas |
| Wafer ASP | Harga jual per wafer | Foundry | Sangat dipengaruhi struktur pelanggan dan perubahan node |
| Bit shipment / bit growth | Pengiriman dan pertumbuhan bit | Memory | Pertumbuhan pendapatan mungkin hanya dari harga, harus diurai volume dan harga |
| Cost per bit | Biaya per unit | Memory | Migrasi proses adalah jalur utama penurunan biaya jangka panjang |
| Hari inventori | Inventori / biaya harian rata-rata | Semua segmen | Perlu dilihat bersamaan dengan inventori pelanggan dan saluran |
| Bookings / backlog | Pesanan dan backlog | Equipment, material | **Backlog bisa dibatalkan, ditunda, atau dipesan ganda** |
| Book-to-bill | Rasio pesanan-pengiriman | Equipment | Sebagian perusahaan sudah berhenti mengungkap, perlu indikator pengganti |
| WFE | Wafer Fab Equipment spending global | Equipment | Indikator total industri, perlu diverifikasi silang dengan capex pelanggan |
| Service / basis instalasi | Pendapatan jasa dan jumlah alat yang beroperasi | Equipment | Pendapatan jasa adalah buffer siklus, perlu dirinci tersendiri |
| RPO / ARR / royalty | Subscription dan royalti | EDA/IP | **Indikator subscription dan siklus royalti tidak boleh dicampur** |
| Porsi pendapatan advanced packaging | Porsi CoWoS/HBM, dll. | OSAT, Foundry | Packaging biasa dan advanced packaging tidak boleh dicampur valuasinya |
| Capex / revenue | Intensitas modal | Foundry, IDM, Memory | Perlu dikaitkan dengan siklus depresiasi dan titik waktu penambahan kapasitas |
| ROIC lintas siklus | Return rata-rata modal yang diinvestasikan lintas siklus | Segmen aset berat | ROIC satu tahun tidak bermakna, harus lintas siklus |
| Porsi pendapatan terbatas | Pendapatan yang terdampak kontrol ekspor | Semua segmen | Perlu dibedakan kerugian permanen dan bagian yang bisa disubstitusi |

8 indikator yang wajib diungkap duluan: pemisahan units dan ASP, mix produk/terminal, pangsa, bridge margin kotor, hari inventori (tiga lapis), capex dan depresiasi, konsentrasi pelanggan, porsi pendapatan terbatas ekspor.

## 5. Struktur Model Keuangan

### Model Pendapatan

Pilih penggerak berdasarkan segmen, hindari ekstrapolasi dari satu tingkat pertumbuhan pendapatan tunggal:

1. **Fabless**: `penjualan terminal × content × pangsa × ASP`, dimodelkan terpisah per pasar terminal (AI/data center, handphone, PC, otomotif, industrial).
2. **Foundry / IDM**: `wafer starts × utilization × wafer ASP`, dilapiskan per node.
3. **Memory**: `bit shipment × ASP`, sekaligus bangun balance supply-demand (penambahan supply vs penambahan permintaan) untuk menentukan arah harga.
4. **Equipment**: `capex pelanggan × pangsa × mix tipe alat` + pendapatan jasa (basis instalasi × pendapatan jasa per mesin).
5. **EDA/IP**: pendapatan subscription (didorong ARR/RPO) dan pendapatan royalti (volume pengiriman pelanggan × tarif royalti) dimodelkan terpisah.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, harus mencantumkan asumsi siklus secara eksplisit (titik balik siklus harga, siklus inventori, siklus capex).
- Dipisah tersendiri kontribusi volume, harga, mix, pangsa, dan nilai tukar; jika tidak bisa dipisah tulis "pemisahan tidak diperoleh" dan turunkan tingkat keyakinan.
- Siklus inventori diverifikasi dengan **tiga lapis**: hari inventori perusahaan + inventori pelanggan/saluran + shipments/ASP industri.

### Model Biaya, Modal, dan Margin Kotor

- **Bridge margin kotor**: minimal diurai harga, mix produk, yield, biaya foundry/material, depresiasi, dan impairment/write-back inventori satu kali. Margin kotor dari pricing akibat kekurangan pasokan tidak boleh diekstrapolasi.
- **Capex dan depresiasi**: bangun bridge 5–10 tahun, cantumkan jelas titik waktu penambahan kapasitas, periode depresiasi, dan kurva ramp-up kapasitas. Subsidi (seperti CHIPS Act) dan uang muka pelanggan dapat mendistorsi FCF, harus dirinci tersendiri.
- **Intensitas R&D**: investasi R&D untuk node advanced dan chip besar adalah barrier masuk, juga fixed cost. Rasio R&D/pendapatan perlu dikaitkan dengan irama roadmap produk.
- **Modal kerja neto**: inventori, piutang usaha, dan komitmen pembelian (purchase commitment) ketiganya akan sama-sama memburuk saat siklus berbalik, perlu dimodelkan bersamaan.
- **Komitmen pembelian dan booking kapasitas**: long-term agreement (LTA), uang muka kapasitas akan menjadi liabilitas saat permintaan menurun, harus diekstrak dari catatan.

### Batasan Asumsi Steady State

- DCF segmen aset berat (Foundry/IDM/Memory) **harus memeriksa ROIC lintas siklus**, tidak boleh mengasumsikan perpetual dengan margin puncak.
- Jika hari inventori naik, guidance capex pelanggan direvisi turun, harga memasuki siklus turun, tidak boleh sekaligus memberi pertumbuhan tinggi, margin kotor tinggi, dan discount rate rendah.
- Industri memory tidak memiliki margin steady state yang stabil, harus menggunakan rata-rata lintas siklus atau balance supply-demand untuk menurunkannya.
- Jika dampak kontrol ekspor dinilai sebagai kerugian permanen, harus langsung menurunkan TAM dan pangsa akhir, bukan hanya menambahkan risk premium.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **Reverse DCF**: dari harga saat ini, dibalik untuk mendapatkan implied permintaan terminal, pangsa, jalur ASP, dan margin kotor steady state, untuk menjawab "apa yang sudah di-price in pasar".
2. **DCF tiga skenario**: skenario harus mencakup permintaan terminal, pangsa, ASP/siklus harga, margin kotor, batasan ekspor, bottleneck supply, dan return capex. **Probabilitas tidak boleh hanya ditentukan oleh guidance manajemen**.
3. **Multiple lintas siklus**: P/E, EV/EBITDA, EV/Sales semua harus menggunakan laba ternormalisasi lintas siklus. **Dilarang menggunakan laba puncak dengan multiple median** — ini adalah kesalahan fatal paling umum dalam valuasi semikonduktor.
4. **Kalibrasi posisi siklus**: tentukan dengan jelas posisi laba saat ini relatif terhadap rata-rata lintas siklus (X% di atas/bawah puncak), dan jelaskan alasannya.

### Opsional

- **P/B dan nilai reposisi**: bisa digunakan untuk Foundry/IDM di dasar siklus, mencerminkan biaya reposisi kapasitas.
- **Metode laba ternormalisasi**: di dasar siklus gunakan margin rata-rata lintas siklus untuk merestorasi laba, baru dikalikan multiple median.
- **SOTP**: perusahaan multi-bisnis dinilai per segmen desain, manufaktur, jaringan, software, atau jasa; **net cash dan investasi strategis dipisah tersendiri, hindari penghitungan ganda**.
- **Metode nilai kapasitas**: perusahaan equipment dan material bisa menggunakan basis instalasi × nilai jasa siklus hidup per mesin sebagai cross-check.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- **Posisi value chain**: Fabless, Foundry, IDM, Memory, Equipment, EDA/IP, OSAT, **tidak boleh dicampur lintas segmen**.
- Eksposur pasar terminal: struktur porsi AI/data center, handphone, PC, otomotif, industrial, konsumen.
- Posisi siklus: fase restocking, destocking, harga naik, atau harga turun.
- Intensitas modal: framework valuasi perusahaan desain aset ringan dan perusahaan manufaktur aset berat berbeda.
- Eksposur geopolitik: tingkat dampak kontrol ekspor, distribusi geografis kapasitas, struktur regional pelanggan.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi intensitas modal, struktur terminal, atau posisi siklus jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

Setelah laporan keuangan harus membangun empat bridge: **bridge pendapatan** (units/ASP/mix), **bridge margin kotor** (harga/yield/biaya), **bridge inventori** (perusahaan/pelanggan/saluran), **bridge supply** (kapasitas/advanced packaging/HBM/equipment).

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan, margin kotor, EPS, guidance kuartal depan relatif terhadap konsensus? |
| Pemisahan pendapatan | Pertambahan berasal dari units, ASP, mix, pangsa, atau nilai tukar? Dari pasar terminal mana? |
| Pesanan dan konsumsi | Apakah pesanan konsisten dengan konsumsi aktual terminal? Permintaan riil atau restocking/double ordering? |
| Inventori | Apakah arah inventori tiga lapis (perusahaan, pelanggan, saluran) konsisten? Hari inventori di persentil berapa? |
| Margin kotor | Perubahan berasal dari harga, yield, mix, depresiasi, atau impairment/write-back inventori? |
| Roadmap produk | Apakah produksi massal generasi berikutnya, ramp-up yield, dan adopsi pelanggan sesuai rencana? Ada keterlambatan? |
| Supply | Apakah advanced packaging, HBM, kapasitas foundry menjadi bottleneck? Bagaimana alokasi kuota? |
| Capex | Apakah capex dan komitmen pembelian mendahului permintaan riil? Apakah jalur return jelas? |
| Geopolitik | Apakah dampak kontrol ekspor berpindah ke pelanggan/regional lain, atau hilang permanen? |
| Guidance | Apakah guidance pendapatan, margin kotor, capex mengubah model jangka panjang dan penilaian siklus? |
| Earnings call | Apakah nada bicara tentang visibilitas permintaan, kualitas pesanan, lingkungan harga, inventori pelanggan melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan permintaan AI, titik balik inventori, siklus harga, atau return capex? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 10% tapi indeks semikonduktor (seperti SOX) naik 6% di hari yang sama, reaksi spesifik perusahaan sekitar +4%.

## 8. Moat & Penilaian Kompetitif

Moat semikonduktor tidak bisa hanya ditulis "unggul teknologi". **Keunggulan teknologi harus bisa tercermin sebagai pangsa, ASP, margin kotor, atau return modal**, jika tidak itu hanya biaya R&D. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Lock-in ekosistem software | Toolchain developer, programming model membentuk barrier migrasi (seperti CUDA) | Hanya keunggulan performa hardware, software bisa disubstitusi |
| Learning curve proses | Kecepatan ramp-up yield node advanced terus memimpin, kurva biaya lebih landai | Follower node, yield tertinggal satu generasi |
| Barrier IP dan paten | Portofolio IP inti membentuk chip cross-licensing dan barrier masuk | IP bisa dihindari atau sudah kadaluarsa |
| Siklus sertifikasi dan peralihan | Siklus sertifikasi otomotif/industrial/medis panjang, biaya peralihan sangat tinggi | Produk level konsumen, pelanggan bisa cepat beralih |
| Skala dan daya tawar procurement | Skala membawa keunggulan biaya wafer, material, packaging | Skala tidak cukup, daya tawar kapasitas lemah |
| Basis instalasi dan jasa | Alat yang beroperasi membentuk pendapatan jasa berkelanjutan dan stickiness pelanggan | Penjualan satu kali, tanpa pendapatan lanjutan |
| Co-design dengan pelanggan | Kolaborasi mendalam dengan pelanggan utama, masuk ke roadmap mereka | Pemasok produk standar, kompetisi harga |
| Kontrol kapasitas dan kuota | Menguasai kapasitas langka (advanced packaging/HBM), bisa mengalokasikan kuota | Bergantung kapasitas pihak ketiga, tanpa hak prioritas |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "unggul teknologi", tapi pangsa menurun, ASP tertekan, margin kotor lebih rendah dari sejenis, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- Inventori dan piutang usaha naik bersamaan, dan pertumbuhannya lebih cepat dari pendapatan.
- Backlog kuat tapi guidance capex pelanggan direvisi turun — pesanan mungkin double ordering atau akan dibatalkan.
- Perbaikan margin kotor utamanya mengandalkan pricing dari kekurangan pasokan, bukan penurunan biaya atau upgrade struktur produk.
- Capex tinggi berbarengan dengan penurunan utilisasi kapasitas.
- Roadmap produk berulang kali tertunda, atau titik waktu produksi massal terus mundur.
- Eksposur terlalu tinggi pada satu pelanggan, satu foundry, atau satu regional tanpa alternatif.
- "Pendapatan AI" yang didefinisikan sendiri oleh perusahaan kurang definisi jelas atau basisnya terus berubah.
- Melakukan buyback besar atau M&A harga tinggi pada level laba puncak siklus.
- Skala komitmen pembelian (LTA) dan uang muka kapasitas besar, tapi visibilitas permintaan menurun.
- Perusahaan memory melakukan ekspansi kapasitas di titik harga tinggi, dan sejenis juga melakukan ekspansi bersamaan (disiplin supply rusak).

### Daftar Bukti Sanggahan

Setiap laporan semikonduktor minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Pangsa di suatu pasar terminal turun N kuartal berturut-turut.
- Margin kotor jatuh di bawah ambang tertentu dan tidak bisa dijelaskan dengan mix atau faktor satu kali.
- Hari inventori melebihi persentil historis tertentu, atau inventori saluran signifikan lebih tinggi dari tren inventori perusahaan.
- Ramp-up yield atau produksi massal node baru tertunda melebihi durasi tertentu.
- Guidance capex pelanggan direvisi turun melebihi besaran tertentu.
- Kontrol ekspor diperluas ke kategori produk yang masih bisa dijual saat ini.

### Kesalahpahaman Umum

- **Menggunakan laba puncak dengan multiple median** — kesalahan nomor satu dalam valuasi semikonduktor. P/E rendah di puncak siklus seringkali justru saat termahal.
- Menganggap permintaan restocking sebagai pertumbuhan struktural, menyebabkan tidak siap menghadapi siklus turun.
- Menganggap backlog sebagai pendapatan yang sudah terkunci, mengabaikan klausul pembatalan dan penundaan.
- Menganggap design win sebagai pendapatan, mengabaikan titik waktu produksi massal, alokasi pangsa, dan volume penjualan akhir.
- Menganggap full capacity sebagai return tinggi, mengabaikan struktur node dan level pricing.
- Menganggap pertumbuhan pendapatan memory sebagai pertumbuhan volume, padahal sebenarnya seluruhnya dari harga.
- Menyamakan langsung keunggulan teknologi dengan nilai investasi, mengabaikan apakah terkonversi menjadi hasil keuangan.
- Menambahkan diskon risiko sederhana untuk dampak kontrol ekspor, tanpa menyesuaikan TAM dan pangsa akhir.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan semikonduktor selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel Positioning Value Chain dan KPI

| Indikator | Nilai Terbaru | YoY/QoQ | Tren 8 Kuartal Terakhir | Posisi vs Sejenis | Sumber & Basis |
|---|---:|---:|---|---|---|
| Positioning value chain dan segmen utama | | | | | |
| Pemisahan Units / ASP | | | | | |
| Struktur pendapatan pasar terminal | | | | | |
| Pangsa (cantumkan denominator) | | | | | |
| Margin kotor (dengan bridge) | | | | | |
| Hari inventori (perusahaan/saluran) | | | | | |
| Capex / depresiasi | | | | | |
| Konsentrasi pelanggan | | | | | |
| Porsi pendapatan terbatas ekspor | | | | | |

### Tabel Siklus Inventori dan Supply

| Lapisan | Level Saat Ini | Persentil Historis | Arah | Sumber |
|---|---:|---:|---|---|
| Hari inventori perusahaan | | | | |
| Inventori pelanggan/saluran | | | | |
| Shipments / ASP industri | | | | |
| Bottleneck supply kunci (advanced packaging/HBM/equipment) | | | | |

### Roadmap dan Titik Verifikasi

| Produk/Node | Titik Waktu Produksi Massal Rencana | Status Yield | Adopsi Pelanggan | Risiko |
|---|---|---|---|---|

### Tabel Asumsi Valuasi (Lintas Siklus)

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Pertumbuhan permintaan terminal | | | | |
| Jalur pangsa | | | | |
| ASP / siklus harga | | | | |
| Margin kotor lintas siklus | | | | |
| ROIC lintas siklus | | | | |
| Laba ternormalisasi dan multiple median | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada pendapatan kuartal ini, melainkan apakah dapat menjaga pangsa Y% di pasar terminal X dalam N tahun ke depan, dan menjaga margin kotor lintas siklus di Z%."
- "Laba saat ini relatif terhadap rata-rata lintas siklus berada di posisi ……; jika menggunakan laba ternormalisasi bukan laba periode berjalan, multiple valuasi seharusnya ……"
- "Jika salah satu indikator inti berikut — pangsa / margin kotor / inventori / yield / capex pelanggan — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
