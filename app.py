import streamlit as st

# Pengaturan halaman utama
st.set_page_config(
    page_title="Asisten Lab Kimia Organik",
    page_icon="🧪",
    layout="wide"
)

# Judul Aplikasi
st.title("🧪 Asisten Digital Laboratorium Kimia Organik")
st.write("Aplikasi bantu untuk identifikasi gugus fungsi senyawa organik dan perhitungan praktikum.")

# Membuat Menu menggunakan Tabs
tab1, tab2, tab3 = st.tabs([
    "🔍 Identifikasi Gugus Fungsi", 
    "🧮 Kalkulator Rendemen (Yield)", 
    "📚 Panduan Reagen"
])

# --- TAB 1: IDENTIFIKASI GUGUS FUNGSI ---
with tab1:
    st.header("Sistem Keputusan Identifikasi Gugus Fungsi")
    st.write("Pilih uji laboratorium yang dilakukan untuk melihat kemungkinan jenis senyawa organik Anda.")

    col1, col2 = st.columns(2)

    with col1:
        # Pilihan Uji Utama
        jenis_uji = st.selectbox(
            "Pilih Jenis Uji Laboratorium:",
            [
                "Uji Lucas (Alkohol)",
                "Uji Tollens (Aldehid/Keton)",
                "Uji Fehling (Aldehid Alifatik)",
                "Uji Iodoform (Metil Keton / Metil Karbinol)",
                "Uji Bromin / KMnO4 (Ikatan Rangkap)"
            ]
        )

    with col2:
        # Logika Dinamis berdasarkan Uji yang dipilih
        if jenis_uji == "Uji Lucas (Alkohol)":
            hasil = st.radio(
                "Pilih Hasil Pengamatan:",
                [
                    "Terbentuk fasa cair keruh/terpisah secara INSTAN (< 1 menit)",
                    "Terbentuk fasa cair keruh dalam waktu 5 - 10 menit",
                    "Tidak terbentuk kekeruhan / larutan tetap jernih"
                ]
            )
            
            st.markdown("### 📊 Kesimpulan Analisis:")
            if "INSTAN" in hasil:
                st.success("✨ **Kemungkinan Besar:** Alkohol Tersier (misalnya: *ters*-butanol). Alkohol tersier bereaksi sangat cepat dengan reagen Lucas via mekanisme Sn1.")
            elif "5 - 10 menit" in hasil:
                st.warning("⚠️ **Kemungkinan Besar:** Alkohol Sekunder (misalnya: 2-propanol). Bereaksi lambat pada suhu kamar.")
            else:
                st.info("ℹ️ **Kemungkinan Besar:** Alkohol Primer (misalnya: etanol). Tidak bereaksi pada suhu kamar.")

        elif jenis_uji == "Uji Tollens (Aldehid/Keton)":
            hasil = st.radio(
                "Pilih Hasil Pengamatan:",
                [
                    "Terbentuk cermin perak (endapan perak mengkilap di dinding tabung)",
                    "Tidak terbentuk cermin perak / larutan tetap bening"
                ]
            )
            
            st.markdown("### 📊 Kesimpulan Analisis:")
            if "Terbentuk cermin perak" in hasil:
                st.success("✨ **Gugus Fungsi Terdeteksi:** **Aldehid** (R-CHO). Aldehid mereduksi $Ag^+$ menjadi logam perak bebas.")
            else:
                st.info("ℹ️ **Gugus Fungsi Kemungkinan:** **Keton** (R-CO-R). Keton tidak mudah dioksidasi oleh reagen Tollens.")

        elif jenis_uji == "Uji Fehling (Aldehid Alifatik)":
            hasil = st.radio(
                "Pilih Hasil Pengamatan:",
                [
                    "Terbentuk endapan merah bata ($Cu_2O$)",
                    "Tetap berwarna biru tua / tidak ada perubahan"
                ]
            )
            
            st.markdown("### 📊 Kesimpulan Analisis:")
            if "merah bata" in hasil:
                st.success("✨ **Gugus Fungsi Terdeteksi:** **Aldehid Alifatik** (misalnya: formaldehid, asetaldehid).")
            else:
                st.info("ℹ️ **Gugus Fungsi Kemungkinan:** **Keton** atau **Aldehid Aromatik** (misalnya: benzaldehid, karena tidak bereaksi dengan Fehling).")

        elif jenis_uji == "Uji Iodoform (Metil Keton / Metil Karbinol)":
            hasil = st.radio(
                "Pilih Hasil Pengamatan:",
                [
                    "Terbentuk endapan kuning cerah dan berbau khas (Iodoform)",
                    "Tidak terbentuk endapan kuning"
                ]
            )
            
            st.markdown("### 📊 Kesimpulan Analisis:")
            if "Terbentuk endapan kuning" in hasil:
                st.success("✨ **Struktur Terdeteksi:** Mengandung gugus **Metil Keton** ($CH_3C=O$) atau **Metil Karbinol** ($CH_3CH-OH$). Contoh: Aseton atau Etanol.")
            else:
                st.info("ℹ️ **Kesimpulan:** Tidak mengandung gugus metil keton atau metil karbinol.")

        elif jenis_uji == "Uji Bromin / KMnO4 (Ikatan Rangkap)":
            hasil = st.radio(
                "Pilih Hasil Pengamatan:",
                [
                    "Warna cokelat bromin atau ungu KMnO4 HILANG (dekolorisasi)",
                    "Warna reagen tetap / tidak berubah"
                ]
            )
            
            st.markdown("### 📊 Kesimpulan Analisis:")
            if "HILANG" in hasil:
                st.success("✨ **Karakteristik Senyawa:** **Sifat Tak Jenuh** (Mengandung ikatan rangkap dua $C=C$ atau tiga $C\equiv C$).")
            else:
                st.info("ℹ️ **Karakteristik Senyawa:** **Sifat Jenuh** (Hanya mengandung ikatan tunggal alkana).")

# --- TAB 2: KALKULATOR RENDEMEN ---
with tab2:
    st.header("Kalkulator Hasil Sintesis (Yield)")
    st.write("Gunakan kalkulator ini untuk menghitung persentase rendemen setelah melakukan proses sintesis atau isolasi zat organik.")

    col_calc1, col_calc2 = st.columns(2)

    with col_calc1:
        massa_teoretis = st.number_input("Masukkan Massa Teoretis / Perhitungan (gram):", min_value=0.0, value=1.0, step=0.01)
        massa_nyata = st.number_input("Masukkan Massa Hasil Nyata / Penimbangan Lab (gram):", min_value=0.0, value=0.8, step=0.01)

    with col_calc2:
        if st.button("Hitung % Rendemen", type="primary"):
            if massa_teoretis > 0:
                rendemen = (massa_nyata / massa_teoretis) * 100
                st.metric(label="Persentase Rendemen", value=f"{rendemen:.2f} %")
                
                if rendemen > 90:
                    st.success("🎉 Luar biasa! Rendemen Anda sangat tinggi. Pastikan produk benar-benar kering dan murni.")
                elif 50 <= rendemen <= 90:
                    st.info("👍 Hasil yang bagus dan wajar untuk skala laboratorium akademis.")
                else:
                    st.warning("⚠️ Rendemen cukup rendah. Periksa kembali kemungkinan kehilangan zat saat proses penyaringan, rekristalisasi, atau ekstraksi.")
            else:
                st.error("Massa teoretis harus lebih besar dari 0.")

# --- TAB 3: PANDUAN REAGEN ---
with tab3:
    st.header("📋 Referensi Pembuatan Reagen Sederhana")
    st.write("Catatan cepat cara pembuatan reagen uji organik di laboratorium:")
    
    reagen_data = {
        "Nama Reagen": ["Reagen Lucas", "Reagen Tollens", "Reagen Fehling A", "Reagen Fehling B"],
        "Komposisi Utama": [
            "Anhidrat ZnCl2 dalam HCl pekat", 
            "Larutan AgNO3 dicampur NaOH dan NH4OH secukupnya", 
            "CuSO4.5H2O dalam air", 
            "K-Na-Tartrat (Garam Rochelle) dan NaOH dalam air"
        ],
        "Kegunaan": [
            "Membedakan jenis alkohol sekunder, primer, tersier.",
            "Menguji keberadaan gugus aldehid (uji cermin perak).",
            "Komponen tembaga untuk oksidasi aldehid alifatik.",
            "Menyediakan suasana basa dan agen pengompleks untuk tembaga."
        ]
    }
    st.table(reagen_data)
