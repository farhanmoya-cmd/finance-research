# Lampiran Riset Mendalam Industri Asuransi

Berlaku untuk asuransi umum (property & casualty), asuransi jiwa, asuransi kesehatan, reasuransi, pialang asuransi, dan grup asuransi terintegrasi. Pisahkan dulu berdasarkan jenis asuransi; risiko underwriting, durasi aset-liabilitas, dan rezim modal berbeda-beda, tidak bisa menilai kualitas hanya dengan "pertumbuhan premi" saja. Jika grup juga memiliki bisnis manajemen aset atau perbankan dalam skala besar, pisahkan dulu laba dan okupansi modal per segmen, baru gunakan lampiran ini hanya untuk bagian asuransi.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Asuransi
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- Pastikan dulu struktur jenis asuransi: model ekonomi asuransi umum, asuransi jiwa/annuitas, asuransi kesehatan, reasuransi, dan pialang sama sekali berbeda, **tidak boleh menggunakan satu set KPI atau multiple valuasi yang sama**.
- Inti riset asuransi bukan pertumbuhan premi, melainkan **apakah underwriting menguntungkan, apakah cadangan (reserve) memadai, apakah modal bisa didistribusikan**. Pertumbuhan premi saat pricing kurang memadai adalah penghancuran nilai.
- Bedakan laba underwriting dan hasil investasi. Model yang menutup kerugian underwriting dengan sisi investasi akan gagal bersamaan ketika suku bunga turun atau terjadi credit event.
- Perbedaan basis akuntansi sangat besar: IFRS 17 dan US GAAP (LDTI), laporan statutori dan laporan grup, EV (embedded value) dan nilai buku. Jembatani dulu sebelum membandingkan lintas pasar.
- Semua kesimpulan "perbaikan laba" harus menjawab dulu: berasal dari underwriting periode berjalan, pelepasan cadangan tahun-tahun sebelumnya (prior-year reserve release), hasil investasi, atau perubahan asumsi aktuaria?
- Cadangan adalah estimasi, bukan fakta. Setiap penilaian kualitas laba harus dibangun berdasarkan triangle perkembangan cadangan (reserve development triangle).

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Laporan regulasi statutori dan laporan solvabilitas**: AS menggunakan statutory statements regulasi negara bagian/NAIC, RBC dan IRIS; Uni Eropa menggunakan SFCR/Solvency II; Tiongkok menggunakan laporan dari NFRA (Badan Pengawas Keuangan Nasional) dan laporan solvabilitas perusahaan; Hong Kong menggunakan HKIA. Digunakan untuk mengonfirmasi modal statutori, kecukupan cadangan, dan kemampuan distribusinya.
2. **Laporan akuntansi perusahaan dan pengungkapan aktuaria**: laporan tahunan, laporan EV, tabel rolling CSM, triangle perkembangan cadangan, analisis sensitivitas.
3. **Data regulasi dan industri**: statistik premi industri, pengajuan pengawasan tarif, informasi publik dari lembaga model bencana (seperti RMS/Verisk), estimasi kerugian industri.
4. **Transkrip earnings call**: melacak perubahan nada manajemen tentang siklus tarif, kecukupan cadangan, anggaran bencana (catastrophe budget), biaya reasuransi, dan return modal.
5. **Pengungkapan sejenis & pihak ketiga**: digunakan untuk membangun peer set dan rentang kewajaran; riset sell-side hanya sebagai pelengkap, tidak boleh menggantikan pengungkapan primer.

**RBC / rasio kecukupan solvabilitas adalah alat intervensi regulasi, bukan indikator ranking lintas perusahaan secara independen** — nilai di bawah rezim modal berbeda tidak dapat dibandingkan langsung.

### Mekanisme Kewajaran

- **Basis diutamakan**: apakah combined ratio termasuk bencana, apakah termasuk prior-year development, apakah net atau gross, berbeda antar perusahaan. Saat pertama kali muncul, cantumkan definisinya; jika tidak diungkap, tulis "definisi perusahaan tidak diperoleh".
- **Pemisahan periode berjalan dan tahun-tahun sebelumnya**: laba underwriting harus diurai menjadi current accident year (tahun kejadian berjalan) dan prior-year development (perkembangan cadangan tahun sebelumnya). Hanya melihat combined ratio total akan sangat menyesatkan.
- **Underwriting dan investasi disandingkan**: setiap kesimpulan "ROE membaik" harus sekaligus menjelaskan kontribusi margin underwriting, imbal hasil investasi, dan leverage modal.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "siklus pricing membaik" harus dikaitkan dengan rate change, retention, loss ratio bisnis baru — bukan hanya mengutip narasi manajemen.
- **Hindari survivorship bias**: peer set harus mencakup sejenis dengan disiplin underwriting yang baik, yang tertekan siklus, dan yang pernah mengalami masalah cadangan.
- **Bedakan siklus dan struktural**: perbaikan combined ratio bisa jadi siklus hard market, bisa juga peningkatan kapabilitas seleksi risiko. Harus dinilai dengan tarif, eksposur, tren kerugian, dan perbandingan sejenis.

## 3. Pohon Penggerak Nilai Asuransi

Nilai intrinsik asuransi dapat diurai menjadi:

```text
Nilai Ekuitas =
  net asset ternormalisasi (P&C) atau embedded value EV (asuransi jiwa)
  + nilai bisnis baru masa depan (VNB × pertumbuhan dan persistensi)
  × profitabilitas underwriting (combined ratio lintas siklus atau MLR)
  × skala float dan keunggulan biaya
  × return portofolio investasi yang disesuaikan risiko
  × efisiensi modal dan kemampuan distribusi
  − risiko kekurangan cadangan (tail risk)
  − eksposur bencana dan konsentrasi
  − batasan modal regulasi dan risiko perubahan asumsi
```

Laporan minimal harus menjawab:

- Apakah underwriting bisa profit secara independen (combined ratio < 100 atau MLR berkelanjutan)? Atau bergantung pada subsidi sisi investasi?
- Apakah biaya float positif atau negatif? Apakah skalanya dapat tumbuh seiring bisnis?
- Apakah perkembangan cadangan terus menguntungkan, netral, atau tidak menguntungkan? Apakah pelepasan yang menguntungkan selama bertahun-tahun sudah menguras buffer?
- Apakah peningkatan hasil investasi diperoleh dengan menurunkan kualitas kredit (credit downgrade), mismatch durasi, atau mengorbankan likuiditas?
- Dapatkah modal di level grup dipindahkan ke holding company dan benar-benar didistribusikan ke pemegang saham?

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Berlaku untuk Jenis | Jebakan Umum |
|---|---|---|---|
| GWP / NWP | Premi tertulis bruto/neto | P&C, Reasuransi | Selisih gross-net mencerminkan ketergantungan pada reasuransi, perlu dipisah |
| Earned premium | Premi yang sudah diakui (earned) | P&C, Kesehatan | Lag dengan premi tertulis dapat mendistorsi rasio di periode pertumbuhan |
| Loss ratio | Klaim / premi earned | P&C, Reasuransi | Perlu diurai antara current accident year dan prior-year development |
| Expense ratio | Biaya / premi earned | P&C, Reasuransi | Komisi dan biaya administrasi perlu dipisah |
| Combined ratio | loss ratio + expense ratio | P&C, Reasuransi | **Di bawah 100 baru berarti profit underwriting**; nilai rendah mungkin dari pelepasan cadangan tahun lalu |
| Prior-year development | Penyesuaian cadangan tahun-tahun sebelumnya | P&C, Reasuransi | Pelepasan menguntungkan berturut-turut bisa menguras buffer masa depan |
| Cat loss ratio | Kerugian bencana / premi earned | P&C, Reasuransi | Tidak ada bencana dalam satu tahun tidak berarti berkelanjutan, perlu dinormalisasi dengan rata-rata multi-tahun |
| Rate change | Perubahan tarif saat perpanjangan | P&C, Reasuransi | Sering tertukar dengan exposure growth, kesalahan umum |
| Retention | Tingkat perpanjangan (retensi) | P&C, Pialang | Retensi tinggi jika dicapai dengan menurunkan harga adalah sinyal negatif |
| APE | Annualized premium equivalent | Asuransi Jiwa | Indikator skala penjualan, bukan setara dengan nilai |
| VNB / NBV | Value of new business | Asuransi Jiwa | Sangat bergantung pada asumsi (discount rate, lapse, mortalitas) |
| VNB margin | VNB / APE | Asuransi Jiwa | Dipengaruhi besar oleh perubahan struktur produk |
| CSM | Contractual service margin (IFRS 17) | Asuransi Jiwa | Perubahan asumsi dapat mendongkrak CSM tanpa perbaikan arus kas riil |
| EV | Embedded value | Asuransi Jiwa | Harus diaudit asumsi dan sensitivitasnya, EV yang tidak diaudit kredibilitasnya rendah |
| Lapse / surrender rate | Tingkat lapse/penarikan polis | Asuransi Jiwa | Lonjakan surrender saat suku bunga naik memaksa realisasi aset |
| Spread | Imbal hasil investasi − biaya garansi | Asuransi Jiwa, Annuitas | Tingkat bunga garansi adalah liabilitas rigid, spread bisa menjadi negatif |
| Membership | Jumlah anggota tertanggung | Asuransi Kesehatan | Struktur anggota (komersial/pemerintah) memiliki margin sangat berbeda |
| MLR | Klaim medis / premi | Asuransi Kesehatan | Dipengaruhi penyesuaian risiko, musiman, dan kebijakan |
| Organic growth | Pertumbuhan pendapatan tanpa M&A | Pialang | Pertumbuhan yang didorong M&A harus direstorasi tersendiri |
| FCF conversion | FCF / EBITDA | Pialang | EBITDA yang disesuaikan sering mengeluarkan biaya recurring |
| Rasio kecukupan solvabilitas | Modal statutori / persyaratan minimum | Semua jenis | Basis grup dan entitas statutori berbeda, transferabilitas harus dinilai tersendiri |
| ROE / ROTCE | Laba bersih / ekuitas | Semua jenis | Perlu dinormalisasi untuk bencana dan perkembangan cadangan |

8 indikator yang wajib diungkap duluan (dipilih sesuai jenis asuransi): combined ratio (dipisah periode berjalan vs tahun sebelumnya), rate change, perkembangan cadangan, kerugian bencana, VNB/CSM (asuransi jiwa), MLR (kesehatan), struktur dan durasi portofolio investasi, rasio kecukupan solvabilitas.

## 5. Struktur Model Keuangan

### Model Underwriting dan Pendapatan

Pilih penggerak berdasarkan jenis asuransi:

1. **P&C**: `unit eksposur × tarif = premi tertulis` → premi earned → diurai loss ratio current accident year dan prior-year development → ditambah expense ratio → combined ratio.
2. **Asuransi jiwa**: `APE × VNB margin = VNB`; stok menggunakan tabel rolling CSM (penambahan, pelepasan, perubahan asumsi, akresi bunga) dan analisis perubahan EV.
3. **Asuransi kesehatan**: `jumlah anggota × premi per kapita = pendapatan premi`; sisi biaya menggunakan `tren biaya medis × utilisasi × harga per unit`.
4. **Reasuransi**: dimodelkan berdasarkan jenis kontrak (proporsional/excess of loss), termasuk limit, attachment point, klausul reinstatement, dan siklus pricing perpanjangan.
5. **Pialang**: `tarif komisi × premi yang diasuransikan + pendapatan fee`, pisahkan pertumbuhan organik dan M&A.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, kerugian bencana menggunakan rata-rata multi-tahun bukan nilai aktual periode berjalan.
- P&C harus membuat triangle accident year/underwriting year, dekomposisi frekuensi/severitas, perkembangan cadangan, dan recoverable reasuransi; bedakan underwriting periode berjalan dan pelepasan tahun sebelumnya.
- Asuransi jiwa harus membuat pencocokan durasi aset-liabilitas, tingkat bunga garansi, spread, lapse, dan imbal hasil reinvestasi; periksa dampak perubahan standar akuntansi (LDTI/IFRS 17).

### Model Investasi, Cadangan, dan Modal

- **Portofolio investasi**: diurai berdasarkan rating kredit, durasi, likuiditas, properti komersial/aset alternatif, dan unrealized gain/loss. **Peningkatan imbal hasil mungkin diperoleh dengan menurunkan kualitas kredit atau mengorbankan likuiditas**, harus dinilai tersendiri.
- **Pencocokan durasi**: liabilitas asuransi jiwa berdurasi panjang, gap aset-liabilitas langsung berdampak pada nilai ekonomi saat suku bunga berubah. Gap harus dikuantifikasi.
- **Kecukupan cadangan**: gunakan triangle perkembangan untuk menilai arah dan besaran bias estimasi cadangan historis; perkembangan menguntungkan yang berturut-turut perlu diwaspadai habisnya buffer.
- **Reasuransi**: periksa konsentrasi lawan transaksi, pengaturan kolateral, klausul kontrak, limit/attachment point, dan tren harga perpanjangan. Kenaikan biaya reasuransi langsung menekan laba yang diretensi neto.
- **Bridge modal**: diurai menjadi laba operasi, perubahan pasar, perubahan model/regulasi, dividen buyback, dan M&A; sekaligus lihat transferabilitas modal antara grup dan entitas statutori.

### Batasan Asumsi Steady State

- P&C berkualitas bisa menjaga combined ratio di bawah 100 dalam jangka panjang, tetapi harus didukung seleksi risiko, disiplin pricing, dan efisiensi biaya, tidak bisa bergantung pada pelepasan cadangan tahun sebelumnya terus-menerus.
- Jika perkembangan cadangan terus tidak menguntungkan, eksposur bencana naik, biaya reasuransi memburuk, tidak boleh sekaligus memberi combined ratio rendah, pertumbuhan tinggi, dan dividen tinggi.
- Jika pertumbuhan VNB tinggi asuransi jiwa bergantung pada asumsi agresif (discount rate tinggi, lapse rate rendah), harus dilakukan sensitivitas dan turunkan tingkat keyakinan.
- Asumsi imbal hasil investasi tidak boleh lebih tinggi dari imbal hasil reinvestasi portofolio saat ini plus spread yang wajar, dan harus konsisten dengan eksposur risiko kredit.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **P&C: P/B atau P/TBV terhadap ROE ternormalisasi**, ditambah discounted dividend/residual income. Kerugian bencana dan pelepasan cadangan harus dinormalisasi lintas siklus.
2. **Asuransi jiwa: P/EV dan multiple VNB**. `Nilai ekuitas ≈ EV ternormalisasi + VNB × multiple bisnis baru`. Harus diaudit asumsi EV, sensitivitas, cost of capital, dan kas yang dapat didistribusikan.
3. **Asuransi kesehatan: P/E atau P/FCF ternormalisasi** + tiga skenario anggota/tarif/biaya medis.
4. **Valuasi terbalik**: minimal menurunkan combined ratio, ROE ternormalisasi, pertumbuhan VNB, atau medical cost trend yang terimplikasi harga saat ini, untuk menjawab "apa yang sudah di-price in pasar".

### Opsional

- **SOTP**: digunakan jika grup asuransi terintegrasi memiliki P&C, asuransi jiwa, kesehatan, dan manajemen aset sekaligus, masing-masing segmen diberi okupansi modal dan multiple berbeda.
- **Pialang: EV/EBITDA atau EV/FCF** dapat digunakan (pialang adalah jasa ringan modal, tidak menanggung risiko underwriting), tetapi M&A, kompensasi berbasis saham, dan leverage harus direstorasi.
- **Nilai likuidasi/net asset yang disesuaikan**: saat diskon parah, gunakan net asset yang disesuaikan (dikurangi defisit cadangan, unrealized loss investasi, dan goodwill) untuk menetapkan batas bawah.

**Tidak bisa otomatis menyamakan diskon nilai buku dengan undervaluasi** — jika ROE ternormalisasi di bawah cost of equity, diskon tersebut wajar.

### Aturan Peer Set

Pilih 5-10 perusahaan pembanding, dan cantumkan alasan pemilihannya:

- Struktur jenis asuransi: P&C komersial, P&C personal, asuransi jiwa, kesehatan, reasuransi, pialang, tidak boleh dicampur.
- Risk appetite: ketidakpastian cadangan asuransi long-tail (liability, workers comp) dan short-tail (mobil, properti) sangat berbeda.
- Geografi dan regulasi: rezim modal yang berlaku (Solvency II / RBC / C-ROSS), intensitas pengawasan tarif, regional eksposur bencana.
- Posisi siklus: fase hard market/soft market, tarif naik/turun.
- Status modal: tingkat surplus solvabilitas dan kapabilitas return modal.

Item yang dikecualikan harus dijelaskan: jika suatu perusahaan tampak sejenis tapi struktur jenis asuransi, karakteristik durasi, atau rezim modal jelas berbeda, tidak boleh dipaksakan masuk ke tabel multiple yang sama.

## 7. Fokus Pola Laporan Keuangan

Mode laporan keuangan harus menjawab "apa yang berubah dari laporan ini", bukan hanya mendaftar beat/miss.

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih premi, combined ratio, hasil investasi, EPS, EV/VNB relatif terhadap konsensus dan guidance? |
| Bridge laba underwriting | Berapa kontribusi masing-masing dari loss ratio current accident year dan prior-year reserve development? Setelah dikurangi pelepasan, apakah underwriting masih profit? |
| Bridge volume-harga premi | Pertumbuhan berasal dari tarif, kenaikan eksposur, pelanggan baru, atau M&A? Apakah tarif mencakup tren kerugian? |
| Bencana dan normalisasi | Posisi kerugian bencana periode ini relatif terhadap anggaran tahunan dan rata-rata multi-tahun? |
| Cadangan | Apakah triangle perkembangan menunjukkan accident year tertentu terus memburuk? Apakah manajemen menyesuaikan asumsi? |
| Khusus asuransi jiwa | Apakah perubahan VNB, CSM, EV berasal dari bisnis baru, perubahan asumsi, volatilitas pasar, atau deviasi operasional? |
| Khusus asuransi kesehatan | Apakah perubahan MLR berasal dari utilisasi, harga per unit, penyesuaian risiko, atau struktur anggota? |
| Investasi | Apakah peningkatan imbal hasil dibarengi penurunan kualitas kredit, perpanjangan durasi, atau penurunan likuiditas? Seberapa besar perubahan unrealized gain/loss? |
| Modal | Apakah perubahan solvabilitas didorong operasi, pasar, atau model? Dapatkah entitas statutori memindahkan dividen ke atas? |
| Guidance | Apakah guidance combined ratio, anggaran bencana, pertumbuhan VNB, atau return modal mengubah model jangka panjang? |
| Earnings call | Apakah nada bicara tentang siklus tarif, kecukupan cadangan, biaya reasuransi, intensitas kompetisi melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan siklus tarif, risiko cadangan, hasil investasi, atau return modal? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika saham naik 7% tapi indeks saham asuransi naik 4% di hari yang sama, reaksi spesifik perusahaan sekitar +3%.

## 8. Moat & Penilaian Kompetitif

Asuransi adalah industri komoditas homogen, moat tidak bisa hanya ditulis "merek bagus". Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Disiplin underwriting | Secara proaktif mengurangi premi saat soft market, combined ratio lintas siklus terus lebih baik dari sejenis | Tetap mengejar pertumbuhan pangsa pasar saat market soft |
| Data dan kapabilitas pricing | Data dan model pricing eksklusif membuat loss ratio risiko sejenis terus lebih rendah | Pricing bergantung pada tabel tarif industri, tidak ada diferensiasi |
| Kontrol distribusi | Penjualan langsung, agen eksklusif, atau embedding mendalam di saluran, biaya akuisisi pelanggan rendah dan stabil | Bergantung pada pialang pihak ketiga, daya tawar lemah |
| Biaya float | Biaya float negatif atau sangat rendah dalam jangka panjang, dan skalanya bisa bertumbuh | Biaya float lebih tinggi dari suku bunga bebas risiko |
| Skala dan daya tawar reasuransi | Skala membawa keunggulan biaya reasuransi dan keunggulan expense ratio | Skala besar tapi expense ratio tidak lebih baik dari sejenis |
| Seleksi risiko | Memiliki keunggulan informasi di segmen tertentu (asuransi spesialis) | Menjual semua jenis asuransi tapi tidak unggul di satu segmen pun |
| Ketahanan modal | Masih bisa melakukan ekspansi underwriting setelah bencana/credit event (kapabilitas kontrasiklikal) | Terpaksa menyusut atau menerbitkan saham baru setelah kejadian |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "disiplin underwriting unggul", tapi loss ratio current accident year lebih tinggi dari sejenis, laba dijaga dengan pelepasan cadangan tahun sebelumnya, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- Perkembangan cadangan terus tidak menguntungkan, terutama terkonsentrasi di jenis asuransi long-tail (liability, workers comp, malpraktik medis).
- Pertumbuhan premi signifikan lebih cepat dari pertumbuhan modal dan perbaikan pricing, mengindikasikan pelonggaran underwriting.
- Combined ratio di bawah 100 tapi sepenuhnya bergantung pada pelepasan cadangan tahun sebelumnya, current accident year sebenarnya merugi.
- Porsi aset berimbal hasil tinggi/tidak likuid/alternatif dalam portofolio investasi naik cepat.
- Lapse rate dan biaya garansi asuransi jiwa naik bersamaan, terutama saat suku bunga naik cepat.
- Biaya reasuransi naik, attachment point dinaikkan, atau limit diperketat, tetapi perusahaan belum menyesuaikan pricing atau retensi.
- Rasio modal grup sehat tapi modal entitas statutori tidak bisa didistribusikan (trapped capital).
- Sering menyesuaikan asumsi aktuaria, dan arahnya selalu menguntungkan laba periode berjalan.
- Pengungkapan model bencana dan eksposur klimat tidak memadai, atau belum diperbarui ke versi model bencana terbaru.
- MLR asuransi kesehatan terus naik tapi pengajuan kenaikan tarif dibatasi regulasi.

### Daftar Bukti Sanggahan

Setiap laporan asuransi minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- Combined ratio current accident year (setelah dikeluarkan perkembangan tahun sebelumnya) menembus ambang tertentu.
- Perkembangan cadangan berubah dari menguntungkan ke tidak menguntungkan, atau accident year tertentu memburuk N periode berturut-turut.
- Lapse rate / MLR melebihi ambang.
- Rasio kecukupan solvabilitas jatuh di bawah rentang target manajemen.
- Unrealized loss portofolio investasi melebihi persentase tertentu dari ekuitas.
- Kenaikan biaya reasuransi melebihi kenaikan tarif.

### Kesalahpahaman Umum

- Menganggap combined ratio rendah sebagai kapabilitas underwriting yang kuat, mengabaikan kontribusi pelepasan cadangan tahun sebelumnya di dalamnya.
- Menganggap laba tinggi dari satu tahun tanpa bencana sebagai berkelanjutan, tanpa normalisasi multi-tahun.
- Menganggap pertumbuhan premi tinggi sebagai perbaikan operasional, mengabaikan kemungkinan itu adalah perebutan pangsa pasar saat soft market.
- Menganggap pertumbuhan EV atau CSM sebagai penciptaan nilai, mengabaikan kontribusi perubahan asumsi.
- Menganggap imbal hasil investasi tinggi sebagai kapabilitas, mengabaikan risiko penurunan kualitas kredit dan durasi.
- Menganggap diskon nilai buku sebagai undervaluasi, mengabaikan bahwa ROE ternormalisasi di bawah cost of equity.
- Menganggap kecukupan solvabilitas grup sebagai dapat diperoleh pemegang saham, mengabaikan batasan transfer modal entitas statutori.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perusahaan asuransi selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel KPI Asuransi (dipilih sesuai jenis asuransi)

| Indikator | Nilai Terbaru | YoY/QoQ | Tren 8 Kuartal Terakhir | Posisi vs Sejenis | Sumber & Basis |
|---|---:|---:|---|---|---|
| Pertumbuhan premi (tarif vs eksposur) | | | | | |
| Combined ratio (dipisah periode berjalan/tahun sebelumnya) | | | | | |
| Kerugian bencana (vs rata-rata multi-tahun) | | | | | |
| Perkembangan cadangan | | | | | |
| VNB / CSM / EV (asuransi jiwa) | | | | | |
| MLR / anggota (asuransi kesehatan) | | | | | |
| Imbal hasil investasi dan struktur portofolio | | | | | |
| Rasio kecukupan solvabilitas | | | | | |
| ROE ternormalisasi | | | | | |

### Bridge Cadangan dan Modal

| Item | Awal Periode | Komponen Perubahan | Akhir Periode | Sumber |
|---|---:|---|---:|---|
| Saldo cadangan | | Provisi baru / perkembangan tahun sebelumnya / klaim | | |
| CSM (asuransi jiwa) | | Bisnis baru / pelepasan / perubahan asumsi / bunga | | |
| Modal solvabilitas | | Laba operasi / perubahan pasar / perubahan model / dividen | | |
| Unrealized gain/loss portofolio investasi | | Suku bunga / spread kredit / ekuitas | | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| Combined ratio atau MLR ternormalisasi | | | | |
| ROE ternormalisasi | | | | |
| Rasio kerugian bencana (rata-rata multi-tahun) | | | | |
| Pertumbuhan VNB (asuransi jiwa) | | | | |
| Cost of equity (COE) | | | | |
| P/B atau P/EV wajar | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi perusahaan ini saat ini paling bergantung bukan pada laba periode ini, melainkan pada kapabilitas underwriting current year setelah dikeluarkan pelepasan cadangan tahun sebelumnya, serta apakah buffer cadangan memadai."
- "Jika salah satu indikator inti berikut — combined ratio / perkembangan cadangan / lapse rate atau MLR / solvabilitas — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
- "Combined ratio dan ROE ternormalisasi yang terimplikasi harga saham saat ini adalah ……; saya menilai implikasi ini wajar/agresif/konservatif, dengan alasan ……"
</content>
