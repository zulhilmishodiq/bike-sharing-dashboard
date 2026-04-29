# 📊 Bike Sharing Data Analysis Dashboard

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis data terhadap penggunaan layanan bike sharing berdasarkan dataset yang tersedia. Analisis difokuskan pada faktor-faktor yang memengaruhi jumlah penyewaan sepeda, seperti kondisi cuaca dan jenis hari (hari kerja atau hari libur).

## Pertanyaan Bisnis

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda selama periode 2011–2012?

2. Bagaimana perbedaan pola penggunaan sepeda antara hari kerja dan hari libur?

## Insight

- Cuaca cerah menghasilkan jumlah penyewaan sepeda tertinggi.

- Kondisi cuaca buruk seperti hujan atau salju menurunkan jumlah penyewaan secara signifikan.

- Hari kerja memiliki tingkat penyewaan lebih tinggi dibandingkan hari libur.

- Sepeda lebih banyak digunakan sebagai sarana transportasi harian dibandingkan rekreasi.

## Rekomendasi

- Menambah jumlah sepeda pada kondisi cuaca cerah.

- Mengoptimalkan operasional saat cuaca buruk untuk efisiensi.

- Memberikan promo atau diskon pada hari libur untuk meningkatkan penggunaan.

## 🗂️ Struktur Direktori

```bash
submission/
├── dashboard/
│   ├── dashboard.py
│   ├── main_data.csv
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## 🚀 Panduan Menjalankan Aplikasi

### Clone Repositori

Langkah pertama, unduh proyek ini ke komputer lokal Anda menggunakan perintah berikut:

```
git clone https://github.com/dicodingacademy/ilt-datascience.git
```

### Instalasi Library

Instal semua dependensi yang dibutuhkan menggunakan pip:

```
pip install -r requirements.txt
```

### Menjalankan Dashboard

Jalankan perintah berikut pada terminal di dalam direktori proyek:

```
streamlit run dashboard/dashboard.py
```

atau

```
python -m streamlit run dashboard/dashboard.py
```

Aplikasi akan secara otomatis terbuka di browser default Anda.

## Catatan

Dashboard dibuat menggunakan Streamlit dan bertujuan untuk menyajikan hasil analisis secara interaktif dan mudah dipahami.
