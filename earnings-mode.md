# Mode Deep Dive Laporan Keuangan

Mode laporan keuangan (earnings mode) digunakan untuk hasil kuartalan/tahunan, 10-Q/10-K, earnings event, earnings call, update guidance, dan keputusan investasi pasca-laporan. Perlakukan laporan keuangan sebagai peristiwa untuk menguji ulang kualitas bisnis, tesis jangka panjang, dan valuasi — jangan menulisnya sebagai ringkasan berita atau daftar beat/miss.

## Daftar Isi

1. Mode dan status cakupan (coverage status)
2. Kedalaman riset minimum
3. Tingkatan sumber dan pengumpulan paralel
4. Protokol rekonsiliasi dan analisis
5. Pembaruan model dan valuasi
6. Template output sembilan bab
7. Ambang kualitas

## 1. Mode dan Status Cakupan

Tentukan dahulu status cakupan, dan jelaskan di bawah judul laporan:

- **Update coverage berkelanjutan**: sudah memperoleh versi laporan sebelumnya, proyeksi, JSON asumsi valuasi, atau tesis investasi yang jelas. Tampilkan item per item "nilai lama → nilai baru → alasan perubahan", simpan file lama.
- **Initiation of coverage dari laporan keuangan**: tidak memperoleh versi laporan atau model sebelumnya. Boleh langsung dieksekusi, tetapi harus membangun baseline historis, kompetitif, proyeksi, dan valuasi; tulis dengan jelas "ini adalah baseline initiation of coverage", jangan gunakan frasa seperti "dinaikkan/diturunkan" atau "tesis diperkuat/dilemahkan" yang mengimplikasikan adanya baseline lama.

Jangan menghentikan riset hanya untuk menentukan status cakupan. Periksa dahulu lampiran sesi, workspace saat ini, dan path yang sudah diberikan pengguna; jika tidak ditemukan, otomatis masuk ke mode initiation of coverage.

## 2. Kedalaman Riset Minimum

Kedua status cakupan wajib menyelesaikan tingkatan berikut:

- Bandingkan periode ini, periode sebelumnya, periode yang sama tahun lalu, guidance perusahaan, dan konsensus yang dapat diverifikasi dalam basis perhitungan yang sama.
- Uraikan pendapatan, harga/volume/mix, segmen, wilayah, pelanggan, atau KPI inti; jelaskan dari mana pertumbuhan berasal dan apakah dapat berlanjut.
- Rekonsiliasi GAAP dengan Non-GAAP, identifikasi stock-based compensation (SBC), restrukturisasi, amortisasi M&A, dampak kurs, tarif pajak, dan item one-off.
- Analisis margin kotor, margin operasi, incremental margin, dan operating leverage; jangan hanya mengulang angka net income.
- Analisis arus kas operasi, free cash flow (FCF), modal kerja, capex, posisi net cash/net debt, dan alokasi modal.
- Bandingkan guidance, nada bicara (tone), urutan prioritas risiko, dan fokus tanya-jawab manajemen antara periode ini dan periode sebelumnya.
- Hubungkan bukti dari laporan keuangan ke daya saing jangka panjang, tesis inti, proyeksi, valuasi, dan aksi investasi.

Continuing coverage minimal melihat kembali 4 kuartal; initiation of coverage minimal melihat kembali 3 tahun fiskal penuh dan 8 kuartal. Jika data memang tidak dapat diperoleh, persempit window dan jelaskan gap-nya, jangan mengisi angka dari memori model. Untuk industri seperti keuangan, asuransi, dan REIT, gantikan metrik FCF umum dengan metrik kunci khusus industrinya, tetapi dengan kedalaman yang setara.

## 3. Tingkatan Sumber dan Pengumpulan Paralel

Ambil data sesuai urutan berikut, dan untuk angka kunci yang sama usahakan cross-check dengan dua materi asli:

1. Pengajuan regulasi: 10-Q, 10-K, 8-K, 6-K, 20-F, atau dokumen asli dari platform pengungkapan resmi bursa.
2. Materi perusahaan: siaran pers laporan keuangan, tabel keuangan tambahan, presentasi investor, prepared remarks.
3. Rekaman asli earnings call atau transkrip yang dapat diandalkan: pisahkan pernyataan manajemen dan tanya-jawab analis.
4. Konsensus dan valuasi: data agregator atau laporan sell-side dengan basis statistik yang jelas dan timestamp sebelum laporan keuangan dipublikasikan.
5. Harga pasar dan media: harga pasca-laporan, volume, kinerja indeks/perusahaan sejenis, dan berita latar belakang.

Usahakan mengumpulkan empat jalur secara paralel:

- **Jalur pengungkapan**: pengajuan regulasi + siaran pers + materi presentasi.
- **Jalur ekspektasi**: konsensus sebelum laporan, guidance asli perusahaan, perbedaan pandangan utama sell-side.
- **Jalur komunikasi**: pernyataan earnings call, tanya-jawab, perubahan nada bicara, dan pertanyaan yang tidak terjawab.
- **Jalur pasar**: harga pre-market/after-hours, hari perdagangan penuh pertama, dan harga pada titik waktu laporan; indeks dan perusahaan sejenis inti pada hari yang sama sebagai pembanding.

Catat tanggal publikasi, periode cakupan, mata uang, GAAP/Non-GAAP, dan basis continuing operations/total untuk setiap materi. "Ekspektasi" yang diperbarui setelah laporan keuangan tidak boleh disamarkan sebagai konsensus sebelum laporan.

## 4. Protokol Rekonsiliasi dan Analisis

Samakan dahulu mata uang, tahun fiskal, kuartalan/kumulatif, ruang lingkup continuing operations, dan basis per saham. Jika nilai kuartalan hanya dapat diperoleh dari pengajuan kumulatif, hitung dengan "kumulatif periode ini − kumulatif periode sebelumnya", dan tandai sebagai nilai hasil kalkulasi; cek restatement, stock split, perubahan kebijakan akuntansi, divestasi M&A, dan dampak kurs. Jika tidak dapat disamakan secara andal, tampilkan berdampingan, jangan dipaksakan untuk dibandingkan.

Item kalkulasi minimum meliputi: selisih nominal dan persentase nilai aktual terhadap konsensus, selisih terhadap titik tengah guidance, perubahan basis poin margin YoY/QoQ, incremental operating margin, FCF margin, rasio konversi FCF/net income, SBC/pendapatan, dan perubahan diluted share count YoY. Hasil kalkulasi dicantumkan beserta field asli dan rumusnya; jika denominator mendekati nol atau basis perhitungan tidak konsisten, jangan dihitung.

### 4.1 Perbedaan Ekspektasi (Expectations Gap)

Untuk pendapatan, EPS, margin, dan KPI inti, hitung masing-masing: nilai aktual, guidance asli perusahaan, konsensus sebelum laporan, YoY, QoQ, dan selisihnya. Bedakan "melampaui ekspektasi rendah", "benar-benar beat ekspektasi", dan "beat berkualitas rendah".

Jika konsensus tidak diperoleh atau basis perhitungannya tidak dapat diverifikasi, tandai dengan jelas, gunakan guidance asli perusahaan, tren historis, dan kinerja perusahaan sejenis sebagai pembanding; jangan menggunakan proyeksi yang direvisi pasca-laporan untuk menambal kekosongan ini.

Jelaskan sumber perbedaan: demand akhir, market share, pricing, volume, product mix, kurs, M&A, pengakuan akuntansi, biaya, tarif pajak, atau buyback. Jangan otomatis menafsirkan EPS beat sebagai perbaikan operasional.

### 4.2 Pendapatan dan Kualitas Bisnis

Bangun jembatan pendapatan (revenue bridge) berdasarkan dimensi yang paling dapat menjelaskan substansi ekonomi: segmen, produk, wilayah, pelanggan, harga/volume/mix, atau subscription/retensi/order. Minimal jawab:

- Driver mana yang struktural, mana yang siklikal, one-off, atau sekadar timing akuntansi?
- Apakah pertumbuhan bergantung pada pelanggan tunggal, promosi, channel stuffing, M&A, atau bisnis margin rendah?
- Apakah order, backlog, deferred revenue, uang muka (prepayment), dan inventori konsisten dengan tren pendapatan?
- Apa makna bukti dari laporan keuangan ini bagi moat, bargaining power, dan posisi kompetitif?

### 4.3 Kualitas Laba dan Arus Kas

Bangun jembatan margin kotor dan margin operasi; hitung incremental operating margin jika data tersedia. Rekonsiliasi item per item untuk penyesuaian Non-GAAP, serta cantumkan secara terpisah SBC terhadap pendapatan, perubahan diluted share count, dan item "non-recurring" yang berulang.

Jembatani dari net income ke arus kas operasi dan free cash flow, jelaskan dampak piutang, inventori, utang usaha, contract liability, dan capex. Jika laba tumbuh tetapi konversi kas memburuk, ini wajib dinaikkan menjadi risiko inti, jangan disembunyikan di catatan kaki.

### 4.4 Guidance dan Sinyal Manajemen

Letakkan guidance lama, guidance baru, ekspektasi pasar, dan asumsi implisit dalam satu tabel. Bedakan perubahan demand, perubahan eksekusi, perubahan mekanis seperti kurs/tarif pajak, dan tingkat konservatisme manajemen.

Bandingkan earnings call periode ini dengan periode sebelumnya: nada bicara yang ditambahkan, dihapus, atau dilemahkan; perubahan urutan prioritas risiko; pertanyaan berulang dari analis; serta pertanyaan yang dihindari atau tidak dikuantifikasi oleh manajemen. Analisis nada bicara adalah penilaian (judgment), wajib disertai bukti asli dan hindari overinterpretasi.

### 4.5 Reaksi Pasar

Catat reaksi after-hours, hari perdagangan penuh pertama, dan reaksi kumulatif sampai titik waktu laporan; bandingkan dengan indeks utama, indeks industri, dan 2–4 perusahaan sejenis inti. Pecah perubahan harga menjadi faktor kinerja, guidance, ekspektasi valuasi, dan faktor pasar; jika tidak dapat diatribusikan secara ketat, tandai dengan jelas sebagai "penilaian saya".

Setelah laporan keuangan, wajib menjawab tiga pertanyaan, dan jawabannya ditulis kembali ke bab pertama:
1. Variabel apa yang paling mungkin diperdagangkan pasar dalam 1–3 bulan ke depan (pendapatan/order, margin, return capex, regulasi, buyback, mean reversion valuasi)?
2. Apakah reaksi harga saat ini lebih seperti sentimen sesaat, repricing valuasi, atau informasi baru yang belum sepenuhnya dipriced-in?
3. Sinyal pembuktian/penggugur (confirmation/disconfirmation signal) upside/downside mana yang akan memaksa saya mengubah aksi, bukan hanya mengubah kata-kata?

## 5. Pembaruan Model dan Valuasi

Ubah informasi baru menjadi asumsi yang dapat diaudit, jangan berhenti di "positif/negatif":

- Perbarui pendapatan, margin, EPS, FCF, dan KPI kunci untuk tahun fiskal ini dan minimal 2 tahun fiskal ke depan; cantumkan nilai lama, nilai baru, besaran perubahan, dan buktinya.
- Jika memiliki model lama, tampilkan jembatan perubahan fair value: pergeseran waktu, net cash/share count, proyeksi dekat, pertumbuhan/margin jangka panjang, WACC/nilai terminal, dan bobot metode.
- Jika tidak memiliki model lama, bangun proyeksi baseline berdasarkan historis dan guidance, dan jelaskan dengan jelas mana yang asumsi, mana yang guidance perusahaan atau konsensus pasar.
- Semua kalkulasi DCF/reverse DCF/scenario DCF/EPV menggunakan `scripts/dcf.py` dan JSON; jalankan sensitivitas dan pembobotan probabilitas tiga skenario.
- Tetap jalankan minimal tiga metode valuasi. Kombinasi yang umum adalah reverse DCF + DCF tiga skenario + relative valuation atau EPV/SOTP; pemilihan harus sesuai dengan model bisnis perusahaan.
- Probabilitas tiga skenario wajib diperbarui sesuai kekuatan bukti dari laporan keuangan. Jika laporan terbaru sudah mendukung skenario bull/bear (misalnya pertumbuhan tinggi dan margin yang naik bersamaan, order/RPO yang berakselerasi, guidance capex sudah memuncak, atau relief regulasi yang melampaui ekspektasi), skenario tersebut tidak boleh tetap diperlakukan sebagai tail risk, kecuali ada bukti sanggahan yang ditulis dengan jelas.
- Petakan undervalued/fairly valued/overvalued dan aksi sesuai Bagian 8 di `valuation-methods.md`. "Mengungguli ekspektasi" pada laporan keuangan itu sendiri tidak boleh mengalahkan disiplin valuasi atau veto governance.

Jika pengungkapan kunci tidak cukup untuk mendukung proyeksi, berikan rentang bersyarat dan variabel yang masih perlu diverifikasi, jangan membuat target harga yang seolah presisi.

## 6. Template Output Sembilan Bab

Judul dibuat sesuai bahasa laporan: untuk bahasa Indonesia gunakan `# Nama Perusahaan (Kode) Analisis Mendalam Laporan Keuangan FYxx Qx`; untuk bahasa Inggris gunakan `# Company (Ticker) FYxx Qx Earnings Deep Dive`. Subjudul menjelaskan tanggal publikasi, data cutoff, status cakupan, dan mata uang laporan; laporan berbahasa Inggris menggunakan field yang setara.

### I. Kesimpulan Lebih Dulu dan Snapshot Laporan Keuangan

Berikan penilaian satu kalimat, trikotomi keputusan (penilaian nilai intrinsik / arah perdagangan pasar 1–3 bulan ke depan / aksi investasi), perubahan positif-negatif inti, pembuktian upside dan penggugur downside. Gunakan tabel untuk menampilkan nilai aktual, ekspektasi, selisih, YoY/QoQ, guidance asli, dan sumber.

### II. Expectations Gap dan Kualitas Kinerja

Bedakan beat/miss untuk pendapatan, margin, EPS, KPI, dan arus kas; jelaskan sumber selisih, keberlanjutannya, dan apakah ambang ekspektasi benar-benar terlampaui.

### III. Pendapatan, Segmen, dan KPI Inti

Tampilkan tren historis, jembatan segmen/wilayah/pelanggan atau price-volume-mix. Jelaskan kualitas pertumbuhan, konsentrasi, order/backlog/retensi, dan implikasi kompetitifnya.

### IV. Margin, Biaya, dan Kualitas Laba

Tampilkan margin kotor, margin operasi, incremental margin, rasio biaya, jembatan GAAP/Non-GAAP, SBC, dan dilusi. Identifikasi item one-off dan yang didorong akuntansi.

### V. Arus Kas, Balance Sheet, dan Alokasi Modal

Tampilkan OCF, FCF, konversi kas, modal kerja, capex, net cash/debt, buyback, dividen, dan M&A; nilai apakah alokasi modal menciptakan value.

### VI. Guidance, Earnings Call, dan Sinyal Manajemen

Tampilkan jembatan guidance lama-baru, asumsi implisit, perubahan nada bicara, kontroversi tanya-jawab, dan kredibilitas manajemen. Daftar komitmen yang perlu diverifikasi pada periode berikutnya, dan untuk masing-masing tulis nilai baseline, rentang/arah proyeksi, indikator leading, kondisi penggugur, dan tanggal verifikasi yang jelas.

### VII. Kompetisi, Industri, dan Reaksi Pasar

Bandingkan kinerja periode ini dengan industri dan perusahaan sejenis inti; analisis market share, pricing power, posisi siklus, bukti moat, dan reaksi harga yang sudah disesuaikan faktor pasar.

### VIII. Model, Valuasi, dan Jembatan Perubahan Fair Value

Tampilkan update proyeksi, minimal tiga valuasi, reverse DCF, sensitivitas, dan hasil tiga skenario. Jika ada model lama, jelaskan perubahan fair value; jika tidak ada model lama, bangun baseline valuasi initiation of coverage.

### IX. Update Tesis Investasi dan Checklist Aksi

Untuk continuing coverage, review dahulu proyeksi yang sudah jatuh tempo dari versi sebelumnya: KPI operasional, jalur katalis, multiple valuasi, dan total return masing-masing ditandai hit/partial hit/miss/tidak dapat diverifikasi, jelaskan apakah karena data, timing, model, shock eksternal, atau kesalahan tesis, dan tulis kembali ke model; untuk initiation of coverage, daftar logika bull-bear baseline. Berikan kalibrasi kesimpulan, 3–5 indikator pemantauan untuk 1–2 kuartal ke depan, kondisi penggugur upside/downside, katalis, dan risiko. Jawab: "Jika ini adalah uang tunai hari ini, apakah saya akan membelinya? Mengapa?" Jika kekuatan bukti dari salah satu skenario kegagalan dalam argumen counter-case adalah menengah-kuat/kuat, wajib jelaskan apakah hal itu sudah mengubah probabilitas skenario, arah perdagangan pasar, atau tempo aksi.

Bagian akhir laporan dilengkapi daftar "sumber data dan timestamp" serta disclaimer.

Mode laporan keuangan berbahasa Inggris menggunakan urutan sembilan bab yang sama dengan judul berbahasa Inggris, menandai penilaian dengan `My view`, data yang hilang dengan `Not obtained`, dan daftar sumber dengan `Sources and timestamps`.

## 7. Ambang Kualitas

Sebelum penyerahan, pastikan:

- Apakah mencakup income statement, cash flow statement, balance sheet, dan metrik operasional kunci secara bersamaan?
- Apakah menjelaskan mengapa angka berubah, bukan hanya mendeskripsikan perubahannya?
- Apakah memisahkan ekspektasi sebelum laporan, guidance perusahaan, dan ekspektasi yang direvisi setelah laporan?
- Apakah sudah menyelesaikan rekonsiliasi GAAP/Non-GAAP, item one-off, SBC, dan dilusi?
- Apakah menghubungkan nada bicara earnings call, bukti kompetitif, dan reaksi pasar dengan tesis jangka panjang?
- Apakah memasukkan hasil laporan keuangan ke dalam model dan menyelesaikan minimal tiga valuasi, sensitivitas, skenario, dan kalibrasi kesimpulan?
- Apakah dengan jelas mengidentifikasi variabel yang paling mungkin diperdagangkan pasar dalam 1–3 bulan ke depan, dan membandingkan reaksi pasar dengan perusahaan sejenis/indeks utama?
- Apakah probabilitas skenario diperbarui sesuai kekuatan bukti laporan keuangan? Apakah bukti menengah-kuat/kuat sudah mengubah probabilitas, penilaian jalur, atau aksi?
- Jika ada coverage lama, apakah menyediakan jembatan perubahan yang lengkap? Jika tidak ada coverage lama, apakah baseline sudah dibangun tanpa memfabrikasi perubahan?
- Apakah mencantumkan semua sumber kunci dan timestamp, konflik, dan data yang tidak diperoleh?
- Apakah bahasa output sesuai dengan yang secara eksplisit ditentukan pengguna, atau default mengikuti bahasa komunikasi umum pengguna/Agent?
- Apakah proyeksi inti memiliki tanggal verifikasi? Apakah proyeksi yang jatuh tempo dari versi sebelumnya tetap menyimpan nilai asli dan menyelesaikan review per item serta atribusi error?

## 8. Pemeriksaan Kualitas Laporan Keuangan (Baru Ditambahkan, Wajib)

Setiap kali ada laporan keuangan, jalankan set pemeriksaan minimum sesuai `forensic-accounting.md`: rasio akrual dan konversi kas (kuartal ini + TTM), divergensi DSO/deferred revenue dengan pertumbuhan pendapatan, keberulangan (recurring) item penyesuaian Non-GAAP, perubahan tingkat provisi QoQ. Setiap item yang memburuk masuk ke badan Bab II "Kualitas Kinerja" bukan ke catatan kaki; grade kredibilitas laporan keuangan diungkapkan di tabel snapshot Bab I dan mengikuti aturan vetonya.
