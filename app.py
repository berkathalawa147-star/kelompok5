import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# KONFIGURASI
# =====================================================

st.set_page_config(
    page_title=" Kelompok 5 Aplikasi Matematika Terapan",
    layout="wide"
)

# =====================================================
# SIDEBAR MENU
# =====================================================

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Home",
        "Kalkulator SPL",
        "Analisis Matriks",
        "Grafik Arus",
        "Tentang Aplikasi"
    ]
)

# =====================================================
# HALAMAN HOME
# =====================================================

if menu == "Home":

    st.title("Aplikasi Matematika Terapan")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",
        width=150
    )

    st.write("""
    Selamat datang di aplikasi matematika terapan berbasis Streamlit.

    Aplikasi ini menggunakan konsep:
    - SPL
    - Matriks
    - Determinan
    - Vektor
    - Logika Boolean
    """)

    st.success("Pilih menu di sidebar untuk mulai menggunakan aplikasi.")

# =====================================================
# HALAMAN SPL
# =====================================================

elif menu == "Kalkulator SPL":

    st.title("⚡ Kalkulator SPL")

    R1 = st.number_input("R1", value=4.0)
    R2 = st.number_input("R2", value=6.0)
    R3 = st.number_input("R3", value=2.0)
    R4 = st.number_input("R4", value=5.0)
    R5 = st.number_input("R5", value=3.0)

    V1 = st.number_input("V1", value=12.0)
    V2 = st.number_input("V2", value=10.0)
    V3 = st.number_input("V3", value=8.0)

    tombol = st.button("Hitung SPL")

    if tombol:

        A = np.array([
            [R1 + R3, -R3, 0],
            [-R3, R2 + R3 + R4, -R4],
            [0, -R4, R4 + R5]
        ])

        B = np.array([V1, V2, V3])

        hasil = np.linalg.solve(A, B)

        I1, I2, I3 = hasil

        # SIMPAN DATA
        st.session_state["grafik"] = [I1, I2, I3]

        st.success("Perhitungan berhasil")

        st.write(f"I1 = {I1:.2f}")
        st.write(f"I2 = {I2:.2f}")
        st.write(f"I3 = {I3:.2f}")
# =====================================================
# HALAMAN MATRIKS
# =====================================================

elif menu == "Analisis Matriks":

    st.title("Analisis Matriks")

    matrix = st.text_area(
        "Masukkan matriks (pisahkan angka dengan spasi)",
        "1 2 3\n4 5 6\n7 8 9"
    )

    try:

        rows = matrix.strip().split("\n")

        data = [list(map(float, row.split())) for row in rows]

        M = np.array(data)

        st.write("### Matriks")

        st.write(M)

        st.write("### Transpose")

        st.write(M.T)

        if M.shape[0] == M.shape[1]:

            st.write("### Determinan")

            st.write(np.linalg.det(M))

        else:
            st.warning("Determinan hanya untuk matriks persegi.")

    except:
        st.error("Format matriks salah.")

# =====================================================
# HALAMAN GRAFIK
# =====================================================

elif menu == "Grafik Arus":

    st.title("📈 Grafik Arus")

    if "grafik" in st.session_state:

        data = st.session_state["grafik"]

        label = ["I1", "I2", "I3"]

        fig, ax = plt.subplots()

        ax.bar(label, data)

        ax.set_title("Grafik Hasil SPL")

        ax.set_ylabel("Nilai Arus")

        st.pyplot(fig)

    else:

        st.warning("Silakan hitung SPL terlebih dahulu.")
# =====================================================
# HALAMAN TENTANG
# =====================================================

elif menu == "Tentang Aplikasi":

    st.title("ℹ Tentang")

    st.write("""
    Aplikasi ini dibuat oleh kelompok 5 untuk memenuhi tugas Matematika Terapan. 

    Konsep yang digunakan:
    - SPL
    - Matriks
    - Determinan
    - Vektor
    - Logika Boolean

    Dibuat menggunakan:
    - Python
    - Streamlit
    - NumPy
    - Matplotlib
    """)
