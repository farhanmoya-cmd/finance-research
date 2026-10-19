# Lampiran Riset Mendalam Industri Perbankan

Berlaku untuk bank komersial, bank ritel, bank investasi/trading, bank regional, bank digital, dan perusahaan induk perbankan (bank holding company). Liabilitas bank adalah bahan baku operasional, tidak dapat diterapkan secara mekanis EV/EBITDA perusahaan industrial biasa atau FCF konvensional. Jika perusahaan juga memiliki bisnis asuransi, manajemen aset, atau pembiayaan konsumen non-bank dalam skala besar, pisahkan dulu laba dan okupansi modal per segmen, baru gunakan lampiran ini hanya untuk bagian perbankan.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai Perbankan
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- Pastikan dulu apakah ini benar-benar bank: pendapatan harus didominasi oleh spread kredit-deposit dan bisnis berlisensi perbankan. Institusi yang didominasi trading, manajemen aset, pembayaran, atau kredit konsumen harus menggunakan lampiran yang sesuai dan menangani okupansi modal secara terpisah.
- Inti riset perbankan bukan pertumbuhan laba, melainkan **apakah return on capital yang disesuaikan risiko dapat dipertahankan lintas siklus**. ROE tinggi yang berasal dari leverage tinggi, provisi rendah, atau underwriting agresif tidak membentuk nilai.
- Bedakan bank ritel, bank korporasi, bank regional, universal bank, bank investasi, dan bank digital. Struktur deposit, sensitivitas terhadap siklus kredit, struktur fee, dan median valuasi sangat berbeda.
- Basis akuntansi dan basis regulasi harus dijembatani. Logika provisi IFRS 9 tiga tahap berbeda dengan CECL Amerika Serikat, jelaskan perbedaannya sebelum membandingkan lintas pasar.
- Semua kesimpulan kualitas aset harus dibangun berdasarkan **bukti migrasi** (overdue→watch list→NPL→write-off), tidak hanya melihat rasio NPL pada satu titik waktu.
- Biaya kredit di laporan laba rugi adalah estimasi, bukan fakta. Setiap kesimpulan "laba membaik" harus menjawab dulu apakah provisi sudah memadai.

## 2. Sumber Informasi & Mekanisme Kewajaran

### Prioritas Sumber

1. **Pengajuan regulasi & pengungkapan modal**: laporan Pillar 3, laporan tahunan/semester, prospektus. Digunakan untuk mengonfirmasi komposisi RWA, rasio kecukupan modal, rasio leverage, indikator likuiditas, eksposur risiko besar, dan transaksi afiliasi.
2. **Database regulator**: AS menggunakan FFIEC Call Reports, FDIC BankFind, Federal Reserve Y-9C; Eropa menggunakan EBA Transparency Exercise dan pengungkapan SSM; Tiongkok menggunakan statistik CBIRC/PBOC; Hong Kong menggunakan HKMA. Basis modal global mengacu pada BIS Basel Framework.
3. **Laporan keuangan bank & tabel pendukung**: earnings release, supplemental financial information, investor presentation. Digunakan untuk mendapatkan bridge NIM, volume-harga deposit, klasifikasi kredit, rekonsiliasi provisi, dan guidance.
4. **Transkrip earnings call**: melacak perubahan nada manajemen tentang kompetisi deposit, migrasi kredit, eksposur CRE, modal regulasi, dan buyback.
5. **Pengungkapan sejenis & pihak ketiga**: digunakan untuk membangun peer set dan rentang kewajaran; riset sell-side hanya sebagai pelengkap, tidak boleh menggantikan pengungkapan primer.

### Mekanisme Kewajaran

- **Basis diutamakan**: perhitungan NIM, NPL, coverage ratio provisi, CET1 berbeda antar bank (apakah termasuk wesel, apakah termasuk off-balance-sheet, apakah menggunakan saldo rata-rata). Saat pertama kali muncul, cantumkan definisinya; jika tidak diungkap, tulis "definisi perusahaan tidak diperoleh".
- **Basis regulasi dan basis akuntansi dipisahkan**: provisi akuntansi, expected loss regulasi, dan economic loss adalah tiga hal berbeda. Saat membandingkan lintas pasar, jelaskan basis mana yang digunakan.
- **Laba dan risiko disandingkan**: setiap kesimpulan "ROE membaik" harus disertai kualitas aset, kecukupan modal, dan stabilitas deposit sebagai batasan.
- **Bukti sanggahan harus dimasukkan lebih dulu**: misalnya "normalisasi biaya kredit" harus dikaitkan dengan rasio overdue, migrasi ke watch list, coverage ratio, atau asumsi makro forward-looking, bukan hanya mengutip guidance manajemen.
- **Hindari survivorship bias**: peer set harus mencakup bank berkualitas, bank yang tertekan siklus, dan bank sejenis yang sudah bermasalah, tidak hanya memilih saham ROTCE tinggi.
- **Bedakan siklus dan struktural**: penyempitan NIM bisa jadi siklus suku bunga, bisa juga hilangnya franchise deposit. Harus dinilai dengan deposit beta, migrasi struktur deposit, dan bukti pangsa pasar.

## 3. Pohon Penggerak Nilai Perbankan

Nilai intrinsik bank dapat diurai menjadi:

```text
Nilai Ekuitas =
  Tangible Book Value (TBV)
  × premium ROTCE berkelanjutan relatif terhadap cost of equity
  × kapabilitas pembentukan modal internal lintas siklus
  × kualitas franchise deposit (biaya, stabilitas, durasi)
  × kapabilitas pricing aset dan seleksi risiko
  × operating leverage biaya
  − kerugian siklus kredit (rata-rata lintas siklus, bukan periode berjalan)
  − batasan modal regulasi dan biaya kepatuhan
  − dilusi, erosi M&A, dan impairment goodwill
```

Laporan minimal harus menjawab:

- Apakah spread berasal dari kapabilitas pricing aset, atau hanya hasil pasif dari lingkungan suku bunga?
- Apakah deposit bersifat berbiaya rendah, loyal, terdiversifikasi sebagai core deposit, atau deposit grosir/besar yang sensitif harga?
- Di mana posisi biaya kredit saat ini relatif terhadap rata-rata lintas siklus? Jika kembali ke rata-rata, berapa laba yang tersisa?
- Apakah surplus modal benar-benar bisa didistribusikan, atau dibangun atas asumsi stress test yang optimistis?
- Apakah ROTCE terus di atas cost of equity? Jika tidak, pertumbuhan justru menghancurkan nilai.

## 4. Kamus KPI Inti

| KPI | Perhitungan/Definisi | Kegunaan Riset | Jebakan Umum |
|---|---|---|---|
| NIM | Pendapatan bunga bersih / rata-rata aset berbunga | Kapabilitas laba inti | Apakah menggunakan saldo rata-rata, apakah termasuk wesel dan interbank, basisnya berbeda antar bank |
| Asset yield | Imbal hasil aset berbunga | Kapabilitas pricing aset | Perubahan struktur (KPR vs kartu kredit) bisa menutupi pricing riil |
| Deposit beta | Perubahan biaya deposit / perubahan suku bunga kebijakan | Transmisi suku bunga dan loyalitas deposit | Beta naik dan beta turun tidak simetris, perlu diukur terpisah |
| Cost of funds | Biaya liabilitas berbunga | Tekanan sisi liabilitas | Pendanaan grosir dan deposit harus dipisah |
| Loan/deposit ratio | Kredit / deposit | Likuiditas dan ruang pertumbuhan | Rasio tinggi memperbesar risiko likuiditas saat tekanan |
| NPL / NPA ratio | Kredit bermasalah / total kredit | Level kualitas aset pada satu titik waktu | Angka titik waktu menutupi migrasi; write-off bisa menekan secara artifisial |
| Porsi Stage 2 | Porsi kredit tahap dua IFRS 9 | Sinyal perburukan forward-looking | CECL AS tidak punya lapisan ini, tidak bisa langsung dibandingkan lintas pasar |
| Net charge-off rate | Net write-off / rata-rata kredit | Kerugian yang sudah terealisasi | Waktu write-off dikendalikan manajemen, perlu dikonfirmasi dengan migrasi |
| Provision / avg loans | Rasio biaya kredit | Intensitas provisi periode berjalan | Hanya bermakna jika dibandingkan dengan rata-rata lintas siklus |
| Coverage ratio | Provisi / NPL | Ketebalan buffer | Coverage tinggi bisa menyesatkan jika pengakuan NPL longgar |
| ACL / loans | Saldo provisi / kredit | Buffer stok | Di bawah CECL sangat dipengaruhi asumsi proyeksi makro |
| Efficiency ratio | Biaya / pendapatan operasional | Kontrol biaya | Volatilitas pendapatan bisa menyesatkan rasio ini |
| CET1 ratio | Modal inti tier 1 / RWA | Margin keamanan modal | Perlu diperiksa apakah RWA density dioptimalkan |
| RWA density | RWA / total aset | Agresivitas pengukuran risiko | Internal rating-based model bisa menekan signifikan, perlu dibandingkan dengan standardized approach |
| LCR / NSFR | Liquidity Coverage Ratio / Net Stable Funding Ratio | Kemampuan bertahan saat tekanan | Tidak semua pasar mewajibkan pengungkapan |
| Porsi deposit tidak terjamin | Porsi deposit di luar limit penjaminan | Kerawanan bank run | Indikator inti krisis bank regional 2023 |
| ROTCE | Laba bersih / rata-rata ekuitas tangible | Return modal riil | Bank dengan goodwill besar, ROE dan ROTCE berbeda signifikan |
| TBVPS | Tangible book value per saham | Basis compounding nilai | Perlu ditambahkan kembali akumulasi dividen untuk melihat compounding riil |

8 indikator yang wajib diungkap duluan: NIM, deposit beta, struktur kredit, migrasi Stage 2/overdue, rasio biaya kredit, coverage ratio, CET1, pertumbuhan ROTCE dan TBVPS.

## 5. Struktur Model Keuangan

### Model Balance Sheet dan Pendapatan

Pilih penggerak dari data yang tersedia, dari paling detail ke paling umum:

1. `Rata-rata aset berbunga × imbal hasil aset − rata-rata liabilitas berbunga × biaya liabilitas = pendapatan bunga bersih`
2. Pemodelan pool kredit terpisah: CRE (kantor/multi-family/ritel), C&I, KPR, kartu kredit, kendaraan, konsumen lain, masing-masing pool diberikan pertumbuhan, imbal hasil, dan biaya kredit.
3. Pendapatan non-bunga dipisah: fee, wealth management, investment banking, trading, interchange kartu kredit, servicing KPR. Pendapatan trading sangat volatil, tidak boleh diekstrapolasi linear.
4. Jika pengungkapan terbatas, minimal pisahkan segmen ritel/korporasi, tidak boleh hanya CAGR total aset.

Persyaratan minimum proyeksi:

- Minimal 3 tahun historis, 8 kuartal historis; mode laporan keuangan pertama kali cover juga berlaku sama.
- Proyeksi eksplisit 5 tahun ke depan, termasuk asumsi jalur suku bunga (harus dicantumkan menggunakan kurva mana).
- Pertumbuhan organik dan dampak M&A dipisah tersendiri; jika tidak bisa dipisah tulis "pemisahan tidak diperoleh" dan turunkan tingkat keyakinan.
- Pool kredit minimal dipisah CRE, C&I, KPR, kartu kredit, kendaraan dan konsumen lain; cantumkan LTV, regional, tenor, dan rating risiko.

### Model Biaya Kredit dan Biaya

- **Rekonsiliasi provisi**: harus dibangun `provisi awal periode + provision − net charge-offs + recovery = provisi akhir periode`, pisahkan provisi akuntansi, kebutuhan modal regulasi, dan economic loss.
- **Biaya kredit**: tidak diekstrapolasi dari nilai aktual periode berjalan, gunakan rata-rata lintas siklus ditambah penyesuaian posisi siklus. Biaya kredit skenario resesi harus mengacu pada peak historis bank tersebut dan peak sejenis.
- **Portofolio surat berharga**: periksa unrealized gain/loss AFS/HTM, durasi, hedging, dan kemampuan pembiayaan dengan kolateral. **Tidak bisa dianggap tidak ada hanya karena kerugian HTM tidak masuk OCI** — saat tekanan, penjualan terpaksa akan merealisasikannya seketika.
- **Deposit**: lihat ritel/korporasi, bebas bunga/berbunga, terjamin/tidak terjamin, konsentrasi, dan deposit beta. Pertumbuhan deposit tidak boleh hanya dilihat dari titik akhir kuartal, harus menggunakan rata-rata harian atau bulanan.
- **Biaya**: pisahkan investasi teknologi, biaya kepatuhan, kompensasi tangguhan, dan penyesuaian jaringan cabang. Operating leverage perlu diverifikasi dengan pertumbuhan pendapatan dikurangi pertumbuhan biaya, bukan hanya lihat efficiency ratio.
- **Bridge modal**: perubahan CET1 harus diurai menjadi laba, perubahan RWA, OCI, dividen, buyback, dan dampak transisi regulasi.

### Batasan Asumsi Steady State

- Bank berkualitas bisa menjaga ROTCE di atas cost of equity dalam jangka panjang, tetapi harus didukung core deposit berbiaya rendah, kualitas aset stabil, dan operating leverage biaya.
- Jika biaya deposit naik, migrasi Stage 2 memburuk, CET1 mendekati batas regulasi, tidak boleh sekaligus memberi pertumbuhan tinggi, biaya kredit rendah, dan dividen tinggi.
- Pertumbuhan hanya menciptakan nilai ketika `ROTCE > COE` dan modal mendukung. Pertumbuhan saat modal tidak cukup akan mendilusi nilai per saham.
- Stress test harus mencakup skenario: resesi, kenaikan tingkat pengangguran, penurunan harga rumah/CRE, kenaikan/penurunan suku bunga tajam, dan kehilangan deposit.

## 6. Metode Valuasi

### Wajib Dilakukan

1. **Cross-check P/TBV dan ROTCE berkelanjutan**: metode inti. `P/TBV wajar ≈ (ROTCE − g) / (COE − g)`. Harus dicantumkan menggunakan ROTCE lintas siklus, bukan peak.
2. **Discounted residual income / dividen**: free cash flow bank dibatasi modal, lebih tepat mendiskon laba yang dapat didistribusikan (setelah dikurangi laba ditahan yang diperlukan untuk menjaga kecukupan modal).
3. **Valuasi terbalik**: dari harga saat ini, dibalik untuk mendapatkan implied ROTCE jangka panjang, biaya kredit, dan cost of equity, untuk menjawab "apa yang sudah di-price in pasar".
4. **P/E ternormalisasi**: menggunakan laba ternormalisasi dengan biaya kredit lintas siklus yang direstorasi, bukan laba periode berjalan.

### Opsional

- **SOTP**: digunakan jika universal bank memiliki ritel, korporasi, investment bank, wealth management, dan asuransi sekaligus, masing-masing segmen diberi okupansi modal dan multiple berbeda.
- **Nilai likuidasi/revaluasi**: ketika diskon parah atau kualitas aset diragukan, gunakan TBV yang disesuaikan (dikurangi unrealized loss HTM, defisit provisi, dan goodwill) untuk menetapkan batas bawah.
- **Perspektif M&A**: periksa goodwill, periode pemulihan dilusi TBV per saham, dan track record realisasi sinergi biaya.

**Jangan gunakan FCF perusahaan biasa / EV-EBITDA sebagai valuasi utama bank** — liabilitas adalah bahan baku operasional, konsep enterprise value tidak berlaku.

### Aturan Peer Set

Pilih 5-10 bank pembanding, dan cantumkan alasan pemilihannya:

- Model bisnis: dominan ritel, dominan korporasi, universal, investment bank, bank digital.
- Skala aset dan tier regulasi: G-SIB, bank regional, bank komunitas memiliki persyaratan modal berbeda.
- Geografi dan lingkungan suku bunga: siklus kebijakan bank sentral yang dihadapi, intensitas kompetisi deposit, posisi siklus properti.
- Posisi siklus kualitas aset: biaya kredit di level rendah, sedang normalisasi, atau sedang clear up.
- Status modal: tingkat surplus CET1 dan kapabilitas dividen/buyback.

Item yang dikecualikan harus dijelaskan: jika suatu bank tampak sejenis tapi struktur aset, framework regulasi, atau persyaratan modal jelas berbeda, tidak boleh dipaksakan masuk ke tabel P/TBV yang sama.

## 7. Fokus Pola Laporan Keuangan

Mode laporan keuangan harus menjawab "apa yang berubah dari laporan ini", bukan hanya mendaftar beat/miss.

| Modul | Pertanyaan Wajib |
|---|---|
| Selisih ekspektasi | Di mana selisih pendapatan bunga bersih, pendapatan non-bunga, biaya kredit, biaya, EPS relatif terhadap konsensus dan guidance? |
| Bridge NII/NIM | Perubahan spread berasal dari repricing aset, biaya liabilitas yang sudah peak, pertumbuhan skala, atau penyesuaian struktur? |
| Bridge volume-harga deposit | Deposit mengalir masuk atau keluar? Berapa kenaikan biayanya? Apakah porsi deposit bebas bunga terus menurun? |
| Migrasi kredit dan overdue | Apakah overdue, watch list, Stage 2 naik lebih dulu dari NPL? Pool kredit mana yang memburuk? |
| Bridge provisi/write-off | Kenaikan provisi karena penyesuaian asumsi makro, eksposur besar individual, atau perburukan umum? |
| Bridge modal | Dari perubahan CET1, berapa kontribusi laba, RWA, OCI, dividen buyback masing-masing? |
| Biaya | Kenaikan biaya karena inflasi, investasi teknologi, atau item one-time? Operating leverage positif atau negatif? |
| Guidance | Apakah guidance NII, biaya kredit, biaya, atau return modal mengubah model jangka panjang? |
| Earnings call | Apakah nada bicara tentang kompetisi deposit, CRE, standar underwriting, modal regulasi, buyback melemah? |
| Arah perdagangan pasar | Dalam 1–3 bulan ke depan, pasar lebih mungkin trading berdasarkan titik balik NIM, biaya kredit, pengembalian modal, atau stabilitas deposit? |

Reaksi harga setelah laporan keuangan harus dikurangi dengan performa pasar dan sejenis: jika bank naik 6% tapi indeks saham perbankan naik 4% di hari yang sama, reaksi spesifik perusahaan sekitar +2%.

Bandingkan nilai akhir periode dan rata-rata kuartalan, untuk mencegah window dressing (pemolesan deposit akhir kuartal, dorongan kredit akhir kuartal).

## 8. Moat & Penilaian Kompetitif

Inti moat perbankan adalah **franchise deposit**, tidak hanya menulis "merek bagus". Beri nilai minimal dari dimensi berikut:

| Dimensi | Bukti Kuat | Bukti Lemah/Sanggahan |
|---|---|---|
| Franchise deposit | Porsi core deposit berbiaya rendah tinggi, deposit beta pada siklus kenaikan suku bunga jauh lebih rendah dari sejenis | Deposit dihimpun dengan bunga tinggi, beta mendekati atau lebih tinggi dari sejenis |
| Diversifikasi deposit | Nominal rata-rata per rekening kecil, porsi terjamin tinggi, industri terdiversifikasi | Deposit besar/tidak terjamin/konsentrasi pada satu industri |
| Relasi bank utama (main bank) | Settlement korporat, cash management, bundling kredit, biaya peralihan tinggi | Hanya relasi kredit tunggal, langsung hilang jika ada kompetisi harga |
| Kapabilitas seleksi risiko | Biaya kredit lintas siklus terus lebih rendah dari sejenis, dan bukan karena aset berisiko rendah berimbal hasil rendah | Aset berimbal hasil tinggi tapi rasio kerugian melonjak saat siklus |
| Efisiensi biaya | Efficiency ratio terus lebih baik dari sejenis dan bukan karena pemotongan investasi | Rasio biaya rendah karena investasi teknologi kurang |
| Skala dan jaringan | Cabang/kanal digital membentuk keunggulan biaya akuisisi pelanggan | Jaringan redundan, biaya pemeliharaan lebih tinggi dari manfaatnya |
| Kapabilitas pembentukan modal internal | Laba bisa sekaligus mendukung pertumbuhan, dividen, dan akumulasi modal | Pertumbuhan bergantung pada pendanaan eksternal atau menekan buffer modal |

Moat kualitatif harus diverifikasi silang dengan bukti keuangan: jika diklaim "basis deposit berkualitas", tapi porsi deposit bebas bunga terus menurun dan deposit beta lebih tinggi dari sejenis, kontradiksi ini harus dijelaskan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

### Red Flag

- Pertumbuhan kredit tinggi berbarengan dengan provisi rendah, terutama di fase akhir siklus kredit.
- Indikator forward-looking NPL (overdue, watch list, Stage 2) memburuk tapi write-off dan provisi tidak bergerak.
- Deposit tidak terjamin atau deposit besar porsinya tinggi dan terkonsentrasi di satu industri (seperti teknologi, kripto, CRE).
- Skala unrealized loss HTM besar dan tidak sepadan dengan buffer modal.
- Pendanaan grosir, pinjaman FHLB, atau deposit melalui broker naik cepat.
- Terjadi pemolesan jelas pada deposit/kredit akhir kuartal, rata-rata harian dan akhir periode berdivergensi.
- Buyback modal dibangun atas asumsi stress test yang optimistis, atau dilanjutkan saat CET1 mendekati batas regulasi.
- M&A yang sering dilakukan menutupi lemahnya pertumbuhan organik, goodwill terus terakumulasi.
- Laba yang disesuaikan ("adjusted") terus-terusan mengeluarkan biaya kepatuhan, litigasi, atau restrukturisasi "one-time" padahal ini terjadi setiap tahun.
- RWA density di bawah model internal rating-based jauh lebih rendah dari sejenis dan tidak bisa dijelaskan dari struktur aset.

### Daftar Bukti Sanggahan

Setiap laporan perbankan minimal harus mencantumkan 3 ambang bukti yang dapat membatalkan kesimpulan utama:

- NIM menyempit N kuartal berturut-turut dan deposit beta di atas batas atas sejenis.
- Rasio Stage 2 / overdue naik QoQ melebihi ambang tertentu.
- Rasio biaya kredit menembus kelipatan tertentu dari rata-rata lintas siklus.
- CET1 jatuh di bawah rentang target manajemen atau persyaratan regulasi plus buffer.
- Porsi deposit bebas bunga atau saldo core deposit jatuh di bawah ambang.
- LTV, tingkat hunian, atau gap refinancing eksposur CRE (terutama kantor) memburuk.

### Kesalahpahaman Umum

- Menganggap P/TBV rendah sebagai murah, mengabaikan bahwa valuasi rendah wajar ketika ROTCE di bawah cost of equity.
- Menganggap biaya kredit rendah periode berjalan sebagai normal, mengabaikan posisi siklus, sehingga laba ternormalisasi dinilai berlebihan.
- Menganggap coverage ratio tinggi sebagai aman, mengabaikan apakah standar pengakuan NPL longgar.
- Menganggap pertumbuhan deposit sebagai peningkatan franchise, mengabaikan bahwa itu dibeli dengan produk berbunga tinggi.
- Menganggap unrealized loss HTM tidak ada, mengabaikan bahwa akan terpaksa direalisasi saat tekanan likuiditas.
- Menganggap ekspansi NIM di siklus kenaikan suku bunga sebagai kapabilitas struktural, mengabaikan kompresi simetris di siklus penurunan suku bunga.
- Menganggap peningkatan EPS dari M&A sebagai penciptaan nilai, mengabaikan dilusi TBV per saham dan periode pemulihannya.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa.

Laporan perbankan selain template utama, wajib menambahkan tabel atau paragraf berikut:

### Tabel KPI Perbankan

| Indikator | Nilai Terbaru | YoY/QoQ | Tren 8 Kuartal Terakhir | Posisi vs Sejenis | Sumber & Basis |
|---|---:|---:|---|---|---|
| NIM / imbal hasil aset | | | | | |
| Deposit beta / biaya deposit | | | | | |
| Pertumbuhan dan struktur kredit | | | | | |
| Migrasi overdue / Stage 2 | | | | | |
| Rasio biaya kredit | | | | | |
| Coverage ratio | | | | | |
| Efficiency ratio | | | | | |
| CET1 / RWA density | | | | | |
| Pertumbuhan ROTCE / TBVPS | | | | | |

### Tabel Struktur Balance Sheet dan Risiko

| Item | Nominal/Porsi | Parameter Risiko Kunci | Sumber |
|---|---:|---|---|
| Pool kredit (CRE/C&I/KPR/kartu kredit/konsumen) | | LTV, regional, rating, tenor | |
| Struktur deposit (ritel/korporasi, bebas bunga/berbunga, terjamin/tidak) | | Konsentrasi, beta | |
| Portofolio surat berharga (AFS/HTM) | | Durasi, unrealized gain/loss, hedging | |
| Pendanaan grosir dan likuiditas | | LCR/NSFR, kolateral tersedia | |

### Tabel Asumsi Valuasi

| Asumsi | Bear | Base | Bull | Dasar |
|---|---:|---:|---:|---|
| ROTCE lintas siklus | | | | |
| Cost of equity (COE) | | | | |
| Rasio biaya kredit lintas siklus | | | | |
| Pertumbuhan TBV jangka panjang g | | | | |
| P/TBV wajar | | | | |
| Probabilitas skenario | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: valuasi bank ini saat ini paling bergantung bukan pada laba kuartal ini, melainkan apakah ROTCE lintas siklus dapat dipertahankan di atas X%, dan berapa laba yang tersisa setelah biaya kredit kembali ke rata-rata."
- "Jika salah satu indikator inti berikut — NIM / deposit beta / Stage 2 / biaya kredit / CET1 — menembus ambang berikut, saya akan menurunkan asumsi jangka panjang: ……"
- "ROTCE jangka panjang dan biaya kredit yang terimplikasi harga saham saat ini adalah ……; saya menilai implikasi ini wajar/agresif/konservatif, dengan alasan ……"
</content>
