# Lampiran Riset Mendalam Industri Properti/REIT

Berlaku untuk equity REIT (ritel/kantor/industrial logistics/data center/residensial/kesehatan/self-storage, dll.), mortgage REIT (mREIT), dan developer. **Prinsip inti: laba bersih tidak bermakna, lihat FFO/AFFO dan NAV; leverage dan sensitivitas suku bunga adalah variabel first-order.**

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai REIT
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Laba bersih tidak bermakna untuk REIT**. Depresiasi dan amortisasi adalah konstruksi akuntansi, sementara properti berkualitas sebenarnya terus naik nilainya. Selalu gunakan FFO/AFFO dan NAV sebagai basis analisis.
- **Equity REIT harus dipisah berdasarkan tipe properti**. Durasi sewa, intensitas capex, dan penggerak siklus masing-masing tipe sama sekali berbeda:
  - **Data center** ≈ siklus capex teknologi, sangat berkorelasi dengan permintaan AI.
  - **Industrial logistics** ≈ didorong penetrasi e-commerce.
  - **Kantor** ≈ secara struktural terdampak (remote working), perlu dievaluasi pergeseran permintaan jangka panjang.
  - **Ritel** ≈ terdivergensi (tipe community shopping center bertahan, tipe department store terdampak e-commerce).
  - **Residensial/self-storage** ≈ sewa jangka pendek, transmisi inflasi cepat.
  - **Kesehatan** ≈ penuaan populasi + risiko kredit operator.
- **mREIT esensinya adalah dana leverage spread**, dianalisis dengan framework net interest margin + mismatch durasi, **jangan dicampur multiple dengan equity REIT**.
- **Developer (terutama developer properti Tiongkok)**: lihat kualitas land bank, tingkat take-up (go-hua lu), saluran pendanaan, dan struktur utang. **Penilaian likuiditas lebih diutamakan dari penilaian valuasi**.
- Suku bunga adalah variabel first-order REIT: mempengaruhi cap rate (denominator valuasi) dan biaya pendanaan (arus kas). Harus dilakukan sensitivitas.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Supplemental material package**: **ini adalah sumber inti riset REIT**. Rincian properti, tabel jatuh tempo sewa, pemisahan same-store, rincian utang, dekomposisi NOI semua ada di sini, bukan di laporan keuangan utama.
2. **10-K/laporan tahunan dan catatan**: akuntansi sewa, kebijakan kapitalisasi, transaksi afiliasi, garansi dan komitmen.
3. **Data industri dan pasar**: statistik industri NAREIT, Green Street (sumber otoritatif cap rate, umumnya berbayar), laporan pasar CBRE/JLL/Cushman (tingkat vacancy, tambahan supply, sewa).
4. **Pembanding transaksi**: cap rate transaksi besar properti sejenis terkini, adalah input langsung valuasi NAV.
5. **Khusus developer Tiongkok**: kebijakan dana regulasi presale, pengungkapan commercial paper, informasi pendanaan trust dan non-standar, data penjualan lahan pemerintah daerah.

### Mekanisme Kewajaran

- **Basis FFO/AFFO harus disamakan**: gunakan definisi NAREIT sebagai basis, item penyesuaian khas perusahaan harus didaftar satu per satu. **Item penyesuaian AFFO yang membengkak tahun demi tahun adalah teknik pemolesan yang umum**.
- **Basis same-store**: same-store pool berubah setiap tahun, aset yang dikeluarkan sering yang performanya buruk. Harus diperiksa perubahan komposisi pool.
- **Basis cap rate**: menggunakan TTM NOI atau forward NOI, selisihnya bisa mencapai puluhan basis point. Harus dicantumkan.
- **Basis selisih sewa**: spread sewa baru dan perpanjangan harus dicantumkan apakah berbasis kas (cash spread) atau straight-line, yang terakhir bisa dipercantik oleh periode bebas sewa.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "pertumbuhan sewa kuat" harus dikaitkan dengan tingkat hunian, selisih sewa, periode bebas sewa, dan perubahan TI (tenant improvement allowance) — bukan hanya melihat sewa straight-line.
- **Bedakan siklus dan struktural**: kenaikan tingkat vacancy kantor adalah siklus atau dampak struktural remote working, penilaiannya sama sekali berbeda.

## 3. Pohon Penggerak Nilai REIT

```text
NAV per saham = (Σ NOI per portofolio properti ÷ cap rate pasar + aset lain − net debt) ÷ jumlah saham

AFFO = FFO − maintenance capex recurring − penyesuaian sewa straight-line − kompensasi berbasis saham, dll.

Pertumbuhan organik =
  pertumbuhan same-store NOI (= perubahan tingkat hunian + selisih sewa + kontrol biaya)
  + keuntungan nilai tambah proyek development/renovasi
  + nilai tambah akuisisi (akuisisi cap rate > biaya modal)
  − dilusi pendanaan ekuitas
  − kenaikan biaya refinancing utang jatuh tempo
```

Laporan minimal harus menjawab:

- Pertumbuhan same-store NOI berasal dari kenaikan tingkat hunian, kenaikan sewa, atau penghematan biaya? Bagaimana keberlanjutannya?
- Apakah selisih sewa baru dan perpanjangan positif atau negatif? Bagaimana tren periode bebas sewa dan subsidi TI?
- Di tahun mana jatuh tempo utang terkonsentrasi (debt wall)? Berapa tambahan biaya bunga jika refinancing dengan suku bunga saat ini?
- Apakah pertumbuhan didorong organik (same-store NOI) atau terus-menerus menerbitkan saham untuk akuisisi? Yang terakhir adalah penghancuran nilai saat harga saham di bawah NAV.
- Berapa rasio payout AFFO? Apakah dividen aman?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Tipe | Jebakan Umum |
|---|---|---|---|
| FFO | Laba bersih + depresiasi amortisasi − keuntungan penjualan | Equity REIT | Basis sedikit berbeda antar perusahaan, gunakan definisi NAREIT untuk menyamakan |
| **AFFO / CAD** | FFO − maintenance capex recurring − penyesuaian sewa straight-line | Equity REIT | **Meremehkan maintenance capex adalah pemolesan paling umum** |
| Pertumbuhan same-store NOI | Pertumbuhan organik setelah dikeluarkan M&A | Equity REIT | **Pool "same-store" berubah setiap tahun, perlu diperiksa komposisinya** |
| Tingkat hunian | Luas tersewa / luas tersewakan | Equity REIT | Perlu dibedakan leased vs occupied (sudah ditandatangani belum beroperasi) |
| Selisih sewa (spread) | Sewa baru/perpanjangan relatif sewa jatuh tempo | Equity REIT | Periode bebas sewa dan subsidi TI tersembunyi off-balance-sheet |
| Periode bebas sewa / TI | Insentif tenant | Equity REIT | Straight-line meratakan insentif, menutupi sewa kas riil |
| Cap rate | NOI ÷ nilai properti | Equity REIT | **Menggunakan TTM atau forward NOI selisihnya besar** |
| NAV / NAV per saham | Nilai properti − net debt | Equity REIT | Sangat bergantung pada asumsi cap rate |
| P/NAV | Harga saham / NAV per saham | Equity REIT | Perlu dibandingkan dengan rentang premium/diskon historis |
| Rasio payout AFFO | Dividen / AFFO | Equity REIT | **> 90% perlu diwaspadai pemotongan** |
| Net debt/EBITDA | Level leverage | Semua tipe | REIT umumnya leverage tinggi, perlu dibandingkan dengan sejenis |
| Porsi suku bunga fixed | Porsi utang suku bunga fixed | Semua tipe | **Porsi floating tinggi = sensitivitas suku bunga membesar** |
| Debt wall (jatuh tempo utang) | Nominal jatuh tempo per tahun | Semua tipe | Konsentrasi jatuh tempo adalah risiko likuiditas |
| Rata-rata tertimbang biaya utang | Biaya pendanaan gabungan | Semua tipe | Selisih dengan suku bunga baru menentukan dampak refinancing |
| Weighted average lease expiry (WALE) | Sisa tahun masa sewa | Equity REIT | Sewa jangka panjang tahan banting tapi transmisi inflasi lambat |
| Konsentrasi tenant | Porsi 10 tenant terbesar | Equity REIT | Dampak kebangkrutan tenant tunggal |
| Pipeline development | Skala dan imbal hasil proyek yang sedang dibangun | Equity REIT | Selisih imbal hasil development dan cap rate adalah sumber nilai tambah |
| Net interest margin | Imbal hasil aset − biaya liabilitas | mREIT | Indikator laba inti |
| Gap durasi | Selisih durasi aset dan liabilitas | mREIT | Amplifier volatilitas suku bunga |
| Tingkat take-up | Terjual/dapat dijual | Developer | Menentukan kecepatan pemasukan kas |
| Kualitas land bank | Porsi tier 1-2, biaya | Developer | Land bank kota tier bawah berisiko impairment |

8 indikator yang wajib diungkap duluan: FFO dan AFFO (dengan rincian item penyesuaian), pertumbuhan same-store NOI, tingkat hunian dan selisih sewa, cap rate dan NAV per saham, rasio payout AFFO, net debt/EBITDA dan porsi suku bunga fixed, debt wall, konsentrasi tenant.

## 5. Struktur Model Keuangan

### Model Pendapatan dan NOI

Dimodelkan per portofolio properti secara terpisah:

1. **Same-store NOI**: `perubahan tingkat hunian × level sewa × (1 + selisih sewa) − biaya operasional`. Dipisah per tipe properti dan regional.
2. **Non-same-store**: kontribusi akuisisi, delivery development, dan divestasi dipisah tersendiri.
3. **Pipeline development**: dimodelkan berdasarkan titik waktu delivery yang diperkirakan, NOI setelah stabil, dan imbal hasil development. **Selisih imbal hasil development dan cap rate pasar adalah sumber nilai tambah riil**.
4. **mREIT**: `aset berbunga × imbal hasil aset − liabilitas pendanaan × biaya liabilitas`, ditambah asumsi mismatch durasi dan prepayment.
5. **Developer**: `nilai barang yang dapat dijual × tingkat take-up × harga jual − biaya tanah − biaya konstruksi − pendanaan`, arus kas diutamakan dari laba.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, harus mencakup asumsi suku bunga refinancing utang jatuh tempo.
- FFO dan AFFO diproyeksikan terpisah, AFFO harus mencantumkan asumsi maintenance capex secara jelas.
- Pisahkan tersendiri pertumbuhan organik (same-store) dan pertumbuhan eksternal (akuisisi/development).

### Model Modal, Liabilitas, dan Dividen

- **Bridge AFFO**: dari FFO dikurangi item per item maintenance capex recurring, penyesuaian sewa straight-line, kompensasi berbasis saham, dan amortisasi insentif sewa. **"Item penyesuaian" yang membengkak tahun demi tahun harus diperiksa tersendiri**.
- **Debt wall**: daftar nominal jatuh tempo per tahun, selisih antara suku bunga saat ini dan suku bunga baru di pasar, hitung dampak refinancing terhadap AFFO.
- **Sensitivitas suku bunga**: porsi utang suku bunga floating × perubahan suku bunga = perubahan langsung biaya bunga; sekaligus kenaikan cap rate akan menekan NAV.
- **Pendanaan ekuitas**: REIT bergantung pada pendanaan eksternal untuk pertumbuhan. **Jika harga saham di bawah NAV tapi terus menerbitkan saham untuk akuisisi, ini adalah penghancuran nilai**, harus diidentifikasi.
- **Keberlanjutan dividen**: rasio payout AFFO, kas yang ditahan, batasan covenant utang terhadap dividen.
- **Pemeriksaan tambahan developer**: utang yang disamarkan sebagai ekuitas (ming-gu shi-zhai), garansi joint venture/afiliasi off-balance-sheet, commercial paper overdue, porsi dana regulasi presale yang dapat digunakan.

### Batasan Asumsi Steady State

- Pertumbuhan same-store NOI jangka panjang tidak boleh signifikan lebih tinggi dari inflasi, kecuali ada bukti ketidakseimbangan supply-demand struktural (seperti data center, logistik).
- Jika tingkat hunian menurun, selisih sewa menjadi negatif, periode bebas sewa diperpanjang, tidak boleh sekaligus mengasumsikan pertumbuhan same-store NOI tinggi.
- Asumsi cap rate harus konsisten dengan lingkungan suku bunga: saat suku bunga bebas risiko naik, asumsi kompresi cap rate memerlukan alasan yang sangat kuat.
- Aset tipe kantor perlu dievaluasi pergeseran permintaan struktural, tidak boleh sekadar mengasumsikan kembali ke level pra-pandemi.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **NAV (metode inti)**: `Σ NOI per portofolio properti ÷ cap rate pasar + aset lain − net debt = NAV per saham`. **Asumsi cap rate harus dilakukan sensitivitas ±50bp**, dan dibandingkan dengan rentang premium/diskon historis P/NAV.
2. **P/AFFO**: dibandingkan dengan historis sendiri dan REIT sejenis tipe properti yang sama. Sekaligus periksa **risiko pemotongan dividen saat rasio payout AFFO > 90%**.
3. **Dividend Discount Model (DDM)**: cocok untuk tipe sewa panjang, pertumbuhan stabil (seperti net lease).
4. **Skenario suku bunga**: berikan dampak ganda terhadap NAV dan AFFO dalam skenario suku bunga naik/turun.

### Opsional

- **DCF**: bisa digunakan, tetapi **basis arus kas harus AFFO**.
- **Biaya reposisi**: pasar dengan supply baru terbatas bisa menggunakan biaya reposisi sebagai batas bawah nilai.
- **Benchmark pasar privat**: cap rate transaksi besar terkini adalah kalibrasi langsung NAV.
- **mREIT: framework P/B** + analisis net interest margin dan durasi, tidak menggunakan FFO.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- **Tipe properti**: kantor, ritel, logistik, data center, residensial, kesehatan, self-storage, **sama sekali tidak boleh dicampur**.
- Regional dan pasar: cap rate dan pertumbuhan kota inti vs pasar tier dua sangat berbeda.
- Struktur sewa: sensitivitas inflasi sewa jangka panjang (net lease) dan sewa jangka pendek (residensial, self-storage) berbeda.
- Eksposur leverage dan suku bunga: porsi suku bunga fixed, struktur jatuh tempo.
- Model pertumbuhan: didorong organik vs didorong akuisisi.

Item yang dikecualikan harus dijelaskan: jika suatu REIT tampak sejenis tapi tipe properti atau struktur sewa jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

**Supplemental material package lebih penting dari laporan keuangan utama** — rincian properti, jatuh tempo sewa, pemisahan same-store semua ada di dalamnya.

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih FFO/AFFO, same-store NOI, tingkat hunian, dan guidance relatif terhadap konsensus? |
| Same-store NOI | Pertumbuhan berasal dari tingkat hunian, sewa, atau biaya? Apakah komposisi same-store pool berubah? |
| Tingkat hunian | Bagaimana perubahan marginal? Berapa selisih leased vs occupied (sudah ditandatangani belum beroperasi)? |
| Selisih sewa | Spread sewa baru dan perpanjangan positif atau negatif? Basis kas atau straight-line? |
| Insentif tenant | Apakah periode bebas sewa dan subsidi TI diperpanjang/ditambah? (sewa riil mungkin menurun) |
| Kualitas AFFO | Apakah item penyesuaian AFFO membengkak? Apakah asumsi maintenance capex wajar? |
| Utang | Biaya refinancing periode ini vs suku bunga existing? Apakah debt wall mendekat? |
| Eksposur suku bunga | Perubahan porsi suku bunga floating? Status jatuh tempo hedging? |
| Akuisisi/divestasi | Selisih cap rate akuisisi dan biaya modal? Apakah menerbitkan saham saat di bawah NAV? |
| Pipeline development | Progres delivery proyek, imbal hasil setelah stabil, kondisi over-budget? |
| Kebijakan dividen | Rasio payout AFFO? Apakah nada bicara manajemen tentang dividen berubah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan suku bunga, same-store NOI, nilai aset, atau keamanan dividen? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika REIT naik 6% tapi indeks REIT naik 4% di hari yang sama, reaksi spesifik perusahaan sekitar +2%.

## 8. Moat & Penilaian Kompetitif

Moat REIT berasal dari **kelangkaan lokasi dan batasan supply**, bukan kapabilitas manajemen. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Kelangkaan lokasi | Lokasi inti, barrier masuk tinggi, tambahan supply terbatas | Pasar pinggiran atau elastisitas supply tinggi |
| Batasan supply | Zoning, lahan langka, siklus konstruksi panjang | Tambahan supply terus mengalir masuk |
| Kualitas tenant | Tenant investment grade, sewa jangka panjang, terdiversifikasi | Kredit tenant lemah atau sangat terkonsentrasi |
| Struktur sewa | Klausul kenaikan sewa built-in, struktur triple-net | Sewa fixed atau perlu renegosiasi sering |
| Daya tawar harga | Selisih sewa perpanjangan terus positif dan di atas inflasi | Perlu periode bebas sewa dan TI untuk menjaga tingkat hunian |
| Keunggulan biaya modal | Rating tinggi, biaya pendanaan lebih rendah dari sejenis | Leverage tinggi, rating tertekan, bergantung utang berbiaya tinggi |
| Kapabilitas development | Imbal hasil development signifikan lebih tinggi dari cap rate akuisisi | Proyek development over-budget atau imbal hasil lebih rendah dari pasar |
| Skala dan platform operasional | Skala membawa keunggulan rasio biaya operasional | Skala tidak cukup, rasio biaya lebih tinggi dari sejenis |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "aset inti langka", tapi tingkat hunian menurun, selisih sewa menjadi negatif, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- **Item penyesuaian AFFO membengkak tahun demi tahun**, basis terus dilonggarkan.
- Asumsi maintenance capex recurring jelas lebih rendah dari REIT sejenis atau level historis.
- **Porsi bunga yang dikapitalisasi naik**, mengalihkan biaya pendanaan ke aset.
- **Sering menerbitkan saham untuk mendanai akuisisi (dilusi untuk menampung akuisisi)** — pertumbuhan didorong penerbitan saham bukan organik, terutama saat harga saham di bawah NAV.
- Pricing transaksi properti dengan pihak afiliasi tanpa penilaian independen.
- Tingkat hunian dijaga dengan memperpanjang periode bebas sewa dan meningkatkan TI, sewa kas aktual menurun.
- Komposisi same-store pool berubah, mengeluarkan aset yang performanya buruk.
- Utang terkonsentrasi jatuh tempo dan suku bunga saat ini jauh lebih tinggi dari suku bunga existing.
- Rasio payout AFFO terus di atas 90%, atau menggunakan dana pendanaan/divestasi untuk menjaga dividen.
- Aset tipe kantor masih dinilai berdasarkan asumsi permintaan pra-pandemi.

**Pemeriksaan tambahan developer Tiongkok**: utang yang disamarkan sebagai ekuitas, garansi joint venture/afiliasi off-balance-sheet, commercial paper overdue, dana regulasi presale yang disalahgunakan atau tidak dapat digunakan.

### Daftar Bukti Sanggahan

Setiap laporan REIT minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Pertumbuhan same-store NOI jatuh di bawah ambang tertentu atau menjadi negatif.
- Tingkat hunian jatuh di bawah level tertentu, atau selisih sewa terus negatif.
- Rasio payout AFFO melebihi persentase tertentu.
- Net debt/EBITDA melebihi ambang covenant, atau porsi suku bunga fixed jatuh di bawah level tertentu.
- Biaya refinancing naik melebihi bp tertentu relatif terhadap suku bunga existing.
- Cap rate pasar naik melebihi bp tertentu (langsung menekan NAV).

### Kesalahpahaman Umum

- **Menganalisis REIT dengan laba bersih atau P/E** — depresiasi amortisasi membuat laba bersih sangat terdistorsi.
- Menggunakan FFO bukan AFFO untuk menilai keamanan dividen, mengabaikan maintenance capex.
- Mengabaikan periode bebas sewa dan TI, menganggap sewa straight-line sebagai sewa kas riil.
- Menganggap pertumbuhan FFO yang didorong akuisisi sebagai penciptaan nilai, mengabaikan dilusi dari penerbitan saham.
- Mengabaikan efek leverage cap rate terhadap NAV (saat NOI tetap, kenaikan cap rate 50bp bisa membuat NAV turun dua digit persentase).
- Menganggap dividend yield tinggi sebagai undervaluasi, mengabaikan rasio payout yang terlalu tinggi dan risiko pemotongan.
- Mengasumsikan rebound siklikal untuk aset kantor, mengabaikan pergeseran permintaan struktural.
- Menilai mREIT seperti equity REIT dengan multiple FFO.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan REIT selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Debt Wall Sewa (Wajib)

| Tahun | Luas Jatuh Tempo | Porsi | Sewa Jatuh Tempo | Sewa Pasar Saat Ini | Prediksi Selisih Sewa |
|---|---:|---:|---:|---:|---:|

### Debt Wall Utang (Wajib)

| Tahun | Nominal Jatuh Tempo | Porsi | Suku Bunga Existing | Suku Bunga Pasar Saat Ini | Dampak Refinancing (AFFO) |
|---|---:|---:|---:|---:|---:|

### Bridge FFO / AFFO

| Item | Nominal | Keterangan |
|---|---:|---|
| Laba bersih | | |
| Tambah: depresiasi amortisasi | | |
| Kurang: keuntungan penjualan | | |
| **FFO** | | |
| Kurang: maintenance capex recurring | | |
| Kurang: penyesuaian sewa straight-line | | |
| Kurang: penyesuaian lain (daftar satu per satu) | | |
| **AFFO** | | |
| Rasio payout AFFO | | |

### Tabel Portofolio Properti dan Operasional

| Tipe Properti/Regional | Porsi NOI | Tingkat Hunian | Pertumbuhan Same-Store NOI | Selisih Sewa Baru | WALE | Cap Rate |
|---|---:|---:|---:|---:|---:|---:|

### Tabel Sensitivitas NAV (Wajib)

| Cap Rate \ Pertumbuhan Sewa | −2% | 0% | +2% | +4% |
|---|---:|---:|---:|---:|
| Cap rate −50bp | | | | |
| Cap rate basis | | | | |
| Cap rate +50bp | | | | |
| Cap rate +100bp | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi REIT ini saat ini paling bergantung bukan pada FFO periode ini, melainkan pada asumsi cap rate X% dan pertumbuhan same-store NOI Y%; setiap kenaikan cap rate 50bp, NAV per saham turun Z%."
- "P/NAV saat ini adalah ……, relatif terhadap rentang historis berada di posisi ……; rasio payout AFFO adalah ……, margin keamanan dividen adalah ……"
- "Jika salah satu indikator inti berikut — same-store NOI / tingkat hunian / selisih sewa / rasio payout / biaya refinancing — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
