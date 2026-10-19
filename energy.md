# Lampiran Riset Mendalam Industri Energi

Berlaku untuk perusahaan sumber daya seperti migas upstream, energi terintegrasi, refining/petrokimia, jasa migas (oilfield services), midstream pipa/LNG, dan batu bara. Utilitas listrik terbarukan sebaiknya menggunakan `industries/utilities.md`; pertambangan logam menggunakan `industries/metals-mining.md`. Jika perusahaan melintasi beberapa segmen rantai nilai, pisahkan dulu produksi, biaya, dan capex per segmen, lalu terapkan framework yang sesuai masing-masing.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Energi
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Nilai perusahaan energi adalah akumulasi aset, bukan multiple dari laba**. Upstream harus membangun NAV per aset satu per satu, menggunakan P/E untuk menilai upstream adalah kesalahan metodologis.
- Harga komoditas adalah variabel eksogen yang tidak bisa dikontrol perusahaan. Fokus riset harus diletakkan pada **bagian yang bisa dikontrol perusahaan**: biaya per unit, efisiensi modal, reserve replacement, kualitas aset, dan alokasi modal.
- **Pertumbuhan produksi itu sendiri tidak memiliki nilai**. Yang bernilai adalah pertumbuhan reserve per saham, produksi per saham, dan free cash flow per saham. Pertumbuhan produksi yang dibeli dengan penerbitan saham baru atau utang untuk M&A bisa jadi penghancuran nilai.
- Harga spot, futures, realized price, benchmark differential, dan harga hedging **tidak boleh dicampur**. Pendapatan harus dijembatani (bridge) secara berjenjang dari harga benchmark hingga harga realisasi aktual.
- Basis reserve harus dicantumkan: proved/probable/possible, menggunakan standar SEC atau PRMS, harga benchmark yang digunakan, dan tanggal efektif. Basis reserve yang berbeda tidak dapat dibandingkan.
- **Maintenance capex (capex pemeliharaan) adalah item yang paling sering diremehkan di industri energi**. Harus diestimasi tersendiri investasi yang diperlukan untuk menjaga level produksi saat ini.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Pengajuan regulasi & laporan teknis/reserve**: 10-K/20-F, laporan reserve (SEC atau penilaian independen pihak ketiga), laporan teknis. Digunakan untuk mengonfirmasi reserve, decline rate, biaya per unit, dan liabilitas abandonment.
2. **Data energi & lisensi pemerintah**: AS menggunakan EIA API (minyak, gas, listrik, inventori, produksi), BSEE, regulator tingkat negara bagian; global menggunakan departemen energi masing-masing negara dan database lisensi.
3. **Lembaga internasional & bursa**: balance supply-demand dari IEA, OPEC, JODI; kurva futures dan harga benchmark dari bursa.
4. **Pengungkapan perusahaan**: laporan keuangan, presentasi investor, update operasional, pengungkapan reserve replacement.
5. **Database komersial**: Rystad, Wood Mackenzie, S&P Commodity Insights, Argus, Kpler dapat melengkapi, tetapi **harus dicantumkan basis model/survei-nya**.

### Mekanisme Kewajaran

- **Lapisan harga harus jelas**: benchmark (WTI/Brent/HH/JKM) → quality differential → location differential → hedge effect → realized price. Setiap lapisan harus punya data.
- **Penandaan reserve**: cantumkan proved developed / proved undeveloped / probable, serta asumsi harga yang digunakan dalam penilaian. Asumsi harga tinggi akan menggelembungkan reserve secara semu.
- **Forward curve adalah jangkar pasar, bukan prediksi**: dapat digunakan sebagai satu skenario, tetapi skenario basis sebaiknya menggunakan harga siklus yang bisa dijelaskan, dan dilakukan stress test harga rendah/tinggi secara terpisah.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "inventori sumur dapat menopang pengembangan 10 tahun" harus dikaitkan dengan luas area, grading kualitas/kapasitas, spacing sumur, dan kurva produktivitas sumur yang sudah terealisasi — bukan hanya mengutip basis dari perusahaan.
- **Bedakan siklus dan struktural**: penurunan biaya per unit bisa jadi siklus deflasi (harga jasa migas turun), bisa juga peningkatan efisiensi. Harus dibedakan dengan indikator efisiensi operasi.
- **Hindari survivorship bias**: peer set harus mencakup sejenis dengan biaya tinggi, leverage tinggi, dan kualitas aset yang menurun.

## 3. Pohon Penggerak Nilai Energi

Nilai perusahaan sumber daya upstream dapat diurai menjadi:

```text
NAV Aset =
  Σ per aset (
      recoverable reserves
      × (realized price − biaya kas per unit − pajak/royalti)
      × kurva produksi dan decline rate
      − capex pengembangan
      − liabilitas abandonment dan lingkungan
    ) didiskon
  + sumber daya belum dikembangkan (setelah diskon risiko)
  + aset midstream/lainnya
  − net debt
  − biaya level korporat

Pertumbuhan nilai per saham =
  reserve replacement ratio × kualitas aset
  × efisiensi modal (investasi per unit produksi)
  − dilusi ekuitas
  − erosi M&A harga tinggi
```

Laporan minimal harus menjawab:

- Berapa capex yang diperlukan untuk menjaga produksi saat ini? Sisa free cash flow setelah itu baru benar-benar bisa didistribusikan.
- Berapa reserve replacement ratio? Apakah kualitas reserve pengganti lebih baik atau lebih buruk dibandingkan yang dikonsumsi?
- Berapa persentil biaya penuh per unit (termasuk maintenance capex dan abandonment) dalam kurva biaya?
- Apakah perbaikan FCF saat ini berasal dari kenaikan harga atau perbaikan operasional? Berapa sisanya dalam skenario harga rendah?
- Apakah return pemegang saham (dividen + buyback) berkelanjutan dalam skenario harga rendah?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Segmen | Jebakan Umum |
|---|---|---|---|
| Production | Produksi harian (boe/d, mcf/d) | Upstream | **Pertumbuhan bisa jadi dari M&A bukan pengembangan organik** |
| Reserve life (R/P) | Reserve / produksi tahunan | Upstream | Perlu dibedakan proved developed dan undeveloped |
| Reserve replacement ratio | Penambahan reserve / produksi | Upstream | Replacement dari akuisisi dan dari pengeboran memiliki nilai berbeda |
| Decline rate | Tingkat penurunan alami | Upstream, shale | Shale decline tajam, menjaga produksi butuh investasi berkelanjutan |
| Lifting cost | Biaya operasi per unit | Upstream | Tidak termasuk maintenance capex, bukan biaya penuh |
| F&D cost | Biaya penemuan dan pengembangan per unit | Upstream | Nilai rolling tiga tahun lebih bermakna dari nilai tahun tunggal |
| Netback | Harga realisasi − berbagai biaya | Upstream | Perlu dicantumkan ruang lingkup pengurangan |
| Breakeven price | Harga impas proyek/sumur | Shale, proyek | Basis half-cycle dan full-cycle sangat berbeda |
| Inventori sumur | Jumlah lokasi sumur yang bisa dibor | Shale | **"Inventori multi-tahun" perlu diskon berdasarkan area, grade, spacing** |
| Well productivity | Produksi awal per sumur dan EUR | Shale | Pengeboran padat (infill drilling) menyebabkan interferensi antar sumur, penurunan kapasitas |
| D&C cost | Biaya drilling & completion | Shale | Biaya jasa sangat fluktuatif secara siklus |
| Reinvestment rate | Capex / arus kas operasi | Upstream | Reinvestment rate tinggi berarti free cash flow rendah |
| Utilization / throughput | Tingkat operasi / volume olahan | Refining | Perlu dikaitkan dengan rencana turnaround |
| Crack spread | Spread penyulingan | Refining | **Spread teoritis tidak sama dengan laba aktual** |
| Capture rate | Margin kotor aktual / spread teoritis | Refining | Mencerminkan kapabilitas operasi riil |
| Turnaround | Rencana pemeliharaan besar (turnaround) | Refining | Laba turun signifikan pada tahun turnaround |
| Contracted volume / MVC | Volume terkontrak / minimum volume commitment | Midstream, LNG | Perlu dilihat sisa masa kontrak dan kredit lawan transaksi (counterparty) |
| Porsi take-or-pay | Porsi kontrak take-or-pay | Midstream, LNG | Inti dari visibilitas arus kas |
| Tariff escalator | Mekanisme penyesuaian tarif | Midstream | Keterkaitan dengan inflasi adalah proteksi penting |
| Day rate / tingkat utilisasi | Tarif harian dan utilisasi fleet | Jasa migas | Sangat siklikal |
| Backlog / book-to-bill | Pesanan di tangan (backlog) | Jasa migas | Perlu dilihat kualitas pesanan dan klausul pembatalan |
| Cash cost | Biaya kas per unit | Batu bara | Perlu disesuaikan dengan jenis batu bara dan jarak angkut |
| Liabilitas abandonment (ARO) | Liabilitas decommissioning dan lingkungan | Semua segmen | Sering diremehkan, dan pengeluaran kas ada di masa depan jauh |
| Tingkat cakupan hedging | Porsi produksi yang sudah di-hedge | Upstream | Laba/rugi hedging bisa menutupi fundamental |

8 indikator yang wajib diungkap duluan: produksi dan produksi per saham, reserve dan replacement ratio, decline rate, biaya penuh per unit (termasuk maintenance capex), bridge realized price, maintenance capex, net debt dan coverage harga rendah, kebijakan return pemegang saham.

## 5. Struktur Model Keuangan

### Model Produksi dan Pendapatan

Dimodelkan per aset/basin secara terpisah:

1. **Model produksi**: `produksi awal periode + sumur baru/proyek baru beroperasi − decline alami − shutdown terjadwal/turnaround = produksi akhir periode`. Capex berkaitan langsung dengan pemeliharaan produksi.
2. **Model pendapatan**: `volume × realized price`. Realized price dijembatani berjenjang dari benchmark ± quality differential ± location differential ± hedge.
3. **Refining**: `throughput × utilization × (crack spread × capture rate)`, dikurangi dampak turnaround.
4. **Midstream/LNG**: dimodelkan dengan arus kas kontrak, termasuk jadwal jatuh tempo kontrak, kredit pelanggan, throughput, tariff escalator, dan return proyek ekspansi. LNG juga dipisahkan biaya likuifaksi, linkage Henry Hub/harga minyak, biaya pelayaran, dan klausul destinasi.
5. **Jasa migas**: `jumlah fleet/rig × tingkat utilisasi × day rate`, termasuk konversi backlog dan indikator leading capex pelanggan.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, harus mencantumkan asumsi harga komoditas secara eksplisit beserta sumbernya.
- Gunakan forward curve sebagai jangkar pasar (satu skenario), skenario basis menggunakan harga siklus yang bisa dijelaskan, lakukan stress test harga rendah/tinggi dan spread secara terpisah.
- Perusahaan shale harus memberikan grading inventori sumur (area tier satu/dua/tiga) beserta harga impas masing-masing.

### Model Biaya, Modal, dan Liabilitas

- **Pemisahan biaya**: biaya operasi kas, transportasi, pajak/royalti, maintenance capex, growth capex, pengeluaran abandonment, dan modal kerja, dimodelkan item per item.
- **Maintenance capex**: estimasi tersendiri capex yang diperlukan untuk menjaga produksi saat ini. `Free cash flow riil = arus kas operasi − maintenance capex`. Ini adalah angka paling krusial dan paling mudah dipercantik di perusahaan energi.
- **Hedging**: cantumkan posisi hedging, harga, tenor, dan rasio cakupan. Laba/rugi hedging harus dibahas terpisah dari performa bisnis dasar.
- **Liabilitas abandonment dan lingkungan (ARO)**: periksa kecukupan provisi, asumsi discount rate, dan jadwal pengeluaran kas. Jika ada persyaratan regulasi terkait emisi metana dan biaya karbon, harus masuk ke biaya.
- **Net debt dan likuiditas**: tes covenant utang dalam skenario harga rendah, jadwal jatuh tempo, dan risiko refinancing.

### Batasan Asumsi Steady State

- **Jangan mengapitalisasi nilai terminal dengan harga spot puncak**. Nilai terminal harus menggunakan harga ekuilibrium jangka panjang, dan jelaskan dasarnya (kurva biaya marginal, rentang historis, balance supply-demand).
- Jika reserve replacement ratio di bawah 100%, kualitas inventori sumur menurun, decline rate naik, tidak boleh sekaligus memberi pertumbuhan produksi dan maintenance capex rendah.
- Sumber daya belum dikembangkan harus dimasukkan ke NAV setelah diskon risiko, tidak boleh diperlakukan setara dengan reserve yang sudah dikembangkan.
- Return pemegang saham (dividen + buyback) harus diuji rasio coverage-nya dalam skenario harga rendah, tidak boleh dikomitmenkan berdasarkan skenario harga tinggi.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **NAV Aset**: metode utama upstream. Modelkan produksi, harga, biaya, pajak, capex, dan abandonment per aset, lalu didiskon dan dijumlahkan.
2. **Reverse NAV / DCF**: dari harga saat ini, dibalik untuk mendapatkan implied harga komoditas jangka panjang, jalur produksi, atau nilai sumber daya yang di-price in pasar, untuk menjawab "apa yang sudah di-price in pasar".
3. **EV/DACF atau EV/FCF ternormalisasi**: menggunakan arus kas ternormalisasi pada harga mid-cycle, bukan periode berjalan.
4. **Sensitivitas harga komoditas**: berikan elastisitas NAV dan FCF terhadap harga (setiap $10/bbl berapa perubahan NAV).

### Opsional

- **SOTP per segmen**: perusahaan energi terintegrasi dinilai per segmen upstream, downstream, kimia, midstream, trading.
- **EBITDA mid-cycle**: refining menggunakan EBITDA pada crack spread rata-rata lintas siklus.
- **DCF arus kas kontrak**: midstream/LNG menggunakan diskonto arus kas yang sudah terkontrak, dan risiko bagian yang belum terkontrak dipisah tersendiri.
- **Nilai reposisi (replacement value)**: digunakan sebagai batas bawah saat undervaluasi ekstrem, menggunakan biaya reposisi aset.

**Nilai reserve harus dikurangi capex pengembangan, waktu pengembangan, pajak, royalti, dan liabilitas abandonment di masa depan** — sumber daya di bawah tanah tidak sama dengan nilai pemegang saham.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Segmen: upstream, terintegrasi, refining, midstream, jasa migas, batu bara, tidak boleh dicampur.
- Jenis sumber daya dan basin: shale, konvensional, deepwater, oil sand, LNG memiliki struktur biaya dan karakteristik decline berbeda.
- Rasio minyak-gas: perusahaan dominan minyak dan dominan gas memiliki eksposur harga sama sekali berbeda.
- Posisi pada kurva biaya: ketahanan siklus produsen biaya rendah dan biaya tinggi sangat berbeda.
- Balance sheet dan hedging: level net debt/EBITDA dan rasio cakupan hedging.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi jenis sumber daya, persentil biaya, atau rasio minyak-gas jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

Setelah laporan keuangan, wajib membangun: **bridge produksi**, **bridge realized price** (benchmark/differential/hedge), **bridge biaya per unit**, **bridge capex**, dan **bridge net debt**. Jelaskan item per item earnings capture relatif terhadap harga komoditas benchmark.

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih produksi, harga realisasi, biaya per unit, EBITDA, FCF relatif terhadap konsensus? |
| Bridge produksi | Kenaikan berasal dari sumur baru, proyek baru, M&A, atau perlambatan decline? Apakah produksi per saham naik? |
| Bridge harga | Bagaimana perubahan selisih harga realisasi relatif terhadap benchmark? Berapa kontribusi hedging? |
| Biaya per unit | Penurunan biaya berasal dari efisiensi, deflasi harga jasa, atau pengenceran dari kenaikan produksi? |
| Earnings capture | Apakah tingkat konversi laba aktual relatif terhadap harga benchmark memburuk? |
| Capex | Berapa masing-masing maintenance dan growth capex? Apakah investasi riil untuk menjaga produksi diremehkan? |
| Reserve dan inventori sumur | Apakah reserve replacement ratio, kualitas inventori sumur, produktivitas per sumur menurun? |
| Progres proyek | Apakah biaya dan waktu beroperasi proyek besar (LNG, deepwater) tertunda? |
| Kontrak midstream | Apakah jatuh tempo kontrak, kredit pelanggan, penyesuaian tarif berubah? |
| Return modal | Apakah dividen buyback berkelanjutan dalam skenario harga rendah? |
| Earnings call | Apakah nada bicara tentang lingkungan harga, biaya jasa, kualitas sumber daya, disiplin modal melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan harga komoditas, disiplin modal, kualitas aset, atau return pemegang saham? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan dampak pasar dan harga komoditas: jika saham naik 6% tapi kenaikan harga minyak mendorong sektor energi naik 4% di periode yang sama, reaksi spesifik perusahaan sekitar +2%.

## 8. Moat & Penilaian Kompetitif

Energi adalah industri komoditas homogen, esensi moat adalah **posisi pada kurva biaya dan umur aset**. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Persentil kurva biaya | Biaya penuh di persentil rendah kurva biaya global, tetap profit di titik rendah siklus | Produsen biaya tinggi, arus kas negatif saat harga rendah |
| Kualitas dan umur sumber daya | Reserve berkualitas di area premium berumur panjang, decline rate rendah | Area inti sudah dikembangkan, sisa adalah blok marginal |
| Kedalaman inventori | Inventori sumur ekonomis dapat menopang pengembangan multi-tahun dan sudah diverifikasi grading-nya | "Inventori multi-tahun" belum digrading dan belum didiskon berdasarkan spacing |
| Infrastruktur dan logistik | Memiliki pipa, terminal, fasilitas pengolahan sendiri sehingga mengurangi kerugian selisih harga | Bergantung pada transportasi pihak ketiga, location differential besar |
| Kualitas kontrak (midstream/LNG) | Kontrak take-or-pay jangka panjang, kredit lawan transaksi baik | Kontrak akan segera jatuh tempo atau kredit lawan transaksi memburuk |
| Disiplin modal | Secara historis tidak ekspansi membabi buta atau M&A harga tinggi saat harga sedang tinggi | Ekspansi procyclical, akuisisi di titik harga tertinggi |
| Eksekusi operasional | Proyek selalu sesuai budget dan jadwal, capture rate stabil lebih baik dari sejenis | Proyek berulang kali over budget dan tertunda |
| Ketahanan balance sheet | Leverage rendah, tetap bisa menjaga dividen dan investasi dalam skenario harga rendah | Leverage tinggi, bergantung pada harga tinggi untuk menjaga covenant |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "produsen biaya rendah", tapi biaya penuh (termasuk maintenance capex) lebih tinggi dari median sejenis, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- Produksi naik tapi **reserve per saham atau FCF per saham menurun** — pertumbuhan dibeli dengan dilusi.
- Maintenance capex dikemas sebagai "investasi pertumbuhan", menggelembungkan free cash flow yang bisa didistribusikan secara semu.
- Menggunakan sumber daya yang belum diberi risk-weighting (bukan reserve) untuk mendukung NAV.
- Melakukan M&A besar atau buyback di saat harga komoditas tinggi, sekaligus menambah leverage.
- Laba/rugi hedging menutupi memburuknya bisnis dasar, atau rasio hedging justru menurun saat harga rendah.
- Provisi liabilitas abandonment, lingkungan, dan pengurangan emisi metana tidak memadai.
- Kredit pelanggan midstream memburuk atau kontrak terkonsentrasi jatuh tempo tanpa diperpanjang.
- Biaya dan waktu beroperasi proyek besar berulang kali tertunda.
- Asumsi harga yang digunakan dalam penilaian reserve jauh lebih tinggi dari kurva forward saat ini.
- Perusahaan shale melakukan infill drilling yang menyebabkan produktivitas per sumur menurun, tapi masih memprediksi dengan kurva lama.

### Daftar Bukti Sanggahan

Setiap laporan energi minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Produksi atau produksi per saham turun N kuartal berturut-turut.
- Biaya penuh per unit naik melebihi ambang tertentu, atau persentil kurva biaya bergeser turun.
- Reserve replacement ratio terus di bawah 100%.
- Proyek kunci over budget melebihi persentase tertentu dari anggaran atau tertunda melebihi durasi tertentu.
- Net debt/EBITDA menembus ambang covenant dalam skenario harga rendah.
- Rasio coverage return pemegang saham di bawah 1 dalam skenario harga rendah.

### Kesalahpahaman Umum

- **Menggunakan laba periode harga tinggi dengan P/E median** — mengabaikan siklus harga komoditas.
- Menganggap arus kas operasi sebagai free cash flow, mengabaikan capex yang diperlukan untuk menjaga produksi.
- Menganggap pertumbuhan produksi sebagai penciptaan nilai, mengabaikan basis per saham dan sumber modal.
- Menganggap jumlah sumber daya sebagai reserve, dan menganggap reserve sebagai nilai pemegang saham (mengabaikan biaya pengembangan, pajak, dan waktu).
- Menganggap crack spread teoritis sebagai laba kilang, mengabaikan capture rate.
- Menganggap arus kas stabil dari hedging sebagai kapabilitas operasional.
- Menganggap EBITDA stabil midstream sebagai bebas risiko, mengabaikan kredit pelanggan dan jatuh tempo kontrak.
- Mengapitalisasi nilai terminal menggunakan harga puncak.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan energi selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Peta Aset / Basin

| Aset/Basin | Porsi Produksi | Reserve | Umur Tersisa | Decline Rate | Biaya Penuh per Unit | Harga Impas |
|---|---:|---:|---:|---:|---:|---:|

### Tabel Reserve dan Decline

| Item | Periode Ini | Periode Lalu | Keterangan |
|---|---:|---:|---|
| Reserve proved developed | | | |
| Reserve proved undeveloped | | | |
| Reserve replacement ratio | | | |
| Decline rate alami | | | |
| Inventori sumur ekonomis (grading) | | | |

### Bridge Harga / Differential / Hedging

| Lapisan | Periode Ini | YoY | Keterangan |
|---|---:|---:|---|
| Harga benchmark | | | |
| Quality differential | | | |
| Location differential | | | |
| Dampak hedging | | | |
| Realized price | | | |
| Earnings capture rate | | | |

### Unit Economics dan Maintenance Capex

| Indikator | Periode Ini | Posisi vs Sejenis | Sumber |
|---|---:|---|---|
| Biaya operasi kas per unit | | | |
| Pajak / royalti | | | |
| Maintenance capex (per unit) | | | |
| Biaya penuh per unit | | | |
| FCF riil (arus kas operasi − maintenance capex) | | | |

### Sensitivitas Harga Komoditas dan Stress Test Return Modal

| Skenario | Harga Komoditas | NAV | FCF | Net Debt/EBITDA | Coverage Dividen+Buyback |
|---|---:|---:|---:|---:|---:|
| Bear (harga rendah) | | | | | |
| Base (mid-cycle) | | | | | |
| Bull (harga tinggi) | | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada harga komoditas periode berjalan, melainkan pada asumsi harga ekuilibrium jangka panjang X, dan apakah biaya penuh per unit dapat dipertahankan di level Y pada harga tersebut."
- "Setelah dikurangi capex yang diperlukan untuk menjaga produksi, free cash flow riil adalah ……; rasio coverage kebijakan return pemegang saham saat ini dalam skenario harga rendah adalah ……"
- "Jika salah satu indikator inti berikut — produksi / biaya per unit / reserve replacement / progres proyek / net debt — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
