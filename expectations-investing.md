# Expectations Investing (Investasi Berbasis Perbedaan Ekspektasi) — Alur Analisis Utama Laporan

Gagasan inti (Rappaport & Mauboussin): harga saham bukanlah proyeksi masa depan, melainkan **sekumpulan ekspektasi yang sudah dipriced-in**. Output dari riset bukanlah "perusahaan ini bagus atau tidak", melainkan "**ekspektasi yang implisit dalam harga pasar vs ekspektasi saya, di mana perbedaannya, atas dasar apa, dan kapan akan terkoreksi**". Tanpa perbedaan ekspektasi (expectations gap, atau variant view) yang dapat dinyatakan secara jelas, laporan hanyalah kompilasi data.

## 1. Kerangka Tiga Langkah

**Langkah Pertama: Membaca Ekspektasi Pasar (Bukan Memprediksi, Hanya Mendekode)**
- Gunakan reverse DCF (blok `reverse` pada `dcf.py`) untuk menguraikan dari harga saat ini: steady-state FCF yang implisit, pendapatan yang dibutuhkan, dan implied CAGR.
- Gunakan dekomposisi PVGO (blok `pvgo` pada `dcf.py`): `harga saat ini = nilai pertumbuhan nol (E/r) + nilai opsi pertumbuhan (PVGO)`, untuk menghitung **berapa persen dari harga saat ini sebenarnya adalah pembayaran untuk "pertumbuhan yang belum terjadi"**.
- Terjemahkan ekspektasi implisit ke dalam kerangka referensi yang dapat dipahami: "secara implisit menuntut pertumbuhan X% selama 10 tahun ke depan — secara historis, perusahaan yang kapitalisasi pasarnya sudah melebihi $Y dan mampu melakukan ini hanya N perusahaan" (bandingkan dengan `base-rates.md`).

**Langkah Kedua: Membangun Ekspektasi Sendiri (Dengan Disiplin Perspektif Eksternal/Outside View)**
- Untuk setiap driver kunci (pendapatan, margin, return reinvestasi), cek dahulu distribusi historis di `base-rates.md`, lalu posisikan asumsi sendiri di dalam distribusi tersebut ("asumsi pertumbuhan saya berada di persentil ke-80 historis").
- Asumsi yang melampaui base rate wajib disertai **alasan struktural** (sumber moat, posisi pada kurva penetrasi industri, indikator leading yang dapat diverifikasi); "manajemen percaya diri" bukan alasan yang valid.

**Langkah Ketiga: Menyatakan Perbedaan Ekspektasi dan Jalur Koreksi**
- Tulis perbedaan pandangan dalam bentuk proposisi yang dapat digugurkan (falsifiable): "Pasar berpikir X, saya berpikir Y, karena bukti Z; sinyal verifikasinya adalah W (dengan titik waktu)".
- Identifikasi **pemicu koreksi ekspektasi (expectations revision trigger)**: KPI pada kuartal mana yang akan memaksa pasar mengubah pricing-nya; undervaluation tanpa pemicu bisa tetap undervalued dalam waktu lama.
- Nilai secara terpisah **variabel yang paling mungkin diperdagangkan pasar dalam 1–3 bulan ke depan**: variabel ini bisa berbeda dari penilaian nilai intrinsik. Misalnya, valuasi jangka panjang sudah wajar, tetapi laporan keuangan baru saja membuktikan satu variabel yang sangat kontroversial, sehingga pasar jangka pendek masih mungkin terus melakukan upward repricing; risiko jalur seperti ini wajib ditulis di bab pertama.

## 2. Tabel Expectations Gap (Kewajiban Bab Pertama)

| Driver Kunci | Implisit Pasar (reverse DCF/konsensus) | Ekspektasi Saya | Persentil Base Rate | Dasar Perbedaan | Sinyal Verifikasi & Titik Waktu |
|---|---|---|---|---|---|
| CAGR Pendapatan (5 tahun) | | | | | |
| Margin Operasi Steady-State | | | | | |
| Return Reinvestasi (ROIIC) | | | | | |
| Multiple Terminal/Pertumbuhan Perpetual (g) | | | | | |
| **Arah Net Expectations Gap** | Bullish / Bearish / Netral | | | | |

Setelah tabel Gap, wajib ditambahkan satu kalimat "variabel yang diperdagangkan pasar": dalam 1–3 bulan ke depan, apa yang paling mungkin diperdagangkan pasar lebih dulu, dan pembuktian/penggugur upside/downside mana yang akan mengubah penilaian tersebut.

## 3. Uji Pandangan Independen (Wajib)

Sebelum laporan selesai, jawab pertanyaan berikut; jika tidak bisa dijawab, tidak boleh memberikan rekomendasi "beli/kurangi" (hanya boleh "observasi/wait and see"):

1. Apa **perbedaan tunggal terbesar** antara saya dan konsensus? Satu kalimat.
2. **Mengapa** perbedaan ini ada (kesalahan apa yang dapat diidentifikasi dari pasar: ekstrapolasi, anchoring, arbitrase horizon waktu, atau perubahan struktural yang belum disadari)?
3. Jika saya salah, **paling cepat kapan, melalui data apa** hal itu akan terlihat?

## 4. Hubungan dengan Modul Lain

- Reverse DCF naik status dari "salah satu metode valuasi" menjadi **kerangka pembuka bab pertama**; DCF forward/EPV/relative valuation bertugas menjawab "menurut ekspektasi saya, ini bernilai berapa".
- Arah expectations gap wajib konsisten dengan label kalibrasi di Bagian 8: jika label "undervalued" tetapi tabel Gap menunjukkan ekspektasi saya lebih rendah dari implisit pasar → ada kontradiksi, harus ditelusuri ulang mana yang salah.
- Mode laporan keuangan: setiap kali ada laporan keuangan, rekonsiliasi tiga garis "aktual vs ekspektasi pasar vs ekspektasi saya"; saat expectations gap terverifikasi/tergugurkan harus dicatat secara eksplisit (scoring tesis).
