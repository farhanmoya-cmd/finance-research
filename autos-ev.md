# Lampiran Riset Mendalam Industri Otomotif/EV

Berlaku untuk OEM mobil utuh (integral), pemain baru EV, komponen, dealer, dan sisi integrator rantai baterai. Karakteristik: aset berat, margin rendah, siklikal kuat + rekonstruksi value chain oleh elektrifikasi/kepintaran (smart). **Framework tradisional dan framework pertumbuhan harus dipisahkan penggunaannya, baru kemudian direkonsiliasi.**

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Otomotif
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Identifikasi dulu tipe perusahaannya**, karena frameworknya sangat berbeda:
  - **OEM tradisional**: framework saham siklikal bernilai — profitabilitas mid-cycle, utilisasi kapasitas, net cash. **Anak usaha pembiayaan (financial captive) wajib dipisah**: entitas industrial dan entitas keuangan dinilai (valuasi) secara terpisah.
  - **Pure player EV**: framework pertumbuhan — unit economics (ASP − BOM − biaya manufaktur), kemiringan kurva ramp-up produksi, runway kas. Untuk perusahaan yang belum profit, gunakan reverse DCF + skenario.
  - **Komponen**: keterikatan pelanggan/platform, logika kenaikan content per vehicle (CPV) (diuntungkan atau dirugikan oleh elektrifikasi), tekanan penurunan harga tahunan (year-on-year price-down).
  - **Dealer**: margin kotor mobil baru, layanan purna jual, penetrasi F&I (finance & insurance), perputaran inventori.
- **Pendapatan software/self-driving adalah aset bersifat opsi (optionality)**, harus diberi nilai (pricing) terpisah, **beri probabilitas, jangan beri kepastian**. Pendapatan software yang belum terealisasi tidak boleh dimasukkan ke skenario basis.
- Otomotif adalah industri aset berat dan siklikal kuat. Setiap kesimpulan profitabilitas harus menjawab **berapa volume penjualan titik impas (break-even)**, dan di mana posisi volume saat ini relatif terhadap titik tersebut.
- **Basis wholesale (grosir ke dealer) dan retail (penjualan ritel akhir) harus dipisahkan**. Pelebaran selisih wholesale-retail adalah bukti langsung penumpukan inventori di saluran (channel stuffing).
- Margin kotor per unit harus dihitung **setelah mengeluarkan pendapatan dari kredit regulasi (regulatory credits)**, karena jika tidak akan secara sistematis melebih-lebihkan kapabilitas manufaktur.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Data pendaftaran/asuransi wajib per negara**: data asuransi wajib kendaraan (compulsory traffic insurance) Tiongkok, data ACEA Eropa, data registrasi Amerika Serikat. **Data ini lebih diutamakan dibanding angka pengiriman (deliveries) yang dilaporkan sendiri oleh perusahaan**, karena mencerminkan penjualan akhir riil, bukan pengiriman ke saluran distribusi.
2. **Pengajuan regulasi & pengungkapan perusahaan**: 10-K/10-Q/laporan tahunan, pengumuman pengiriman bulanan atau kuartalan, pengungkapan kapasitas dan pabrik, laporan keuangan terpisah anak usaha pembiayaan.
3. **Asosiasi industri & data pemerintah**: data produksi-penjualan asosiasi industri otomotif masing-masing negara, teks asli kebijakan subsidi, regulasi emisi dan sistem kredit.
4. **Pemantauan harga di lapangan (terminal)**: diskon dealer, harga transaksi akhir, koefisien inventori. Merupakan indikator frekuensi tinggi yang krusial selama periode perang harga.
5. **Riset rantai pasok dan saluran distribusi**: pasokan baterai, chip — hanya sebagai petunjuk awal, perlu diverifikasi silang.

### Mekanisme Kewajaran

- **Basis pengiriman harus dicantumkan jelas**: wholesale vs retail, apakah termasuk ekspor, apakah termasuk flotila sewa (leasing fleet), apakah termasuk kendaraan yang sudah diproduksi tapi belum dikirim.
- **Basis margin kotor per unit**: harus dicantumkan apakah dikeluarkan kredit regulasi (seperti dual-credit system Tiongkok, ZEV credits AS, CO2 pooling Uni Eropa), apakah termasuk biaya pengiriman, apakah termasuk provisi garansi.
- **Volume dan harga harus dipisahkan**: pertumbuhan pendapatan diurai menjadi volume, ASP, mix model, mix regional, dan nilai tukar.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya klaim "permintaan kuat" harus dikaitkan dengan data asuransi wajib, siklus pesanan/pengiriman, diskon akhir, dan hari inventori — bukan hanya mengutip narasi manajemen.
- **Bedakan siklus dengan struktural**: penurunan volume penjualan bisa jadi siklus industri, bisa juga penurunan daya saing produk. Harus dibedakan dengan bukti pangsa pasar dan harga akhir.
- **Hindari survivorship bias**: peer set harus mencakup OEM tradisional yang kehilangan pangsa pasar dan pemain baru EV yang sudah tersingkir dari pasar.

## 3. Pohon Penggerak Nilai Otomotif

```text
Nilai OEM =
  Volume penjualan × (ASP − biaya per unit) × penyesuaian siklus
  + bisnis purna jual/komponen
  + nilai anak usaha pembiayaan (dinilai terpisah)
  + opsi software/self-driving (berbobot probabilitas)
  − beban kapasitas berlebih dan biaya fixed cost
  − nilai residu, recall, dan liabilitas garansi
  − capex transisi elektrifikasi

Unit economics = ASP − biaya material (BOM) − tenaga kerja langsung − alokasi overhead manufaktur − biaya pengiriman dan garansi
Volume penjualan break-even = biaya fixed / margin kontribusi per unit
```

Laporan minimal harus menjawab:

- Berapa margin kotor per unit yang sebenarnya setelah dikeluarkan kredit regulasi? Bagaimana trennya?
- Berapa volume penjualan break-even? Di mana posisi volume saat ini relatif terhadap titik itu, dan berapa margin of safety-nya?
- Apakah pertumbuhan penjualan berasal dari model baru, penurunan harga, atau penumpukan inventori di saluran distribusi?
- Bagaimana jalur biaya baterai ($/kWh)? Apakah jalur teknologi yang dipilih memiliki kelemahan biaya atau kinerja?
- Berapa kuartal lagi kas dapat menopang operasi (wajib dijawab untuk pemain baru EV)?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Tipe | Jebakan Umum |
|---|---|---|---|
| Volume penjualan / pengiriman | Per regional per model | OEM, EV | **Basis wholesale vs retail wajib dipisahkan dengan jelas** |
| Volume asuransi wajib / registrasi | Penjualan akhir riil | OEM, EV | Lebih diutamakan dibanding pengiriman self-reported perusahaan |
| Selisih wholesale-retail | Volume wholesale − volume retail | OEM | **Pelebaran = penumpukan inventori di saluran** |
| Hari inventori saluran | Inventori dealer / rata-rata penjualan harian | OEM, Dealer | Inventori tinggi menandai penurunan harga ke depan |
| ASP | Harga jual rata-rata | OEM, EV | Perubahan mix model bisa menutupi penurunan harga riil |
| Margin kotor per unit | (ASP − biaya per unit) | OEM, EV | **Wajib dihitung setelah dikeluarkan kredit regulasi** |
| Pendapatan kredit regulasi | Pendapatan ZEV/dual-credit/CO2 pooling | EV, OEM | Sering dimasukkan ke margin kotor untuk mempercantik margin |
| Biaya per unit / BOM | Biaya bill of materials | EV | Baterai porsi terbesar, perlu dirinci tersendiri |
| Biaya baterai $/kWh | Biaya sel dan pack | EV | Penyesuaian harga bahan baku ada lag |
| Utilisasi kapasitas | Produksi aktual / kapasitas desain | OEM, EV | Utilisasi rendah menyebabkan alokasi fixed cost yang kurang memadai |
| Volume penjualan break-even | Biaya fixed / kontribusi per unit | OEM, EV | **Indikator inti industri aset berat** |
| Siklus pesanan / pengiriman | Backlog pesanan dan lama tunggu | EV | **Pesanan yang deposit-nya bisa direfund penuh rawan inflasi angka** |
| Diskon akhir (terminal) | Harga transaksi aktual relatif terhadap harga acuan | OEM, EV | Pembacaan langsung intensitas perang harga |
| CPV (content per vehicle) | Nilai komponen dalam satu kendaraan | Komponen | Elektrifikasi bisa menambah atau mengurangi nilai berbagai komponen |
| Penurunan harga tahunan (year-on-year price-down) | Tuntutan penurunan harga tahunan | Komponen | Biasanya 3–5%/tahun, menekan margin |
| Porsi pendapatan terkait ICE | Pendapatan terkait mobil bensin | Komponen | Faktor kunci diskon nilai terminal |
| Penetrasi pembiayaan | Rasio penetrasi skema pembiayaan | OEM Finance | Subsidi bunga promosi bisa tersembunyi di anak usaha pembiayaan |
| Risiko nilai residu | Asumsi nilai residu kendaraan sewa | OEM Finance | Penurunan nilai residu EV merupakan risiko besar |
| Rasio kredit bermasalah (bad debt) | Kerugian kredit anak usaha pembiayaan | OEM Finance | Naik cepat saat ekonomi melemah |
| Runway kas | Kas / net burn rate kuartalan | Pemain baru EV | **Indikator pertama untuk perusahaan pra-profit** |
| Tingkat kapitalisasi R&D | R&D yang dikapitalisasi / total R&D | Semua tipe | Kapitalisasi agresif mempercantik laba periode berjalan |

8 indikator yang wajib diungkap duluan: volume penjualan (wholesale/retail dipisah), volume asuransi wajib, margin kotor per unit tanpa kredit, volume penjualan break-even, hari inventori saluran, diskon akhir, tren biaya baterai, runway kas (EV).

## 5. Struktur Model Keuangan

### Model Pendapatan dan Unit Economics

1. **Model volume penjualan**: dimodelkan per regional × model, membedakan wholesale dan retail, secara eksplisit menampilkan perubahan inventori saluran.
2. **Model ASP**: `harga acuan − diskon akhir × penyesuaian mix`, harus diperbarui per kuartal selama periode perang harga.
3. **Biaya per unit**: diurai menjadi BOM (baterai, chip, lainnya), tenaga kerja langsung, alokasi overhead manufaktur, biaya pengiriman dan provisi garansi.
4. **Komponen**: `volume penjualan platform pelanggan × CPV × pangsa`, dikurangi penurunan harga tahunan.
5. **Anak usaha pembiayaan**: buat balance sheet terpisah — aset berbunga, spread suku bunga, penetrasi, nilai residu, dan bad debt, **tidak boleh dikonsolidasikan dengan entitas industrial**.
6. **Software/self-driving**: dimodelkan berdasarkan penetrasi × harga per unit × probabilitas, dirinci tersendiri dan ditandai sebagai nilai opsi.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, dengan kurva ramp-up kapasitas dan titik break-even yang eksplisit (perusahaan EV).
- Margin kotor per unit harus diberikan per kuartal, dan setelah dikeluarkan kredit regulasi.
- OEM tradisional harus melakukan normalisasi volume penjualan lintas siklus, tidak boleh mengekstrapolasi dari puncak siklus.

### Model Biaya, Kapasitas, dan Kas

- **Fixed cost dan break-even**: tentukan skala fixed cost secara jelas, hitung volume penjualan break-even. Kerugian periode ramp-up pabrik baru **tidak boleh diklasifikasikan sebagai "one-time"** — ramp-up adalah bagian normal dari operasi.
- **Jalur biaya baterai**: berikan tren $/kWh berdasarkan jalur teknologi (LFP/NMC/solid-state), dan jelaskan lag penyesuaian harga bahan baku.
- **Kapasitas dan utilisasi**: kapasitas berlebih akan memburukkan biaya per unit secara signifikan, utilisasi perlu dikaitkan dengan biaya per unit.
- **Modal kerja**: **perpanjangan abnormal siklus utang usaha (payables) sama dengan menjadikan pemasok sebagai sumber pembiayaan**, harus diidentifikasi tersendiri dan dikurangkan dalam penilaian kualitas arus kas.
- **Runway kas** (wajib untuk pemain baru EV): `kas yang tersedia / net burn rate kuartalan`, dan jelaskan waktu dan dilusi pendanaan ronde berikutnya.
- **Garansi dan recall**: apakah provisi memadai, frekuensi recall historis dan biaya per kejadian.

### Batasan Asumsi Steady State

- Nilai terminal OEM tradisional harus menggunakan margin mid-cycle, rentang historis biasanya jauh lebih rendah dari rata-rata manufaktur, tidak boleh memberi margin tinggi secara perpetual.
- Perusahaan EV dengan volume penjualan di bawah titik break-even tidak boleh sekaligus mengasumsikan penurunan biaya cepat, ASP tetap, dan tanpa dilusi pendanaan.
- Penetrasi steady state pendapatan software/self-driving harus memiliki batasan probabilitas, tidak boleh default terealisasi penuh.
- Nilai terminal perusahaan komponen harus didiskon berdasarkan porsi pendapatan yang tergantung pada ICE.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **OEM tradisional**: EPS mid-cycle × P/E median historis (biasanya 6–10x) + penyesuaian net cash industrial + valuasi terpisah anak usaha pembiayaan. **EV/Sales tidak bermakna untuk saham siklikal.**
2. **Fase pertumbuhan EV**: reverse DCF sebagai framework utama — dari harga saat ini, dibalik untuk mendapatkan implied volume penjualan × profit per unit, dan **diverifikasi terhadap batas fisik total profit pool industri otomotif global** untuk menguji kewajaran.
3. **DCF tiga skenario**: mencakup volume penjualan, ASP/perang harga, biaya per unit, utilisasi kapasitas, dan dilusi pendanaan.
4. **Komponen**: EV/EBITDA + coverage order book; **eksposur elektrifikasi (porsi pendapatan terkait ICE) sebagai faktor diskon nilai terminal**.

### Opsional

- **SOTP**: entitas industrial + anak usaha pembiayaan + opsi software + investasi lain dinilai terpisah.
- **Metode unit economics**: `volume penjualan steady state × laba bersih per unit steady state × P/E median` sebagai cross-check.
- **Nilai reposisi (replacement value)**: digunakan sebagai batas bawah saat undervaluasi ekstrem, menggunakan biaya reposisi kapasitas.

**Risiko nilai residu, recall, dan perang harga harus ditangani dengan probabilitas skenario, bukan dirata-ratakan** — ini adalah risiko ekor (tail risk), perataan akan menutupi kemungkinan kebangkrutan.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Tipe: OEM tradisional, pure player EV, komponen, dealer, tidak boleh dicampur.
- Rentang harga dan posisi merek: struktur margin mewah, mainstream, ekonomi sangat berbeda.
- Fase elektrifikasi: dominan ICE, dalam transisi, full EV.
- Regional: intensitas kompetisi, subsidi, dan regulasi berbeda di Tiongkok, Eropa, Amerika Utara.
- Status profitabilitas: sudah profit, mendekati break-even, kerugian dalam, frameworknya berbeda.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi status profitabilitas atau fase elektrifikasinya jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pengiriman, ASP, margin kotor per unit, EPS, dan guidance relatif terhadap konsensus? |
| Kualitas volume | Apakah wholesale dan retail berdivergensi? Perubahan hari inventori saluran? Bagaimana konfirmasi dari volume asuransi wajib? |
| Margin kotor per unit | **Perubahan QoQ setelah dikeluarkan kredit**? Penurunan biaya berasal dari baterai, skala, atau optimasi desain? |
| Aksi harga | Apakah terjadi penurunan harga periode ini? Berapa besar diskon akhir? Dampaknya terhadap margin ke depan? |
| Ramp-up kapasitas | Apakah ramp-up pabrik/model baru sesuai rencana? Utilisasi dan biaya per unit? |
| Break-even | Berapa jarak volume penjualan saat ini dari titik break-even? Kapan bisa tercapai? |
| FCF | **Untuk perusahaan fase pertumbuhan, kas lebih penting satu tingkat dibanding laba** — bagaimana perubahan burn rate dan runway? |
| Anak usaha pembiayaan | Penetrasi, asumsi nilai residu, apakah rasio bad debt memburuk? Apakah sedang mensubsidi penjualan? |
| Pendapatan software | Apakah ada pengakuan pendapatan tangguhan (deferred revenue) yang riil? Penetrasi dan pricing? |
| Guidance | Apakah guidance pengiriman, margin kotor, capex mengubah model jangka panjang? |
| Earnings call | Apakah nada bicara tentang permintaan, perang harga, pesanan, kapasitas, pendanaan melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan pengiriman, margin kotor per unit, perang harga, atau progres self-driving? |

**Penjualan bulanan wajib dipantau dengan frekuensi tinggi**, dikombinasikan dengan data diskon akhir untuk memantau intensitas perang harga.

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 10% tapi sektor otomotif naik 5% di hari yang sama, reaksi spesifik perusahaan sekitar +5%.

## 8. Moat & Penilaian Kompetitif

Otomotif adalah industri aset berat, margin rendah, kompetisi tinggi, moat tergolong jarang. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Merek dan daya tawar harga | Pricing premium jangka panjang, diskon akhir jauh lebih rendah dari sejenis | Mengandalkan diskon promosi untuk menjaga penjualan |
| Struktur biaya | Biaya per unit struktural lebih rendah dari sejenis dan berkelanjutan | Keunggulan biaya berasal dari subsidi atau harga bahan baku sementara |
| Skala dan platform | Platform mengurangi biaya R&D dan manufaktur | Model tersebar, tingkat reuse platform rendah |
| Teknologi baterai dan e-powertrain | Baterai sendiri atau kemitraan mendalam, $/kWh terdepan | Mengandalkan baterai beli dari luar, tanpa daya tawar |
| Software dan data | Skala data flotila membentuk keunggulan iterasi self-driving, dan sudah termonetisasi | Software hanya narasi, tanpa validasi pendapatan |
| Saluran dan jaringan layanan | Jaringan dealer langsung/distribusi cakupan luas, laba purna jual stabil | Jaringan kurang atau dealer merugi |
| Kontrol rantai pasok | Komponen kunci diproduksi sendiri atau terkunci kontrak jangka panjang | Chip/baterai dikuasai pihak lain |
| Eksekusi transisi | Transisi elektrifikasi berjalan sesuai rencana tanpa merusak arus kas | Investasi transisi besar tetapi pangsa pasar tidak naik |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "premium merek", tapi diskon akhir melebar dan margin kotor per unit tanpa kredit lebih rendah dari sejenis, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- **Selisih wholesale-retail melebar** (wholesale jauh lebih tinggi dari retail), hari inventori saluran naik.
- **Perpanjangan abnormal siklus utang usaha** — menjadikan pemasok sebagai sumber pembiayaan.
- Margin kotor per unit bergantung pada pendapatan kredit regulasi, setelah dikeluarkan mendekati atau di bawah nol.
- Rasio kapitalisasi R&D meningkat agresif, mempercantik laba periode berjalan.
- Kerugian ramp-up pabrik baru berulang kali diklasifikasikan sebagai beban "one-time".
- Angka pesanan terlihat bagus tapi deposit bisa direfund penuh, dan siklus pengiriman makin pendek.
- Penetrasi anak usaha pembiayaan naik cepat, kemungkinan mensubsidi penjualan dengan subsidi bunga.
- Asumsi nilai residu EV belum disesuaikan turun seiring harga mobil bekas yang turun.
- Rasio gadai saham (pledge) founder atau pemegang saham utama tinggi.
- Runway kas kurang dari 4 kuartal tanpa diungkapnya rencana pendanaan.
- Sering menurunkan harga tapi volume penjualan tidak naik proporsional (elastisitas permintaan hilang).

### Daftar Bukti Sanggahan

Setiap laporan otomotif minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Volume asuransi wajib turun YoY N bulan berturut-turut, atau pangsa pasar jatuh di bawah ambang tertentu.
- Margin kotor per unit tanpa kredit jatuh di bawah ambang tertentu atau menjadi negatif.
- Hari inventori saluran melebihi level tertentu.
- Besaran diskon akhir melebihi rasio tertentu.
- Utilisasi kapasitas di bawah level yang dibutuhkan untuk break-even.
- Runway kas di bawah N kuartal dan lingkungan pendanaan memburuk.

### Kesalahpahaman Umum

- **Menggunakan EV/Sales untuk menilai OEM siklikal** — indikator ini sama sekali tidak bermakna untuk industri aset berat margin rendah.
- Menganggap margin kotor yang mengandung kredit regulasi sebagai kapabilitas manufaktur.
- Menganggap pengiriman wholesale sebagai permintaan akhir, mengabaikan penumpukan inventori di saluran.
- Menganggap volume pesanan sebagai permintaan yang terkunci, mengabaikan deposit yang bisa direfund.
- Menggabungkan valuasi entitas industrial dan anak usaha pembiayaan, menutupi risiko sisi keuangan.
- Memasukkan pendapatan self-driving/software ke skenario basis, bukan sebagai nilai opsi.
- Mengabaikan volume penjualan break-even, meremehkan daya rusak leverage fixed cost.
- Untuk perusahaan EV fase pertumbuhan, hanya melihat laba tanpa melihat kas, mengabaikan dilusi pendanaan.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan otomotif selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel Unit Economics (wajib, per kuartal)

| Kuartal | Volume Pengiriman | ASP | Pendapatan Kredit Regulasi | ASP Tanpa Kredit | Biaya per Unit | **Margin Kotor per Unit Tanpa Kredit** | Margin Kotor per Unit (%) |
|---|---:|---:|---:|---:|---:|---:|---:|

### Perhitungan Break-Even (wajib)

| Item | Nilai | Keterangan |
|---|---:|---|
| Fixed cost tahunan | | |
| Margin kontribusi per unit | | |
| **Volume penjualan break-even** | | |
| Volume penjualan tahunan saat ini (annualized) | | |
| Margin of safety | | |

### Tabel Kualitas Volume Penjualan

| Indikator | Nilai Terbaru | YoY/QoQ | Tren | Sumber & Basis |
|---|---:|---:|---|---|
| Pengiriman wholesale | | | | |
| Retail/volume asuransi wajib | | | | |
| Selisih wholesale-retail | | | | |
| Hari inventori saluran | | | | |
| Besaran diskon akhir | | | | |
| Pangsa pasar | | | | |

### Tabel Runway Kas (wajib untuk target EV)

| Item | Nilai |
|---|---:|
| Kas dan setara kas yang tersedia | |
| Arus kas operasi bersih kuartalan | |
| Capex kuartalan | |
| Net burn rate kuartalan | |
| **Jumlah kuartal yang dapat ditopang** | |
| Asumsi pendanaan ronde berikutnya dan dilusi | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Volume penjualan steady state | | | | |
| ASP steady state | | | | |
| Margin kotor per unit tanpa kredit steady state | | | | |
| Utilisasi kapasitas | | | | |
| Probabilitas dan skala pendapatan software | | | | |
| Nilai anak usaha pembiayaan | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada pengiriman kuartal ini, melainkan pada apakah margin kotor per unit tanpa kredit dapat dipertahankan di level X, dan apakah volume penjualan dapat stabil di atas titik break-even Y."
- "Kombinasi volume penjualan dan laba per unit yang terimplikasi harga saat ini adalah ……; dibandingkan dengan total profit pool industri otomotif global, implikasi ini wajar/agresif/konservatif."
- "Jika salah satu indikator inti berikut — volume asuransi wajib / margin kotor per unit tanpa kredit / inventori saluran / diskon akhir / runway kas — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
