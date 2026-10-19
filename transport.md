# Lampiran Riset Mendalam Industri Penerbangan/Transportasi

Berlaku untuk maskapai penerbangan, bandara, kereta api, pelayaran (shipping), kurir/logistik, dan freight forwarding. Kesamaan: aset berjenis jaringan + tarif siklikal kuat + operating leverage tinggi, **framework valuasi antar sub-sektor sangat berbeda, tidak boleh dicampur**. Bagian yang teregulasi dari bandara dan kereta api sebaiknya mengacu pada framework aset teregulasi di `industries/utilities.md`.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Transportasi
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Identifikasi dulu sub-sektornya**, framework valuasi sama sekali berbeda:
  - **Maskapai penerbangan**: **salah satu industri penghancur modal terbesar dalam sejarah**. Lihat unit revenue (RASK/PRASK) − unit cost (CASK, tanpa fuel), load factor, rencana fleet. Low-cost carrier dan full-service carrier harus dibandingkan terpisah.
  - **Bandara/kereta api**: infrastruktur teregulasi, gunakan framework aset teregulasi + valuasi segmen non-aero/diversifikasi (duty-free, properti).
  - **Pelayaran (shipping)**: murni siklus tarif (BDI, SCFI, TCE), lihat siklus order book/delivery kapasitas + nilai fleet (NAV).
  - **Kurir/logistik**: volume × harga per unit − biaya per unit, efek jaringan skala signifikan. Pisahkan lanskap kompetisi paket e-commerce dan paket time-sensitive.
  - **Freight forwarding**: laba siklikal aset ringan (spread tarif), **laba di periode tarif melonjak tidak bisa diperpetualkan**.
- **Sisi supply adalah sumber utama excess return di industri ini**. Order book, pensiun/scrapping, batasan regulasi (hak penerbangan/slot/lisensi) lebih bisa diriset dan diprediksi dibanding proyeksi permintaan.
- **Dilarang menggunakan P/E di puncak siklus**. Saat laba di titik puncak, P/E rendah adalah sinyal jual, bukan sinyal beli.
- Operating leverage tinggi berarti perubahan kecil permintaan atau tarif akan membawa fluktuasi laba besar. Harus diberikan titik break-even (load factor atau tarif).
- Liabilitas sewa, sale-leaseback, dan komitmen pesanan adalah beban off-balance-sheet/semi-off-balance-sheet yang paling umum di industri ini, harus direstorasi.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Data operasional (frekuensi tinggi, mudah diperoleh)**: data operasional bulanan IATA dan masing-masing maskapai, throughput pelabuhan, Clarksons (tarif dan order book pelayaran), badan pos nasional (volume kurir), statistik volume kereta. **Ini adalah keunggulan terbesar industri ini — data operasional frekuensi tinggi tersedia publik.**
2. **Pengajuan regulasi dan pengungkapan perusahaan**: 10-K/20-F, rincian fleet/armada kapal, jadwal pesanan dan delivery, catatan sewa, dokumen pricing regulasi.
3. **Indeks tarif**: BDI, SCFI, CCFI, TCE, indeks tarif kargo udara; pemantauan harga tiket pesawat.
4. **Regulasi dan kebijakan**: hak penerbangan, alokasi slot, regulasi emisi (seperti CORSIA, EU ETS), dokumen siklus pricing regulasi.
5. **Asosiasi industri dan konsultan**: statistik IATA, ICAO, asosiasi logistik masing-masing negara, perlu dicantumkan basisnya.

### Mekanisme Kewajaran

- **Basis indikator per unit**: RASK/CASK harus dicantumkan apakah termasuk kargo, apakah tanpa fuel, berdasarkan available seat kilometer atau revenue seat kilometer. Samakan sebelum membandingkan lintas perusahaan.
- **Pencantuman sumber tarif**: tarif spot, kontrak jangka panjang, dan TCE sangat berbeda, harus dicantumkan yang mana yang digunakan dan titik waktunya.
- **Prioritaskan data supply**: rasio order book/kapasitas existing, jadwal delivery, volume scrapping adalah data keras yang bisa diverifikasi, diutamakan dari proyeksi permintaan.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "tarif akan tetap tinggi" harus dikaitkan dengan order book, irama delivery, dan volume scrapping — bukan hanya mengutip harga spot periode berjalan.
- **Bedakan siklus dan struktural**: penurunan unit revenue bisa jadi siklus penambahan kapasitas, bisa juga memburuknya lanskap kompetisi. Harus dibedakan dengan data supply dan pangsa.
- **Hindari survivorship bias**: peer set maskapai dan pelayaran harus mencakup perusahaan yang pernah mengalami restrukturisasi kebangkrutan — ini adalah norma industri, bukan anomali.

## 3. Pohon Penggerak Nilai Transportasi

```text
Nilai maskapai = ASK (kapasitas) × load factor × unit revenue (RASK) − unit cost (CASK) − fuel − sewa
Nilai pelayaran = kapasitas fleet × utilisasi × TCE − biaya operasional − biaya pendanaan; batas bawah adalah NAV fleet
Nilai kurir = volume × pendapatan per paket − biaya per paket (pengenceran skala)
Nilai bandara = volume penumpang × biaya aeronautika (teregulasi) + pendapatan non-aero (duty-free/properti/iklan)

Enterprise Value =
  pertumbuhan volume/kapasitas
  × selisih unit revenue dan unit cost
  × penyesuaian posisi siklus (persentil historis tarif)
  × intensitas batasan supply (order book, slot, hak penerbangan)
  ÷ discount rate risiko
  − liabilitas sewa dan komitmen pesanan off-balance-sheet
  − eksposur fuel/nilai tukar
  − kesalahan alokasi modal dari ekspansi di puncak siklus
```

Laporan minimal harus menjawab:

- Di persentil historis berapa tarif/unit revenue saat ini?
- Berapa penambahan kapasitas sisi supply dalam 2–3 tahun ke depan (rasio order book/kapasitas existing)? Apakah akan menekan tarif?
- Berapa load factor atau tarif break-even? Berapa margin of safety saat ini?
- Di mana posisi unit cost (tanpa fuel) relatif terhadap sejenis? Apakah keunggulan biaya bersifat struktural?
- Berapa leverage riil setelah direstorasi sewa dan komitmen pesanan?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Sub-sektor | Jebakan Umum |
|---|---|---|---|
| ASK / ATK | Available seat kilometer / available ton kilometer | Maskapai | Indikator penambahan kapasitas |
| RPK | Revenue passenger kilometer | Maskapai | Dibandingkan dengan ASK untuk mendapat load factor |
| Load factor | RPK / ASK | Maskapai | Load factor tinggi jika dari diskon tidak bermakna |
| RASK / PRASK | Pendapatan per available seat kilometer | Maskapai | Perlu dilihat bersama load factor |
| CASK ex-fuel | Unit cost tanpa fuel | Maskapai | **Indikator kompetitif inti** |
| Selisih per unit | RASK − CASK | Maskapai | Menentukan profitabilitas |
| Fleet dan pesanan | Fleet existing, order book, waktu delivery | Maskapai | Pesanan adalah komitmen modal yang rigid |
| Rasio hedging fuel | Porsi fuel yang sudah di-hedge | Maskapai | Hedging menunda dampak harga minyak |
| Porsi pendapatan ancillary | Pendapatan tambahan seperti biaya bagasi | Maskapai | **Kenaikan ketergantungan secara tiba-tiba adalah red flag** |
| TCE | Time charter equivalent | Pelayaran | Indikator pemurnian tarif spot |
| Rasio order book/kapasitas | Kapasitas yang sedang dibangun / kapasitas existing | Pelayaran | **Indikator leading paling penting di sisi supply** |
| Usia kapal / volume scrapping | Usia fleet dan skala pembongkaran kapal | Pelayaran | Scrapping kapal tua adalah sinyal clear-out supply |
| NAV fleet | Nilai kapal bekas − net debt | Pelayaran | Batas bawah valuasi di dasar siklus |
| Pertumbuhan volume | Volume bisnis kurir | Kurir | Dibandingkan pertumbuhan industri untuk melihat pangsa |
| Pendapatan per paket (ASP) | Pendapatan / volume | Kurir | Terus menurun saat perang harga |
| Biaya per paket | Biaya / volume | Kurir | Pengenceran skala adalah logika inti |
| Utilisasi kapasitas | Utilisasi kapasitas sorting/transportasi | Kurir | Menentukan biaya per unit |
| Operating ratio (OR) | Biaya operasional / pendapatan operasional | Kereta api | **Perbaikan jika dari pemotongan capex adalah menguras masa depan** |
| Mix volume | Struktur batu bara/kimia/intermodal, dll. | Kereta api | Harga dan siklus berbeda per jenis kargo |
| Volume penumpang | Throughput bandara | Bandara | Kontribusi non-aero penumpang internasional jauh lebih tinggi dari domestik |
| Porsi pendapatan non-aero | Pendapatan duty-free/iklan/properti | Bandara | **Penandatanganan ulang kontrak duty-free adalah risiko besar** |
| Liabilitas sewa | Kapitalisasi operating lease | Semua sub-sektor | Sering diremehkan, perlu direstorasi ke EV |
| Load factor/tarif break-even | Level yang diperlukan untuk impas | Maskapai, pelayaran | Indikator inti operating leverage tinggi |

8 indikator yang wajib diungkap duluan: unit revenue dan unit cost (tanpa fuel), load factor/rasio muat, order book sisi supply dan rencana delivery, persentil historis tarif, titik break-even, liabilitas sewa dan komitmen pesanan, eksposur fuel/nilai tukar, tren unit economics.

## 5. Struktur Model Keuangan

### Model Pendapatan

Pilih penggerak berdasarkan sub-sektor:

1. **Maskapai**: `ASK × load factor × RASK`, dilapiskan per jaringan rute (domestik/internasional/regional), kargo dipisah tersendiri.
2. **Pelayaran**: `kapasitas fleet × utilisasi × TCE`, dilapiskan per tipe kapal dan rute; kontrak jangka panjang dan spot dipisah.
3. **Kurir**: `volume × pendapatan per paket`, dilapiskan per produk (paket e-commerce/time-sensitive/internasional).
4. **Bandara**: `volume penumpang × biaya aeronautika per kapita` (teregulasi) + `volume penumpang × konsumsi non-aero per kapita × rate komisi`.
5. **Kereta api**: `volume × tarif rata-rata`, dilapiskan per jenis kargo, OR dimodelkan tersendiri.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, **harus mencantumkan asumsi penambahan kapasitas sisi supply secara eksplisit** (dari order book dan jadwal delivery).
- Asumsi tarif selalu diberikan tiga tier skenario: harga spot, harga mid-cycle, harga yang didukung biaya jangka panjang.
- Unit revenue dan unit cost harus diproyeksikan terpisah, tidak boleh hanya proyeksi margin.

### Model Biaya, Aset, dan Liabilitas

- **Pemisahan biaya per unit**: fuel, tenaga kerja, biaya takeoff-landing/pelabuhan, perbaikan, depresiasi, sewa dimodelkan terpisah. **CASK ex-fuel adalah pembacaan inti daya saing**.
- **Fuel dan nilai tukar**: berikan skala eksposur, rasio hedging dan tenor, elastisitas laba terhadap perubahan harga per unit.
- **Restorasi sewa**: operating lease harus dikapitalisasi masuk ke EV dan leverage. Net debt yang terlihat di laporan maskapai dan pelayaran sering sangat meremehkan beban riil.
- **Komitmen pesanan**: pesanan pesawat/kapal di tangan adalah komitmen modal yang rigid, harus dicantumkan nominal dan jadwal delivery, akan menjadi beban fatal saat siklus turun.
- **Pemeliharaan dan depresiasi**: overhaul besar pesawat, drydocking kapal adalah pengeluaran besar siklikal, tidak boleh diratakan.
- **Perhitungan break-even**: tentukan fixed cost secara jelas, hitung level load factor atau tarif yang diperlukan untuk impas.

### Batasan Asumsi Steady State

- **Dilarang memperpetualkan harga spot**. Nilai terminal harus menggunakan harga yang didukung biaya jangka panjang atau rata-rata lintas siklus.
- Jika rasio order book/kapasitas tinggi (banyak kapal/pesawat baru akan delivery), tidak boleh sekaligus mengasumsikan tarif tetap tinggi.
- ROIC jangka panjang maskapai dan pelayaran secara historis umumnya lebih rendah dari WACC, memberikan return perpetual di atas cost of capital memerlukan alasan struktural yang sangat kuat.
- "Mengompensasi harga dengan volume" di kurir ada batasnya: kecepatan penurunan biaya per paket harus bisa menutupi penurunan pendapatan per paket, jika tidak ekspansi skala adalah penghancuran nilai.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **Maskapai/pelayaran: laba mid-cycle × multiple median rendah (biasanya 5–8x) + dual anchor NAV**. NAV menggunakan nilai pasar kapal/pesawat bekas dikurangi net debt, sebagai batas bawah valuasi di dasar siklus.
2. **Positioning siklus**: tentukan dengan jelas persentil historis tarif/unit revenue saat ini. **Dilarang menggunakan P/E di puncak siklus** — P/E rendah berarti laba sedang di titik puncak.
3. **Reverse DCF**: dari harga saat ini, dibalik untuk mendapatkan implied tarif jangka panjang, selisih per unit, dan asumsi volume.
4. **Skenario sisi supply**: berdasarkan order book dan jadwal delivery, berikan skenario pertumbuhan kapasitas dan tekanannya terhadap tarif.

### Opsional

- **Bandara/kereta api: EV/EBITDA + framework return aset teregulasi**, arus kas stabil bisa menggunakan DCF dengan periode eksplisit panjang.
- **Kurir: DCF unit economics + EV/EBITDA**, pemimpin skala diberi premium barrier jaringan.
- **Freight forwarding: laba ternormalisasi**, dikeluarkan laba berlebih dari periode tarif melonjak.
- **Nilai reposisi**: digunakan sebagai batas bawah saat undervaluasi ekstrem, menggunakan biaya reposisi kapasitas.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Sub-sektor: maskapai, pelayaran, kurir, bandara, kereta api, freight forwarding, **sama sekali tidak boleh dicampur**.
- Model bisnis: low-cost vs full-service carrier; paket e-commerce vs time-sensitive.
- Struktur aset: rasio milik sendiri vs sewa, mempengaruhi leverage dan struktur biaya.
- Jaringan rute/jalur: siklus domestik, internasional, regional tidak sinkron.
- Posisi siklus dan resiliensi balance sheet.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi struktur aset atau positioning jaringan jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan, unit revenue, unit cost, EPS, guidance kapasitas relatif terhadap konsensus? |
| Unit economics | Perubahan QoQ RASK/pendapatan per paket dan CASK/biaya per paket? Selisih melebar atau menyempit? |
| Load factor | Perubahan load factor/utilisasi kapasitas? Apakah dicapai dengan menurunkan harga? |
| Guidance kapasitas | Guidance pertumbuhan kapasitas perusahaan vs pertumbuhan permintaan? Bagaimana penambahan kapasitas industri secara keseluruhan? |
| Sisi supply | Apakah order book, rencana delivery, pensiun/scrapping berubah? |
| Fuel dan nilai tukar | Perubahan eksposur dan hedging? Dampaknya terhadap biaya periode depan? |
| Sewa dan komitmen | Apakah sewa off-balance-sheet, sale-leaseback, komitmen pesanan bertambah? |
| Ancillary/non-aero | Apakah porsi pendapatan ancillary melonjak tiba-tiba (menutupi lemahnya bisnis utama)? Apakah kontrak duty-free akan segera ditandatangani ulang? |
| Positioning siklus | Apakah posisi persentil historis tarif saat ini berubah? |
| Earnings call | Apakah nada bicara tentang visibilitas permintaan, lingkungan pricing, disiplin kapasitas, tekanan biaya melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan tarif, penambahan kapasitas, perbaikan biaya, atau pemulihan permintaan? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 8% tapi sektor transportasi naik 5% di hari yang sama, reaksi spesifik perusahaan sekitar +3%.

## 8. Moat & Penilaian Kompetitif

Industri transportasi mayoritas jasa homogen, **moat utamanya berasal dari kelangkaan regulasi dan densitas jaringan**. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Resource langka teregulasi | Slot, hak penerbangan, pelabuhan, hak jalan, dll. langka dan sulit ditiru | Rute/jalur kompetisi bebas, tanpa barrier masuk |
| Densitas jaringan | Densitas jaringan hub atau last-mile membawa keunggulan biaya dan waktu | Jaringan jarang, bergantung transit pihak ketiga |
| Keunggulan biaya per unit | CASK ex-fuel atau struktur biaya per paket struktural lebih rendah dari sejenis | Keunggulan biaya dari hedging fuel sementara atau subsidi |
| Kualitas aset | Fleet/armada kapal muda dan efisien, biaya fuel dan pemeliharaan rendah | Aset usang, biaya pemeliharaan tinggi dan menghadapi batasan emisi |
| Stickiness pelanggan | Program frequent flyer, kontrak enterprise, logistik kontrak mengunci | Kompetisi harga murni, pelanggan tanpa biaya peralihan |
| Disiplin pricing | Konsentrasi industri tinggi dan secara historis tidak ada perang harga | Perang harga sering terjadi, kapasitas berlebih |
| Bisnis non-aero/bernilai tambah | Duty-free, properti, jasa supply chain memberikan margin tinggi stabil | Pendapatan transportasi tunggal, eksposur siklus terbuka penuh |
| Disiplin modal | Secara historis tidak memesan kapasitas membabi buta di puncak tarif | Memesan kapal/pesawat besar-besaran di puncak siklus |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "unggul biaya", tapi CASK ex-fuel lebih tinggi dari median sejenis, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- **Memesan kapal/pesawat besar-besaran di puncak siklus** — ini adalah perilaku penghancuran nilai paling klasik di industri ini.
- Sering menggunakan sale-leaseback untuk mempercantik balance sheet, beban riil tidak berkurang.
- Porsi pendapatan ancillary (seperti biaya bagasi) melonjak tiba-tiba, menutupi penurunan unit revenue bisnis utama.
- Perusahaan freight forwarding atau pelayaran melakukan ekspansi fixed cost atau akuisisi di posisi tarif tinggi.
- Load factor/rasio muat naik tapi unit revenue menurun (mengompensasi harga dengan volume).
- Perbaikan OR kereta api utamanya dari pemotongan maintenance capex, bersifat menguras masa depan.
- Kontrak duty-free bandara akan segera ditandatangani ulang dan daya tawar menurun.
- Rasio hedging fuel rendah saat harga minyak rendah, tinggi saat harga minyak tinggi (gagal timing).
- Rasio order book/kapasitas berada di persentil historis tertinggi tapi manajemen masih bullish terhadap tarif.
- Rasio liabilitas sewa dan komitmen pesanan terhadap market cap terlalu tinggi, tidak tertahankan saat siklus turun.

### Daftar Bukti Sanggahan

Setiap laporan transportasi minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Unit revenue (RASK/pendapatan per paket) turun melebihi besaran tertentu N kuartal berturut-turut.
- CASK ex-fuel atau biaya per paket naik melebihi ambang tertentu.
- Load factor/rasio muat jatuh di bawah level break-even.
- Rasio order book/kapasitas industri melebihi persentil historis tertentu.
- Tarif jatuh di bawah harga yang didukung biaya jangka panjang.
- Net debt/EBITDA setelah restorasi sewa melebihi ambang tertentu.

### Kesalahpahaman Umum

- **Menggunakan P/E rendah sebagai indikasi murah di puncak siklus** — P/E rendah saat laba di puncak adalah sinyal bahaya.
- Memperpetualkan harga spot, mengabaikan shock supply dari order book.
- Hanya melihat load factor tanpa melihat unit revenue, mengabaikan kompensasi harga dengan volume.
- Mengabaikan operating lease, secara signifikan meremehkan leverage riil.
- Mengabaikan komitmen modal yang rigid dari pesanan di tangan.
- Menganggap laba freight forwarding di periode tarif melonjak sebagai kapabilitas operasional.
- Menganggap perbaikan OR kereta api sebagai peningkatan efisiensi, mengabaikan bahwa itu dari pemotongan pengeluaran maintenance.
- Memberikan asumsi ROIC jangka panjang di atas cost of capital untuk industri penerbangan, tanpa alasan struktural.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan transportasi selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel Unit Economics (Wajib)

| Periode | Kapasitas (ASK/kapasitas/volume) | Load Factor/Rasio Muat | Unit Revenue | Unit Cost (tanpa fuel) | **Selisih per Unit** | Biaya Fuel per Unit |
|---|---:|---:|---:|---:|---:|---:|

### Tabel Pesanan/Kapasitas Sisi Supply (Wajib)

| Item | Jumlah/Kapasitas | Rasio terhadap Kapasitas Existing | Waktu Delivery/Pensiun | Keterangan |
|---|---:|---:|---|---|
| Kapasitas existing | | | | |
| Pesanan di tangan | | | | |
| Rencana pensiun/scrapping | | | | |
| Rasio order book/kapasitas industri | | | | |
| Pertumbuhan kapasitas bersih 3 tahun ke depan | | | | |

### Tabel Positioning Siklus (Wajib)

| Indikator | Terendah Historis | Median Historis | Tertinggi Historis | Nilai Saat Ini | **Posisi Persentil** |
|---|---:|---:|---:|---:|---:|
| Tarif / unit revenue | | | | | |
| Selisih per unit | | | | | |
| Load factor/rasio muat | | | | | |

### Tabel Break-Even dan Leverage

| Item | Nilai | Keterangan |
|---|---:|---|
| Load factor/tarif break-even | | |
| Level saat ini dan margin of safety | | |
| Net debt dari laporan | | |
| Tambah: kapitalisasi operating lease | | |
| Tambah: komitmen pesanan di tangan | | |
| **Beban riil setelah restorasi** | | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Tarif / unit revenue jangka panjang | | | | |
| Unit cost (tanpa fuel) | | | | |
| Load factor/rasio muat | | | | |
| Laba mid-cycle | | | | |
| Multiple median | | | | |
| NAV aset (batas bawah) | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: tarif/unit revenue saat ini berada di persentil historis ke-X; menggunakan level mid-cycle bukan level periode berjalan untuk valuasi, nilai implisitnya adalah ……"
- "Pertumbuhan kapasitas bersih industri dalam 3 tahun ke depan adalah X% (dari order book), tekanan terhadap tarif adalah ……; ini adalah dasar utama saya menilai posisi siklus."
- "Jika salah satu indikator inti berikut — unit revenue / unit cost / load factor / rasio order book / leverage setelah restorasi — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
