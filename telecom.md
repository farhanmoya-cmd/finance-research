# Lampiran Riset Mendalam Industri Telekomunikasi

Berlaku untuk operator mobile/fixed-line, menara telekomunikasi, dan komunikasi satelit. Karakteristik: aset berat + regulasi kuat + kompetisi oligopoli + dividen tinggi. **Nilai hampir seluruhnya ditentukan tiga hal: rasionalitas kompetisi, disiplin capex, dan keberlanjutan dividen.**

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Telekomunikasi
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Telekomunikasi adalah bisnis pasar lokal**. Harus dianalisis per negara/pasar untuk lanskap kompetisinya: **kompetisi rasional 3 pemain dan perang harga 4 pemain valuasinya jauh berbeda**. Grup multinasional selalu gunakan SOTP.
- **Default skeptis terhadap narasi pertumbuhan**. 5G, FTTH, IoT, edge computing, dan narasi "siklus baru" lainnya secara historis **mayoritas tidak terkonversi menjadi perbaikan ROIC** — capex naik, tapi ARPU tidak naik. Perlu bukti empiris hubungan ARPU dan return capex, bukan deskripsi prospek teknologi.
- **Segmen menara/infrastruktur dinilai terpisah**: kontrak jangka panjang, linkage CPI, arus kas stabil, seharusnya diberi multiple signifikan lebih tinggi dari bisnis operasi.
- **FCF dan coverage dividen adalah inti**, bukan EBITDA. Antara EBITDA dan FCF telekomunikasi ada jarak capex dan belanja spektrum yang besar.
- **Biaya spektrum adalah capex tersembunyi**, harus dimasukkan ke arus kas, tidak boleh hanya disebut satu kalimat di catatan.
- Standar akuntansi (sewa IFRS 16) akan secara signifikan mendongkrak EBITDA. Perbandingan lintas periode dan lintas perusahaan harus menggunakan basis setelah penyesuaian sewa (after-lease, aL).

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Statistik lembaga regulasi**: FCC (AS), Ofcom (UK), Kementerian Komunikasi (Tiongkok), NRA masing-masing negara. Menyediakan jumlah pelanggan, pangsa pasar, tingkat komplain, kepemilikan spektrum, dan hasil lelang — **ini adalah sumber paling objektif untuk menilai lanskap kompetisi**.
2. **Paket KPI perusahaan**: operator umumnya mengungkap sangat detail (pisahan postpaid/prepaid, ARPU, churn, rincian capex).
3. **Data industri**: GSMA, Ericsson Mobility Report, statistik penetrasi broadband masing-masing negara.
4. **Dokumen lelang spektrum**: aturan lelang, hasil, jadwal pembayaran, dan klausul perpanjangan.
5. **Pengungkapan kompetitor**: perilaku pricing dan promosi kompetitor di pasar yang sama adalah bukti langsung rasionalitas kompetisi.

### Mekanisme Kewajaran

- **Basis pelanggan harus dicantumkan**: apakah postpaid dan prepaid, koneksi IoT, pelanggan wholesale (MVNO) termasuk atau tidak. **Kartu IoT dan prepaid bisa dengan mudah mendongkrak volume, menutupi churn pelanggan riil**.
- **Basis ARPU**: apakah termasuk penjualan terminal, apakah termasuk pendapatan wholesale, apakah service ARPU. **Pertumbuhan pendapatan jasa (tanpa terminal) adalah indikator operasional riil**.
- **Basis EBITDA**: harus dicantumkan apakah setelah penyesuaian sewa (aL). IFRS 16 mengeluarkan operating lease dari biaya, secara artifisial mendongkrak EBITDA.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "5G mendorong kenaikan ARPU" harus dikaitkan dengan penetrasi paket tier, perubahan service ARPU aktual, dan return capex — bukan hanya mengutip narasi teknologi.
- **Bedakan siklus dan struktural**: penurunan ARPU bisa jadi siklus promosi, bisa juga memburuknya lanskap kompetisi. Harus dibedakan dengan data pricing kompetitor dan pangsa.
- **Hindari survivorship bias**: peer set harus mencakup operator di pasar perang harga, tidak hanya memilih perusahaan di pasar oligopoli rasional.

## 3. Pohon Penggerak Nilai Telekomunikasi

```text
Nilai operator =
  jumlah pelanggan × ARPU × margin EBITDA(aL)
  − maintenance capex − expansion capex
  − biaya spektrum (lelang dan perpanjangan)
  − pembayaran bunga dan sewa
  = free cash flow yang dapat didistribusikan

Enterprise Value =
  FCF yang dapat didistribusikan × keberlanjutan
  × stabilitas lanskap kompetisi (jumlah pemain dan rasionalitas)
  + nilai segmen menara/infrastruktur (multiple terpisah)
  − net debt (termasuk cicilan spektrum dan sewa)
  − risiko regulasi dan perpanjangan spektrum
```

Laporan minimal harus menjawab:

- Berapa jumlah pemain di pasar tersebut? Apakah kompetisi rasional atau perang harga? Apakah ada kemungkinan pemain baru masuk atau M&A disetujui?
- Berapa pertumbuhan pendapatan jasa (tanpa terminal)? Apakah perubahan ARPU berasal dari harga, struktur paket, atau promosi?
- Di mana posisi Capex/pendapatan dalam siklus? Apakah puncak investasi 5G/FTTH sudah lewat?
- Berapa rasio coverage dividen ÷ FCF (termasuk belanja spektrum)? Apakah dividen dijaga dengan berutang?
- Apakah aset menara sudah di-spin-off atau bisa di-spin-off? Berapa nilai spin-off-nya?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Kegunaan Riset | Jebakan Umum |
|---|---|---|---|
| Net addition postpaid | Penambahan bersih pelanggan postpaid | **Indikator inti kualitas pelanggan** | Kartu prepaid/IoT mendongkrak volume menutupi churn postpaid |
| Churn (tingkat churn) | Rasio churn pelanggan bulanan | Intensitas kompetisi dan loyalitas | Perlu dibedakan churn voluntary dan involuntary |
| ARPU | Pendapatan rata-rata per pengguna | Kapabilitas monetisasi | Paket bundling mendistribusi ulang antar bisnis, mendistorsi ARPU per item |
| Pertumbuhan pendapatan jasa | Pendapatan tanpa penjualan terminal | **Indikator operasional riil** | Fluktuasi penjualan terminal bisa menutupi penurunan pendapatan jasa |
| EBITDA margin (aL) | Margin setelah penyesuaian sewa | Profitabilitas | **IFRS 16 secara artifisial mendongkrak EBITDA yang belum disesuaikan** |
| Capex / pendapatan | Intensitas modal | Posisi siklus | Basis "maintenance capex" berbeda antar perusahaan |
| Maintenance vs expansion capex | Pemisahan capex | FCF riil | Expansion capex harus dikaitkan dengan bukti return |
| **FCF** | EBITDA − capex − spektrum − bunga − pajak | Basis dividen | Sering ditutupi oleh EBITDA |
| **Rasio coverage dividen** | FCF / dividen | Keamanan dividen | **< 100% berarti dividen dibayar dengan berutang** |
| Net debt/EBITDA | Leverage | Ruang rating dan dividen | **Harus termasuk cicilan spektrum dan liabilitas sewa** |
| Kepemilikan dan jatuh tempo spektrum | Band, bandwidth, kadaluarsa lisensi | Hak operasi jangka panjang | Biaya perpanjangan bisa sangat tinggi |
| Rencana lelang spektrum | Waktu lelang dan estimasi pengeluaran yang diketahui | Capex tersembunyi | Harus masuk ke proyeksi arus kas |
| Cakupan 5G/FTTH | Rasio cakupan jaringan | Posisi kompetitif | Cakupan tidak sama dengan monetisasi |
| Penetrasi paket bundling | Rasio bundling mobile+broadband | Stickiness | Bundling menurunkan churn tapi juga menurunkan ARPU per item |
| Pendapatan wholesale/MVNO | Pendapatan wholesale jaringan | Utilisasi kapasitas | Bisa membina kompetitor sendiri |
| Jumlah menara dan rasio tenant | Rata-rata tenant per menara | Nilai aset menara | Rasio tenant adalah inti valuasi menara |
| Pangsa pasar | Pangsa pendapatan atau pelanggan | Posisi kompetitif | Perlu dilihat dari basis postpaid |
| Jumlah pemain | Jumlah operator di pasar | **Variabel tunggal terbesar valuasi** | Konsolidasi 4→3 umumnya signifikan meningkatkan return industri |

8 indikator yang wajib diungkap duluan: net addition postpaid dan churn, pertumbuhan pendapatan jasa, ARPU, EBITDA margin (aL), capex/pendapatan, FCF dan rasio coverage dividen, net debt/EBITDA termasuk spektrum dan sewa, jumlah pemain pasar dan pangsa.

## 5. Struktur Model Keuangan

### Model Pendapatan

**Dimodelkan per pasar secara terpisah**, grup multinasional dilarang menggabungkan proyeksi:

1. **Mobile**: `jumlah pelanggan (postpaid/prepaid dipisah) × ARPU`, postpaid digulirkan berdasarkan net addition dan churn.
2. **Fixed-line/broadband**: `jumlah rumah tangga tercakup × penetrasi × ARPU`, kenaikan ARPU dari upgrade FTTH perlu bukti empiris.
3. **Enterprise/wholesale**: pendapatan kontrak, termasuk wholesale MVNO dan leased line enterprise.
4. **Penjualan terminal**: dipisah tersendiri, **tidak dimasukkan ke pertumbuhan pendapatan jasa**.
5. **Menara/infrastruktur**: `jumlah menara × rata-rata tenant per menara × sewa per tenant`, termasuk klausul linkage CPI.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5–10 tahun ke depan (perlu mencakup satu siklus capex penuh).
- Pendapatan jasa dan pendapatan terminal harus dipisah.
- Perubahan ARPU harus diurai menjadi kontribusi harga, struktur paket, dan promosi.

### Model Capex, Spektrum, dan Arus Kas

- **Siklus capex**: tentukan dengan jelas apakah saat ini sedang di puncak investasi, plateau, atau fase turun. **Penurunan capex setelah puncak 5G/FTTH adalah sumber utama perbaikan FCF**, tetapi perlu diverifikasi apakah penurunan riil atau hanya ditunda.
- **Maintenance vs expansion capex**: investasi expansion harus dikaitkan dengan bukti kenaikan ARPU, kenaikan pangsa, atau penghematan biaya, jika tidak dianggap penghancuran nilai.
- **Spektrum**: masukkan semua **rencana lelang yang diketahui, jadwal pembayaran, dan perpanjangan lisensi** ke dalam arus kas. Spektrum adalah pengeluaran besar yang paling mudah terlewat di telekomunikasi.
- **Bridge FCF**: `EBITDA(aL) → kurangi capex → kurangi spektrum → kurangi bunga → kurangi pajak → kurangi pembayaran sewa = FCF yang dapat didistribusikan`.
- **Basis net debt**: **harus termasuk cicilan spektrum dan liabilitas sewa**. Sale-leaseback aset menara akan membentuk beban off-balance-sheet, harus direstorasi.
- **Keberlanjutan dividen**: dividen / FCF yang dapat didistribusikan. Di bawah 100% berarti dividen dijaga dengan berutang atau divestasi aset.

### Batasan Asumsi Steady State

- **Tidak boleh langsung memperpetualkan FCF di tahun titik rendah capex**. Nilai terminal harus menggunakan intensitas modal rata-rata sepanjang siklus capex.
- Jika pasar ada perang harga atau pemain baru, tidak boleh sekaligus mengasumsikan ARPU stabil dan margin naik.
- Asumsi kenaikan ARPU dari 5G/teknologi baru harus memiliki dukungan bukti empiris penetrasi paket tier.
- Pengeluaran perpanjangan spektrum dan lelang masa depan harus dimasukkan ke arus kas sebelum nilai terminal, tidak boleh diasumsikan nol.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **EV/EBITDA (aL) + FCF yield sebagai utama**. Basis setelah penyesuaian sewa adalah prasyarat perbandingan lintas perusahaan.
2. **DCF, periode eksplisit mencakup satu siklus capex penuh (7–10 tahun)**, **hindari langsung memperpetualkan FCF di tahun titik rendah capex**.
3. **Dividend Discount Model (DDM)**: cocok untuk pemimpin pasar matang, tetapi harus diverifikasi dulu rasio coverage dividen.
4. **Skenario lanskap kompetisi**: M&A disetujui, pemain baru, hasil lelang spektrum ditangani dengan **probabilitas skenario**. **Ini adalah variabel tunggal terbesar valuasi telekomunikasi** — konsolidasi 4 menjadi 3 pemain umumnya signifikan meningkatkan return seluruh industri.

### Opsional

- **SOTP**: grup multinasional dinilai per pasar negara; segmen menara/infrastruktur diberi multiple lebih tinggi tersendiri.
- **Valuasi independen menara**: `jumlah menara × nilai per menara` atau EV/EBITDA (multiple industri menara signifikan lebih tinggi dari operator).
- **Biaya reposisi**: biaya reposisi jaringan sebagai referensi saat undervaluasi ekstrem.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- **Lanskap kompetisi pasar**: pasar rasional 3 pemain dan pasar perang harga 4+ pemain, **sama sekali tidak boleh dicampur**.
- Struktur bisnis: mobile murni, terintegrasi (mobile+fixed-line), dengan aset menara.
- Maturitas pasar: pasar matang dengan penetrasi jenuh vs pasar berkembang yang masih bertumbuh.
- Posisi siklus capex: sedang di puncak investasi 5G vs sudah lewat puncak.
- Leverage dan kebijakan dividen: operator matang dengan payout tinggi vs operator yang sedang deleveraging.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi lanskap kompetisi pasar atau posisi siklus capex jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan jasa, EBITDA(aL), FCF, net addition pelanggan relatif terhadap konsensus dan guidance? |
| Kualitas pelanggan | Bagaimana **net addition postpaid dan churn**? Apakah prepaid dan IoT mendongkrak volume untuk menutupi churn postpaid? |
| ARPU | Perubahan QoQ berasal dari harga, upgrade paket, atau promosi? Dampak bundling terintegrasi? |
| Pendapatan jasa | Berapa **pertumbuhan pendapatan jasa setelah dikeluarkan terminal**? Berapa selisih dengan pertumbuhan total pendapatan? |
| Perilaku kompetisi | Apakah kompetitor memulai perang harga? Bagaimana intensitas promosi? Apakah ada pemain baru? |
| Kualitas EBITDA | Apakah pertumbuhan dari perbaikan operasional riil, atau efek akuntansi dari IFRS 16/kapitalisasi? |
| Capex | Apakah guidance capex berubah? Pemisahan maintenance dan expansion? Apakah posisi siklus berubah? |
| Spektrum | Apakah ada rencana lelang baru, obligasi pembayaran, atau risiko perpanjangan? |
| FCF dan dividen | Berapa rasio coverage FCF terhadap dividen? Apakah nada bicara manajemen tentang kebijakan dividen berubah? |
| Leverage | Apakah net debt/EBITDA termasuk spektrum dan sewa memburuk? Tekanan rating? |
| Menara/divestasi aset | Apakah ada rencana spin-off, sale-leaseback? Pertimbangan harga dan obligasi sewa lanjutan? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan perubahan lanskap kompetisi, titik balik capex, keamanan dividen, atau M&A? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 5% tapi sektor telekomunikasi naik 3% di hari yang sama, reaksi spesifik perusahaan sekitar +2%.

## 8. Moat & Penilaian Kompetitif

Moat telekomunikasi berasal dari **kelangkaan lisensi, cakupan jaringan, dan struktur pasar**, dan struktur pasar sering lebih penting dari kapabilitas perusahaan. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| **Struktur pasar** | 3 pemain atau lebih sedikit, secara historis kompetisi rasional | 4 pemain atau lebih, atau ada pemain baru yang agresif |
| Aset spektrum | Memegang band frekuensi rendah berkualitas (keunggulan cakupan) dan bandwidth cukup | Spektrum tidak cukup atau akan segera kadaluarsa dan biaya perpanjangan tinggi |
| Cakupan dan kualitas jaringan | Cakupan dan kecepatan jaringan terus unggul, diverifikasi tes pihak ketiga | Cakupan tertinggal, perlu investasi besar untuk mengejar |
| Kapabilitas integrasi | Bundling mobile+broadband+TV, churn signifikan lebih rendah dari sejenis | Bisnis tunggal, mudah direbut paket bundling |
| Skala dan biaya | Biaya jaringan per pelanggan signifikan lebih rendah dari sejenis | Skala tidak cukup, pengenceran capex kurang memadai |
| Aset infrastruktur | Menara, fiber, data center milik sendiri, bisa dimonetisasi atau menurunkan biaya | Sudah sepenuhnya sale-leaseback, sewa menjadi beban rigid |
| Bisnis enterprise dan wholesale | Pelanggan enterprise stickiness tinggi dan kontrak wholesale | Bisnis consumer murni, sensitif harga |
| Relasi regulasi | Regulasi stabil, kebijakan M&A dan spektrum dapat diprediksi | Regulasi sering mengintervensi pricing atau memaksa wholesale |

Penilaian kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "unggul jaringan", tapi net addition postpaid negatif, ARPU menurun, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- **Membeli pertumbuhan pelanggan dengan subsidi terminal**, pendapatan jasa justru menurun bukan naik.
- Net addition postpaid negatif, tapi ditutupi dengan prepaid atau koneksi IoT.
- **Pertumbuhan EBITDA sepenuhnya dari faktor akuntansi** (reklasifikasi sewa IFRS 16, kapitalisasi biaya).
- **Rasio coverage dividen di bawah 100% dan sekaligus menambah leverage** — berutang untuk bayar dividen.
- Risiko perpanjangan lisensi spektrum belum terungkap memadai, atau biaya perpanjangan jauh lebih tinggi dari ekspektasi.
- Capex dipotong besar untuk menjaga FCF, tapi indikator kualitas jaringan ikut menurun (menguras masa depan).
- Aset menara sale-leaseback demi kas satu kali, tapi membentuk beban sewa jangka panjang yang rigid.
- Pemain baru mendapat spektrum atau persetujuan regulasi, tapi perusahaan masih mengasumsikan lanskap kompetisi tidak berubah.
- Investasi 5G/FTTH sudah bertahun-tahun tapi ARPU dan ROIC tidak membaik.
- Basis net debt tidak termasuk cicilan spektrum atau liabilitas sewa, meremehkan leverage riil.

### Daftar Bukti Sanggahan

Setiap laporan telekomunikasi minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Net addition postpaid negatif N kuartal berturut-turut.
- Pertumbuhan pendapatan jasa (tanpa terminal) jatuh di bawah ambang tertentu atau menjadi negatif.
- ARPU turun YoY melebihi besaran tertentu.
- Rasio coverage dividen FCF jatuh di bawah 100%.
- Net debt/EBITDA termasuk spektrum dan sewa melebihi ambang tertentu.
- Muncul pemain baru di pasar atau M&A ditolak, lanskap kompetisi memburuk.

### Kesalahpahaman Umum

- **Menggunakan EBITDA untuk valuasi tanpa mengabaikan capex dan belanja spektrum yang besar** — EBITDA dan FCF telekomunikasi memiliki jarak yang sangat besar.
- Memperpetualkan FCF di tahun titik rendah capex, secara sistematis melebih-lebihkan nilai.
- Mengabaikan dongkrakan IFRS 16 terhadap EBITDA, mendistorsi perbandingan lintas periode atau lintas perusahaan.
- Menganggap pertumbuhan total pendapatan sebagai perbaikan operasional, mengabaikan fluktuasi penjualan terminal.
- Menganggap pertumbuhan total pelanggan sebagai perbaikan kualitas, mengabaikan churn postpaid.
- Percaya narasi 5G/teknologi baru akan mendorong kenaikan ARPU, tanpa dukungan bukti empiris.
- Mengabaikan obligasi perpanjangan dan lelang spektrum, melebih-lebihkan free cash flow jangka panjang.
- Menggunakan dividend yield tinggi untuk menilai undervaluasi, mengabaikan rasio coverage yang tidak memadai dan risiko pemotongan.
- Mengabaikan jumlah pemain pasar — ini adalah faktor penentu terbesar return telekomunikasi.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan telekomunikasi selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel Pangsa-ARPU-Margin per Pasar (Wajib)

| Pasar/Negara | Jumlah Pemain | Pangsa Perusahaan | Net Addition Postpaid | Churn | ARPU | Pertumbuhan Pendapatan Jasa | EBITDA Margin (aL) |
|---|---:|---:|---:|---:|---:|---:|---:|

### Bridge FCF (Wajib)

| Item | Nominal | Keterangan |
|---|---:|---|
| EBITDA (aL) | | |
| Kurang: maintenance capex | | |
| Kurang: expansion capex | | |
| Kurang: belanja spektrum (lelang/perpanjangan) | | |
| Kurang: bunga | | |
| Kurang: pajak | | |
| Kurang: pembayaran sewa | | |
| **FCF yang dapat didistribusikan** | | |
| Total dividen | | |
| **Rasio coverage dividen** | | |

### Tabel Spektrum dan Lisensi

| Band Frekuensi | Bandwidth | Kadaluarsa Lisensi | Estimasi Biaya Perpanjangan | Rencana Lelang yang Diketahui |
|---|---:|---|---:|---|

### Tabel Restorasi Leverage

| Item | Nominal |
|---|---:|
| Net debt dari laporan | |
| Tambah: cicilan spektrum | |
| Tambah: liabilitas sewa | |
| Tambah: obligasi sale-leaseback | |
| **Net debt setelah restorasi** | |
| Net debt setelah restorasi / EBITDA (aL) | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Pertumbuhan pendapatan jasa | | | | |
| EBITDA margin (aL) | | | | |
| Capex/pendapatan rata-rata siklus | | | | |
| Belanja spektrum rata-rata tahunan | | | | |
| Skenario lanskap kompetisi (jumlah pemain) | | | | |
| Keberlanjutan kebijakan dividen | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada EBITDA periode ini, melainkan apakah lanskap kompetisi pasar dapat dipertahankan di X pemain, dan apakah FCF dapat kembali ke Y setelah puncak capex lewat."
- "Rasio coverage dividen adalah ……; penilaian saya yang jelas tentang keberlanjutan dividen adalah [aman / tertekan / kemungkinan besar dipotong], dengan alasan ……"
- "Jika salah satu indikator inti berikut — net addition postpaid / pertumbuhan pendapatan jasa / ARPU / rasio coverage dividen / leverage setelah restorasi — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
