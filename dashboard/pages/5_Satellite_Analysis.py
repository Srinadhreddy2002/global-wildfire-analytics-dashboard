import streamlit as st
import plotly.express as px
from utils import load_data

# Load data
df = load_data()

st.title("🛰️ Satellite Analysis")

st.markdown("""
This page compares wildfire detections recorded by different satellites.
The NASA FIRMS dataset primarily includes Terra and Aqua satellites.
""")

# ==========================
# KPI Cards
# ==========================

col1, col2, col3 = st.columns(3)

col1.metric("Total Satellites", df["satellite"].nunique())
col2.metric("Most Used Satellite", df["satellite"].mode()[0])
col3.metric("Total Records", f"{len(df):,}")

st.divider()

# ==========================
# Satellite Counts
# ==========================

st.subheader("Wildfires Detected by Satellite")

satellite_counts = (
    df["satellite"]
    .value_counts()
    .reset_index()
)

satellite_counts.columns = ["Satellite", "Wildfires"]

fig = px.bar(
    satellite_counts,
    x="Satellite",
    y="Wildfires",
    color="Satellite",
    title="Wildfires Detected by Each Satellite"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Pie Chart
# ==========================

st.subheader("Satellite Contribution")

fig = px.pie(
    satellite_counts,
    names="Satellite",
    values="Wildfires",
    title="Percentage of Wildfires by Satellite"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Average Brightness
# ==========================

st.subheader("Average Brightness by Satellite")

brightness = (
    df.groupby("satellite")["brightness"]
    .mean()
    .reset_index()
)

fig = px.bar(
    brightness,
    x="satellite",
    y="brightness",
    color="brightness",
    title="Average Brightness",
    color_continuous_scale="Oranges"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Average FRP
# ==========================

st.subheader("Average Fire Radiative Power")

frp = (
    df.groupby("satellite")["frp"]
    .mean()
    .reset_index()
)

fig = px.bar(
    frp,
    x="satellite",
    y="frp",
    color="frp",
    title="Average Fire Radiative Power",
    color_continuous_scale="Reds"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Summary Table
# ==========================

st.subheader("Satellite Summary")

summary = (
    df.groupby("satellite")
    .agg({
        "brightness": "mean",
        "confidence": "mean",
        "frp": "mean"
    })
    .round(2)
)

st.dataframe(summary, use_container_width=True)

st.divider()

# ==========================
# Insights
# ==========================

st.subheader("Insights")

top_sat = satellite_counts.iloc[0]

st.success(f"""
• **{top_sat['Satellite']}** detected the highest number of wildfires.

• Both Terra and Aqua satellites provide valuable wildfire observations.

• Satellite comparison helps understand differences in wildfire monitoring.

• Average Brightness, Confidence and FRP are useful indicators for evaluating satellite performance.
""")