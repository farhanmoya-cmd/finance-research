# Lampiran Riset Mendalam Industri Infrastruktur Pasar Modal

Berlaku untuk manajer aset (asset manager), bursa dan lembaga kliring, broker/investment bank, lembaga pemeringkat (rating agency), dan penyedia data pasar. Bank berlisensi deposit menggunakan `industries/banks.md`; jaringan pembayaran dan platform kredit konsumen menggunakan `industries/payments-fintech.md`.

## Daftar Isi

1. Prinsip Penggunaan
2. Sumber Informasi & Mekanisme Kewajaran
3. Pohon Penggerak Nilai
4. Kamus KPI Inti
5. Struktur Model Keuangan
6. Metode Valuasi
7. Fokus Pola Laporan Keuangan
8. Moat & Penilaian Kompetitif
9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum
10. Persyaratan Output Laporan

## 1. Prinsip Penggunaan

- Pisahkan dulu berdasarkan model bisnis. Manajer aset dilihat dari AUM dan net inflow; bursa dilihat dari volume transaksi, open interest, dan pendapatan data; broker dilihat dari aset klien, bisnis trading/bunga/investment banking; lembaga pemeringkat dilihat dari volume penerbitan dan subscription non-transaksional.
- Pisahkan beta pasar dari alpha struktural. Kenaikan AUM dari kenaikan harga aset, kenaikan volume transaksi dari volatilitas, tidak sama dengan peningkatan pangsa pasar atau nilai pelanggan.
- Modal regulasi, segregasi aset klien, dan likuiditas adalah batasan utama (first-order constraint) bagi broker. Pertumbuhan laba tidak boleh menutupi risiko net capital atau risiko tenor pendanaan.
- Efek jaringan bursa dan lembaga pemeringkat dibatasi regulasi; kesimpulan moat harus diverifikasi sekaligus dengan harga, pangsa pasar, multi-homing pelanggan, dan risiko substitusi kebijakan.

## 2. Sumber Informasi & Mekanisme Kewajaran

1. Pengajuan regulasi, laporan modal statutori dan aset klien, laporan periodik dana.
2. Data volume transaksi, open interest, listing, dan pengungkapan data pasar primer dari bursa/lembaga kliring.
3. Laporan keuangan perusahaan, laporan bulanan AUM/net inflow, pool fee investment banking dan catatan basis bisnis.
4. Statistik SEC IAPD, FINRA, CFTC, ESMA, dan regulator sekuritas lokal.

Pangsa pasar harus disatukan basisnya untuk produk, regional, kelas aset, dan periode; perubahan AUM diurai menjadi pasar, nilai tukar, net inflow, dan M&A.

## 3. Pohon Penggerak Nilai

```text
Pendapatan manajer aset = rata-rata AUM periode × tarif fee manajemen + performance fee
Pendapatan bursa = volume transaksi/kliring × tarif fee per unit + data pasar + listing/layanan teknologi
Pendapatan broker = aset klien × tingkat monetisasi + volume transaksi × pendapatan per unit + pool fee investment banking × pangsa
Pendapatan lembaga pemeringkat = volume penerbitan obligasi × tarif fee rating × pangsa + pendapatan subscription/data
Nilai = kualitas pendapatan × operating leverage × kebutuhan modal × daya tahan regulasi
```

## 4. Kamus KPI Inti

| Model | KPI Wajib | Jebakan Basis |
|---|---|---|
| Manajer aset | AUM, net inflow, tarif fee manajemen, performance fee, performa investasi | AUM akhir periode disamarkan sebagai AUM rata-rata periode; kenaikan pasar disamarkan sebagai net inflow |
| Bursa | ADV/volume kontrak, open interest, capture rate, ARR data | Siklus volatilitas; rebate belum dinetto |
| Broker | Aset klien, net new asset, pembiayaan margin, sensitivitas pendapatan bunga bersih, net capital | Tailwind suku bunga dianggap perpetual; basis sweep kas klien |
| Lembaga pemeringkat | Volume penerbitan, pangsa, fee per transaksi, pendapatan non-transaksi | Siklus refinancing dicampur dengan pertumbuhan struktural |

## 5. Struktur Model Keuangan

- Bangun model volume × harga per lini bisnis; minimal berikan tiga skenario bear/base/bull untuk aktivitas pasar.
- Bridge AUM manajer aset: awal periode + pasar/nilai tukar + net inflow + M&A = akhir periode.
- Broker: buat sensitivitas pendapatan bunga bersih terhadap suku bunga, kas klien, dan deposit beta; pisahkan tersendiri modal regulasi dan kapabilitas buyback.
- Untuk platform dengan fixed cost tinggi, modelkan secara eksplisit incremental margin; untuk bisnis broker yang padat modal, batasi ROE.

## 6. Metode Valuasi

- Manajer aset: DCF, P/E, EV/AUM (hanya untuk cross-check), tarif fee dan net inflow menentukan median.
- Bursa/lembaga pemeringkat: DCF, P/E, EV/EBITDA, pisahkan pendapatan data recurring dan pendapatan trading/penerbitan yang siklikal.
- Broker: P/TBV-ROTCE, residual income; modal berlebih dipisah tersendiri, jangan anggap seluruh kas sebagai bisa didistribusikan.
- Grup campuran gunakan SOTP, dikurangi biaya kantor pusat, defisit modal regulasi, dan double leverage.

## 7. Fokus Pola Laporan Keuangan

Jembatani per kuartal antara pasar/nilai tukar dan net inflow organik, volume transaksi dan capture rate, suku bunga dan pendapatan bunga bersih, tarif biaya dan incremental margin. Perubahan guidance harus dipisahkan antara asumsi pasar, pangsa pasar, pricing, dan aksi biaya.

## 8. Moat & Penilaian Kompetitif

Periksa jaringan likuiditas, embedding benchmark/rating, biaya peralihan data, kapabilitas distribusi, dan lisensi regulasi. Jika multi-homing pelanggan, substitusi gratis, kompresi tarif fee pasif, atau open interface regulasi terus melemahkan daya tawar harga, turunkan skor moat.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

- Menganggap AUM pasar bullish, volume transaksi dari volatilitas, atau spread suku bunga tinggi sebagai laba ternormalisasi.
- Hanya melaporkan total inflow, tidak melaporkan net inflow dana jangka panjang, redemption, dan mix tarif fee.
- Aset klien broker naik tapi net new asset, tingkat aktivitas, atau tingkat monetisasi menurun.
- Buyback mengonsumsi modal regulasi, atau menggunakan pendanaan jangka pendek untuk mendukung aset berdurasi panjang.
- Menuliskan pertumbuhan pendapatan data dari M&A sebagai pertumbuhan organik.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa. Selain template utama, wajib ditambahkan:

### Bridge Volume Aktivitas dan Aset (Wajib)

| Indikator | Awal Periode | Pasar/Nilai Tukar | Net Inflow atau Perubahan Organik | M&A | Akhir Periode | Sumber |
|---|---:|---:|---:|---:|---:|---|
| AUM / aset klien / basis volume transaksi | | | | | | |

### Tabel Kualitas Pendapatan dan Modal (Wajib)

| Bisnis | Volume | Tarif per Unit | Pendapatan | Siklikal/Recurring | Okupansi Modal | Asumsi Ternormalisasi |
|---|---:|---:|---:|---|---:|---|

### Kalimat Kesimpulan Wajib

- "Penilaian saya: dari laba saat ini, porsi yang berasal dari beta pasar, suku bunga, atau volatilitas adalah ……, pertumbuhan struktural yang berkelanjutan adalah ……."
- "AUM/aktivitas transaksi, tarif fee, dan margin laba ternormalisasi yang terimplikasi harga saham saat ini adalah ……; indikator dan tanggal paling awal yang dapat memverifikasi asumsi ini adalah ……."
</content>
