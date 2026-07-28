import streamlit as st

st.set_page_config(
    page_title="Global Wildfire Analytics",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 Global Wildfire Analytics Dashboard")

st.markdown("""
Welcome to the **Global Wildfire Analytics Dashboard**.

This project analyzes NASA FIRMS wildfire data to identify wildfire patterns,
seasonal trends, fire intensity, confidence levels, satellite observations,
and geographic distribution.
""")

st.sidebar.success("Select any analysis page from the sidebar.")