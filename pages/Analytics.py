import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Analytics Dashboard")

with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
        width=120
    )

    st.markdown("---")

    st.write("Cloud-Based Student Assignment Management System")


conn = sqlite3.connect("uploads.db")

df = pd.read_sql_query(
    "SELECT * FROM uploads",
    conn
)

conn.close()

if df.empty:
    st.warning("No uploads found.")
else:

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Uploads",
            len(df)
        )

    with col2:
        st.metric(
            "Total Storage",
            f"{df['size'].sum()} bytes"
        )

    fig = px.bar(
        df,
        x="filename",
        y="size",
        title="File Size Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(df)