# Metode Valuasi

Tujuan: memberikan rentang nilai wajar menggunakan **minimal tiga** metode yang saling independen, dirangkum dalam satu tabel, dan menghitung implied upside/downside relatif terhadap harga saat ini. Makna dari multi-metode terletak pada validasi silang — jika rentangnya berdekatan, kesimpulan lebih dapat dipercaya; jika perbedaannya besar, harus dijelaskan mengapa (biasanya karena asumsi pertumbuhan/profitabilitas atau perbedaan tingkat diskonto), dan jelaskan mana yang diikuti.

Prinsip:
- Setiap metode **wajib mencantumkan asumsi kunci secara eksplisit**, asumsi lebih penting daripada angka di belakang titik desimal; di samping asumsi kunci, cantumkan persentil base rate (lihat `base-rates.md`).
- **Semua kalkulasi DCF/EPV/EVA/Monte Carlo wajib dieksekusi menggunakan `scripts/dcf.py`, dilarang menghitung di kepala**. Asumsi disimpan dalam bentuk JSON, yang sekaligus berfungsi sebagai dokumentasi.
- Tingkat diskonto harus bersumber dan bernilai sama di seluruh laporan, metode konstruksinya lihat `cost-of-capital.md`; risiko hanya dihukum satu kali (pilih salah satu antara tingkat diskonto atau probabilitas skenario).
- Valuasi adalah rentang, bukan titik tunggal; label kesimpulan dihasilkan dari pemetaan aturan pra-registrasi di Bagian 9, tidak boleh diputuskan secara spontan.
- **Prasyarat valuasi**: jika grade kredibilitas laporan keuangan (`forensic-accounting.md`) adalah C/D, valuasi harus mengalah pada masalah kredibilitas.

---

## 1. Relative Valuation (Perusahaan Pembanding + Rentang Historis + Multiple yang Wajar)

Multiple yang umum dipilih berdasarkan jenis perusahaan: P/E (laba stabil), EV/EBITDA (aset berat/perbedaan struktur modal besar), P/S (growth yang belum profitable), PEG (kasar), EV/ARR (subscription), P/B–ROE (finansial).

Langkah:
1. **Rentang multiple historis** perusahaan itu sendiri (persentil 25/50/75 selama 5–10 tahun terakhir), lihat posisi saat ini.
2. Perbandingan multiple yang sama dengan 3–6 **perusahaan sejenis (comparable companies)** (pembanding untuk saham A China/saham Hong Kong lihat Bagian 6 di `markets-cn-hk.md`).
3. **Disiplin warranted multiple (multiple yang wajar)**: dilarang langsung menyalin median peer. Multiple adalah fungsi dari pertumbuhan g, return ROIC, dan risiko r; pada kondisi steady-state, warranted P/E ≈ (1 − g/ROIIC)/(r − g). Hitung dahulu multiple wajar berdasarkan fundamental perusahaan, baru bandingkan dengan multiple yang diberikan pasar; selisihnya mencerminkan entah pasar yang salah (peluang) atau risiko yang belum anda lihat (peringatan) — atribusikan secara eksplisit.
4. "Multiple wajar × metrik keuangan terkait" = rentang nilai wajar per saham.

| Multiple | Saat Ini | Median Historis Sendiri | Median Peer | Multiple Wajar (rumus) | Dipilih | Implied Nilai Per Saham |
|---|---|---|---|---|---|---|

---

## 2. Valuasi Absolut: DCF (Forward) + Disiplin Nilai Terminal

Tiga tahap: periode eksplisit 5–10 tahun + periode fade pertumbuhan 3–6 tahun + perpetuity. Periode fade membuat pertumbuhan di tahun terakhir menurun secara linear ke pertumbuhan perpetual (g), menghindari penurunan drastis (cliff).

Asumsi kunci (wajib dicantumkan, dilampiri persentil base rate): jalur pendapatan, jalur margin FCF, WACC (lihat `cost-of-capital.md`), pertumbuhan perpetual g (≤ PDB nominal jangka panjang), tingkat dilusi saham.

**Disiplin nilai terminal (tiga pemeriksaan kewajaran nilai terminal)**:
1. Implied exit P/FCF (keluaran otomatis skrip) ≤ multiple saat ini dari perusahaan sejenis yang sudah matang, jika melebihi harus diargumentasikan.
2. Jika nilai terminal menyumbang > 80% dari total nilai → berarti periode eksplisit terlalu singkat atau pasar membeli cerita yang terlalu jauh di masa depan, ungkapkan secara jelas.
3. **Secara default, biarkan return inkremental konvergen ke biaya modal**: ROIIC investasi baru pada periode perpetuity → WACC (pertumbuhan tidak lagi menambah nilai, artinya nilai periode perpetuity ≈ nilai pertumbuhan nol gaya EPV). Untuk mempertahankan excess return di nilai terminal, harus diargumentasikan secara eksplisit melalui Competitive Advantage Period (CAP) — secara historis perusahaan dengan periode excess return >15–20 tahun sangat jarang (lihat Bagian 4 di `base-rates.md`).

Eksekusi: JSON asumsi → `scripts/dcf.py --config`. Sensitivitas WACC×g 3×3 wajib dilakukan; untuk saham growth tambahkan sensitivitas pertumbuhan pendapatan × margin steady-state.

---

## 3. Metode Three-Factor: Asset Reproduction · EPV · Franchise Growth (Graham–Greenwald)

(Metodologi tidak berubah, konsisten dengan versi sebelumnya; jika bertentangan dengan metode lain di manual ini, acuan utama adalah buku asli Greenwald.)

**Layer Pertama · Nilai Reproduksi Aset (Harga Dasar/Floor)**: kurangi "air" (mark-down) secara item per item pada balance sheet, kurangi total liabilitas. Referensi diskon: kas 100%, sekuritas 95–100%, piutang 80–90%, inventori (bahan baku/barang jadi) 80–90%/50–70%, peralatan 20–30%, pabrik 40–60%, properti sesuai harga pasar, goodwill umumnya 0.

**Layer Kedua · EPV (Inti)**: `EPV = Laba Ternormalisasi ÷ Biaya Modal` (perpetuity pertumbuhan nol). Laba ternormalisasi mengecualikan item non-recurring, menambahkan kembali growth capex yang melebihi maintenance capex; secara default menggunakan basis NOPAT (÷WACC menghasilkan EV, dikurangi net debt ditambah excess cash menghasilkan equity value); jika data tidak cukup, gunakan basis net income (coc diperlakukan sebagai cost of equity). Biaya modal harus bersumber sama dengan WACC pada DCF. **Verifikasi finansial moat**: tren multi-tahun EPV/aset bersih yang disesuaikan — ≈1 berarti tidak ada moat, <1 berarti merusak nilai, ≫1 dan stabil jangka panjang = ukuran finansial dari moat; disilangkan dengan skor kualitatif Bab III.

**Layer Ketiga · Nilai Pertumbuhan (Hanya Dihitung dalam Lingkup Moat)**: `Nilai = E×(1 − g/ROIIC)/(coc − g)`, mensyaratkan ROIIC > coc dan g < coc; jika tidak, kembali ke rumus sederhana EPV×(1+g konservatif). g konservatif = ambil nilai yang lebih rendah antara CAGR laba historis 5 tahun dan jangkar makro.

Eksekusi: blok `epv` di JSON → skrip menghasilkan tangga titik beli (floor < EPV < pertumbuhan yang disesuaikan) dan posisi harga saat ini dalam rentang tersebut.

---

## 4. Reverse DCF + Dekomposisi PVGO — Alur Analisis Utama Expectations Gap (Kerangka Pembuka Bab Pertama)

Reverse DCF menanyakan "**apa yang diasumsikan harga saat ini**", dan ini adalah alur analisis utama seluruh laporan (metodologi lengkap lihat `expectations-investing.md`).

- Blok `reverse`: menguraikan dari harga saat ini, FCF steady-state yang dibutuhkan → dikonversi menjadi pendapatan yang dibutuhkan dan implied CAGR berdasarkan tingkat margin steady-state.
- Blok `pvgo`: `harga saat ini = E/r (nilai pertumbuhan nol) + PVGO`, menghasilkan **persentase harga saat ini yang merupakan pembayaran untuk pertumbuhan masa depan**. Untuk saham dengan proporsi PVGO >50%, laporan wajib menjawab "pertumbuhan ini datang dari mana, siapa yang membayarnya".
- Penyajian: terjemahkan tuntutan implisit ke dalam kerangka referensi (bandingkan dengan base rates: "secara implisit menuntut pertumbuhan Y% selama N tahun berturut-turut, secara historis proporsi perusahaan yang mampu melakukannya adalah Z%"). Kalimat kesimpulan: "pasar bukan memberi harga pada ×, melainkan memberi harga pada ×".
- Output **tabel Expectations Gap** (kerangka lihat Bagian 2 di `expectations-investing.md`), ditempatkan di Bab I laporan.

---

## 5. Fair Value Tertimbang Skenario + Monte Carlo

**Tiga Skenario (Wajib)**: bear/base/bull masing-masing berupa satu set asumsi yang konsisten secara internal (bukan sekadar base ±20%); skenario bear harus menanyakan "pada saat itu, apa yang akan dilakukan manajemen yang rasional". Berikan probabilitas (totalnya 1) beserta dasarnya; skrip menyelesaikan pembobotan dalam satu kali jalan. Setiap skenario wajib ditandai **kekuatan bukti saat ini** (lemah/menengah/menengah-kuat/kuat) dan sumber buktinya. Jika skenario bull atau bear sudah memiliki bukti menengah-kuat/kuat (misalnya KPI laporan keuangan terbaru, margin yang naik bersamaan, order/backlog, reaksi harga, atau progres regulasi), probabilitasnya tidak boleh hanya diberi bobot tail; probabilitas harus dinaikkan, atau dijelaskan secara eksplisit mengapa bukti tersebut belum cukup mengubah probabilitas. **Uji ketahanan (robustness test)**: dorong probabilitas ke kombinasi yang paling tidak menguntungkan bagi kesimpulan, lihat apakah labelnya berbalik; jika berbalik, tulis dengan jujur "kesimpulan sensitif terhadap probabilitas".

**Monte Carlo (Opsional, Penguat, Digunakan Saat Distribusi Hasil Sangat Lebar atau Path-Dependent)**: blok `montecarlo` memberikan distribusi untuk driver kunci (pertumbuhan: normal terpotong/truncated normal; margin: triangular; WACC: uniform band sempit), simulasi N≥2.000 kali, output fair value P10/P25/P50/P75/P90, **P(nilai intrinsik < harga saat ini)** (yaitu probabilitas "membeli di harga saat ini adalah keputusan yang salah") dan expected value. Monte Carlo tidak menggantikan tiga skenario (jika setting korelasinya tidak transparan justru menghasilkan presisi palsu), melainkan sebagai bukti pelengkap untuk bentuk distribusi.

**Peringatan Repricing Pasar**: nilai skenario menjawab "pada akhirnya bernilai berapa", tidak otomatis menjawab "apa yang akan diperdagangkan pasar lebih dulu". Ketika laporan keuangan atau peristiwa terbaru baru saja mengubah variabel inti, harus ditulis secara terpisah arah perdagangan pasar 1–3 bulan ke depan: pasar lebih mungkin memperdagangkan akselerasi pendapatan/order, margin, return capex, risiko regulasi, perubahan buyback, atau mean reversion valuasi lebih dulu. Penilaian ini masuk ke trikotomi keputusan Bab I, tidak mengubah label nilai intrinsik, tetapi mempengaruhi tempo aksi.

---

## 6. EVA / Residual Income (Laba Ekonomi) — Penggaris Lain untuk Moat

`EVA_t = NOPAT_t − WACC × Invested_Capital_{t-1}`; `Nilai = Invested Capital Saat Ini + Σ EVA Masa Depan yang Didiskontokan`.

Mengapa layak dilakukan secara terpisah: memecah nilai menjadi "modal yang sudah ada + excess return", langsung mengungkap dua masalah yang tidak terlihat di DCF biasa —
1. **Apakah perusahaan saat ini benar-benar menghasilkan return di atas biaya modal** (saham "growth" dengan EVA negatif selama bertahun-tahun adalah penghancur nilai);
2. **Sumber nilai dari pertumbuhan**: `pertumbuhan organik g = reinvestment rate (RR) × ROIIC` — jika menginginkan pertumbuhan 10% sementara ROIIC hanya 12%, berarti harus menginvestasikan kembali 83% dari laba, sehingga FCF yang tersisa sangat sedikit. Dalam DCF, pertumbuhan dan margin adalah dua parameter bebas; kerangka EVA memaksa keduanya konsisten satu sama lain.

Eksekusi: blok `eva` di JSON (`invested_capital`, `nopat`, `wacc`, `fade_years`: excess return Δ=ROIC−WACC mereda secara linear ke 0) → skrip menghasilkan seri EVA, nilai residual income, dan nilai per saham. Untuk saham finansial, gunakan versi ekuitas dari residual income (net income − CoE×ekuitas bersih), yang merupakan metode valuasi absolut utama untuk bank/asuransi.

---

## 7. Metode Lain yang Berlaku

- **SOTP (Sum of the Parts)**: untuk perusahaan multi-bisnis, jumlahkan nilai per segmen, kurangi net debt dan biaya kantor pusat; perbedaan dengan DCF = kuantifikasi dari sentimen pasar. Wajib untuk platform/grup usaha.
- **Fair Value Morningstar**: sebagai jangkar pihak ketiga, cantumkan tanggal/star rating/uncertainty; bedakan fair value dari analis dengan rating kuantitatif.
- **Metode Khusus Industri**: NAV (pertambangan/pelayaran/properti), rNPV (pipeline farmasi), P/EV (asuransi), P/AFFO (REIT), metode laba mid-cycle (saham siklikal, aturan umum: EPS mid-cycle = titik tengah band margin 10 tahun × pendapatan saat ini; dilarang mengalikan peak×peak).

---

## 8. Ringkasan Valuasi dan Football Field

Rangkum rentang dari masing-masing metode dalam satu tabel + grafik football field versi teks (cara membuatnya lihat Bagian 4 di `output-format.md`), berikan rentang gabungan dan implied upside/downside; satu kalimat menjelaskan metode mana yang lebih diandalkan dan alasannya; perbedaan antar-metode wajib diatribusikan, dilarang diam-diam mengambil rata-rata.

| Metode | Rentang Nilai Wajar | Implied Upside/Downside | Bobot/Kredibilitas | Asumsi Kunci/Perbedaan |
|---|---|---|---|---|
| Reverse DCF + PVGO | (untuk menggugurkan harga saat ini) | | Framework | Implied pasar vs base rate |
| DCF Tertimbang Skenario (±Monte Carlo) | | | | |
| Three-factor/EPV | | | | |
| EVA/Residual Income | | | | |
| Relative Valuation (Multiple Wajar) / SOTP | | | | |
| **Rentang Gabungan [L, H]** | | | | |

Jika input tidak cukup untuk mendukung rentang yang dapat dipercaya, tulis dengan jujur "tidak dapat memberikan rentang valuasi yang dapat diandalkan" dan jelaskan apa yang kurang.

---

## 9. Kalibrasi Kesimpulan dan Pemikiran Posisi (Pra-Registrasi, Tidak Boleh Diputuskan Secara Spontan)

**Label Valuasi** (rentang gabungan [L, H], harga saat ini P, buffer band ±15%):

| Kondisi | Label |
|---|---|
| P < 0,50L | Signifikan Undervalued |
| 0,50L ≤ P < 0,85L | Undervalued |
| 0,85L ≤ P ≤ 1,15H | Fairly Valued |
| 1,15H < P ≤ 1,50H | Overvalued |
| P > 1,50H | Signifikan Overvalued |

**Matriks Aksi** (label × ketidakpastian; ketidakpastian diutamakan dari rating Morningstar, jika tidak ada lakukan evaluasi diri dengan dasar yang ditulis jelas):

| Label \ Ketidakpastian | Rendah / Menengah | Tinggi / Sangat Tinggi |
|---|---|---|
| Signifikan Undervalued | Beli | Beli bertahap (baru boleh membangun posisi awal jika P < 0,70L) |
| Undervalued | Beli/beli bertahap | Coba posisi kecil atau tunggu |
| Fairly Valued | Wait and see (yang sudah memegang tetap hold) | Wait and see |
| Overvalued | Kurangi/hindari | Hindari |
| Signifikan Overvalued | Hindari, yang sudah memegang kurangi | Sama seperti kiri; default tidak merekomendasikan short |

**Item Veto (Penurunan Grade Otomatis)**: red flag governance ≥2 item serius atau **kredibilitas laporan keuangan C** → aksi maksimum "wait and see"; **kredibilitas D** → hindari; moat "tidak ada" dan label overvalued → langsung hindari. Untuk dual listing, kalibrasi per pasar sesuai `markets-cn-hk.md`.

**Koreksi Tempo Aksi**: matriks aksi memberikan aksi default dalam disiplin nilai; jika arah perdagangan pasar 1–3 bulan ke depan berlawanan dengan label nilai (misalnya nilai intrinsik "fairly valued/sedikit mahal", tetapi arah repricing pasca-laporan "bias naik"), tidak boleh hanya ditulis "wait and see" begitu saja. Harus dijelaskan secara spesifik apakah itu "tunggu koreksi", "hold tanpa menambah", "review dipicu saat breakout/koreksi", atau "pantau dengan posisi kecil", disertai kondisi pemicunya.

**Pemikiran Posisi (blok `position`, memberi ukuran kuantitatif pada aksi)**:
- Expected value `EV = Σ p_i × (V_i/P − 1)` (gunakan nilai per saham dan probabilitas dari tiga skenario).
- **Rasio asimetri = ruang upside ÷ ruang downside** (kenaikan skenario bull ÷ penurunan skenario bear); rasio <1,5 pada kondisi "undervalued" biasanya tidak sepadan untuk dibangun posisinya.
- Posisi referensi Kelly-lite = ¼ × fraksi Kelly (skrip menghitung dengan pendekatan dua titik), hanya sebagai referensi orde besaran, batas atas 15%, **bukan merupakan rekomendasi alokasi** — laporan hanya menyatakan "struktur odds ini mendukung posisi kecil/menengah/standar".
- Probabilitas kerugian P(loss) (dapat diperoleh dari Monte Carlo) dan downside maksimum yang dapat ditoleransi ditampilkan bersamaan.

**Persyaratan Konsistensi**: label, aksi, dan arah expectations gap di Bab I dan Bab IX wajib konsisten dan dapat dihitung ulang sesuai aturan ini; `dcf.py` secara otomatis menghasilkan saran label ketika diberikan range_low/range_high, `check_research_output.py` mereview ulang konsistensi teks laporan.
