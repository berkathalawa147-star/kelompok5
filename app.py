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

    st.title("Kalkulator SPL Rangkaian Listrik")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Input Resistor")

        R1 = st.number_input("R1", value=4.0)
        R2 = st.number_input("R2", value=6.0)
        R3 = st.number_input("R3", value=2.0)
        R4 = st.number_input("R4", value=5.0)
        R5 = st.number_input("R5", value=3.0)

    with col2:

        st.subheader("Input Tegangan")

        V1 = st.number_input("V1", value=12.0)
        V2 = st.number_input("V2", value=10.0)
        V3 = st.number_input("V3", value=8.0)

    st.subheader("Model Matematis")

    st.latex(r"""
    \begin{cases}
    (R1+R3)I_1 - R3I_2 = V1 \\
    -R3I_1 + (R2+R3+R4)I_2 - R4I_3 = V2 \\
    -R4I_2 + (R4+R5)I_3 = V3
    \end{cases}
    """)

    A = np.array([
        [R1 + R3, -R3, 0],
        [-R3, R2 + R3 + R4, -R4],
        [0, -R4, R4 + R5]
    ])

    B = np.array([V1, V2, V3])

    determinan = np.linalg.det(A)

    st.write("### Determinan")
    st.write(f"Det(A) = {determinan:.2f}")

    if determinan != 0:

        hasil = np.linalg.solve(A, B)

        I1, I2, I3 = hasil

        st.write("## Hasil Arus")

        c1, c2, c3 = st.columns(3)

        c1.metric("I1", f"{I1:.2f} A")
        c2.metric("I2", f"{I2:.2f} A")
        c3.metric("I3", f"{I3:.2f} A")

        magnitude = np.sqrt(I1**2 + I2**2 + I3**2)

        st.write("### Magnitude Vektor")

        st.latex(r"|\vec{I}| = \sqrt{I_1^2 + I_2^2 + I_3^2}")

        st.write(f"Hasil = {magnitude:.2f}")

        overload = (I1 > 5) or (I2 > 5) or (I3 > 5)

        if overload:
            st.error("⚠ Sistem OVERLOAD")

        else:
            st.success("Sistem NORMAL")

    else:
        st.error("Sistem tidak memiliki solusi unik.")

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

   elif menu == "Grafik Arus":

    st.title("Grafik Arus Listrik")

    if "I1" in st.session_state:

        I1 = st.session_state["I1"]
        I2 = st.session_state["I2"]
        I3 = st.session_state["I3"]

        label = ["I1", "I2", "I3"]
        data = [I1, I2, I3]

        fig, ax = plt.subplots()

        ax.bar(label, data)

        ax.set_title("Grafik Arus Hasil SPL")

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
