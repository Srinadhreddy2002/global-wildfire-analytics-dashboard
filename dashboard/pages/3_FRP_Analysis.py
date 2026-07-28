import streamlit as st
import plotly.express as px
from utils import load_data

# Load data
df = load_data()

st.title("🔥 Fire Radiative Power (FRP) Analysis")

st.markdown("""
Fire Radiative Power (FRP) measures the intensity of a wildfire.
Higher FRP values generally indicate more intense fires.
""")

# ==========================
# KPI Cards
# ==========================

col1, col2, col3 = st.columns(3)

col1.metric("Average FRP", f"{df['frp'].mean():.2f}")
col2.metric("Maximum FRP", f"{df['frp'].max():.2f}")
col3.metric("Minimum FRP", f"{df['frp'].min():.2f}")

st.divider()

# ==========================
# FRP Distribution
# ==========================

st.subheader("Distribution of Fire Radiative Power")

fig = px.histogram(
    df,
    x="frp",
    nbins=30,
    title="Distribution of FRP"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Top 20 Highest FRP
# ==========================

st.subheader("Top 20 Highest FRP Records")

top20 = (
    df.sort_values("frp", ascending=False)
      .head(20)
)

fig = px.bar(
    top20,
    x=top20.index.astype(str),
    y="frp",
    color="frp",
    title="Top 20 Fire Radiative Power Values",
    color_continuous_scale="Reds"
)

fig.update_layout(
    xaxis_title="Record",
    yaxis_title="FRP"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Scatter Plot
# ==========================

st.subheader("Brightness vs FRP")

fig = px.scatter(
    df,
    x="brightness",
    y="frp",
    color="confidence",
    title="Brightness vs Fire Radiative Power",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Dataset Preview
# ==========================

st.subheader("Top FRP Records")

st.dataframe(
    top20[
        [
            "acq_date",
            "satellite",
            "brightness",
            "frp",
            "confidence"
        ]
    ],
    use_container_width=True
)

st.divider()

# ==========================
# Insights
# ==========================

st.subheader("Insights")

st.success(f"""
• Average Fire Radiative Power: **{df['frp'].mean():.2f}**

• Maximum Fire Radiative Power: **{df['frp'].max():.2f}**

• Higher FRP values generally correspond to higher wildfire intensity.

• The scatter plot shows the relationship between brightness and FRP.

• High-confidence wildfire detections usually exhibit higher FRP values.
""")