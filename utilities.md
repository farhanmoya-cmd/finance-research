# Lampiran Riset Mendalam Industri Utilitas

Berlaku untuk listrik/gas/air teregulasi, perusahaan holding utilitas, independent power producer, dan infrastruktur listrik dengan kontrak jangka panjang. Pisahkan dulu rate base teregulasi, pembangkit listrik kompetitif, proyek development, dan bisnis non-utilitas; keempatnya memiliki risiko, mekanisme return, dan metode valuasi yang sama sekali berbeda, tidak boleh dicampur menggunakan satu set multiple yang sama.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Utilitas
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- **Identifikasi dulu sifat regulasinya**: return bisnis teregulasi ditentukan keputusan regulasi, pembangkit listrik kompetitif ditentukan harga listrik pasar. Menerapkan valuasi rate-base ke pembangkit listrik merchant adalah kesalahan fundamental.
- Garis utama nilai utilitas adalah **pertumbuhan rate base × return yang benar-benar diperoleh**, bukan pertumbuhan pendapatan. Pertumbuhan pendapatan yang tidak membawa ekspansi rate base dan pemulihan tepat waktu tidak menciptakan nilai.
- **"Allowed rate of return" tidak sama dengan earned ROE aktual**; **aset regulasi tidak otomatis bisa direcovery**. Harus membaca teks asli keputusan final rate case.
- Capex tinggi tidak sama dengan nilai per saham tinggi. Jika capex dibiayai dengan penerbitan ekuitas, pertumbuhan per saham akan tergerus oleh dilusi.
- Cuaca adalah faktor gangguan besar, semua perbandingan beban dan laba harus dinormalisasi cuaca.
- Keterjangkauan (customer bill/affordability) adalah batasan politik. Kenaikan tagihan yang terlalu cepat akan membatasi ruang kenaikan tarif masa depan, ini adalah plafon implisit return jangka panjang.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Keputusan dan pengajuan regulasi**: keputusan Public Utility Commission (PUC/PSC) negara bagian/nasional, pengajuan FERC. AS menggunakan FERC eLibrary/Data (Form 1, 2, 3-Q, 714, EQR), dokumen rate case PUC negara bagian. Ini adalah satu-satunya sumber yang bisa mengonfirmasi allowed ROE, equity layer, alokasi biaya, dan mekanisme pemulihan.
2. **Pengungkapan statutori dan keuangan perusahaan**: 10-K/10-Q, laporan akuntansi regulasi, presentasi rencana modal.
3. **Data sistem dan industri**: data pembangkitan/beban/bahan bakar/harga ritel listrik EIA, asesmen reliabilitas NERC, kapasitas dan clearing price dari system operator (ISO/RTO).
4. **Pasar lain**: menggunakan teks asli lembaga regulasi energi lokal, system operator, dan dokumen lisensi.
5. **Database profesional dan sell-side**: hanya sebagai pelengkap, tidak boleh menggantikan teks asli rate case.

### Mekanisme Kewajaran

- **Wajib membaca keputusan final rate case**: alokasi biaya, regulatory lag, klausul penyesuaian bahan bakar, insentif dan penalti kinerja semua ada di keputusan tersebut, ringkasan dan press release tidak cukup.
- **Allowed vs earned harus disandingkan**: hanya menulis allowed ROE tidak lengkap. Harus memberikan earned ROE aktual dan alasan gap-nya (lag, over-budget, cuaca, biaya yang tidak bisa direcovery).
- **Pengungkapan per jurisdiksi**: nilai rata-rata grup multi-jurisdiksi akan menutupi jurisdiksi yang lemah. Harus mendaftar rate base, allowed ROE, dan lingkungan regulasi per jurisdiksi.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "beban data center akan mendorong pertumbuhan" harus dikaitkan dengan posisi antrian interkoneksi, kontrak yang sudah ditandatangani, kredit pelanggan, dan titik waktu — bukan hanya mengutip letter of intent.
- **Bedakan basis akuntansi**: GAAP EPS, adjusted EPS, dan laba akuntansi regulasi adalah tiga set angka berbeda, perbandingan lintas periode harus konsisten.
- **Hindari survivorship bias**: peer set harus mencakup perusahaan di jurisdiksi dengan lingkungan regulasi ramah dan tidak ramah.

## 3. Pohon Penggerak Nilai Utilitas

Nilai utilitas teregulasi dapat diurai menjadi:

```text
Kebutuhan pendapatan regulasi ≈ biaya operasional + depresiasi + pajak + rate base yang disetujui × allowed return

Pertumbuhan nilai per saham =
  tingkat pertumbuhan rate base
  × return yang benar-benar diperoleh (earned ROE)
  × ketepatan waktu pemulihan (1 − kerugian regulatory lag)
  − dilusi pendanaan ekuitas
  − over-budget proyek dan bagian yang tidak bisa direcovery
  − sanksi regulasi dan batasan keterjangkauan
```

Laporan minimal harus menjawab:

- Apakah rencana pertumbuhan rate base sudah disetujui regulasi? Atau hanya rencana perusahaan?
- Berapa besar gap antara earned ROE dan allowed ROE? Apakah gap tersebut struktural atau siklikal?
- Apa struktur pendanaan rencana modal? Berapa persentase penerbitan saham akan mendilusi EPS per saham?
- Di mana posisi pertumbuhan tagihan pelanggan relatif terhadap inflasi dan pertumbuhan pendapatan? Apakah keterjangkauan sudah menjadi isu politik?
- Siapa yang menanggung risiko over-budget dan keterlambatan proyek besar (nuklir, transmisi, angin lepas pantai)?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Kegunaan Riset | Jebakan Umum |
|---|---|---|---|
| Rate base | Aset bersih yang disetujui dimasukkan ke dalam return | Basis pertumbuhan nilai | Basis berbeda antar jurisdiksi, perlu dipisah per jurisdiksi |
| Tingkat pertumbuhan rate base | Rate base YoY | Penggerak utama pertumbuhan EPS jangka panjang | Perlu dibedakan yang sudah disetujui dan yang masih direncanakan |
| Allowed ROE | Return on equity yang disetujui regulasi | Batas atas teoretis | **Tidak sama dengan return yang benar-benar diperoleh** |
| Earned ROE | Return on equity aktual | Kapabilitas laba riil | Jika terus-menerus lebih rendah dari allowed menunjukkan masalah struktural |
| Equity layer | Porsi ekuitas yang diakui regulasi | Menentukan basis return ekuitas | Struktur modal aktual bisa berbeda dari asumsi regulasi |
| Regulatory lag | Lag waktu dari biaya terjadi sampai dipulihkan melalui tarif | Sumber erosi return | Di periode inflasi tinggi, kerugian lag signifikan membesar |
| Customer bill | Tagihan rata-rata per rumah tangga | Keterjangkauan dan risiko politik | Kenaikan tagihan terlalu cepat akan membatasi kenaikan tarif masa depan |
| Weather-normalized load | Beban yang dinormalisasi cuaca | Tren permintaan riil | Perbandingan beban yang belum dinormalisasi tidak bermakna |
| Sales / load growth | Pertumbuhan penjualan listrik | Penggerak permintaan | Perlu diurai data center, elektrifikasi, populasi, dan cuaca |
| SAIDI / SAIFI | Durasi/frekuensi pemadaman | Reliabilitas | Reliabilitas buruk bisa memicu penalti kinerja |
| Capacity factor | Utilisasi unit pembangkit | Efisiensi aset pembangkit | Teknologi berbeda tidak bisa dibandingkan langsung |
| Heat rate | Heat rate | Efisiensi pembangkit termal | Menentukan biaya bahan bakar dan prioritas dispatch |
| Capex | Belanja modal | Sumber pertumbuhan rate base | Perlu diurai maintenance, reliabilitas, pertumbuhan, dan proyek lingkungan |
| CWIP | Construction work in progress | Rate base masa depan | Apakah dimasukkan ke rate base mempengaruhi titik waktu arus kas |
| AFUDC | Kapitalisasi biaya modal masa konstruksi | Komposisi laba akuntansi | **AFUDC mendongkrak laba tapi tidak menghasilkan kas** |
| FFO / Debt | Arus kas operasi / utang | Indikator inti rating | Downgrade rating akan mendongkrak biaya modal |
| Interest coverage | Rasio coverage bunga | Kapabilitas bayar utang | Tertekan signifikan saat suku bunga naik |
| Merchant exposure | Porsi pembangkitan yang belum terkontrak | Risiko fluktuasi harga listrik | Harus dinilai terpisah dari bisnis teregulasi |
| Cakupan PPA / hedge | Porsi volume listrik yang sudah terkunci | Visibilitas arus kas | Risiko harga saat kontrak ditandatangani ulang setelah jatuh tempo |
| Liabilitas decommissioning dan lingkungan | Decommissioning nuklir, abu batu bara, provisi wildfire | Liabilitas implisit | Provisi tidak memadai adalah risiko besar |

8 indikator yang wajib diungkap duluan: rate base dan pertumbuhan per jurisdiksi, allowed vs earned ROE, regulatory lag, rencana modal dan struktur pendanaan, beban yang dinormalisasi cuaca, pertumbuhan tagihan pelanggan, FFO/Debt, rasio coverage dividen.

## 5. Struktur Model Keuangan

### Model Pendapatan dan Rate Base

Dimodelkan per jurisdiksi secara terpisah, **nilai rata-rata grup akan menutupi jurisdiksi yang lemah**:

1. Setiap jurisdiksi membangun: rate base, capex, depresiasi, allowed ROE, equity layer, dan regulatory lag.
2. Rencana modal dipisah menjadi maintenance, reliabilitas, transmisi-distribusi, pembangkitan, kepatuhan lingkungan, dan proyek pertumbuhan.
3. **Catat per proyek**: status persetujuan regulasi, anggaran, jumlah yang sudah diinvestasikan, perkiraan titik waktu operasi, dan mekanisme pemulihan.
4. Pembangkitan kompetitif dimodelkan terpisah: kapasitas × utilisasi × (harga listrik − biaya bahan bakar − biaya variabel), termasuk cakupan PPA/hedge dan eksposur spot.
5. Proyeksi beban dipisah: data center, elektrifikasi (EV/heat pump), pertumbuhan populasi/ekonomi, cuaca, dan kerugian efisiensi energi.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, termasuk jadwal rate case per jurisdiksi dan ekspektasi hasilnya.
- Dampak cuaca harus dinormalisasi, dan kontribusi cuaca terhadap EPS dipisah tersendiri.
- **Beban data center/elektrifikasi harus diverifikasi**: posisi antrian interkoneksi, kontrak yang sudah ditandatangani, titik waktu interkoneksi, progres konstruksi, dan kredit pelanggan. Beban yang hanya berupa letter of intent tidak boleh dimasukkan ke skenario basis.

### Model Pendanaan, Modal, dan Liabilitas

- **Model pendanaan harus terkait**: penerbitan utang, suku bunga, ambang rating (FFO/Debt), penerbitan ekuitas, dan kebijakan dividen. **Pertumbuhan capex tinggi tidak sama dengan nilai per saham tinggi** — jika pendanaan dominan dari penerbitan saham, pertumbuhan per saham akan tergerus dilusi.
- **AFUDC dan aset regulasi**: bunga yang dikapitalisasi masa konstruksi mendongkrak EPS akuntansi tapi tidak menghasilkan kas. Harus dirinci tersendiri, dan jelaskan titik waktu konversi ke kas.
- **Tekanan rating**: saat FFO/Debt mendekati ambang downgrade, perusahaan sering terpaksa menerbitkan saham atau memotong capex, keduanya merusak nilai per saham.
- **Liabilitas lingkungan dan decommissioning**: provisi decommissioning nuklir, pembuangan abu batu bara, pembayaran wildfire harus diperiksa kecukupan provisi dan mekanisme pemulihan.
- **Coverage dividen**: dividen / arus kas operasi dikurangi maintenance capex, menilai apakah dividen didukung kas operasi atau bergantung pendanaan.

### Batasan Asumsi Steady State

- Earned ROE jangka panjang tidak boleh diasumsikan terus lebih tinggi dari allowed ROE; jurisdiksi yang terus-menerus di bawah allowed harus dicerminkan di model.
- Jika pertumbuhan tagihan pelanggan terus lebih tinggi dari pertumbuhan pendapatan penduduk, ruang kenaikan tarif masa depan harus diturunkan.
- Probabilitas over-budget proyek besar dan risiko tidak bisa direcovery harus masuk ke skenario bear, tidak boleh diasumsikan recovery penuh.
- Pembangkitan kompetitif tidak boleh menggunakan logika rate-base untuk perpetual, harus menggunakan harga listrik ekuilibrium jangka panjang dan harga kapasitas.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **Discounted dividend / DCF**: bisnis teregulasi digerakkan oleh pertumbuhan rate-base, allowed/earned ROE, struktur modal, dan dilusi pendanaan.
2. **Cross-check P/B dan earned ROE**: `P/B wajar ≈ (earned ROE − g) / (COE − g)`, cross-check dengan P/E.
3. **SOTP**: grup terintegrasi harus menilai terpisah bisnis teregulasi, pembangkitan kompetitif, development renewable, dan aset non-core.
4. **Valuasi terbalik**: menjawab pertumbuhan rate-base, earned ROE, P/E terminal, dan skala pendanaan ekuitas yang terimplikasi harga saat ini.

### Opsional

- **P/E ternormalisasi**: laba setelah dinormalisasi cuaca dan faktor satu kali.
- **Nilai reposisi aset**: pembangkitan kompetitif bisa menggunakan biaya reposisi atau nilai kapasitas sebagai cross-check.
- **NPV proyek renewable**: pipeline development dijumlahkan berdasarkan NPV per proyek, perlu dikurangi tingkat kegagalan development.

**Dividend yield tidak bisa menggantikan analisis nilai intrinsik** — dividend yield tinggi bisa mencerminkan pertumbuhan yang stagnan atau dividen yang tidak berkelanjutan.

Harus dilakukan sensitivitas untuk variabel berikut: suku bunga, spread kredit, allowed ROE, besaran over-budget proyek, dan durasi regulatory lag.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Sifat regulasi: murni teregulasi, campuran, dominan pembangkitan kompetitif.
- Kualitas jurisdiksi: keramahan lingkungan regulasi, hasil rate case historis, tingkat lag.
- Tipe bisnis: intensitas modal dan jalur pertumbuhan listrik, gas, air berbeda.
- Fase pertumbuhan: fase pertumbuhan capex tinggi vs cash cow matang pertumbuhan rendah.
- Status balance sheet: level FFO/Debt dan rating.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi sifat regulasi atau kualitas jurisdiksi jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

Setelah laporan keuangan wajib membangun: **bridge EPS** (cuaca, tarif, rate base, pendanaan, satu kali), **bridge rencana modal**, **milestone proyek**, **progres kasus regulasi**, **beban dan tagihan pelanggan**, **FFO/Debt dan coverage dividen**.

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih EPS, beban, capex, dan guidance relatif terhadap konsensus? |
| Bridge EPS | Pertumbuhan berasal dari kenaikan tarif, pertumbuhan rate base, cuaca, kontrol biaya, atau item satu kali? |
| Normalisasi cuaca | Bagaimana laba riil dan tren beban setelah dikeluarkan cuaca? |
| Kasus regulasi | Progres rate case yang sedang berjalan, rencana settlement, ekspektasi titik waktu dan hasil keputusan? |
| Earned vs allowed | Mengapa ROE aktual menyimpang dari allowed? Karena lag, over-budget, atau biaya yang tidak bisa direcovery? |
| Rencana modal | Apakah capex direvisi naik? Apakah bagian yang direvisi sudah disetujui regulasi? |
| Progres proyek | Apakah proyek besar tertunda atau over-budget? Siapa yang menanggung? |
| Beban | Apakah beban data center/elektrifikasi bersifat kontraktual atau hanya intensi? Titik waktu interkoneksi? |
| Pendanaan | Apakah perlu penerbitan saham baru? Berapa besar dilusi? Apakah indikator rating tertekan? |
| Keterjangkauan | Apakah pertumbuhan tagihan pelanggan dan sentimen politik memburuk? |
| Earnings call | Apakah nada bicara tentang lingkungan regulasi, pemulihan proyek, rencana pendanaan melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan suku bunga, hasil rate case, pertumbuhan beban, atau dilusi pendanaan? |

Harus dibedakan **GAAP EPS, adjusted EPS, dan laba akuntansi regulasi** — perbedaan ketiganya sering menunjukkan di mana masalahnya berada.

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 5% tapi indeks utilitas naik 3% di hari yang sama, reaksi spesifik perusahaan sekitar +2%.

## 8. Moat & Penilaian Kompetitif

Utilitas adalah monopoli alami yang teregulasi, moat berasal dari **hak konsesi dan relasi regulasi**, bukan kompetisi pasar. Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Konsesi wilayah layanan | Wilayah layanan eksklusif, tanpa kompetisi masuk | Ada tekanan municipalization atau kompetisi ritel |
| Kualitas lingkungan regulasi | Hasil rate case historis baik, lag pendek, ada forward test year | Sering dipotong, lag panjang, intervensi politik kuat |
| Ekonomi wilayah layanan | Pertumbuhan populasi/beban, kredit pelanggan baik, keterjangkauan memadai | Populasi menyusut, rasio tagihan terhadap pendapatan tinggi |
| Mekanisme pemulihan | Klausul penyesuaian otomatis bahan bakar/modal, CWIP dimasukkan ke rate base | Harus mengajukan per kasus, recovery tidak pasti |
| Kapabilitas eksekusi modal | Riwayat proyek besar sesuai budget dan jadwal | Proyek berulang kali over-budget dan tertunda |
| Ketahanan balance sheet | Rating memadai, biaya pendanaan lebih rendah dari sejenis | Mendekati ambang downgrade, bergantung pendanaan ekuitas |
| Positioning transisi energi | Capex transisi bisa mendapat dukungan regulasi dan dimasukkan ke rate base | Risiko stranded asset tinggi, mekanisme recovery biaya decommissioning tidak jelas |

Penilaian kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "lingkungan regulasi ramah", tapi earned ROE terus lebih rendah dari allowed melebihi 150bp, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- Rencana capex direvisi naik tapi persetujuan regulasi lagging, investasi mendahului kepastian pemulihan.
- Earned ROE terus-menerus signifikan lebih rendah dari allowed ROE, dan manajemen tidak memiliki jalur perbaikan yang jelas.
- AFUDC dan aset regulasi mendorong kenaikan laba akuntansi, tapi arus kas operasi justru memburuk bersamaan.
- Pertumbuhan dividen bergantung pada penerbitan saham berkelanjutan, bukan arus kas operasi.
- Pertumbuhan tagihan pelanggan signifikan lebih tinggi dari inflasi dan pertumbuhan pendapatan penduduk.
- Proyek besar (nuklir, angin lepas pantai, transmisi) berulang kali tertunda dan over-budget.
- FFO/Debt mendekati ambang downgrade rating tapi rencana modal belum disesuaikan.
- Provisi liabilitas wildfire, lingkungan, decommissioning nuklir tidak memadai atau mekanisme pemulihan tidak jelas.
- Beban data center hanya berupa kesepakatan intensi, tanpa kontrak interkoneksi, titik waktu, dan dukungan kredit pelanggan.
- Sering menggunakan "adjusted EPS" untuk mengeluarkan item yang terjadi berulang.

### Daftar Bukti Sanggahan

Setiap laporan utilitas minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Earned ROE lebih rendah dari allowed ROE melebihi bp tertentu dan berlanjut N kuartal.
- Hasil keputusan rate case utama di bawah nilai pengajuan melebihi persentase tertentu.
- Proyek besar over-budget melebihi persentase tertentu dari anggaran, atau tertunda melebihi durasi tertentu.
- FFO/Debt jatuh di bawah ambang downgrade lembaga rating.
- Skala pendanaan ekuitas tahunan melebihi nominal tertentu, dilusi melebihi persentase tertentu.
- Pertumbuhan tagihan pelanggan YoY melebihi ambang tertentu, memicu reaksi balik regulasi atau politik.

### Kesalahpahaman Umum

- **Menganggap allowed ROE sebagai return aktual**, mengabaikan gap akibat lag dan biaya yang tidak bisa direcovery.
- Menganggap capex tinggi sebagai pertumbuhan tinggi, mengabaikan bahwa nilai per saham bisa justru menurun setelah dilusi pendanaan ekuitas.
- Menganggap laba akuntansi yang didorong AFUDC sebagai laba riil, mengabaikan tidak adanya aliran kas masuk.
- Menggunakan dividend yield tinggi untuk menilai undervaluasi, mengabaikan keberlanjutan dividen dan stagnasi pertumbuhan.
- Menganggap intensi beban data center sebagai permintaan yang sudah terkunci.
- Menganggap allowed ROE rata-rata grup sebagai kondisi seluruh jurisdiksi, mengabaikan tarikan dari jurisdiksi yang lemah.
- Menerapkan multiple stabil bisnis teregulasi ke pembangkitan merchant.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan utilitas selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Peta Regulasi Jurisdiksi

| Jurisdiksi | Rate Base | Porsi | Allowed ROE | Earned ROE | Equity Layer | Regulatory Lag | Rate Case Berikutnya |
|---|---:|---:|---:|---:|---:|---|---|

### Bridge Rate-Base / ROE

| Item | Awal Periode | Perubahan | Akhir Periode | Keterangan |
|---|---:|---|---:|---|
| Rate base | | capex − depresiasi + lainnya | | |
| Earned ROE | | lag / over-budget / cuaca / biaya | | |
| EPS | | tarif / rate base / pendanaan / cuaca / satu kali | | |

### Jadwal Proyek Modal

| Proyek | Anggaran | Sudah Diinvestasikan | Status Persetujuan Regulasi | Titik Waktu Operasi | Mekanisme Pemulihan | Risiko Over-Budget |
|---|---:|---:|---|---|---|---|

### Tabel Beban, Tarif, dan Pendanaan

| Indikator | Nilai Terbaru | YoY | Tren | Sumber & Basis |
|---|---:|---:|---|---|
| Beban yang dinormalisasi cuaca | | | | |
| Beban data center/elektrifikasi (yang sudah dikontrak) | | | | |
| Tagihan rata-rata per rumah tangga dan pertumbuhannya | | | | |
| FFO / Debt dan rating | | | | |
| Pendanaan ekuitas tahunan dan dilusi | | | | |
| Rasio coverage dividen | | | | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Tingkat pertumbuhan rate base | | | | |
| Earned ROE | | | | |
| Dilusi ekuitas tahunan | | | | |
| Cost of equity (COE) | | | | |
| P/E atau P/B terminal | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada EPS periode ini, melainkan apakah rate base dapat bertumbuh X% dalam N tahun ke depan, sekaligus earned ROE dijaga di Y% dan dilusi ekuitas tidak melebihi Z%."
- "Pertumbuhan rate-base dan earned ROE yang terimplikasi harga saham saat ini adalah ……; dibandingkan dengan hasil keputusan historis masing-masing jurisdiksi perusahaan ini, implikasi ini wajar/agresif/konservatif."
- "Jika salah satu indikator inti berikut — earned ROE / over-budget proyek / regulatory lag / FFO-Debt / dilusi / tagihan pelanggan — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
</content>
