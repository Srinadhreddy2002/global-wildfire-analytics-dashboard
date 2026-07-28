import streamlit as st
import plotly.express as px
from utils import load_data

# Load dataset
df = load_data()

st.title("📊 Overview")

st.markdown("""
This page provides a general overview of the NASA FIRMS wildfire dataset,
including key performance indicators (KPIs), dataset preview, and summary statistics.
""")

# ==========================
# KPI Cards
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", f"{len(df):,}")

with col2:
    st.metric("Total Columns", len(df.columns))

with col3:
    st.metric("Satellites", df["satellite"].nunique())

with col4:
    st.metric("Average Confidence", f"{df['confidence'].mean():.1f}")

st.divider()

# ==========================
# Dataset Preview
# ==========================

st.subheader("Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.divider()

# ==========================
# Summary Statistics
# ==========================

st.subheader("Summary Statistics")

st.dataframe(df.describe(), use_container_width=True)

st.divider()

# ==========================
# Satellite Distribution
# ==========================

st.subheader("Satellite Distribution")

satellite_counts = (
    df["satellite"]
    .value_counts()
    .reset_index()
)

satellite_counts.columns = ["Satellite", "Wildfires"]

fig = px.pie(
    satellite_counts,
    names="Satellite",
    values="Wildfires",
    title="Wildfires Detected by Satellite"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Confidence Distribution
# ==========================

st.subheader("Wildfire Detection Confidence")

fig = px.histogram(
    df,
    x="confidence",
    nbins=20,
    title="Distribution of Detection Confidence"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Key Insights
# ==========================

st.subheader("Key Insights")

st.success("""
• The dataset contains thousands of wildfire observations.

• Multiple satellites (Terra and Aqua) contributed to wildfire detection.

• Detection confidence is generally high, indicating reliable wildfire observations.

• The dataset includes geographical, temporal, and fire intensity information suitable for advanced analytics.
""")