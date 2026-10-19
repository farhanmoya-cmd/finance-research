# Lampiran Riset Mendalam Industri Industrial/Mesin

Berlaku untuk mesin umum, otomasi, peralatan listrik, aerospace & defense (kedirgantaraan dan pertahanan), grup industrial terdiversifikasi, dan jasa konstruksi teknik (engineering construction). Karakteristik: pesanan mendahului (order lead), campuran siklus panjang-pendek, dan after-market/jasa purna jual, inti valuasi terletak pada "identifikasi posisi siklus + stratifikasi kualitas". Grup terdiversifikasi selalu menggunakan SOTP.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Industrial
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Identifikasi dulu panjang siklusnya**, karena ini menentukan indikator leading mana yang digunakan untuk penilaian:
  - **Siklus pendek** (perkakas, komponen umum, distribusi listrik, pneumatik/hidrolik): mengikuti PMI/output industri, siklus inventori sekitar 12–18 bulan.
  - **Siklus panjang** (mesin pesawat, peralatan energi, proyek besar): lihat pesanan/backlog dan irama pengiriman, **pendapatan adalah indikator lagging**.
  - **Industri otomasi/software** (robotika, PLC, software industrial): logika penetrasi struktural berlapis dengan siklus, harus dibahas terpisah.
  - **Pertahanan**: didorong anggaran, lihat siklus hidup proyek senjata dan eksposur cost overrun kontrak harga fixed.
- **Disiplin valuasi inti saham industrial adalah positioning siklus**: harus menjawab dulu "posisi margin saat ini di mana dalam rentang 10 tahun", baru bicara multiple.
- **Pesanan mendahului pendapatan**. Perubahan marginal orders dan book-to-bill adalah sinyal pertama, pengakuan pendapatan biasanya lagging 2–6 kuartal.
- Jasa/after-market adalah dasar stratifikasi kualitas perusahaan industrial. Stabilitas arus kas dari pendapatan jasa yang didorong basis instalasi jauh lebih tinggi dari penjualan alat, sebaiknya diberi multiple terpisah dalam SOTP.
- Grup terdiversifikasi harus menggunakan SOTP, dan **secara eksplisit membahas diskon "bau industrial" (industrial conglomerate discount) dan katalis spin-off**.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Laporan keuangan dan pengumuman pesanan**: 10-K/10-Q, pengungkapan segmen, rincian pesanan dan backlog, catatan contract asset/liability. Perusahaan pertahanan juga melihat dokumen anggaran (DoD budget request AS, white paper pertahanan masing-masing negara).
2. **Data makro/mezo**: PMI (terutama **sub-indeks pesanan baru manufaktur**), output industri, pesanan barang modal inti (Census M3 AS), utilisasi kapasitas.
3. **Statistik asosiasi industri**: data pengiriman dan pesanan dari asosiasi mesin perkakas, asosiasi robotika (IFR), asosiasi peralatan listrik.
4. **Database tender dan proyek, pesanan pameran udara (airshow)**: verifikasi sumber pesanan perusahaan siklus panjang.
5. **Proxy frekuensi tinggi**: data bulanan distributor (seperti Fastenal), survei saluran, sebagai proxy leading untuk permintaan siklus pendek, perlu diverifikasi silang.

### Mekanisme Kewajaran

- **Definisi backlog harus dicantumkan**: apakah termasuk pesanan intensi, apakah bisa dibatalkan, apakah termasuk batch opsional, apakah termasuk kontrak yang belum berlaku. **Perubahan definisi backlog adalah teknik pemolesan yang umum**.
- **Pesanan dan pendapatan harus dipisahkan**: pertumbuhan pesanan tidak sama dengan pertumbuhan pendapatan, perlu dijelaskan siklus konversi dan tingkat pembatalan.
- **Peringatan POC (percentage of completion)**: pengakuan laba perusahaan project-based bergantung pada estimasi progres. **Lonjakan margin yang tiba-tiba harus diverifikasi dengan arus kas**.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "pemulihan pesanan" harus dikaitkan dengan book-to-bill, inventori saluran, dan capex pelanggan akhir, bukan hanya mengutip narasi manajemen.
- **Bedakan restocking dan permintaan riil**: rebound pesanan perusahaan siklus pendek sering kali adalah restocking saluran, perlu diverifikasi dengan data konsumsi terminal.
- **Hindari survivorship bias**: peer set harus mencakup perusahaan di titik rendah siklus dan sejenis yang sudah kehilangan keunggulan teknologi.

## 3. Pohon Penggerak Nilai Industrial

Nilai perusahaan industrial dapat diurai menjadi:

```text
Enterprise Value =
  pendapatan alat/mesin baru × penyesuaian posisi siklus
  + pendapatan jasa/after-market × basis instalasi × attach rate × margin jasa
  + pendapatan terlihat dari konversi backlog siklus panjang
  × margin mid-cycle
  × efisiensi modal (ROIC vs WACC)
  ÷ discount rate risiko
  − risiko eksekusi proyek (over-budget, klaim, penalti)
  − kesalahan alokasi modal siklikal (ekspansi di puncak)
  − goodwill M&A dan erosi integrasi
```

Laporan minimal harus menjawab:

- Posisi siklus saat ini di mana? Margin berada di persentil berapa dalam rentang 10 tahun?
- Bagaimana kualitas pesanan/backlog? Berapa porsi yang bisa dibatalkan? Berapa lama siklus konversi ke pendapatan?
- Berapa porsi jasa dan after-market terhadap pendapatan dan laba? Apakah disubsidi silang oleh bisnis alat?
- Apakah pengakuan POC bisnis project-based sepadan dengan penerimaan kas? Apakah contract asset tumbuh abnormal?
- Apakah M&A mendilusi ROIC? Berapa rasio goodwill terhadap aset bersih?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Tipe | Jebakan Umum |
|---|---|---|---|
| Orders / pertumbuhan pesanan | Pesanan baru yang ditandatangani | Semua tipe | **Mendahului pendapatan, adalah sinyal pertama** |
| Book-to-bill | Pesanan / pengiriman | Siklus panjang, otomasi | Lebih besar dari 1 berarti akumulasi backlog |
| Backlog | Pesanan di tangan | Siklus panjang, project-based | **Definisi bisa mencakup intensi; bagian yang bisa dibatalkan harus dipisah tersendiri** |
| Tahun cakupan backlog | backlog / pendapatan tahunan | Siklus panjang, pertahanan | Menentukan visibilitas pendapatan dan panjang periode eksplisit DCF |
| Inventori saluran | Level inventori distributor | Siklus pendek | **Restocking sering disalahartikan sebagai permintaan terminal** |
| Utilisasi kapasitas | Output aktual / kapasitas | Semua tipe | Mempengaruhi operating leverage dan daya tawar harga |
| Basis instalasi | Jumlah alat yang beroperasi | Bisnis dengan after-market | Basis bagi pendapatan jasa |
| Porsi jasa | Pendapatan jasa / total pendapatan | Semua tipe | Porsi jasa tinggi seharusnya mendapat premium kualitas |
| Attach rate jasa | Pendapatan jasa / basis instalasi | Bisnis dengan after-market | Mencerminkan loyalitas pelanggan dan daya tawar harga |
| Tingkat perpanjangan | Rasio perpanjangan kontrak jasa | Bisnis dengan after-market | Penurunan adalah sinyal awal intensifikasi kompetisi |
| Progres POC | Pengakuan percentage of completion | Project-based, pertahanan | **Lonjakan margin tiba-tiba perlu verifikasi arus kas** |
| Contract asset/liability | Pendapatan belum ditagih / uang muka diterima | Project-based | **Lonjakan contract asset adalah red flag** |
| Klaim dan sengketa | Nominal klaim yang belum selesai | Jasa konstruksi teknik | Sering baru terbuka saat litigasi |
| Porsi kontrak harga fixed | Harga fixed vs cost-plus | Pertahanan | Kontrak harga fixed menanggung risiko cost overrun |
| Margin mid-cycle | Margin operasi rata-rata 10 tahun | Semua tipe | **Jangkar valuasi, bukan margin periode berjalan** |
| Persentil rentang margin | Posisi margin saat ini dalam rentang 10 tahun | Semua tipe | Alat inti untuk positioning siklus |
| ROIC | Return on invested capital | Semua tipe | Perlu diperiksa apakah terdilusi setelah M&A |
| Goodwill / aset bersih | Akumulasi M&A | Grup terdiversifikasi | Goodwill tinggi dibarengi ROIC rendah adalah sinyal penghancuran nilai |
| Frekuensi biaya restrukturisasi | Frekuensi munculnya biaya "one-time" | Semua tipe | Jika terjadi setiap tahun berarti bukan one-time |

8 indikator yang wajib diungkap duluan: pesanan dan book-to-bill, backlog beserta kualitasnya, inventori saluran, porsi pendapatan jasa dan attach rate, persentil margin saat ini dalam rentang 10 tahun, perubahan contract asset, ROIC, porsi goodwill.

## 5. Struktur Model Keuangan

### Model Pendapatan

Pilih penggerak berdasarkan tipe siklus:

1. **Siklus pendek**: `permintaan terminal (proxy PMI/output industri) × pangsa × harga`, ditambah penyesuaian restocking/destocking inventori saluran.
2. **Siklus panjang**: `backlog awal periode + pesanan baru − pengakuan pengiriman − pembatalan = backlog akhir periode`, pendapatan dikonversi dari backlog sesuai irama pengiriman.
3. **Jasa/after-market**: `basis instalasi × attach rate × pendapatan jasa per unit`, basis instalasi terakumulasi dari penjualan alat baru dan berkurang sesuai tingkat decommission.
4. **Project-based**: dimodelkan per proyek dengan kurva POC, nilai kontrak, anggaran biaya, dan klaim; irama penerimaan kas dipisah tersendiri.
5. **Pertahanan**: dimodelkan berdasarkan siklus hidup proyek senjata (R&D→produksi awal rate rendah→produksi massal→jasa), bedakan kontrak harga fixed dan cost-plus.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, harus mencantumkan asumsi siklus secara eksplisit (fase siklus saat ini, kapan mencapai puncak/dasar).
- Pendapatan alat dan jasa harus dipisah, masing-masing diberi margin.
- Pertumbuhan organik dan M&A dipisah tersendiri; jika tidak bisa dipisah tulis "pemisahan tidak diperoleh" dan turunkan tingkat keyakinan.

### Model Biaya, Margin, dan Modal

- **Rentang margin**: bangun rentang margin operasi 10 tahun (tertinggi, terendah, median), cantumkan posisi saat ini. Ini adalah alat inti untuk positioning siklus.
- **Operating leverage**: sensitivitas transmisi volume, harga, dan biaya. Perubahan margin kotor QoQ perusahaan siklus pendek adalah **pembacaan langsung dari transmisi volume-harga dan biaya**.
- **Margin jasa**: harus diungkap atau diestimasi tersendiri. Jika margin jasa digunakan untuk subsidi silang kerugian bisnis alat, perlu direstorasi profitabilitas riil bisnis alat.
- **Biaya proyek**: risiko cost overrun kontrak harga fixed harus dimodelkan, terutama untuk unit pertama, teknologi baru, dan kontrak jangka panjang.
- **Modal kerja**: perubahan contract asset, inventori, dan uang muka diterima akan mempengaruhi arus kas secara signifikan. **Contract asset (pendapatan belum ditagih) yang terus tumbuh lebih cepat dari pendapatan adalah red flag besar**.
- **M&A dan goodwill**: periksa kontribusi ROIC dari M&A historis, risiko impairment goodwill, dan biaya integrasi.

### Batasan Asumsi Steady State

- **Dilarang menggunakan margin puncak sebagai asumsi perpetual**. Nilai terminal harus menggunakan margin mid-cycle.
- Jika pesanan menurun, inventori saluran tinggi, utilisasi kapasitas menurun, tidak boleh sekaligus memberi pertumbuhan tinggi dan margin tinggi.
- Tingkat konversi backlog perusahaan siklus panjang harus dikurangi rata-rata tingkat pembatalan historis, tidak boleh dikonversi 100%.
- Pertumbuhan pendapatan jasa dibatasi oleh pertumbuhan basis instalasi, tidak boleh lebih tinggi dari pertumbuhan penjualan alat baru dalam jangka panjang.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **Laba mid-cycle × multiple median**: disiplin inti saham industrial. **Dilarang laba puncak × multiple puncak** — ini adalah kesalahan fatal paling umum dalam valuasi saham siklikal. Gunakan rentang margin 10 tahun untuk positioning siklus saat ini.
2. **Reverse DCF**: dari harga saat ini, dibalik untuk mendapatkan implied margin mid-cycle, tingkat pertumbuhan, dan ROIC.
3. **Multiple utama EV/EBITDA**: perbedaan struktur modal perusahaan industrial besar, basis EV lebih bisa dibandingkan dari P/E.
4. **SOTP**: grup terdiversifikasi harus valuasi per segmen, bisnis jasa/after-market diberi multiple lebih tinggi tersendiri.

### Opsional

- **EPV**: berlaku untuk target industrial yang matang, stabil, dan bertumbuh rendah.
- **Diskonto backlog**: perusahaan pertahanan/kontrak jangka panjang bisa menggunakan tahun cakupan backlog untuk menghitung visibilitas pendapatan, periode eksplisit DCF bisa diperpanjang sesuai.
- **Nilai spin-off**: grup terdiversifikasi menghitung secara eksplisit selisih antara total nilai bagian-bagian setelah spin-off dan kapitalisasi pasar saat ini (diskon konglomerat).

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Panjang siklus: siklus pendek, siklus panjang, project-based, tidak boleh dicampur.
- Porsi jasa: median valuasi porsi after-market tinggi dan penjualan alat murni berbeda signifikan.
- Pasar terminal: siklus aerospace, energi, otomotif, konstruksi, peralatan semikonduktor tidak sinkron.
- Kandungan teknologi: tingkat otomasi/software menentukan batas atas margin.
- Struktur modal dan strategi M&A: dominan pertumbuhan organik vs didorong M&A.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi panjang siklus atau porsi jasa jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

**Laporan keuangan harus melihat pesanan sebelum pendapatan**: perubahan marginal orders/book-to-bill adalah sinyal pertama.

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pesanan, pendapatan, margin, EPS, dan guidance relatif terhadap konsensus? |
| Pesanan | Bagaimana perubahan marginal pertumbuhan pesanan dan book-to-bill? Bagaimana divergensi per pasar terminal dan regional? |
| Backlog | Apakah kualitas backlog berubah? Bagaimana tingkat pembatalan? Apakah definisinya disesuaikan? |
| Inventori saluran | Apakah rebound pesanan perusahaan siklus pendek adalah restocking atau permintaan terminal? |
| Margin kotor QoQ | Berapa kontribusi masing-masing dari volume, harga, transmisi biaya? (Pembacaan langsung untuk perusahaan siklus pendek) |
| Jasa | Apakah pertumbuhan pendapatan jasa dan attach rate membaik? Bagaimana tingkat perpanjangan? |
| Eksekusi proyek | Apakah progres POC normal? Ada cost overrun, klaim, atau penalti? |
| Contract asset | Apakah contract asset tumbuh lebih cepat dari pendapatan? Apakah penerimaan kas lagging? |
| Positioning siklus | Apakah posisi margin saat ini dalam rentang 10 tahun berubah? |
| Guidance | Apakah guidance pesanan, pendapatan, margin mengubah penilaian siklus? |
| Earnings call | Apakah nada bicara tentang visibilitas permintaan, capex pelanggan, lingkungan pricing, transmisi biaya melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan titik balik pesanan, perbaikan margin, puncak siklus, atau katalis spin-off? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 7% tapi sektor industrial naik 4% di hari yang sama, reaksi spesifik perusahaan sekitar +3%.

## 8. Moat & Penilaian Kompetitif

Inti moat industrial adalah **basis instalasi dan biaya peralihan (switching cost)**, bukan sekadar teknologi. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Basis instalasi dan after-market | Basis instalasi besar membawa pendapatan jasa attach rate tinggi, margin signifikan lebih tinggi dari alat baru | Porsi jasa rendah, atau jasa diambil pihak ketiga |
| Sertifikasi dan lock-in spesifikasi | Produk tercantum dalam spesifikasi pelanggan atau standar industri, peralihan perlu sertifikasi ulang | Komponen umum, bisa langsung diganti |
| Teknologi dan paten | Teknologi inti membentuk gap kinerja dan tercermin sebagai premium harga | Gap teknologi menyempit, kompetisi harga intensif |
| Jaringan distribusi | Jaringan distribusi dan jasa dengan cakupan luas dan respons cepat | Bergantung pada distribusi pihak ketiga, tanpa akses terminal |
| Skala dan biaya | Skala membawa keunggulan biaya procurement dan manufaktur | Skala tidak cukup atau utilisasi kapasitas rendah secara kronis |
| Kedalaman relasi pelanggan | Co-development, masuk ke roadmap produk pelanggan | Pricing melalui tender, tanpa relasi jangka panjang |
| Track record eksekusi proyek | Riwayat proyek besar sesuai budget dan jadwal | Sering over-budget, tertunda, dan klaim |
| Alokasi modal | M&A terus meningkatkan ROIC, tanpa impairment goodwill | M&A menumpuk goodwill tapi ROIC terdilusi |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "unggul teknologi", tapi margin mid-cycle tidak lebih tinggi dari sejenis dan ROIC terus menurun, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- **Contract asset (pendapatan belum ditagih) melonjak**, dan pertumbuhannya signifikan lebih cepat dari pendapatan.
- Margin kotor proyek POC melonjak tiba-tiba, tapi arus kas operasi tidak membaik seiring.
- Sering mencatat "biaya restrukturisasi", dan terjadi setiap tahun.
- Definisi backlog diubah (misalnya memasukkan pesanan intensi atau batch opsional) tanpa restatement historis.
- Pesanan naik tapi guidance capex pelanggan terminal justru direvisi turun — mungkin restocking saluran atau pesanan dini.
- Akuisisi terus menumpuk goodwill, sekaligus ROIC terdilusi.
- Margin jasa abnormal tinggi, mungkin sedang mensubsidi silang kerugian bisnis alat.
- Porsi kontrak harga fixed naik tapi inflasi biaya belum tercermin dalam pricing.
- Piutang usaha dan inventori sama-sama tumbuh lebih cepat dari pendapatan.
- Ekspansi besar-besaran atau M&A harga tinggi di puncak siklus.

### Daftar Bukti Sanggahan

Setiap laporan industrial minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Book-to-bill di bawah 1 selama N kuartal berturut-turut.
- Pesanan turun YoY melebihi besaran tertentu, atau tingkat pembatalan backlog melebihi ambang.
- Margin operasi jatuh di bawah persentil tertentu dalam rentang 10 tahun.
- Rasio contract asset / pendapatan melebihi level historis tertentu.
- Pertumbuhan pendapatan jasa atau tingkat perpanjangan jatuh di bawah ambang.
- ROIC di bawah WACC dan M&A terus berlanjut.

### Kesalahpahaman Umum

- **Menggunakan laba puncak dikali multiple puncak** — kesalahan nomor satu dalam valuasi saham siklikal. P/E rendah di puncak siklus seringkali paling berbahaya.
- Menganggap restocking saluran sebagai pemulihan permintaan terminal, menyebabkan tidak siap menghadapi siklus destocking.
- Menganggap backlog sebagai pendapatan yang sudah terkunci, mengabaikan klausul pembatalan dan siklus konversi.
- Menganggap laba yang diakui POC sudah terealisasi, mengabaikan verifikasi arus kas.
- Menganggap margin keseluruhan grup sebagai profitabilitas riil per segmen, mengabaikan subsidi silang jasa terhadap alat.
- Menganggap pertumbuhan pendapatan yang didorong M&A sebagai perbaikan operasional, mengabaikan dilusi ROIC.
- Menggunakan P/E tunggal untuk grup terdiversifikasi, mengabaikan perbedaan kualitas segmen dan diskon konglomerat.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan industrial selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Peta Positioning Siklus (Wajib)

| Indikator | Terendah 10 Tahun | Median 10 Tahun | Tertinggi 10 Tahun | Nilai Saat Ini | Posisi Persentil |
|---|---:|---:|---:|---:|---:|
| Margin operasi | | | | | |
| Pertumbuhan pendapatan | | | | | |
| Utilisasi kapasitas | | | | | |
| ROIC | | | | | |

### Tabel Tiga Garis Pesanan / Pendapatan / Laba (Wajib)

| Kuartal | Pesanan | YoY | Book-to-bill | Pendapatan | YoY | Margin Operasi |
|---|---:|---:|---:|---:|---:|---:|

### Tabel Kualitas Backlog

| Item | Nominal | Porsi | Keterangan |
|---|---:|---:|---|
| Total backlog | | | |
| Di antaranya: bagian yang bisa dibatalkan | | | |
| Di antaranya: batch intensi/opsional | | | |
| Tahun cakupan | | | |
| Rata-rata tingkat pembatalan historis | | | |

### Tabel Jasa dan After-Market

| Indikator | Nilai Terbaru | YoY | Posisi vs Sejenis | Sumber |
|---|---:|---:|---|---|
| Basis instalasi | | | | |
| Porsi pendapatan jasa | | | | |
| Attach rate jasa | | | | |
| Margin jasa | | | | |
| Tingkat perpanjangan | | | | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Pertumbuhan pendapatan mid-cycle | | | | |
| Margin operasi mid-cycle | | | | |
| Jalur porsi jasa | | | | |
| EV/EBITDA median | | | | |
| ROIC vs WACC | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: margin perusahaan ini saat ini berada di persentil ke-X dalam rentang 10 tahun; menggunakan margin mid-cycle bukan margin periode berjalan untuk valuasi, nilai implisitnya adalah ……"
- "Pesanan dan book-to-bill menunjukkan siklus sedang berada di fase ……; jika ini adalah restocking bukan permintaan terminal, proyeksi pendapatan perlu diturunkan ……"
- "Jika salah satu indikator inti berikut — book-to-bill / pesanan / persentil margin / contract asset / perpanjangan jasa — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
