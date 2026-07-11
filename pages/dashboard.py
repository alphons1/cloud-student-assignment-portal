import streamlit as st
import pandas as pd
import plotly.express as px
from aws_utils import get_files

st.set_page_config(page_title="Dashboard", page_icon="☁", layout="wide")

st.title("☁ Cloud-Based Student Assignment Management System")

# ----------------------------
# Fetch files FIRST
# ----------------------------
files = get_files()

if files:
    df = pd.DataFrame(files)
else:
    df = pd.DataFrame(columns=["Filename", "Size", "LastModified"])

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
        width=120
    )

    st.markdown("---")
    st.write("Cloud Storage Portal")

# ----------------------------
# CSS
# ----------------------------
st.markdown("""
<style>

[data-testid="stMetric"]{
    background-color:#262730;
    border:1px solid #404040;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

[data-testid="stMetricLabel"]{
    color:white !important;
    font-size:18px !important;
    font-weight:600 !important;
}

[data-testid="stMetricValue"]{
    color:#4CAF50 !important;
    font-size:40px !important;
    font-weight:bold !important;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Description
# ----------------------------
st.markdown("""
### AWS-Powered Assignment Management System

Store, manage and analyze files securely using Amazon S3.

**Built with**

- AWS S3
- Python
- Streamlit
- SQLite
- AWS IAM
""")

# ----------------------------
# Dashboard Metrics
# ----------------------------
total_files = len(df)

total_storage_mb = (
    df["Size"].sum() / (1024 * 1024)
    if not df.empty else 0
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Files Stored",
        total_files
    )

with col2:
    st.metric(
        "Cloud Provider",
        "AWS"
    )

with col3:
    st.markdown(f"""
    <div style="
        background:#262730;
        border:1px solid #404040;
        border-radius:15px;
        padding:20px;
        text-align:center;
    ">
        <div style="
            color:white;
            font-size:18px;
            font-weight:600;
            margin-bottom:10px;
        ">
            Region
        </div>

        <div style="
            color:#4CAF50;
            font-size:24px;
            font-weight:bold;
        ">
            Singapore
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# Chart
# ----------------------------
if not df.empty:

    fig = px.bar(
        df,
        x="Filename",
        y="Size",
        color="Size",
        title="Storage Usage by File"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info("No files found in your S3 bucket.")

# ----------------------------
# Architecture
# ----------------------------
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

# ----------------------------
# Storage Summary
# ----------------------------
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Files",
        total_files
    )

with col2:
    st.metric(
        "Total Storage",
        f"{total_storage_mb:.2f} MB"
    )

# ----------------------------
# File Table
# ----------------------------
st.subheader("Files Stored in Amazon S3")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning("No files uploaded yet.")