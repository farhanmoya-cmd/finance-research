# Lampiran Riset Mendalam Industri Pembayaran/Fintech

Berlaku untuk card network, acquiring, dompet digital, remitansi lintas negara, BNPL, platform broker/trading, dan bank teknologi (bank tech). **Tidak termasuk entitas bank berlisensi, yang menggunakan `industries/banks.md`**. Bisnis bertipe kredit (BNPL, kredit konsumen) harus juga mengacu pada framework kualitas aset di banks.md.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Pembayaran dan Fintech
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Identifikasi dulu model bisnisnya**, KPI dan sumber risiko sama sekali berbeda:
  - **Card network (jaringan kartu)**: murni efek jaringan + model tarif, hampir tanpa risiko kredit. Lihat volume transaksi, mix lintas negara, client incentives (rebate ke klien, termasuk contra revenue).
  - **Acquiring/gateway**: lihat TPV, **net take rate** (basis gross vs net adalah jebakan terbesar), struktur merchant (merchant besar punya tarif lebih rendah).
  - **Dompet digital/super app**: lihat funnel MAU → penetrasi pembayaran → monetisasi jasa finansial.
  - **BNPL/bertipe kredit**: **esensinya adalah perusahaan kredit**, harus menggunakan framework kualitas aset (loss rate vintage, biaya pendanaan, mismatch durasi).
  - **Platform broker/trading**: pendapatan transaksional (siklikal) dan pendapatan bunga/subscription (struktural) harus dipisah, lihat aset klien dan tingkat monetisasi.
- **Basis pendapatan adalah jebakan utama di industri ini**. Gross revenue acquirer termasuk porsi interchange yang lewat (pass-through), berbeda beberapa kali lipat dari pendapatan neto. Semua take rate harus menggunakan basis neto.
- **Pertumbuhan tinggi bisnis bertipe kredit bisa menutupi eksposur bad debt yang tertunda (lag)**. Setiap kesimpulan pertumbuhan harus dipasangkan dengan kurva loss vintage.
- **Regulasi adalah sumber risiko first-order**, bukan catatan kaki. Pengaturan tarif (seperti Durbin Amendment), persyaratan lisensi, lokalisasi data harus ditangani dengan skenario.
- Pendapatan transaksional (PFOF, komisi transaksi, trading kripto) sangat siklikal, **tidak boleh diperpetualkan pada level bull market**.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Laporan keuangan dan pengajuan regulasi**: 10-K/10-Q/laporan tahunan, dokumen lisensi regulasi, catatan segmen dan basis. Definisi basis pendapatan (gross vs net) ada di catatan.
2. **Statistik pembayaran bank sentral**: Federal Reserve payment research AS, laporan sistem pembayaran PBoC, BIS Red Book. Digunakan untuk mengonfirmasi total volume industri dan proses substitusi tunai.
3. **Data operasional publik card network**: pengungkapan operational performance Visa/Mastercard adalah benchmark frekuensi tinggi untuk volume transaksi seluruh industri.
4. **Laporan statistik industri**: Nilson Report, laporan pembayaran global FIS/Worldpay, dll., harus dicantumkan basis dan tanggal publikasi.
5. **Data aplikasi pihak ketiga**: jumlah download, aktivitas hanya sebagai petunjuk, perlu diverifikasi silang dengan pengungkapan perusahaan.

### Mekanisme Kewajaran

- **Basis pendapatan harus dicantumkan**: apakah gross (termasuk interchange dan network fee pass-through) atau net (hanya yang diretensi perusahaan). **Take rate selalu dihitung dengan basis neto**, dan cantumkan definisi denominator TPV.
- **Client incentives (rebate) dipisah tersendiri**: rebate card network adalah contra revenue, jika pertumbuhannya lebih cepat dari pendapatan akan menggerogoti pertumbuhan yang terlihat. Harus diberikan tren rate rebate.
- **Indikator kredit harus diungkap berdasarkan vintage**: loss rate keseluruhan akan terdilusi oleh kredit baru, hanya kurva vintage berdasarkan tahun/kuartal pencairan yang bisa menunjukkan kualitas aset riil.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "take rate stabil" harus dikaitkan dengan struktur merchant, mix produk, dan bukti pricing kompetitif — bukan hanya melihat angka konsolidasi.
- **Bedakan siklus dan struktural**: penurunan pendapatan transaksional bisa jadi siklus pasar (volume), bisa juga hilangnya pangsa atau tarif. Harus dibedakan dengan pemisahan volume-harga.
- **Hindari survivorship bias**: peer set harus mencakup sejenis yang terdampak pengaturan tarif dan yang sudah mengalami masalah kredit.

## 3. Pohon Penggerak Nilai Pembayaran dan Fintech

```text
Nilai pembayaran = TPV × net take rate × operating leverage − biaya fraud/kepatuhan
Nilai kredit = aset berbunga × NIM − loss rate lintas siklus − biaya pendanaan
Nilai platform = aset klien × tingkat monetisasi + pendapatan bunga − biaya akuisisi pelanggan

Enterprise Value =
  pertumbuhan volume transaksi (substitusi tunai + penetrasi e-commerce + GDP)
  × keberlanjutan net take rate
  × operating leverage (pengenceran fixed cost)
  × peningkatan mix lintas negara/jasa bernilai tambah
  ÷ discount rate risiko
  − risiko pengaturan tarif regulasi (skenario)
  − kerugian kredit (bertipe kredit)
  − biaya kepatuhan dan fraud
```

Laporan minimal harus menjawab:

- Apakah pertumbuhan volume transaksi berasal dari substitusi tunai, penetrasi e-commerce, perolehan pangsa, atau inflasi (kenaikan nilai transaksi rata-rata)?
- Bagaimana tren net take rate? Penurunannya karena perubahan struktur merchant, penurunan harga kompetitif, atau mix produk?
- Apakah pertumbuhan client incentives lebih cepat dari pertumbuhan pendapatan?
- Apakah kurva loss vintage bisnis kredit memburuk? Apakah kenaikan biaya pendanaan sudah ditransmisikan?
- Apakah pangsa TPV yang terimplikasi harga saat ini mungkin relatif terhadap total pasar pembayaran global (yang memiliki batas fisik)?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Tipe | Jebakan Umum |
|---|---|---|---|
| TPV / GDV | Total payment/gross dollar value | Acquiring, dompet digital | Basis apakah termasuk P2P, top-up, transfer internal |
| Jumlah transaksi | Jumlah transaksi yang diproses | Network, acquiring | Dilihat terpisah dari nominal untuk menilai perubahan nilai transaksi rata-rata |
| Net take rate | Pendapatan neto / TPV | Acquiring, dompet digital | **Basis gross dapat menggelembungkan beberapa kali lipat** |
| Gross vs net revenue | Apakah termasuk pass-through interchange | Acquiring | **Perubahan basis adalah red flag besar** |
| Porsi transaksi lintas negara | TPV lintas negara / total TPV | Network, remitansi | Tarif lintas negara signifikan lebih tinggi dari lokal, mix berdampak besar |
| Client incentives | Rebate ke penerbit kartu/merchant | Card network | Contra revenue, jika pertumbuhannya cepat akan menggerogoti pertumbuhan |
| Rate rebate | Insentif / gross revenue | Card network | Tren lebih penting dari nilai absolut |
| Struktur merchant | Porsi merchant besar vs UKM | Acquiring | Merchant besar tarif rendah tapi churn juga rendah |
| Attrition / churn | Tingkat churn merchant | Acquiring | Churn tinggi memerlukan investasi akuisisi tinggi |
| MAU / penetrasi pembayaran | Pengguna aktif dan tingkat penggunaan pembayaran | Dompet digital | Lapisan pertama funnel monetisasi |
| ARPU | Pendapatan per pengguna | Dompet digital, platform | Perlu dibedakan kontribusi pembayaran dan jasa finansial |
| Aset klien (AUC) | Aset klien yang dikustodi | Platform broker | Menentukan pendapatan bunga dan ruang monetisasi |
| Tingkat monetisasi | Pendapatan / aset klien | Platform broker | Tinggi saat bull market, perlu dinormalisasi |
| Porsi pendapatan transaksional | Komisi/PFOF terhadap pendapatan | Platform broker | **Sangat siklikal, tidak bisa diperpetualkan** |
| Porsi pendapatan bunga | Porsi pendapatan bunga neto | Broker, BNPL | Berfluktuasi seiring siklus suku bunga |
| Loss rate vintage | Kerugian kumulatif berdasarkan periode pencairan | BNPL, kredit | **Loss rate keseluruhan terdilusi oleh kredit baru** |
| Rasio pinjaman berulang | Porsi peminjaman berulang | BNPL | Peminjaman berulang tinggi bisa menutupi gali lubang tutup lubang |
| Biaya pendanaan | Rasio biaya pembiayaan | BNPL, kredit | Menekan spread signifikan saat suku bunga naik |
| Loss rate fraud | Kerugian fraud / TPV | Semua tipe | Kenaikan menunjukkan kegagalan risk control |
| Denda kepatuhan | Frekuensi dan nominal sanksi regulasi | Semua tipe | Kenaikan frekuensi menandakan masalah sistemik |
| Dana float/dana klien | Saldo dana float klien | Dompet digital, platform | Tanda penyalahgunaan adalah red flag fatal |

8 indikator yang wajib diungkap duluan: TPV dan jumlah transaksi, net take rate (tren 5 tahun), penjelasan basis pendapatan, rate client incentives, porsi lintas negara, kurva loss vintage (bertipe kredit), porsi pendapatan transaksional, biaya kepatuhan dan fraud.

## 5. Struktur Model Keuangan

### Model Pendapatan

Pilih penggerak berdasarkan model:

1. **Card network**: `jumlah transaksi × nilai per transaksi × tarif − client incentives`, lintas negara dan lokal dipisah (selisih tarif besar).
2. **Acquiring**: `TPV × net take rate`, dilapiskan berdasarkan skala merchant (merchant besar tarif rendah retensi tinggi, UKM tarif tinggi churn tinggi).
3. **Dompet digital**: `MAU × tingkat penetrasi pembayaran × TPV per kapita × take rate` + monetisasi jasa finansial (kredit, wealth management, asuransi).
4. **BNPL/kredit**: `aset berbunga × imbal hasil − biaya pendanaan − kerugian kredit`, harus dimodelkan berdasarkan vintage.
5. **Platform broker**: pendapatan transaksional (volume transaksi × tarif/PFOF) dan pendapatan bunga (kas klien × spread) + pendapatan subscription, ketiganya dipisah.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, harus mencantumkan asumsi tren take rate secara eksplisit beserta dasarnya.
- Volume dan harga harus diproyeksikan terpisah, tidak boleh hanya CAGR pendapatan.
- Bertipe kredit harus membangun model kerugian kredit tersendiri, dan menggunakan loss rate lintas siklus bukan periode berjalan.

### Model Biaya, Kredit, dan Kepatuhan

- **Operating leverage**: biaya marginal jaringan pembayaran sangat rendah, efek skala signifikan. Tetapi perlu dibedakan leverage riil dari investasi yang kurang memadai.
- **Client incentives**: dimodelkan tersendiri sebagai contra revenue, pertumbuhannya terkait dengan kontrak penerbit kartu/merchant baru yang ditandatangani.
- **Kerugian kredit (bertipe kredit)**: bangun kurva kerugian kumulatif berdasarkan vintage, bedakan indikator dini (first-day delinquency rate) dengan kerugian akhir. **Kredit baru akan mendilusi loss rate keseluruhan, harus diobservasi berdasarkan vintage**.
- **Biaya pendanaan**: sumber pendanaan BNPL dan bisnis kredit (modal sendiri, ABS, fasilitas bank) dan biayanya, lag transmisi saat suku bunga naik.
- **Fraud dan kepatuhan**: loss rate fraud, investasi kepatuhan, riwayat denda. Biaya kepatuhan adalah item kenaikan rigid saat regulasi diperketat.
- **Manajemen dana float**: apakah dana klien disegregasi, apakah menghasilkan pendapatan bunga, apakah ada risiko penyalahgunaan.

### Batasan Asumsi Steady State

- Take rate tertekan dalam jangka panjang adalah hukum industri (efek skala ditransmisikan ke merchant). **Asumsi take rate stabil atau naik dalam jangka panjang memerlukan alasan struktural**.
- Jika struktur merchant bergeser ke merchant besar, kompetisi intensif, regulasi membatasi tarif, tidak boleh sekaligus memberi pertumbuhan TPV tinggi dan take rate stabil.
- Pendapatan transaksional harus dinormalisasi pada level lintas siklus, **diskon valuasi di akhir bull market bukan opsional**.
- Loss rate steady state bisnis bertipe kredit harus menggunakan data siklus kredit penuh, tidak boleh menggunakan loss rate rendah dari periode ekspansi.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **Network/acquiring: DCF tiga tahap + valuasi relatif EV/EBITDA**. Harus dilakukan **tes plafon penetrasi** — proses substitusi tunai berdasarkan kurva S per negara, nilai apakah ruang pertumbuhan sudah di-price in.
2. **Bertipe kredit: framework ROE setelah provisi × P/B**, normalisasi dengan loss rate lintas siklus.
3. **Reverse DCF**: dari harga saat ini, dibalik untuk mendapatkan implied skala atau pangsa TPV, diverifikasi terhadap **batas fisik total pasar pembayaran global**.
4. **Skenario regulasi**: pengaturan tarif, batasan lisensi, lokalisasi data ditangani dengan **probabilitas skenario**, jangan disembunyikan dalam WACC.

### Opsional

- **SOTP**: super app atau fintech multi-bisnis dinilai per segmen pembayaran, kredit, wealth management, asuransi.
- **Metode aset klien**: platform broker bisa menggunakan `aset klien × multiple monetisasi pembanding` sebagai cross-check.
- **EV/Revenue**: hanya digunakan saat pertumbuhan tinggi dan laba belum terealisasi, dan harus menggunakan basis pendapatan neto.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Model: network, acquiring, dompet digital, kredit, broker, tidak boleh dicampur.
- Eksposur risiko kredit: framework valuasi tanpa risiko kredit (network) dan yang menanggung risiko kredit (BNPL) sama sekali berbeda.
- Regional dan regulasi: tingkat pengaturan tarif, barrier lisensi, progres substitusi tunai.
- Struktur pelanggan: menyasar merchant besar, UKM, atau konsumen.
- Fase pertumbuhan dan status profitabilitas.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi eksposur risiko kredit atau basis pendapatan jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan neto, TPV, take rate, EPS, dan guidance relatif terhadap konsensus? |
| Pemisahan volume-harga | Apakah pertumbuhan berasal dari jumlah transaksi, nilai per transaksi (inflasi), atau tarif? |
| Take rate | Alasan perubahan net take rate? Struktur merchant, mix produk, atau penurunan harga kompetitif? |
| Basis pendapatan | Apakah terjadi perubahan basis gross/net? Apakah historis direstatement? |
| Client incentives | Tren rate rebate? Apakah pertumbuhannya lebih cepat dari pendapatan? |
| Lintas negara | Tingkat pemulihan dan perubahan porsi transaksi lintas negara? (tarif signifikan lebih tinggi) |
| Kualitas kredit | **Perubahan marginal kurva loss vintage** (prioritas pertama bertipe kredit)? First-day delinquency rate? |
| Biaya pendanaan | Apakah kenaikan biaya pembiayaan sudah ditransmisikan ke pricing? Berapa kompresi spread? |
| Pendapatan transaksional | Porsi pendapatan transaksi platform broker? Di posisi mana relatif terhadap siklus bull-bear? |
| Kepatuhan | Apakah ada denda baru, masalah lisensi, atau investigasi regulasi? |
| Guidance | Apakah guidance pendapatan, take rate, loss rate mengubah model jangka panjang? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan belanja konsumen, tekanan take rate, siklus kredit, atau hasil regulasi? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 8% tapi sektor fintech naik 5% di hari yang sama, reaksi spesifik perusahaan sekitar +3%.

## 8. Moat & Penilaian Kompetitif

Moat pembayaran adalah **efek jaringan dua sisi dan biaya peralihan**, sementara bertipe kredit hampir tidak memiliki moat. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Efek jaringan dua sisi | Pemegang kartu dan merchant saling menguatkan, pemain baru sulit cold-start | Skala satu sisi, atau multi-homing umum |
| Cakupan jaringan penerimaan | Jaringan penerimaan global, merchant dan penerbit kartu terikat mendalam | Jaringan regional, mudah disubstitusi solusi lokal |
| Biaya peralihan | Terintegrasi mendalam ke ERP/POS/proses rekonsiliasi merchant | Jalur pembayaran murni, bisa langsung berganti |
| Data dan risk control | Skala data transaksi terkonversi menjadi keunggulan loss rate fraud yang terukur | Risk control bergantung pihak ketiga, loss rate fraud lebih tinggi dari sejenis |
| Barrier lisensi dan kepatuhan | Lisensi multi-regional membentuk barrier masuk | Lisensi mudah diperoleh atau berisiko dicabut |
| Ekonomi skala | Biaya pemrosesan per transaksi signifikan lebih rendah dari sejenis | Skala tidak cukup, pengenceran fixed cost tidak memadai |
| Jasa bernilai tambah | Jasa bernilai tambah seperti risk control, data, marketing meningkatkan take rate | Bisnis jalur murni, tarif terus menurun |
| Keunggulan biaya pendanaan (kredit) | Saluran pendanaan terdiversifikasi, biaya lebih rendah dari sejenis | Bergantung pada satu sumber pendanaan atau pendanaan berbiaya tinggi |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "efek jaringan kuat", tapi net take rate terus turun, churn merchant naik, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- **Net take rate terus turun tanpa penjelasan yang wajar**.
- **Perubahan basis pendapatan gross/net** tanpa restatement data historis.
- Pertumbuhan client incentives terus lebih cepat dari pertumbuhan pendapatan.
- Kebijakan pengakuan bad debt perusahaan kredit dilonggarkan (seperti memperpanjang hari pengakuan overdue, melonggarkan kriteria restrukturisasi).
- BNPL pertumbuhan tinggi tapi kurva loss vintage memburuk generasi demi generasi.
- Rasio pinjaman berulang abnormal tinggi, mungkin ada praktik gali lubang tutup lubang.
- Dana float klien tercampur dengan modal sendiri, atau ada indikasi penyalahgunaan.
- Frekuensi denda kepatuhan naik, atau diinvestigasi secara bersamaan di beberapa regional.
- Platform broker memberi guidance yang memperpetualkan pendapatan transaksional pada level bull market.
- Loss rate fraud naik tapi investasi risk control tidak meningkat.
- Kontrak merchant atau penerbit kartu kunci akan segera jatuh tempo dan belum pasti diperpanjang.

### Daftar Bukti Sanggahan

Setiap laporan pembayaran/fintech minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Net take rate jatuh di bawah ambang tertentu atau turun N kuartal berturut-turut.
- Pertumbuhan TPV di bawah pertumbuhan industri dengan persentase tertentu (kehilangan pangsa).
- Rate client incentives melebihi level tertentu.
- Loss rate kumulatif vintage melebihi ambang tertentu, atau first-day delinquency rate terus memburuk.
- Kenaikan biaya pendanaan melebihi bp tertentu dan belum bisa ditransmisikan.
- Regulasi mengeluarkan batas atas tarif atau batasan lisensi.

### Kesalahpahaman Umum

- **Menghitung take rate menggunakan gross revenue**, menyebabkan penilaian kapabilitas laba sama sekali terdistorsi.
- Menganggap stabilnya loss rate keseluruhan sebagai kualitas aset baik, mengabaikan efek dilusi dari kredit baru.
- Menilai BNPL seperti perusahaan teknologi, mengabaikan esensinya sebagai institusi pemberi pinjaman yang menanggung risiko kredit.
- Memperpetualkan pendapatan transaksional saat bull market.
- Menganggap pertumbuhan TPV sebagai penciptaan nilai, mengabaikan penurunan take rate yang bersamaan.
- Mengabaikan client incentives, melebih-lebihkan pertumbuhan pendapatan riil card network.
- Memasukkan risiko regulasi ke dalam discount rate, bukan dimodelkan secara eksplisit dengan skenario.
- Mengekstrapolasi linear ruang substitusi tunai, mengabaikan fase saturasi kurva S.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan pembayaran/fintech selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel Tren Take Rate 5 Tahun (Wajib)

| Tahun | TPV | Jumlah Transaksi | Gross Revenue | Net Revenue | **Net Take Rate** | Alasan Perubahan |
|---|---:|---:|---:|---:|---:|---|

### Tabel Volume-Harga dan Mix

| Indikator | Nilai Terbaru | YoY | Tren 8 Kuartal Terakhir | Posisi vs Sejenis | Sumber & Basis |
|---|---:|---:|---|---|---|
| TPV | | | | | |
| Jumlah transaksi | | | | | |
| Nilai per transaksi | | | | | |
| Porsi lintas negara | | | | | |
| Rate client incentives | | | | | |
| Struktur merchant (besar/UKM) | | | | | |

### Kurva Loss Vintage (Wajib untuk bertipe kredit, jika tidak ada tulis jelas "tidak diperoleh")

| Periode Pencairan | Kerugian Kumulatif 3 Bulan | 6 Bulan | 12 Bulan | 24 Bulan | Penilaian Tren |
|---|---:|---:|---:|---:|---|

### Tabel Skenario Regulasi

| Skenario | Probabilitas | Dampak terhadap Take Rate/Loss Rate | Dampak terhadap Valuasi |
|---|---:|---|---|

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Tingkat pertumbuhan TPV | | | | |
| Net take rate steady state | | | | |
| Margin operasi steady state | | | | |
| Loss rate kredit lintas siklus (bertipe kredit) | | | | |
| Level normalisasi pendapatan transaksional (platform) | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada TPV kuartal ini, melainkan apakah net take rate dapat dipertahankan di X, dan apakah operating leverage dapat mendorong margin ke Y."
- "Skala atau pangsa TPV yang terimplikasi harga saat ini adalah ……; dibandingkan dengan total pasar pembayaran global dan posisi kurva S substitusi tunai negara tersebut, implikasi ini wajar/agresif/konservatif."
- "Jika salah satu indikator inti berikut — net take rate / pangsa TPV / rate rebate / loss vintage / biaya pendanaan — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
