import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# APLIKASI MATEMATIKA TERAPAN
# ANALISIS RANGKAIAN LISTRIK MENGGUNAKAN SPL
# =========================================================

st.set_page_config(
    page_title="Analisis Rangkaian Listrik",
    layout="wide"
)

st.title("⚡ Aplikasi Analisis Rangkaian Listrik")
st.subheader("Implementasi Matematika Terapan Menggunakan Python & Streamlit")

st.write("""
Aplikasi ini menggunakan konsep:
1. SPL (Sistem Persamaan Linear)
2. Matriks
3. Determinan
4. Vektor
5. Logika
6. Visualisasi Grafik
""")

st.divider()

# =========================================================
# INPUT
# =========================================================

st.header("📥 Input Nilai Komponen")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Resistor (Ohm)")
    R1 = st.number_input("R1", value=10.0)
    R2 = st.number_input("R2", value=8.0)
    R3 = st.number_input("R3", value=6.0)
    R4 = st.number_input("R4", value=4.0)
    R5 = st.number_input("R5", value=5.0)

with col2:
    st.subheader("Tegangan (Volt)")
    V1 = st.number_input("V1", value=12.0)
    V2 = st.number_input("V2", value=9.0)
    V3 = st.number_input("V3", value=6.0)

st.divider()

# =========================================================
# MODEL MATEMATIKA
# =========================================================

st.header("📘 Model Matematis")

st.latex(r'''
\begin{cases}
(R1+R3)I_1 - R3I_2 = V1 \\
-R3I_1 + (R2+R3+R4)I_2 - R4I_3 = V2 \\
-R4I_2 + (R4+R5)I_3 = V3
\end{cases}
''')

st.write("Bentuk Matriks:")

st.latex(r'''
AX = B
''')

# =========================================================
# MEMBENTUK MATRKS
# =========================================================

A = np.array([
    [R1 + R3, -R3, 0],
    [-R3, R2 + R3 + R4, -R4],
    [0, -R4, R4 + R5]
])

B = np.array([V1, V2, V3])

st.subheader("Matriks A")
st.write(A)

st.subheader("Matriks B")
st.write(B)

# =========================================================
# DETERMINAN
# =========================================================

st.header("🧮 Determinan Matriks")

determinan = np.linalg.det(A)

st.latex(r'\det(A)')

st.write("Nilai Determinan:", round(determinan, 2))

# =========================================================
# LOGIKA
# =========================================================

st.header("🧠 Analisis Logika")

if determinan == 0:
    st.error("Sistem tidak memiliki solusi unik!")
else:
    st.success("Sistem memiliki solusi unik.")

# =========================================================
# MENYELESAIKAN SPL
# =========================================================

st.header("📌 Penyelesaian SPL")

if determinan != 0:

    solusi = np.linalg.solve(A, B)

    I1 = solusi[0]
    I2 = solusi[1]
    I3 = solusi[2]

    st.subheader("Hasil Arus")

    st.write(f"I1 = {I1:.3f} Ampere")
    st.write(f"I2 = {I2:.3f} Ampere")
    st.write(f"I3 = {I3:.3f} Ampere")

    # =====================================================
    # VEKTOR
    # =====================================================

    st.header("➡️ Konsep Vektor")

    magnitude = np.sqrt(I1**2 + I2**2 + I3**2)

    st.latex(r'''
    |\vec{I}| = \sqrt{I_1^2 + I_2^2 + I_3^2}
    ''')

    st.write("Magnitude Vektor Arus:", round(magnitude, 3))

    # =====================================================
    # BOOLEAN & LOGIKA KOMPLEKS
    # =====================================================

    st.header("🔍 Status Sistem")

    overload = (I1 > 5) or (I2 > 5) or (I3 > 5)
    aman = (I1 < 5) and (I2 < 5) and (I3 < 5)

    if overload:
        st.error("⚠️ Sistem OVERLOAD")

    elif aman:
        st.success("✅ Sistem AMAN")

    else:
        st.warning("⚡ Sistem dalam kondisi NORMAL")

    # =====================================================
    # VISUALISASI GRAFIK
    # =====================================================

    st.header("📊 Visualisasi Grafik")

    arus = [I1, I2, I3]
    label = ['I1', 'I2', 'I3']

    fig, ax = plt.subplots()

    ax.bar(label, arus)

    ax.set_title("Grafik Arus Tiap Loop")
    ax.set_xlabel("Loop")
    ax.set_ylabel("Arus (Ampere)")

    st.pyplot(fig)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.info("""
Aplikasi ini dibuat menggunakan:
- Python
- Streamlit
- NumPy
- Matplotlib
""")