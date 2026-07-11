import streamlit as st
import pandas as pd
import plotly.express as px
from aws_utils import get_files

st.title("Cloud-Based Student Assignment Management System")

# Sidebar
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
        width=120
    )
    st.markdown("---")
    st.write("Cloud Storage Portal")

# Custom metric styles
st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #262730;
    border: 1px solid #404040;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}
[data-testid="stMetricLabel"] {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
    color: #4CAF50 !important;
    font-size: 40px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
### AWS-Powered Assignment Management System

Store, manage and analyze files securely using Amazon S3.

Built with:
- AWS S3
- Python
- Streamlit
- SQLite
- AWS IAM
""")

# ✅ Define columns BEFORE using them
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Files Stored", len(df))

with col2:
    st.metric("Cloud Provider", "AWS")

with col3:
    # ✅ Moved the custom Region card here, after col3 is defined
    st.markdown("""
    <div style="
        background-color:#262730;
        border:1px solid #404040;
        border-radius:15px;
        padding:20px;
        text-align:center;
    ">
        <div style="color:white; font-size:18px; font-weight:600; margin-bottom:10px;">
            Region
        </div>
        <div style="color:#4CAF50; font-size:22px; font-weight:bold;">
            Singapore
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ Fetch files once
files = get_files()

# ✅ Guard df creation — only build chart if files exist
if files:
    df = pd.DataFrame(files)

    fig = px.bar(
        df,
        x="Filename",
        y="Size",
        color="Size",
        title="Storage Usage by File"
    )
    st.plotly_chart(fig, use_container_width=True, key="storage_chart")
else:
    st.warning("No files found.")

st.divider()

st.subheader("System Architecture")
st.code("""
                   User
                    │
                    ▼
            Streamlit Frontend
                    │
                    ▼
                Python Backend
                    ├── AWS S3
                    └── SQLite
""")

# ✅ Reuse already-fetched files instead of calling get_files() again
if files:
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Files in S3", len(df))

    with col2:
        st.metric("Total Storage", f"{df['Size'].sum()} bytes")

    st.dataframe(df)
else:
    st.warning("No files found.")