# Import library
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Mengatur konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Membaca data yang sudah dibersihkan
df = pd.read_csv('main_data.csv')
# Mengubah kolom tanggal menjadi datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Judul dashboard
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Dashboard ini menjawab dua pertanyaan bisnis utama terkait penggunaan sepeda.")

# Sidebar untuk filter
st.sidebar.header("🔍 Filter Data")

# Filter berdasarkan cuaca
selected_weather = st.sidebar.multiselect(
    "Pilih Cuaca",
    options=df['weathersit'].unique(),
    default=df['weathersit'].unique()
)

# Menerapkan filter
filtered_df = df[df['weathersit'].isin(selected_weather)]

# Menampilkan ringkasan data
st.subheader("📊 Ringkasan Data")

col1, col2 = st.columns(2)
# Menampilkan Total Penyewaan
col1.metric("Total Penyewaan", int(filtered_df['cnt'].sum()))
# Menampilkan Rata-rata harian
col2.metric("Rata-rata Harian", int(filtered_df['cnt'].mean()))

st.markdown("---")

# =========================
# PERTANYAAN BISNIS 1
# =========================
st.header("1️⃣ Pengaruh Cuaca terhadap Penyewaan Sepeda")

st.markdown("""
**Pertanyaan:**  
Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
""")

fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=filtered_df, ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.success("""
Insight:
- Cuaca cerah menghasilkan penyewaan tertinggi
- Semakin buruk cuaca, jumlah penyewaan menurun
""")

st.markdown("---")

# =========================
# PERTANYAAN BISNIS 2
# =========================
st.header("2️⃣ Hari Kerja vs Hari Libur")

st.markdown("""
**Pertanyaan:**  
Bagaimana perbedaan penyewaan antara hari kerja dan hari libur?
""")

fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=filtered_df, ax=ax)
ax.set_xticklabels(["Libur", "Kerja"])
ax.set_xlabel("Tipe Hari")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.success("""
Insight:
- Hari kerja memiliki jumlah penyewaan lebih tinggi
- Menunjukkan sepeda banyak digunakan untuk aktivitas rutin
""")

st.markdown("---")

# =========================
# SUPPORTING ANALYSIS
# =========================
st.header("📈 Tren Penyewaan (Pendukung Analisis)")

trend = filtered_df.groupby('dteday')['cnt'].sum()

fig, ax = plt.subplots()
trend.plot(ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.info("Grafik ini membantu melihat pola penggunaan dari waktu ke waktu.")

# FOOTER
st.markdown("---")
st.caption("Dashboard dibuat untuk mendukung analisis Bike Sharing Dataset")