import base64
from PIL import Image
from faker import Faker 
import streamlit as st
from io import BytesIO
from src.request_predict import SendRequest

send_request = SendRequest()

st.title("🔍 Alzheimer Prediction")

name_input = st.text_input("Nama Pasien")

# Kalau kosong, isi otomatis pakai Faker
if not name_input:
    fake = Faker()
    name_input = fake.name()

st.write(f"**Nama Pasien:** {name_input}")


st.write("Upload gambar buat diprediksi!")
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])
if uploaded_file:
    image_data = uploaded_file.read()
    encoded_image = base64.b64encode(image_data).decode("utf-8")  

    # Buka gambar dengan PIL
    image = Image.open(BytesIO(image_data))

    # Resize gambar (misalnya, width=300, height otomatis menyesuaikan aspek rasio)
    max_width = 150
    w_percent = (max_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    resized_image = image.resize((max_width, h_size))

    # Tampilkan gambar yang sudah diresize
    st.image(resized_image)
    
    response = send_request.send_predict_request(encoded_image, name_input)
    st.write(f"Prediction : {response['prediction']}")
