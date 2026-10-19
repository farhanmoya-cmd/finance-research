# Lampiran Riset Mendalam Industri Hardware/Elektronik Konsumen/Server AI

Berlaku untuk elektronik konsumen, perangkat komputasi, peralatan jaringan, server, sistem storage, dan perusahaan yang berbasis penjualan sistem hardware. Value chip menggunakan `industries/semiconductors.md`; software subscription dan jasa menggunakan `industries/saas.md`.

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

- Pendapatan harus diurai menjadi units, ASP, mix produk, inventori saluran, nilai tukar, dan M&A; narasi AI atau produk baru tidak dapat menggantikan bridge pengiriman dan margin kotor.
- Bedakan sell-in dan sell-through. Pengisian ulang (restocking) inventori saluran akan mempercepat pencatatan pendapatan, tetapi tidak menciptakan permintaan akhir.
- BOM, konsentrasi pemasok, pembayaran muka kapasitas (capacity prepayment), komitmen pembelian, dan kecepatan penurunan biaya menentukan margin kotor; hanya melihat harga jual akan menghasilkan penilaian yang salah.
- Perangkat sekali jual (one-time device) dinilai terpisah dari jasa/consumable/software bermargin tinggi, verifikasi apakah basis instalasi (installed base) benar-benar membentuk pendapatan recurring.

## 2. Sumber Informasi & Mekanisme Kewajaran

1. Pengajuan perusahaan, pengungkapan segmen/produk, komitmen pembelian, inventori, dan catatan konsentrasi pelanggan.
2. Pengungkapan primer perusahaan hulu-hilir, data pengiriman bea cukai/regulasi, dan verifikasi silang rantai pasok.
3. Inventori saluran, aktivasi ritel, dan survei terminal; sampel serta basis sell-in/sell-through harus dicantumkan.
4. Estimasi teardown produk/BOM hanya bisa menjadi bukti rentang, dan harus direkonsiliasi dengan margin kotor perusahaan dan pengungkapan pemasok.

## 3. Pohon Penggerak Nilai

```text
Pendapatan hardware = units × ASP × mix produk/regional
Margin kotor hardware = pendapatan - BOM - manufaktur/logistik - garansi - insentif saluran
Pendapatan jasa = basis instalasi aktif × attach rate × ARPU
Nilai = arus kas hardware ternormalisasi lintas siklus + nilai jasa recurring - risiko inventori/komitmen/konsentrasi
```

## 4. Kamus KPI Inti

| Model | KPI Wajib | Jebakan Basis |
|---|---|---|
| Elektronik konsumen | sell-through, aktivasi, ASP, siklus ganti perangkat, inventori saluran | sell-in disamarkan sebagai permintaan akhir |
| Server AI | pengiriman/rack, ASP, BOM GPU/jaringan/power, pendinginan cair, siklus pengiriman | komponen harga tinggi yang lewat (pass-through) mendongkrak pendapatan, menekan margin |
| Perangkat jaringan/enterprise | pesanan, backlog, book-to-bill, pendapatan tangguhan (deferred revenue), attach jasa | pelonggaran supply menciptakan lonjakan pengiriman satu kali |
| Perangkat+jasa | basis instalasi, tingkat perpanjangan/consumable, ARPU jasa, churn | basis instalasi nominal tidak sama dengan basis instalasi aktif |

## 5. Struktur Model Keuangan

- Bangun model units × ASP × mix per produk; jelaskan asumsi permintaan akhir, pangsa pasar, dan inventori saluran.
- BOM minimal dipisah komputasi inti, storage, jaringan, power/pendinginan, manufaktur casing, dan garansi; lakukan sensitivitas harga komponen kunci.
- Bangun bridge inventori dan komitmen pembelian, identifikasi risiko restocking akibat kekurangan pasokan, over-procurement, dan impairment.
- Jasa/software menggunakan model cohort basis instalasi, margin hardware dan pendapatan recurring dimodelkan terpisah.

## 6. Metode Valuasi

- Hardware matang: DCF lintas siklus, EV/EBITDA, P/E; menggunakan margin kotor ternormalisasi dan siklus inventori.
- Sistem AI pertumbuhan tinggi: reverse DCF menguji pendapatan, pass-through BOM, pangsa pasar, dan margin steady state.
- Perusahaan campuran: SOTP untuk hardware, jasa/software, bisnis pembiayaan, dikurangi pembiayaan pelanggan dan liabilitas garansi.
- Aset desain/merek bisa diberi premium, tetapi harus diverifikasi dengan ROIC, retensi, dan bukti pricing.

## 7. Fokus Pola Laporan Keuangan

Jembatani units, ASP, mix, BOM, biaya pengiriman, insentif saluran, impairment inventori, dan pendapatan jasa. Guidance harus diverifikasi silang dengan pengiriman pemasok, komitmen pembelian, dan permintaan akhir.

## 8. Moat & Penilaian Kompetitif

Periksa merek, lock-in ekosistem, saluran distribusi, daya tawar rantai pasok, desain sistem, layanan purna jual, dan siklus sertifikasi. Kekurangan pasokan jangka pendek, pasokan chip tunggal, atau subsidi saja tidak membentuk keunggulan berkelanjutan.

## 9. Red Flag, Bukti Sanggahan & Kesalahpahaman Umum

- Sell-in saluran naik tapi aktivasi, sell-through, atau pangsa pasar terminal menurun.
- Pertumbuhan inventori dan komitmen pembelian lebih tinggi dari pendapatan secara berkelanjutan, dan proteksi pembatalan tidak memadai.
- Pertumbuhan tinggi pendapatan server AI berasal dari pass-through GPU harga tinggi, pertumbuhan margin kotor absolut dan ROIC belum membaik.
- Konsentrasi tinggi pada pelanggan atau pemasok, tapi belum dibuat skenario untuk harga, pengiriman, dan substitusi.
- Attach jasa tidak sepadan dengan basis instalasi, narasi pendapatan recurring tidak bisa divalidasi.

## 10. Persyaratan Output Laporan

Nama tabel, field, dan kalimat kesimpulan wajib di bagian ini harus diterjemahkan lengkap sesuai bahasa laporan; tidak boleh mencampur bahasa. Selain template utama, wajib ditambahkan:

### Bridge Units-ASP-BOM (Wajib)

| Produk | Units | ASP | Pendapatan | BOM/Biaya per Unit | Margin Kotor (%) | Driver YoY | Sumber |
|---|---:|---:|---:|---:|---:|---|---|

### Tabel Inventori dan Konsentrasi (Wajib)

| Indikator | Nilai Terbaru | YoY | Persentil Historis | Ambang Risiko | Sumber |
|---|---:|---:|---:|---:|---|
| Hari inventori/inventori saluran | | | | | |
| Porsi 5 pelanggan terbesar | | | | | |
| Porsi 5 pemasok terbesar | | | | | |
| Komitmen pembelian/pendapatan 12 bulan ke depan | | | | | |

### Kalimat Kesimpulan Wajib

- "Penilaian saya: pertumbuhan pendapatan masing-masing dikontribusikan oleh units, ASP, dan mix sebesar ……, perubahan BOM/rantai pasok membuat margin kotor per unit ……."
- "Pengiriman, pangsa pasar, dan margin kotor steady state yang terimplikasi harga saham saat ini adalah ……; permintaan akhir dan inventori saluran akan terverifikasi pada tanggal ……."
</content>
