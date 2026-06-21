import streamlit as st
from database import init_db

init_db()

st.set_page_config(
    page_title="Cloud Storage Dashboard",
    page_icon="☁️",
    layout="wide"
)

st.title("☁My Cloud Portal")

st.write("""
Upload assignments securely to AWS S3.
""")