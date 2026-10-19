# Referensi Base Rate (Tingkat Dasar Historis / Perspektif Eksternal)

Tujuan: membatasi proyeksi dengan distribusi historis. Dalam DCF, selisih asumsi pertumbuhan 2% bisa menghasilkan selisih valuasi 50%, dan satu-satunya penawar racun ini adalah menempatkan setiap asumsi ke dalam "distribusi aktual seluruh perusahaan di sepanjang sejarah". Rentang empiris di bawah ini sebagian besar bersumber dari *The Base Rate Book* karya Mauboussin, riset Chan/Karceski/Lakonishok, dan riset jangka panjang McKinsey Valuation (berbasis sampel besar perusahaan terbuka AS). **Ini adalah acuan orde besaran, bukan nilai presisi**; bila memungkinkan, cek ulang secara daring untuk riset terbaru dan cantumkan versi yang dirujuk.

## 1. Pertumbuhan Pendapatan: Reversi ke Rata-Rata Lebih Cepat dari Intuisi Kebanyakan Orang

| Kondisi Awal | Pola Empiris (horizon 10 tahun) |
|---|---|
| Perusahaan dengan pertumbuhan > 20%/tahun | Setelah 10 tahun, median pertumbuhan turun ke level digit tunggal menengah; proporsi yang mampu mempertahankan 20%+ selama 10 tahun berturut-turut hanya sekitar 1–3% |
| Pertumbuhan 10–20% | Dalam 5 tahun, median turun ke 5–8% |
| Pertumbuhan dua digit 5 tahun berturut-turut | Probabilitas kemunculannya menurun tajam seiring skala; untuk saham berkapitalisasi besar (pendapatan >$100 miliar) hampir tidak ada lagi |
| Proyeksi pertumbuhan jangka panjang analis | Secara sistematis terlalu tinggi 3–5 poin persentase, dan bias ini lebih besar pada proyeksi pertumbuhan tinggi |

**Penalti skala**: setiap kenaikan satu orde besaran pada basis pendapatan, probabilitas historis untuk mempertahankan tingkat pertumbuhan yang sama kira-kira terpangkas separuh. Mengasumsikan CAGR 15% untuk perusahaan dengan pendapatan $300 miliar setara dengan mengasumsikan perusahaan itu "menciptakan kembali" satu perusahaan Fortune 100 setiap 5 tahun.

## 2. Margin: Margin Kotor Tinggi Lebih Berkelanjutan daripada Pertumbuhan Tinggi

- Autokorelasi tahun-ke-tahun pada margin kotor sangat tinggi (>0,9): margin kotor adalah atribut model bisnis, sehingga asumsi perbaikan drastis membutuhkan bukti struktural (perubahan mix, kekuatan harga/pricing power, proses produksi).
- Margin operasi cenderung reversi ke rata-rata industri, tetapi **kelompok dengan moat (ROIC tinggi dan stabil) mereversi jauh lebih lambat dibanding kelompok tanpa moat** — ini adalah bukti empiris bahwa moat layak dibayar mahal.
- "Margin steady-state = level terbaik di antara perusahaan sejenis saat ini" adalah bentuk kecurangan yang umum: harus disertai berapa tahun yang dibutuhkan pembanding itu untuk mencapai margin tersebut dan pada skala berapa.

## 3. Persistensi ROIC

- Perusahaan dengan ROIC tinggi (kuartil teratas) yang masih berada di kuartil teratas setelah 10 tahun proporsinya sekitar 40–50% — persistensi ada, tetapi jauh dari pasti.
- Reversi ROIC lebih didorong oleh margin, bukan oleh perputaran aset (asset turnover); perputaran aset adalah komponen yang lebih "struktural".
- **ROIC inkremental (ROIIC) lebih penting daripada ROIC stok (yang sudah ada)**: saat menilai value dari pertumbuhan, gunakan ROIIC — jangan menyamarkan ROIC historis stok sebagai ROIIC.

## 4. Jangkar Historis untuk Asumsi Nilai Terminal

- Batas atas pertumbuhan perpetual (g) = PDB nominal jangka panjang (AS ~4%, China tergantung basis perhitungan ~5–6%); melampaui ini secara implisit berarti perusahaan "akhirnya menelan seluruh ekonomi".
- Implied exit P/FCF (keluaran otomatis `dcf.py`) harus dibandingkan dengan multiple saat ini dari pembanding yang sudah matang: jika exit multiple > 25x tetapi asumsi pertumbuhan steady-state hanya 3%, nilai terminal secara diam-diam terlalu optimistis.
- Competitive Advantage Period (CAP): periode return berlebih (excess return) yang melampaui 15–20 tahun secara historis sangat jarang terjadi; secara default biarkan ROIIC pada periode nilai terminal konvergen ke WACC (lihat disiplin nilai terminal di `valuation-methods.md`).

## 5. Aturan Penggunaan (Wajib)

1. Setiap asumsi kunci dalam DCF/skenario harus diberi anotasi **persentil base rate** (misalnya "CAGR 18% selama 5 tahun ≈ persentil ke-85 historis").
2. Jika asumsi berada di atas persentil ke-80 → wajib menyertakan alasan struktural + indikator leading yang dapat diverifikasi, jika tidak maka harus diturunkan.
3. Skenario bear di antara tiga skenario tidak boleh lebih baik dari peristiwa persentil ke-30 historis ("skenario bear masih tumbuh 10%" biasanya adalah lelucon).
4. Saat laporan mengutip angka dari file ini, cantumkan sumber "base rate empiris, bersumber dari riset jangka panjang Mauboussin/McKinsey", jangan menyamarkannya sebagai statistik presisi.
