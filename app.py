import streamlit as st
from database import init_db

init_db()

st.set_page_config(
    page_title="Cloud Storage Dashboard",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ My Cloud Portal")

st.markdown("""
### Welcome to the Cloud-Based Student Assignment Management System

Manage your assignments securely using **Amazon Web Services (AWS)**.

This platform demonstrates how cloud technologies can be used to upload,
store and manage files through a modern web application.

#### Features

- ☁️ Secure cloud storage with Amazon S3
- 🔒 Identity & Access Management (AWS IAM)
- 📤 Upload assignments instantly
- 📊 View file statistics and storage usage
- 🐍 Built with Python & Streamlit

---
""")