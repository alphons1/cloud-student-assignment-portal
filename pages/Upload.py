import streamlit as st
from aws_utils import upload_file
from database import log_upload

st.title("Upload Your File")


with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
        width=120
    )

    st.markdown("---")

    st.write("Cloud-Based Student Assignment Management System")

uploaded_file = st.file_uploader(
    "Choose file"
)

if uploaded_file:

    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"Size: {uploaded_file.size} bytes")

    if st.button("Upload"):

        upload_file(uploaded_file)

        log_upload(
            uploaded_file.name,
            uploaded_file.size
        )

        st.success(
            "File uploaded successfully!"
        )