# Manual Biaya Modal (WACC / Tingkat Diskonto)

Prinsip: tingkat diskonto adalah "biaya kesempatan" (opportunity cost), bukan "tombol penyetel parameter". **Dalam satu laporan yang sama, WACC pada DCF, coc pada EPV, dan tarif biaya modal pada EVA wajib berasal dari sumber dan nilai yang sama**; inkonsistensi tingkat diskonto antar metode adalah bentuk kecurangan yang paling tersembunyi.

## 1. Urutan Konstruksi

1. **Risk-free rate**: yield obligasi pemerintah tenor 10 tahun yang sesuai dengan mata uang valuasi (pada tanggal yang sama, cantumkan timestamp). Untuk bisnis domestik China gunakan obligasi pemerintah China (CDB) 10 tahun; untuk laporan keuangan dalam dolar AS gunakan UST 10Y.
2. **Equity Risk Premium (ERP)**: utamakan **implied ERP** (forward-looking) yang diperbarui bulanan oleh Damodaran; alternatif berikutnya adalah ERP historis (4–6%). Untuk pasar berkembang, tambahkan country risk premium (country risk premia Damodaran), dibobot berdasarkan pendapatan menurut wilayah operasional bisnis, bukan berdasarkan tempat listing.
3. **Beta**: beta industri tanpa leverage (unlevered) yang kemudian dilever ulang sesuai struktur modal target lebih diutamakan dibanding regresi beta saham individual (noise-nya terlalu besar). Untuk tingkat keyakinan tinggi/rendah, dapat disesuaikan dalam rentang ±0,2 dengan alasan tertulis.
4. **Biaya utang (cost of debt)**: tingkat bunga penerbitan obligasi aktual atau "risk-free + credit spread" (sesuai rating), setelah pajak.
5. **Pembobotan**: gunakan bobot nilai pasar (market value weights) dan struktur modal target; untuk perusahaan dengan kas sangat besar, perhatikan bahwa ketika net debt negatif, WACC ≈ cost of equity.

## 2. Jangkar yang Umum Dipakai (Jalur Cepat, Harus Ditandai sebagai Penyederhanaan)

| Pasar/Jenis | Referensi Cost of Equity | Keterangan |
|---|---|---|
| Blue chip kapitalisasi besar AS | 8–9,5% | Ambil ujung bawah jika kepastian tinggi |
| Saham growth AS volatilitas tinggi | 10–13% | Atau gunakan probabilitas skenario untuk menanggung risiko sambil menjaga tingkat diskonto tetap netral (pilih salah satu, jangan ditumpuk) |
| Saham A China | 8–10% (CNY) | Risk-free rendah tetapi ERP tinggi |
| Saham Hong Kong (perusahaan berbasis China daratan) | 9–12% | Termasuk premi governance dan likuiditas |
| Jalur sederhana EPV | AS ≈ 8% / China ≈ 6% | Hanya digunakan jika WACC level perusahaan tidak dapat dibangun |

## 3. Disiplin

- **Risiko hanya dihukum satu kali**: pilih salah satu — masuk ke tingkat diskonto (menambah premi) atau masuk ke arus kas (probabilitas skenario) — dilarang menghukum dua kali di kedua sisi (double counting) atau tidak menghukum di kedua sisi sama sekali.
- Premi saham kecil/likuiditas: secara akademis masih diperdebatkan; jika digunakan, harus dicantumkan secara eksplisit dan disertai sensitivitas pembanding tanpa premi tersebut.
- Bisnis multi-mata uang: mata uang arus kas harus sesuai dengan mata uang tingkat diskonto; untuk dual listing A-share/H-share, ikuti Bagian 6 di `markets-cn-hk.md` — satu nilai enterprise value untuk seluruh grup, dikonversi menjadi dua harga per saham sesuai masing-masing pasar.
- Alasan untuk setiap komponen nilai WACC ditulis di bagian valuasi laporan; tabel sensitivitas mencakup rentang ±1pp.
