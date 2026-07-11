import streamlit as st
import pandas as pd
import plotly.express as px
from aws_utils import get_files

# ============================================================
# Page config
# ============================================================
st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")

st.title("📊 Analytics Dashboard")

# ============================================================
# Sidebar
# ============================================================
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
        width=120
    )
    st.markdown("---")
    st.write("Cloud-Based Student Assignment Management System")

# ============================================================
# Dark theme styling (matches Dashboard page)
# ============================================================
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

# ============================================================
# Data source: AWS S3 (single source of truth)
# ------------------------------------------------------------
# get_files() is called exactly once here. Both the Dashboard
# and Analytics pages read directly from S3 via this same
# function, so the two pages can never disagree about which
# files exist — there is no separate SQLite copy to drift
# out of sync with the bucket.
# ============================================================
try:
    files = get_files()
except Exception as e:
    st.error(f"Failed to fetch files from S3: {e}")
    files = []

if files:
    df = pd.DataFrame(files)
else:
    df = pd.DataFrame(columns=["Filename", "Size", "LastModified"])

# Ensure Size is numeric so sums/charts never crash on bad/missing data
if "Size" in df.columns:
    df["Size"] = pd.to_numeric(df["Size"], errors="coerce").fillna(0)
else:
    df["Size"] = 0

# Add a convenience column: size in MB, used for display and charting
df["SizeMB"] = df["Size"] / (1024 * 1024)

# ============================================================
# Empty-bucket handling
# ============================================================
if df.empty:
    st.warning("No files found in your S3 bucket.")
else:
    # --------------------------------------------------------
    # Metrics
    # --------------------------------------------------------
    total_files = len(df)
    total_storage_mb = df["SizeMB"].sum()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Uploads", total_files)

    with col2:
        st.metric("Total Storage", f"{total_storage_mb:.2f} MB")

    # --------------------------------------------------------
    # Chart: file size distribution (in MB)
    # --------------------------------------------------------
    fig = px.bar(
        df,
        x="Filename",
        y="SizeMB",
        color="SizeMB",
        title="File Size Distribution (MB)",
        labels={"SizeMB": "Size (MB)", "Filename": "File"}
    )

    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------------
    # File table
    # --------------------------------------------------------
    st.subheader("Files in S3")

    display_df = df[["Filename", "SizeMB", "LastModified"]].rename(
        columns={"SizeMB": "Size (MB)"}
    )

    st.dataframe(display_df, use_container_width=True)