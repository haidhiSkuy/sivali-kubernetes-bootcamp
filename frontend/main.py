import streamlit as st
from dotenv import load_dotenv
load_dotenv()

predict_page = st.Page("src/send_image.py", title="Predict", icon=":material/add_circle:")
data_page = st.Page("src/patient_data.py", title="Patient Data", icon=":material/delete:")

pg = st.navigation([predict_page, data_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()