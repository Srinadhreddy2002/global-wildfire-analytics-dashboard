import streamlit as st
import plotly.express as px
from utils import load_data

# Load data
df = load_data()

st.title("🌍 Geographic Analysis")

st.markdown("""
This page visualizes the geographical distribution of wildfire occurrences
using latitude and longitude coordinates from the NASA FIRMS dataset.
""")

# ==========================
# KPI Cards
# ==========================

col1, col2, col3 = st.columns(3)

col1.metric("Maximum Latitude", f"{df['latitude'].max():.2f}")
col2.metric("Minimum Latitude", f"{df['latitude'].min():.2f}")
col3.metric("Total Locations", f"{len(df):,}")

st.divider()

# ==========================
# Wildfire Map
# ==========================

st.subheader("Global Wildfire Locations")

fig = px.scatter_mapbox(
    df.sample(min(5000, len(df))),   # Plot up to 5000 points for speed
    lat="latitude",
    lon="longitude",
    color="brightness",
    size="frp",
    hover_name="satellite",
    hover_data={
        "confidence": True,
        "brightness": True,
        "frp": True
    },
    zoom=1,
    height=700,
    color_continuous_scale="Hot",
    title="Global Wildfire Distribution"
)

fig.update_layout(
    mapbox_style="open-street-map",
    margin=dict(l=0, r=0, t=50, b=0)
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Brightness vs Latitude
# ==========================

st.subheader("Brightness by Latitude")

fig = px.scatter(
    df,
    x="latitude",
    y="brightness",
    color="confidence",
    title="Latitude vs Brightness",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# FRP vs Longitude
# ==========================

st.subheader("FRP by Longitude")

fig = px.scatter(
    df,
    x="longitude",
    y="frp",
    color="brightness",
    title="Longitude vs Fire Radiative Power",
    color_continuous_scale="Reds"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Dataset Preview
# ==========================

st.subheader("Location Data")

st.dataframe(
    df[
        [
            "latitude",
            "longitude",
            "brightness",
            "confidence",
            "frp",
            "satellite"
        ]
    ].head(20),
    use_container_width=True
)

st.divider()

# ==========================
# Insights
# ==========================

st.subheader("Insights")

st.success("""
• Wildfires are distributed across multiple geographic regions.

• Scatter Map provides a global view of wildfire hotspots.

• Fire Radiative Power and Brightness vary across locations.

• Geographic visualization helps identify regions with higher wildfire activity and supports disaster monitoring.
""")