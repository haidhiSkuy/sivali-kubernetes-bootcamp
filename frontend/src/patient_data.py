import os
import psycopg2
import pandas as pd
import streamlit as st

def get_data():
    """Ambil data dari PostgreSQL dan return dalam format DataFrame"""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRESS_DB"),
            user=os.getenv("POSTGRESS_USER"),
            password=os.getenv("POSTGRESS_PASSWORD"),
            host=os.getenv("POSTGRESS_HOST"),
            port=os.getenv("POSTGRESS_PORT")
        )
        cur = conn.cursor()

        # Query ambil data
        query = "SELECT patient_id, patient_name, alzheimer_status FROM patients"
        cur.execute(query)

        # Ambil hasilnya
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=["patient_id","Patient Name", "Alzheimer Status"])

        # Tutup koneksi
        cur.close()
        conn.close()

        return df

    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return DataFrame kosong kalau error

# Tampilan Streamlit
st.title("📊 Patient Data")
st.write("Ini halaman buat melihat data pasien dari PostgreSQL!")

# Fetch & tampilkan data
df = get_data().reset_index(drop=True)  # Hilangkan index
if not df.empty:
    st.table(df.style.hide(axis="index"))
else:
    st.write("Tidak ada data yang ditemukan.")
