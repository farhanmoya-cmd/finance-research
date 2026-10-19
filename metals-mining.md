# Lampiran Riset Mendalam Industri Logam/Pertambangan

Berlaku untuk logam dasar, logam mulia, logam baterai, bijih besi, perusahaan tambang batu bara, dan smelting/pengolahan. Karakteristik: **price taker (penerima harga) + aset yang bersifat depletable (bisa habis)**. Rumus inti: nilai = asumsi harga komoditas × posisi pada kurva biaya × umur reserve. Perusahaan sumber daya migas gunakan `industries/energy.md`.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Pertambangan
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Perusahaan tambang tidak memiliki daya tawar harga**. Separuh dari riset ini adalah riset terhadap komoditasnya sendiri: balance supply-demand, kurva biaya (**cash cost persentil 90 adalah jangkar harga jangka panjang**), siklus inventori, dan substitusi produk.
- **NAV adalah framework utama**: akumulasi DCF per tambang dikurangi net debt dikurangi liabilitas penutupan/reklamasi. **Umur tambang terbatas, sama sekali tidak boleh mengasumsikan perpetual tanpa batas** — ini adalah perbedaan paling fundamental antara pertambangan dan manufaktur.
- **Posisi pada kurva biaya menentukan hidup-mati**: perusahaan tambang dengan biaya persentil satu/dua bisa bertahan lintas siklus, perusahaan tambang persentil empat pada dasarnya adalah call option terhadap harga komoditas, framework valuasinya sama sekali berbeda.
- Perusahaan tambang logam mulia juga melihat AISC dan reserve replacement ratio; **perusahaan eksplorasi adalah portofolio opsi, bukan aset arus kas**, tidak boleh menggunakan DCF sebagai valuasi utama.
- Penurunan grade (kadar bijih) adalah hukum alam pertambangan. Produksi tetap tapi grade menurun berarti biaya per unit pasti naik, harus dimodelkan secara eksplisit.
- Risiko politik dan pajak adalah variabel first-order dalam pertambangan, didiskon tersendiri berdasarkan negara lokasi tambang.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Laporan teknis**: NI 43-101 (Kanada), JORC (Australia), SK-1300 (AS) adalah **sumber otoritatif primer** untuk reserve, grade, biaya, dan rencana tambang. Tabel reserve dalam laporan tahunan harus direkonsiliasi per tahun.
2. **Pengajuan regulasi dan pengungkapan perusahaan**: laporan tahunan, laporan kuartalan, laporan produksi, pengumuman update reserve, materi site visit tambang.
3. **Data pasar komoditas**: inventori dan harga LME/COMEX/SHFE, bukti gudang (warehouse receipt) SHFE, posisi bursa.
4. **Data kurva biaya**: kurva biaya global dari Wood Mackenzie, CRU (umumnya berbayar); sumber alternatif publik termasuk rekap horizontal dari pengungkapan AISC sejenis.
5. **Statistik resmi**: USGS Mineral Yearbook, data impor-ekspor bea cukai masing-masing negara, statistik produksi asosiasi industri.

### Mekanisme Kewajaran

- **Basis reserve harus dicantumkan**: Proven & Probable (P&P, reserve) dan Measured/Indicated/Inferred (M&I&I, resource) adalah konsep yang sama sekali berbeda. **Resource tidak sama dengan reserve yang dapat ditambang**.
- **Asumsi harga reserve**: perhitungan reserve bergantung pada asumsi harga komoditas. **Menaikkan asumsi harga bisa "menciptakan" reserve**, harus diperiksa harga yang digunakan dalam laporan reserve tahun-tahun sebelumnya.
- **Basis biaya disamakan**: definisi C1 cash cost, AISC (all-in sustaining cost), dan total cost sangat berbeda, **basis by-product credit (kredit produk sampingan) terutama tidak konsisten**. Samakan basis sebelum membandingkan lintas perusahaan.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "produsen biaya rendah" harus dikaitkan dengan persentil industri AISC, tren grade, dan maintenance capex — bukan hanya mengutip basis C1 cost dari perusahaan.
- **Bedakan siklus dan struktural**: kenaikan biaya per unit bisa jadi siklus inflasi, bisa juga faktor struktural dari penurunan grade atau kedalaman tambang yang meningkat. Harus dibedakan dengan data grade dan stripping ratio.
- **Hindari survivorship bias**: peer set harus mencakup perusahaan tambang biaya tinggi dan tambang yang sudah berhenti produksi karena penurunan harga.

## 3. Pohon Penggerak Nilai Pertambangan

```text
NAV = Σ per tambang [ produksi × (harga realisasi − AISC) × umur tersisa, didiskon per tahun ]
      + opsi eksplorasi/sumber daya belum dikembangkan (setelah diskon risiko)
      − net debt
      − liabilitas reklamasi dan penutupan
      − biaya level korporat

Pertumbuhan nilai per saham =
  reserve replacement ratio (eksplorasi atau akuisisi)
  × kualitas sumber daya (grade, stripping ratio, recovery rate metalurgi)
  × kemampuan menjaga persentil kurva biaya
  − dilusi ekuitas
  − erosi M&A di puncak siklus
```

Laporan minimal harus menjawab:

- Di persentil berapa AISC perusahaan dalam kurva biaya global? Apakah persentil itu dapat menjaga arus kas positif saat harga turun?
- Berapa umur tersisa masing-masing tambang? Apa yang tersisa setelah rata-rata umur tertimbang berakhir?
- Bagaimana tren grade? Berapa bijih tambahan yang perlu diolah untuk menjaga produksi saat ini (dengan biaya tambahan berapa)?
- Berapa maintenance capex? Berapa free cash flow riil setelah dikurangi?
- Bagaimana reserve replacement ratio? Apakah grade dan biaya reserve tambahan lebih baik atau lebih buruk dibandingkan aset existing?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Kegunaan Riset | Jebakan Umum |
|---|---|---|---|
| Guidance produksi | Per tambang, per logam | Basis pendapatan | **Penurunan grade sering ditutupi oleh total produksi** |
| Grade (kadar bijih) | Kandungan logam per unit bijih | Penggerak dasar biaya dan produksi | High-grading (menambang area grade tinggi lebih dulu) akan menguras masa depan |
| Stripping ratio | Waste rock / bijih | Penggerak biaya tambang terbuka | Naik seiring kedalaman penambangan |
| Recovery rate | Rasio recovery metalurgi | Output aktual | Perubahan karakteristik bijih dapat menurunkan recovery |
| **C1 cash cost** | Biaya operasi kas langsung | Keputusan shutdown jangka pendek | **Basis by-product credit sangat berbeda** |
| **AISC** | All-in sustaining cost (termasuk maintenance capex, reklamasi, biaya korporat) | **Indikator kompetitif inti** | Masih ada perbedaan definisi antar perusahaan, perlu diverifikasi |
| Persentil kurva biaya | Posisi AISC dalam kurva global | Ketahanan siklus | Persentil satu/dua bisa bertahan lintas siklus |
| Reserve P&P | Reserve proven + probable | Sumber daya yang dapat ditambang | **Bergantung pada asumsi harga** |
| Resource M&I&I | Sumber daya measured/indicated/inferred | Potensi sumber daya | **Tidak sama dengan reserve yang dapat ditambang** |
| Umur reserve | Reserve / produksi tahunan | Durasi aset | Menentukan panjang periode eksplisit DCF |
| Reserve replacement ratio | Reserve tambahan / reserve terkonsumsi | Keberlanjutan | Replacement dari akuisisi dan dari eksplorasi memiliki nilai berbeda |
| Maintenance capex | Investasi untuk menjaga kapasitas saat ini | Item pengurang FCF riil | **Terus-menerus di bawah depresiasi adalah sinyal berbahaya** |
| Growth capex | Investasi ekspansi/pembangunan baru | Kapasitas masa depan | Perlu dievaluasi return-nya secara terpisah |
| Harga realisasi | Harga jual aktual | Pendapatan | Selisih dengan harga benchmark (penalti grade, biaya pengiriman, biaya pengolahan) |
| TC/RC | Treatment and refining charge | Smelting, penjualan konsentrat | Mempengaruhi pendapatan bersih produsen konsentrat |
| Posisi hedging | Produksi dan harga yang sudah terkunci | Eksposur harga | **Di bull market dibatasi hedging (upside capped)** |
| Liabilitas reklamasi/penutupan | Liabilitas penutupan tambang | Liabilitas implisit | **Discount rate agresif akan meremehkan liabilitas** |
| Risiko negara | Sejarah nasionalisasi sumber daya, windfall tax | Faktor diskon | Harus dievaluasi tersendiri per negara lokasi tambang |
| Konflik komunitas/lingkungan | Risiko ESG dan lisensi | Risiko shutdown | Eskalasi dapat menyebabkan penghentian produksi jangka panjang |

8 indikator yang wajib diungkap duluan: produksi per tambang dan grade, AISC dan persentil kurva biaya, reserve P&P dan umur, reserve replacement ratio, maintenance capex, harga realisasi dan selisih dari benchmark, liabilitas reklamasi, eksposur risiko negara.

## 5. Struktur Model Keuangan

### Model Produksi dan Pendapatan

**Harus dimodelkan per tambang**, tidak boleh digabungkan:

1. **Produksi**: `volume bijih diolah × grade × recovery rate = produksi logam`. Grade berubah per tahun sesuai rencana tambang, tidak boleh menggunakan nilai fixed.
2. **Pendapatan**: `produksi × harga realisasi`. Harga realisasi dikurangi dari harga benchmark setelah penalti grade, biaya pengiriman, TC/RC, dan dampak hedging.
3. **Umur tambang**: dihitung berdasarkan reserve P&P dan kapasitas produksi tahunan. **Periode eksplisit DCF sampai akhir umur tambang, setelah itu tidak ada nilai terminal** (atau hanya sisa nilai residu/pengeluaran reklamasi).
4. **Proyek belum dikembangkan**: dimodelkan berdasarkan probabilitas pengembangan, periode konstruksi, capex, dan arus kas setelah beroperasi, dimasukkan setelah diskon risiko.
5. **Aset eksplorasi**: diperlakukan sebagai opsi, tidak masuk DCF basis.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Periode eksplisit mencakup seluruh umur tambang-tambang utama.
- Tren grade harus diberikan eksplisit, dan dikaitkan dengan biaya per unit.
- Asumsi harga komoditas harus mencantumkan sumbernya (forward curve, long-term incentive price, estimasi lembaga).

### Model Biaya, Modal, dan Liabilitas

- **Struktur biaya**: per tambang, diurai biaya operasi kas, royalti, transportasi, TC/RC, maintenance capex, biaya korporat, dirangkum sebagai AISC.
- **Keterkaitan biaya dan grade**: ketika grade turun, untuk menjaga produksi logam yang sama diperlukan pengolahan bijih lebih banyak, biaya per unit pasti naik. Keterkaitan ini harus dimodelkan, tidak bisa mengasumsikan biaya konstan.
- **Maintenance capex**: diestimasi tersendiri. **Free cash flow riil = arus kas operasi − maintenance capex**. Terus-menerus di bawah depresiasi adalah sinyal menguras kapasitas.
- **Liabilitas reklamasi dan penutupan**: periksa kecukupan provisi, asumsi discount rate, dan jadwal pengeluaran kas. **Discount rate agresif akan meremehkan liabilitas secara sistematis**.
- **Hedging**: cantumkan posisi, harga, tenor, dan rasio cakupan. Hedging akan membatasi ruang upside saat bull market.
- **Pajak negara**: royalti, windfall tax, batasan ekspor dimodelkan terpisah per negara lokasi tambang.

### Batasan Asumsi Steady State

- **Dilarang mengapitalisasi harga spot secara perpetual**. Harga jangka panjang harus dijangkar pada **incentive price** — yaitu harga yang diperlukan untuk mendukung supply baru, biasanya setara dengan persentil 90 kurva biaya plus return wajar.
- Umur tambang berakhir berarti arus kas berakhir, **tidak boleh mengasumsikan perpetual tanpa batas**. Jika mengasumsikan reserve terus direplace, harus diberikan asumsi biaya dan grade replacement-nya.
- Jika grade menurun, stripping ratio naik, maintenance capex naik, tidak boleh sekaligus mengasumsikan biaya stabil dan produksi naik.
- Perusahaan tambang biaya persentil empat tidak boleh diberi multiple valuasi yang sama dengan produsen biaya rendah — yang pertama akan berhenti produksi saat harga turun.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **NAV / P/NAV (metode utama)**: akumulasi DCF per tambang. Harga komoditas menggunakan **dual anchor forward curve + long-term incentive price**, **dilarang mengapitalisasi harga spot secara perpetual**.
2. **Positioning kurva biaya**: tentukan dengan jelas persentil AISC perusahaan dalam kurva biaya global, ini menentukan ketahanan siklus dan median valuasi.
3. **Sensitivitas harga komoditas (wajib dilakukan)**: elastisitas FCF dan NAV terhadap harga komoditas ±20%. **Elastisitas perusahaan tambang leverage tinggi bisa mencapai 3–5 kali**.
4. **Laba mid-cycle × EV/EBITDA median**: sebagai cross-check NAV, skenario spot dan skenario harga jangka panjang dipisah.

### Opsional

- **Rentang historis P/NAV**: dibandingkan dengan rentang premium/diskon P/NAV historis perusahaan dan sejenis.
- **Nilai reposisi**: capex membangun kapasitas setara baru, sebagai referensi batas bawah saat undervaluasi ekstrem.
- **Option pricing**: perusahaan eksplorasi dan proyek belum dikembangkan menggunakan framework opsi, bukan DCF.
- **Nilai per unit sumber daya**: `EV / jumlah sumber daya` sebagai perbandingan horizontal kasar, bukan valuasi utama.

**Risiko politik/pajak didiskon tersendiri per negara lokasi tambang** — riwayat nasionalisasi sumber daya, windfall tax, larangan ekspor adalah input penting.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Jenis logam: logam mulia, logam dasar, logam baterai, bijih besi, batu bara memiliki penggerak siklus yang sama sekali berbeda.
- Persentil kurva biaya: framework valuasi perusahaan tambang biaya rendah dan biaya tinggi berbeda.
- Fase aset: produksi, pembangunan, eksplorasi.
- Umur tambang dan kualitas reserve: tambang berkualitas berumur panjang dan tambang marginal berumur singkat.
- Risiko negara: aset di negara OECD dan aset di jurisdiksi berisiko tinggi.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi persentil biaya atau risiko negara jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih produksi, AISC, harga realisasi, EPS, FCF relatif terhadap konsensus dan guidance? |
| Produksi dan grade | Perubahan produksi berasal dari volume olahan, grade, atau recovery rate? Apakah grade menurun sesuai rencana? |
| Apakah terjadi high-grading | Apakah sedang memprioritaskan penambangan area grade tinggi untuk mempercantik biaya jangka pendek? |
| AISC QoQ | Perubahan biaya berasal dari grade, stripping ratio, inflasi, nilai tukar, atau pengenceran produksi? |
| Harga realisasi | Bagaimana perubahan selisih relatif terhadap harga benchmark? Berapa dampak hedging? |
| Maintenance capex | Apakah ditekan untuk mempercantik FCF? Bagaimana rasionya terhadap depresiasi? |
| Progres proyek | Apakah proyek yang sedang dibangun over budget atau tertunda? Apakah intensitas modal naik? |
| Update reserve | Perubahan reserve berasal dari eksplorasi, revaluasi, atau penyesuaian asumsi harga? |
| Liabilitas reklamasi | Apakah asumsi provisi dan discount rate berubah? |
| Alokasi modal | Apakah membagikan dividen puncak atau melakukan M&A besar di saat harga tinggi? |
| ESG/komunitas | Apakah ada eskalasi risiko penghentian produksi, lisensi, atau konflik komunitas? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan harga komoditas, kontrol biaya, progres proyek, atau return modal? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan dampak pasar dan harga komoditas: jika saham naik 7% tapi kenaikan harga logam mendorong sektor naik 5% di periode yang sama, reaksi spesifik perusahaan sekitar +2%.

## 8. Moat & Penilaian Kompetitif

Pertambangan adalah industri komoditas murni, moat hanya berasal dari **endowment sumber daya dan posisi biaya**. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Persentil kurva biaya | AISC di persentil satu/dua global, tetap menghasilkan kas di titik rendah harga | Biaya persentil empat, terpaksa berhenti produksi saat harga rendah |
| Grade dan skala sumber daya | Grade tinggi, skala besar, stripping ratio rendah | Grade rendah, dalam, stripping ratio tinggi |
| Umur tambang | Rata-rata tertimbang umur panjang, tanpa risiko penghabisan jangka pendek | Tambang utama umur tersisa pendek tanpa penggantinya |
| Infrastruktur | Rel kereta, pelabuhan, listrik milik sendiri mengurangi biaya transportasi | Bergantung pada logistik pihak ketiga, biaya tinggi dan tidak stabil |
| Stabilitas negara dan lisensi | Jurisdiksi OECD, lisensi stabil, sistem pajak dapat diprediksi | Jurisdiksi berisiko tinggi, riwayat nasionalisasi atau windfall tax |
| Struktur produk sampingan | Kredit produk sampingan signifikan menurunkan biaya logam utama | Logam tunggal, tanpa buffer biaya |
| Eksekusi proyek | Proyek historis sesuai budget dan tepat waktu | Berulang kali over budget dan tertunda |
| Disiplin modal | Tidak melakukan M&A harga tinggi atau ekspansi berlebihan di puncak harga | Ekspansi procyclical, akuisisi di puncak siklus |

Penilaian kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "produsen biaya rendah", tapi AISC lebih tinggi dari median sejenis atau grade terus menurun, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- **Asumsi harga reserve dinaikkan tiap tahun** — "menciptakan" reserve dengan harga, bukan dengan eksplorasi.
- **Maintenance capex terus-menerus di bawah depresiasi**, kapasitas sedang terkuras.
- Memprioritaskan penambangan area grade tinggi (high-grading) untuk menekan AISC jangka pendek, mengorbankan ekonomi keseluruhan tambang.
- Melakukan M&A besar atau meningkatkan dividen signifikan saat harga komoditas tinggi.
- Asumsi discount rate liabilitas reklamasi dan penutupan agresif, atau provisi jelas lebih rendah dari sejenis.
- Eskalasi konflik komunitas, lingkungan, atau masyarakat adat, bisa menyebabkan pencabutan lisensi atau penghentian produksi jangka panjang.
- Guidance produksi dipertahankan tapi guidance grade diturunkan, tanpa menaikkan guidance biaya secara sepadan.
- Rasio hedging rendah saat harga rendah, tinggi saat harga tinggi (gagal timing).
- Sering merevisi rencana tambang atau menunda update laporan teknis.
- Resource (M&I&I) digunakan untuk mendukung valuasi, bukan reserve (P&P).

### Daftar Bukti Sanggahan

Setiap laporan pertambangan minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- AISC naik melebihi ambang tertentu, atau persentil kurva biaya bergeser turun.
- Grade menurun melebihi persentase tertentu dari rencana tambang.
- Reserve replacement ratio terus di bawah 100%.
- Harga komoditas jatuh di bawah AISC perusahaan atau biaya persentil 90 industri.
- Tambang kunci mengalami penghentian produksi, pencabutan lisensi, atau kejadian konflik komunitas.
- Net debt/EBITDA menembus ambang covenant dalam skenario harga rendah.

### Kesalahpahaman Umum

- **Mengapitalisasi NAV dengan harga spot secara perpetual**, secara sistematis melebih-lebihkan nilai di puncak siklus.
- **Mengasumsikan umur tambang tanpa batas** — sumber daya bersifat habis, harus ada titik akhir.
- Menganggap resource (M&I&I) sebagai reserve (P&P) dalam perhitungan nilai.
- Menggunakan C1 cash cost bukan AISC untuk menilai daya kompetitif, meremehkan biaya riil.
- Mengabaikan keterkaitan antara penurunan grade dan kenaikan biaya.
- Mengabaikan maintenance capex, menganggap arus kas operasi sebagai free cash flow.
- Di puncak siklus menggunakan P/E rendah sebagai indikasi murah (sama seperti semua saham siklikal).
- Tidak melakukan diskon negara untuk aset di jurisdiksi berisiko tinggi.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan pertambangan selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Positioning Kurva Biaya (Wajib)

Tuliskan dengan jelas dalam teks: **"AISC perusahaan ini adalah X, berada di persentil Y pada kurva biaya global logam tersebut"**, dan jelaskan sumber data serta perbandingan dengan sejenis.

| Perusahaan | AISC | Persentil Kurva Biaya | Negara Lokasi Tambang Utama |
|---|---:|---:|---|

### Tabel NAV per Tambang (Wajib)

| Tambang | Negara | Produksi | Tren Grade | AISC | Umur Tersisa | Diskon Negara | NAV | Porsi |
|---|---|---:|---|---:|---:|---:|---:|---:|

### Tabel Reserve dan Resource

| Item | Periode Ini | Periode Lalu | Alasan Perubahan | Asumsi Harga yang Digunakan |
|---|---:|---:|---|---:|
| Reserve P&P | | | | |
| Resource M&I | | | | |
| Resource Inferred | | | | |
| Reserve replacement ratio | | | | |
| Rata-rata tertimbang umur tambang | | | | |

### Unit Economics dan Maintenance Capex

| Indikator | Periode Ini | YoY | Posisi vs Sejenis | Sumber |
|---|---:|---:|---|---|
| C1 cash cost | | | | |
| AISC | | | | |
| Maintenance capex | | | | |
| Maintenance capex / depresiasi | | | | |
| FCF riil (arus kas operasi − maintenance capex) | | | | |

### Tabel Sensitivitas Harga Komoditas (Wajib)

| Skenario | Harga Komoditas | NAV | NAV per Saham | FCF | Net Debt/EBITDA |
|---|---:|---:|---:|---:|---:|
| Harga −20% | | | | | |
| Forward curve | | | | | |
| Long-term incentive price | | | | | |
| Harga +20% | | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada harga logam periode berjalan, melainkan pada asumsi long-term incentive price X, dan apakah AISC perusahaan dapat dipertahankan di persentil Y kurva biaya global."
- "Rata-rata tertimbang umur tersisa tambang utama adalah N tahun; aset penggantinya setelah umur berakhir adalah ……, diskon risiko yang saya berikan untuk bagian ini adalah ……"
- "Jika salah satu indikator inti berikut — AISC / grade / reserve replacement / harga komoditas / kebijakan negara — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
