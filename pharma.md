# Lampiran Riset Mendalam Industri Farmasi

Berlaku untuk obat inovatif (innovative drug), bioteknologi, perusahaan farmasi matang, obat generik, biosimilar, dan perusahaan yang berbasis R&D dan komersialisasi obat. Alat kesehatan, rumah sakit, CRO/CDMO bisa meminjam sebagian framework ini, tetapi harus menyesuaikan tersendiri indikator pesanan, utilisasi, dan regulasi. Jika perusahaan juga memiliki bisnis consumer health atau alat kesehatan dalam skala besar, pisahkan dulu per segmen, baru gunakan lampiran ini hanya untuk bagian obat.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Farmasi
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan dan Event
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Lakukan dekomposisi aset dulu, baru bicara perusahaan**. Nilai perusahaan farmasi adalah akumulasi sekelompok aset, bukan satu kurva pendapatan. Pisahkan dulu berdasarkan produk yang dijual, aset yang sudah diajukan, klinis fase III/II/I, praklinis, hak kemitraan, dan teknologi platform.
- Setiap aset harus dicatat: indikasi, regional, mekanisme kerja, fase, porsi hak, milestone, periode paten/eksklusivitas, dan titik waktu katalis berikutnya.
- Bedakan obat inovatif, perusahaan farmasi matang, obat generik, dan biosimilar. Keempatnya memiliki penggerak, struktur margin kotor, risiko paten, dan metode valuasi yang sama sekali berbeda.
- **Probabilitas keberhasilan harus dieksplisitkan**. Setiap valuasi pipeline harus mencantumkan basis rate fase yang digunakan, penyesuaian spesifik aset, dan alasan penyesuaian, tidak boleh ditetapkan berdasarkan narasi manajemen saja.
- Prioritas interpretasi data klinis selalu: endpoint primer > endpoint sekunder > subgroup > analisis eksploratori. Urutan ini tidak boleh dibalik.
- Patent cliff (tebing paten/LOE) bukan peringatan risiko, melainkan kejadian pasti yang harus masuk ke nilai terminal.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Persetujuan regulasi dan dokumen review**: AS menggunakan FDA Drugs@FDA, Orange Book (paten dan eksklusivitas molekul kecil), Purple Book (produk biologis), materi Advisory Committee, opini review dan label; regional lain menggunakan teks asli EMA, NMPA/CDE, PMDA, dll.
2. **Registrasi dan hasil uji klinis**: ClinicalTrials.gov, EU CTR, database registrasi lokal. **Informasi registrasi diajukan oleh sponsor, tidak sama dengan efikasi yang sudah diverifikasi regulator.**
3. **Jurnal peer-reviewed dan abstrak konferensi primer**: abstrak dan presentasi asli ASCO, ESMO, AHA, ADA, dll., lebih diutamakan dari press release.
4. **Pengajuan dan presentasi perusahaan**: 10-K/10-Q/20-F, presentasi investor, pengungkapan milestone.
5. **Database profesional dan media**: hanya sebagai pelengkap dan petunjuk, harus ditelusuri kembali ke sumber asli.

### Mekanisme Kewajaran

- **Bedakan submission, acceptance, dan approval**: submission ≠ acceptance ≠ approval. Menganggap submission atau acceptance sebagai approval adalah kesalahan fakta paling umum.
- **Prioritaskan efek absolut**: efikasi harus dituliskan sebagai efek absolut (seperti kenaikan bulan median PFS, penurunan risiko absolut), bukan hanya efek relatif (HR, RRR). Perbaikan relatif pada baseline rendah akan sangat melebih-lebihkan signifikansi klinis.
- **Perbandingan antar uji coba harus dicantumkan ketidakterbandingannya**: populasi berbeda, endpoint berbeda, standar perawatan era berbeda, uji coba single-arm tidak dapat dibandingkan langsung satu sama lain.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "aset ini akan menjadi standard of care" harus dikaitkan dengan data head-to-head, update guideline, atau titik waktu readout aset kompetitor — bukan hanya mengutip opini KOL.
- **Korelasi kegagalan**: beberapa aset dengan mekanisme atau indikasi yang sama, kegagalannya **bukan kejadian independen**. Probabilitas kombinasi tidak bisa sekadar dikalikan.
- **Hindari survivorship bias**: basis rate harus berasal dari statistik konversi fase yang lengkap, bukan hanya melihat kasus sukses.

## 3. Pohon Penggerak Nilai Farmasi

Nilai intrinsik perusahaan farmasi dapat diurai menjadi:

```text
Enterprise Value =
  Σ (DCF produk yang dijual)
  + Σ (rNPV aset pipeline = peak sales × probabilitas sukses × diskon waktu peluncuran)
  + nilai platform/kemitraan (hanya dimasukkan jika sudah divalidasi berulang kali)
  + net cash (dikurangi konsumsi hingga titik balik nilai berikutnya)
  − tebing pendapatan akibat patent cliff
  − biaya fixed R&D dan komersialisasi
  − dilusi pendanaan masa depan
```

Penggerak penjualan satu aset:

```text
Penjualan = pasien yang dapat dirawat × tingkat diagnosis × porsi sesuai label × tingkat penetrasi
          × durasi pengobatan/kepatuhan × harga bersih × porsi hak
```

Laporan minimal harus menjawab:

- Pendapatan terkonsentrasi di berapa produk? Kapan titik waktu LOE produk terbesar?
- Berapa aset di pipeline yang bisa secara substansial mengubah nilai perusahaan? Apa titik waktu readout berikutnya?
- Apakah kas dapat menopang sampai titik balik nilai berikutnya? Jika tidak, berapa besar dilusinya?
- Berapa tingkat penetrasi pasien yang sesuai dengan asumsi peak sales? Apakah tingkat penetrasi ini agresif atau konservatif dibanding realisasi historis obat sejenis?
- Apakah asumsi harga bersih sudah memperhitungkan gross-to-net, negosiasi asuransi kesehatan, dan erosi harga pasca-peluncuran?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Kegunaan Riset | Jebakan Umum |
|---|---|---|---|
| Peak sales | Penjualan tahunan tertinggi dalam siklus hidup produk | Input inti valuasi aset | Sering dilebih-lebihkan secara sistematis, perlu dibandingkan dengan realisasi aktual obat sejenis |
| PoS (probability of success) | Probabilitas konversi fase | Penyesuaian risiko rNPV | Tidak boleh disesuaikan berdasarkan keyakinan manajemen; harus menggunakan basis rate fase |
| Tingkat konversi tiap layer funnel pasien | Epidemiologi→diagnosis→label→penetrasi | Basis proyeksi penjualan | Melebih-lebihkan 20% di setiap layer akan menghasilkan beberapa kali lipat overestimate di akhir |
| Tingkat penetrasi | Pasien yang diobati / pasien yang dapat dirawat | Tingkat realisasi komersialisasi | Perlu dibandingkan dengan kurva pasca-peluncuran obat sejenis |
| Gross-to-net | Harga bersih / harga daftar | Realisasi harga riil | Rebate AS, 340B, diskon Medicaid bisa mencapai 50%+ dari harga daftar |
| Perubahan YoY harga bersih | Harga bersih YoY | Lingkungan pricing | Kenaikan harga daftar bisa dibarengi penurunan harga bersih |
| TRx / NRx | Total prescription / new prescription | Indikator leading tren permintaan | Restocking saluran bisa membuat volume pengiriman mendahului resep riil |
| Kepatuhan / tingkat lanjutan pengobatan | Porsi pasien yang terus menjalani pengobatan | Nilai durasi pengobatan | Kepatuhan obat penyakit kronis sangat beragam |
| Titik waktu LOE | Kadaluarsa paten/eksklusivitas | Titik waktu tebing pendapatan | Perlu dibedakan paten komponen, paten formulasi, dan periode eksklusivitas data |
| Tipe eksklusivitas | Eksklusivitas NCE/Orphan/BLA | Kekuatan proteksi | Kecepatan erosi generik untuk biologis dan molekul kecil sama sekali berbeda |
| Kurva erosi | Jalur penurunan pendapatan pasca-LOE | Asumsi nilai terminal | Molekul kecil bisa turun 80%+ di tahun pertama; biosimilar erosinya lebih lambat |
| Runway kas | Kas / net burn kuartalan | Risiko pendanaan | Perlu dikurangi pembayaran milestone dan jatuh tempo utang |
| Biaya R&D / proyek | Anggaran proyek per fase | Proyeksi biaya | **Tidak bisa diekstrapolasi dengan rasio terhadap pendapatan** |
| Kecepatan enrollment | Enrollment aktual vs rencana | Risiko eksekusi uji coba | Keterlambatan sering merupakan sinyal dini masalah kompetisi atau desain |
| Milestone dan revenue share | Klausul kemitraan | Alokasi hak | Perlu dibedakan yang sudah diterima, bersyarat, dan maksimum teoretis |
| Margin kotor | Margin kotor produk | Ekonomi produksi | COGS biologis, terapi sel signifikan lebih tinggi dari molekul kecil |

8 indikator yang wajib diungkap duluan: struktur dan konsentrasi pendapatan produk, titik waktu LOE tiap aset, asumsi peak sales dan dasarnya, probabilitas sukses dan sumber basis rate, asumsi tiap layer funnel pasien, gross-to-net, runway kas, titik waktu katalis berikutnya.

## 5. Struktur Model Keuangan

### Model Pendapatan

Produk yang dijual/akan diluncurkan dimodelkan berdasarkan funnel pasien, minimal diurai menjadi:

1. **Epidemiologi**: prevalensi, insidensi, definisi populasi yang dapat dirawat.
2. **Lini pengobatan**: lini pertama/kedua/lanjutan, skala populasi tiap lini berbeda.
3. **Lanskap kompetisi**: standar perawatan existing, aset kompetitor yang sedang diteliti dan titik waktu readout-nya.
4. **Lingkup label**: indikasi yang disetujui, batasan populasi, black box warning.
5. **Saluran dan reimbursement**: cakupan asuransi kesehatan, posisi formulary, ambang prior authorization.
6. **Gross-to-net**: AS mempertimbangkan rebates, 340B/Medicaid, restrukturisasi Part D, negosiasi IRA, dan biaya saluran; pasar lain mempertimbangkan negosiasi asuransi, tender terpusat, dan linkage harga.
7. **Dosis/durasi pengobatan dan penghentian**: durasi pengobatan, kepatuhan, tingkat penghentian.
8. **Kapasitas dan hak regional**: komersialisasi sendiri vs revenue share kemitraan.

Model biotech inovatif juga diurai: runway kas, anggaran proyek R&D, penerimaan-pembayaran milestone, dan dilusi pendanaan.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi masa depan harus diperpanjang sampai setelah LOE produk utama, kurva erosi diberikan secara eksplisit.
- **Biaya R&D tidak bisa diekstrapolasi dengan rasio terhadap pendapatan**, harus dibangun bottom-up berdasarkan fase uji coba, jumlah uji coba, dan anggaran per uji coba.

### Model Pipeline dan Probabilitas Klinis

| Dimensi | Yang Harus Diperiksa | Kesalahpahaman Umum |
|---|---|---|
| Desain klinis | Random/blinded/kontrol, ukuran sampel, kriteria inklusi-eksklusi, endpoint primer/sekunder, rencana statistik | Menggunakan endpoint sekunder atau eksploratori untuk mengganti endpoint primer yang gagal |
| Efikasi | Efek absolut, efek relatif, confidence interval, maturitas data, konsistensi subgroup | Hanya melihat p-value, tidak melihat signifikansi klinis dan koreksi multiplisitas |
| Keamanan | AE/SAE, tingkat penghentian, kematian, dose-dependency, durasi follow-up | Sampel kecil dan follow-up singkat meremehkan risiko langka dan risiko tertunda |
| Keterbandingan | Standar perawatan, pipeline kompetitor, perbedaan populasi antar uji coba | Membandingkan langsung uji coba single-arm dengan populasi dan endpoint berbeda |
| Eksekusi | Kecepatan enrollment, jumlah center, amandemen protokol, perubahan endpoint, data cutoff | Keterlambatan dan perubahan endpoint bisa jadi sinyal risiko |
| Regulasi | Accelerated approval, persyaratan uji konfirmatori, CMC, lingkup label | Menganggap submission atau acceptance sebagai approval |
| Kekayaan intelektual | Paten komponen/formulasi/penggunaan, eksklusivitas data, tantangan paten | Hanya melihat paten terpanjang, mengabaikan kadaluarsa paten inti |

**Penyesuaian probabilitas harus dicantumkan secara eksplisit: basis rate fase + penyesuaian spesifik aset + bukti penyesuaian.** Tidak boleh menetapkan probabilitas sukses tinggi hanya karena narasi manajemen.

### Batasan Asumsi Steady State

- Asumsi peak sales harus dibandingkan dengan realisasi historis aktual obat dengan indikasi dan mekanisme sama, jika melebihi basis harus diberikan alasan struktural.
- Jika aset kompetitor readout lebih kuat, label lebih sempit, reimbursement terbatas, tidak boleh sekaligus memberi tingkat penetrasi tinggi, harga bersih tinggi, dan siklus hidup panjang.
- Nilai terminal perusahaan farmasi matang harus secara eksplisit mencakup level pendapatan pasca-patent cliff, tidak boleh memperpetualkan laba pra-cliff.
- Nilai platform hanya dimasukkan jika didukung oleh **validasi berulang, kontrak kemitraan pihak ketiga, atau aset independen**; hindari memberi nilai positif untuk setiap proyek awal.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **rNPV per aset**: peak sales, waktu peluncuran, margin kotor, investasi penjualan/R&D lanjutan, periode paten, probabilitas sukses, dan discount rate **dimodelkan per aset**, jangan digabung secara keseluruhan.
2. **DCF produk yang dijual**: dimodelkan per produk/indikasi/regional, secara eksplisit mencakup LOE dan kurva erosi.
3. **SOTP**: perusahaan farmasi matang menggunakan DCF produk yang dijual + rNPV pipeline + net cash yang dijumlahkan.
4. **Valuasi terbalik**: menjawab berapa aset yang harus sukses pada harga saat ini, dengan kombinasi peak sales dan probabilitas sukses apa. **Patent cliff harus dimasukkan secara eksplisit ke nilai terminal.**

### Opsional

- **P/E ternormalisasi / P/FCF**: bisa digunakan untuk perusahaan farmasi matang, tetapi harus dijelaskan apakah denominator sudah dikurangi kontribusi produk yang akan segera kadaluarsa.
- **Pembanding transaksi**: nilai transaksi M&A (upfront + milestone) bisa menjadi kalibrasi pasar untuk aset pipeline, tetapi perlu dibedakan upfront dan contingent consideration.
- **Valuasi platform**: hanya digunakan jika ada beberapa aset yang sudah divalidasi atau nilai kemitraan signifikan.

Penanganan net cash: dikurangi konsumsi kas sebelum titik balik nilai berikutnya, utang, milestone yang harus dibayar, dan sewa; pendanaan masa depan dicerminkan dengan probabilitas atau skenario untuk dilusi, tidak boleh mengasumsikan dilusi nol.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Fase: biotech praklinis/awal, biotech fase lanjut, awal komersialisasi, perusahaan farmasi matang.
- Area terapi: tingkat keberhasilan, pricing, dan intensitas kompetisi onkologi, imunologi, neurologi, metabolik, penyakit langka sangat berbeda.
- Modalitas: molekul kecil, antibodi, ADC, terapi sel/gen, vaksin, oligonukleotida — COGS dan barrier berbeda.
- Struktur pendapatan: ketergantungan satu produk vs terdiversifikasi multi-produk.
- Eksposur LOE: porsi pendapatan yang kadaluarsa dalam 5 tahun ke depan.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi fase, modalitas, atau eksposur LOE jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan dan Event

Selain laporan keuangan rutin, **readout klinis, keputusan regulasi, ekspansi label, litigasi paten, dan pricing asuransi kesehatan semuanya masuk ke mode event mendalam**.

Bangun bridge perubahan "asumsi lama → bukti baru → probabilitas sukses/waktu peluncuran/peak sales → rNPV".

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan produk, biaya R&D, EPS relatif terhadap konsensus? |
| Volume-harga produk | Apakah pertumbuhan berasal dari volume resep, harga bersih, restocking saluran, atau indikasi baru? |
| Gross-to-net | Apakah realisasi harga bersih memburuk? Apakah struktur rebate atau asuransi berubah? |
| Tren resep | Apakah TRx/NRx dan volume pengiriman berdivergensi? Seberapa besar perubahan inventori saluran? |
| Progres klinis | Apakah enrollment, data cutoff, titik waktu readout sesuai rencana? Ada amandemen protokol? |
| Event regulasi | Titik waktu review, kesimpulan AdCom, lingkup label, persyaratan uji konfirmatori? |
| Kompetisi | Apakah readout aset kompetitor mengubah positioning pasar dan asumsi peak sales produk ini? |
| Kas | Apakah runway mencakup readout kunci berikutnya? Apakah perlu pendanaan? |
| Dana kemitraan | Apakah pengakuan milestone bersifat satu kali atau berkelanjutan? Bagaimana rasio revenue share? |
| Earnings call | Apakah nada bicara tentang progres peluncuran, akses reimbursement, kompetisi, pricing melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan readout klinis, keputusan regulasi, LOE, atau kebijakan pricing? |

Setelah pengumuman harus **membedakan permintaan terminal riil dari restocking saluran** — divergensi antara volume pengiriman dan volume resep adalah sumber kesalahpahaman paling umum.

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 9% tapi indeks bioteknologi naik 5% di hari yang sama, reaksi spesifik perusahaan sekitar +4%.

## 8. Moat & Penilaian Kompetitif

Inti moat farmasi adalah **eksklusivitas**, tetapi eksklusivitas ada batas waktunya. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Kekuatan kekayaan intelektual | Periode paten molekul inti panjang, paten formulasi/penggunaan membentuk pertahanan berlapis | Hanya paten sekunder, paten inti mendekati kadaluarsa atau dipertentangkan |
| Data dan eksklusivitas regulasi | Eksklusivitas produk biologis, eksklusivitas obat langka, perpanjangan pediatrik | Eksklusivitas akan segera berakhir, generik/biosimilar sudah diajukan |
| Diferensiasi klinis | Data head-to-head superior, atau masuk rekomendasi lini pertama guideline | Hanya non-inferior, atau bergantung pada narasi subgroup |
| Kompleksitas manufaktur | Barrier proses produk biologis, terapi sel membuat generik sulit dibuat | Molekul kecil dengan jalur sintesis publik |
| Jaringan komersialisasi | Jaringan resep spesialis, relasi KOL, kapabilitas akses reimbursement | Bergantung pada komersialisasi mitra, tanpa saluran mandiri |
| Kapabilitas ekspansi indikasi | Molekul yang sama terus mendapat persetujuan indikasi baru, memperpanjang siklus hidup | Indikasi tunggal, uji coba ekspansi gagal |
| Reproduktibilitas platform | Platform sudah menghasilkan beberapa aset yang masuk fase lanjut | Narasi platform kuat tapi hanya satu aset yang tervalidasi |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "proteksi paten kuat", tapi generik sudah disetujui atau paten inti kadaluarsa dalam 3 tahun, tebing tersebut harus tercermin di nilai terminal.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- Endpoint primer tidak tercapai, tapi dinarasikan ulang menggunakan endpoint sekunder atau eksploratori.
- Hanya mengungkap perbaikan relatif (HR, RRR), menghindari efek absolut dan confidence interval.
- Hasil subgroup mendominasi narasi keseluruhan, dan subgroup tersebut tidak pre-specified.
- Readout uji coba kompetitor lebih kuat, tapi perusahaan belum memperbarui asumsi peak sales sepadan.
- Mengakui pendapatan saluran sebelum approval, atau volume pengiriman signifikan mendahului volume resep.
- Pernyataan paten/eksklusivitas kabur, tidak jelas membedakan paten komponen dari paten sekunder.
- Kas tidak cukup untuk menopang sampai readout kunci berikutnya, tapi manajemen belum menyebut rencana pendanaan.
- Sering memperluas narasi "platform", tapi tidak ada aset baru yang masuk fase lanjut.
- Bukti kunci berasal dari studi pihak terafiliasi atau jurnal berdampak rendah.
- Sinyal keamanan terkubur di materi suplementer atau tidak disebutkan di press release.
- Endpoint uji coba klinis atau rencana statistik disesuaikan sebelum/setelah data unblinding.

### Daftar Bukti Sanggahan

Setiap laporan farmasi minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Endpoint primer uji coba kunci tidak mencapai signifikansi statistik, atau ukuran efek di bawah ambang signifikansi klinis.
- Kejadian keamanan (SAE, tingkat penghentian, kematian) melebihi ambang tertentu atau lebih tinggi dari kelompok kontrol.
- Kecepatan enrollment signifikan tertinggal dari rencana, menyebabkan titik waktu readout mundur melebihi durasi tertentu.
- Regulasi meminta uji konfirmatori tambahan atau membatasi label secara signifikan.
- Penurunan harga bersih tahunan melebihi ambang tertentu, atau hasil negosiasi asuransi di bawah ekspektasi.
- Runway kas tidak cukup untuk menutupi readout berikutnya, terpaksa melakukan pendanaan pada posisi harga rendah.

### Kesalahpahaman Umum

- **Secara sistematis melebih-lebihkan peak sales** — optimisme 20% di setiap layer funnel pasien akan menghasilkan hasil akhir yang overestimate beberapa kali lipat.
- Menganggap submission atau acceptance sebagai approval, menganggap accelerated approval sebagai keberhasilan yang pasti.
- Mengabaikan gross-to-net, menggunakan harga daftar untuk memproyeksikan pendapatan (bisa overestimate dua kali lipat di pasar AS).
- Menganggap volume pengiriman sebagai permintaan riil, mengabaikan restocking saluran.
- Menggunakan keyakinan manajemen untuk mengganti basis rate fase dalam menetapkan probabilitas sukses.
- Menganggap keberhasilan beberapa aset dengan mekanisme sama sebagai kejadian independen, meremehkan risiko korelasi.
- Mengabaikan patent cliff, menggunakan laba pra-cliff untuk asumsi perpetual.
- Menganggap narasi platform sebagai nilai, memberi nilai positif untuk setiap proyek awal.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan farmasi selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Peta Aset / Pipeline

| Aset | Indikasi | Fase | Porsi Hak | Katalis Berikutnya dan Titik Waktu | LOE / Eksklusivitas | Asumsi Peak Sales | PoS |
|---|---|---|---|---|---|---:|---:|

### Tabel Bukti Klinis

| Uji Coba | Desain | Endpoint Primer | Efek Absolut | Confidence Interval | Sinyal Keamanan | Keterangan Keterbandingan |
|---|---|---|---|---|---|---|

### Funnel Pasien ke Penjualan

| Layer | Nilai Asumsi | Dasar | Nilai Historis Obat Sejenis |
|---|---:|---|---:|
| Pasien yang dapat dirawat | | | |
| Tingkat diagnosis | | | |
| Porsi sesuai label | | | |
| Tingkat penetrasi | | | |
| Durasi pengobatan/kepatuhan | | | |
| Harga bersih (setelah gross-to-net) | | | |

### Timeline Paten dan Eksklusivitas

| Produk | Pendapatan Saat Ini | Kadaluarsa Paten Komponen | Kadaluarsa Eksklusivitas Data | Prediksi Kurva Erosi | Dampak Nilai Terminal |
|---|---:|---|---|---|---|

### Tabel rNPV / SOTP per Aset

| Aset | Peak Sales | PoS | Tahun Peluncuran | Discount Rate | rNPV | Porsi dari Total Nilai |
|---|---:|---:|---:|---:|---:|---:|

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada produk yang dijual, melainkan apakah aset X dapat disetujui pada tahun Y dengan probabilitas Z% dan mencapai peak sales N miliar."
- "Jumlah aset sukses dan kombinasi peak sales yang terimplikasi harga saat ini adalah ……; dibandingkan dengan realisasi historis obat sejenis, implikasi ini wajar/agresif/konservatif."
- "Jika salah satu indikator inti berikut — efikasi / keamanan / enrollment / regulasi / harga bersih / pendanaan — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
