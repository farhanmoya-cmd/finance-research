# Aturan Pemilihan dan Eksekusi Lampiran Industri

File ini adalah satu-satunya pintu masuk manusia-terbaca untuk klasifikasi industri. Identifikasi dahulu kolam laba (profit pool) utama perusahaan dalam rantai nilai, baru kemudian baca lampiran yang sesuai; jangan hanya memilih secara mekanis berdasarkan label perusahaan atau nama GICS.

## 1. Protokol Pemilihan

1. Pilih satu lampiran utama berdasarkan kontribusi nilai dalam 3–5 tahun ke depan, dinilai bersama dari proporsi pendapatan, laba ternormalisasi, invested capital, dan bobot valuasi.
2. Hanya muat lampiran sekunder jika bisnis tersebut akan mengubah KPI, model arus kas, atau metode valuasi.
3. Perusahaan holding atau dengan tiga segmen penting atau lebih harus dipecah dengan SOTP; setiap segmen menggunakan lampiran yang sesuai, sementara level grup mencantumkan net debt, biaya kantor pusat, dan cross-holding secara terpisah.
4. Jika tidak ada yang cocok sepenuhnya, pilih lampiran dengan model ekonomi yang paling mendekati, dan tulis dengan jelas di laporan bagian mana yang cocok dan bagian mana yang tidak tercakup.
5. Nama tabel, nama field, dan kalimat kesimpulan wajib dalam lampiran industri adalah persyaratan semantik. Terjemahkan secara lengkap sesuai bahasa laporan, jangan mempertahankan label template bahasa Mandarin dalam laporan berbahasa Inggris, atau sebaliknya.

## 2. Matriks Routing

| Lampiran Utama | Batas Penerapan | Metode Valuasi Utama | KPI Wajib | Lampiran Sekunder yang Umum |
|---|---|---|---|---|
| [SaaS](../industries/saas.md) | Software berbasis subscription atau usage-based | Reverse DCF, DCF, EV/ARR | NRR/RPO, efisiensi akuisisi pelanggan, Rule of 40 | Internet/platform, hardware |
| [Semikonduktor](../industries/semiconductors.md) | Chip, foundry, equipment, material, EDA/IP, test-packaging | DCF lintas siklus, EV/EBITDA, P/E | Siklus inventori, ASP/unit, yield/utilisasi | Hardware, industrial |
| [Perbankan](../industries/banks.md) | Bank berlisensi yang menghimpun deposit dan menanggung risiko kredit | Residual income, P/TBV-ROTCE | NIM, deposit beta, biaya kredit, CET1 | Pembayaran/fintech, pasar modal |
| [Asuransi](../industries/insurance.md) | Asuransi umum, asuransi jiwa, asuransi kesehatan, reasuransi | P/B-ROE, P/EV, residual income | Combined ratio/VNB, reserve, solvabilitas | Pasar modal |
| [Farmasi](../industries/pharma.md) | Bisnis inti berupa riset dan komersialisasi obat | rNPV per aset, SOTP | PoS (probability of success), katalis, LOE (loss of exclusivity), cash runway | Layanan kesehatan |
| [Layanan Kesehatan/Alat Medis/CRO-CDMO](../industries/healthcare-services.md) | Rumah sakit, klinik, alat medis, diagnostik, outsourcing riset dan produksi | DCF, EV/EBITDA, SOTP | Volume/utilisasi, reimbursement, order/unit economics | Farmasi, industrial |
| [Konsumer](../industries/consumer.md) | Brand, retail, restoran, produk konsumen | DCF, P/E, EV/EBITDA | Mix volume-harga, same-store sales, sell-through, inventori | Internet/platform, hardware |
| [Energi](../industries/energy.md) | Upstream minyak-gas, midstream, refining, dan energi terintegrasi | NAV aset, DCF siklus | Reserve/decline rate, full cost, hedging | Utilitas, industrial berbasis kimia |
| [Utilitas](../industries/utilities.md) | Air-listrik-gas teregulasi, pembangkit listrik kompetitif, infrastruktur kontrak jangka panjang | Rate-base, DDM, DCF | Allowed vs earned ROE, pembiayaan, tagihan konsumen | Energi, REIT |
| [Internet/Platform](../industries/internet-platform.md) | Iklan, e-commerce, local life service, platform internet | SOTP segmen, DCF | Engagement pengguna, tingkat monetisasi, GMV/take rate | Pembayaran, SaaS, media & gaming |
| [Pembayaran/Fintech](../industries/payments-fintech.md) | Jaringan kartu, acquiring, dompet digital, BNPL, platform transaksi | DCF, EV/pendapatan, P/E | TPV, net take rate, vintage kerugian (loss vintage) | Perbankan, pasar modal |
| [Infrastruktur Pasar Modal](../industries/capital-markets.md) | Asset management, bursa, broker, lembaga rating | DCF, P/E, driver AUM/volume transaksi | AUM/net inflow atau volume transaksi, tarif fee, modal | Perbankan, pembayaran |
| [Properti/REIT](../industries/reits.md) | Equity REIT, mREIT, developer | NAV, P/AFFO, DDM | FFO/AFFO, same-store NOI, cap rate, dinding jatuh tempo utang | Utilitas, perbankan |
| [Industrial/Mesin](../industries/industrials.md) | Peralatan, otomasi, aerospace, manufaktur rekayasa | DCF siklus menengah, EV/EBITDA | Order, book-to-bill, backlog, aftermarket | Semikonduktor, hardware |
| [Telekomunikasi](../industries/telecom.md) | Operator mobile/fixed-line, menara, komunikasi satelit | DCF, SOTP, yield dividen | ARPU/churn, capex, spektrum, cakupan dividen | REIT, media |
| [Otomotif/EV](../industries/autos-ev.md) | OEM mobil dan perusahaan dengan ekonomi inti berbasis kendaraan utuh | DCF siklus, SOTP | Unit economics, titik impas volume penjualan, inventori/runway | Hardware, konsumer |
| [Logam/Pertambangan](../industries/metals-mining.md) | Mining company dan pengembang eksplorasi | NAV per tambang, metode opsi | AISC/cost curve, cadangan (reserve), umur tambang | Industrial, energi |
| [Penerbangan/Transportasi](../industries/transport.md) | Penerbangan, bandara, kereta, pelayaran, kurir/logistik | DCF siklus, NAV, EV/EBITDA | Unit revenue/cost, load factor, order book kapasitas | Utilitas, REIT |
| [Gaming/Media/Content IP](../industries/media-gaming.md) | Gaming, film-TV, musik, penerbitan, streaming, lisensi IP | IP SOTP, DCF, EV/subscriber | Pengguna/audiens, pembayaran, ROI konten, amortisasi | Internet/platform, konsumer |
| [Hardware/Elektronik Konsumen/AI Server](../industries/hardware.md) | Device, perangkat end-user, server, dan sistem hardware | DCF siklus, EV/EBITDA, SOTP | Unit/ASP/BOM, inventori, konsentrasi pelanggan-supplier | Semikonduktor, SaaS, industrial |

## 3. Pintu Masuk Data Primer yang Dapat Dieksekusi

Pintu masuk berikut digunakan untuk menemukan data mentah secara cepat; untuk perusahaan spesifik tetap utamakan pengajuan regulator lokal, IR perusahaan, dan catatan kaki dengan definisi lengkap.

| Industri | Pintu Masuk Resmi atau Primer |
|---|---|
| Pengajuan perusahaan umum | [SEC EDGAR](https://www.sec.gov/edgar/search/) · [HKEXnews](https://www.hkexnews.hk/) · [Cninfo (巨潮资讯)](https://www.cninfo.com.cn/) |
| SaaS / Internet / Konsumer / Hardware | IR perusahaan dan pengajuan regulasi; data pengguna atau channel hanya sebagai bukti pendukung |
| Semikonduktor | [WSTS](https://www.wsts.org/) · [SIA](https://www.semiconductors.org/) · [SEMI](https://www.semi.org/en/market-data) |
| Perbankan / Pembayaran | [FDIC BankFind Suite](https://banks.data.fdic.gov/bankfind-suite/) · [FFIEC CDR](https://cdr.ffiec.gov/public/) · [BIS payments](https://www.bis.org/statistics/payment_stats.htm) · [People's Bank of China](https://www.pbc.gov.cn/) |
| Asuransi | [NAIC](https://content.naic.org/industry/financial-data) · [EIOPA statistics](https://www.eiopa.europa.eu/tools-and-data/insurance-statistics_en) · [National Financial Regulatory Administration China](https://www.nfra.gov.cn/) |
| Farmasi / Kesehatan | [ClinicalTrials.gov](https://clinicaltrials.gov/) · [FDA databases](https://www.fda.gov/drugs/drug-approvals-and-databases) · [CMS datasets](https://data.cms.gov/) · [NMPA](https://www.nmpa.gov.cn/) |
| Energi / Utilitas | [EIA](https://www.eia.gov/) · [FERC eLibrary](https://elibrary.ferc.gov/eLibrary/search) · [NERC](https://www.nerc.com/) |
| Pasar Modal | [SEC Investment Adviser Public Disclosure](https://adviserinfo.sec.gov/) · [FINRA statistics](https://www.finra.org/rules-guidance/guidance/reports-studies) · [CFTC market data](https://www.cftc.gov/MarketReports/index.htm) |
| Properti / REIT | Supplemental package perusahaan · [Nareit data](https://www.reit.com/data-research) · data registrasi tanah dan properti lokal |
| Telekomunikasi | [FCC reports and data](https://www.fcc.gov/reports-research) · [Ofcom data](https://www.ofcom.org.uk/research-and-data/) · [Statistik Ministry of Industry and Information Technology China](https://www.miit.gov.cn/gxsj/index.html) |
| Otomotif | [NHTSA](https://www.nhtsa.gov/data) · [ACEA](https://www.acea.auto/figure/) · [China Association of Automobile Manufacturers](https://www.caam.org.cn/) |
| Logam / Pertambangan | [USGS mineral statistics](https://www.usgs.gov/centers/national-minerals-information-center) · [LME market data](https://www.lme.com/en/market-data) · [CME metals](https://www.cmegroup.com/markets/metals.html) |
| Penerbangan / Transportasi | [IATA economics](https://www.iata.org/en/publications/economics/) · [BTS](https://www.bts.gov/) · [State Post Bureau of China](https://www.spb.gov.cn/) |
| Gaming / Media | [Steamworks statistics](https://store.steampowered.com/stats/) · [FCC media data](https://www.fcc.gov/media) · regulator penerbitan, penyiaran, dan film lokal |

Basis data berbayar atau media industri dapat membantu menemukan petunjuk, tetapi tidak boleh menggantikan sumber primer yang tersedia. Setiap kutipan wajib mencatat URL, tanggal publikasi, periode data, definisi, dan tanggal pengambilan data.

## 4. Registrasi dan Review Proyeksi

Kesimpulan industri harus ditulis sebagai proyeksi yang dapat ditelusuri, bukan opini yang bersifat umum. Setiap proyeksi inti minimal mencatat:

| Field | Persyaratan |
|---|---|
| Objek Proyeksi | KPI, harga, margin, peristiwa, atau variabel valuasi yang jelas |
| Nilai Baseline dan Tanggal Cutoff | Tulis dengan jelas nilai saat ini, periode, sumber |
| Rentang dan Jangka Waktu Proyeksi | Berikan rentang, arah, dan tanggal verifikasi yang jelas |
| Driver dan Indikator Leading | 2–4 variabel yang dapat diobservasi beserta ambangnya |
| Kondisi Penggugur (Invalidation) | Definisikan masing-masing penggugur upside dan downside |
| Hasil Review | Hit/partial hit/miss/tidak dapat diverifikasi |
| Atribusi Error | Data, timing, model, shock eksternal, atau kesalahan tesis |
| Penulisan Ulang Model | Sesuaikan asumsi, probabilitas skenario, atau sumber data; tidak boleh menulis ulang proyeksi asli setelah fakta terjadi |

Saat memperbarui laporan, pertahankan proyeksi lama beserta timestamp-nya, tambahkan baris review baru. Perubahan harga saham hanya dapat dijadikan salah satu hasil pasar, tidak dapat membuktikan sendiri bahwa proyeksi operasional benar atau salah; wajib mereview secara terpisah KPI operasional, jalur katalis, multiple valuasi, dan total return.
