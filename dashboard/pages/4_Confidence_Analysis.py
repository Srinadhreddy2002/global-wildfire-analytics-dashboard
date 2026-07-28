import streamlit as st
import plotly.express as px
from utils import load_data

# Load data
df = load_data()

st.title("🎯 Wildfire Detection Confidence Analysis")

st.markdown("""
This page analyzes the confidence level assigned to each wildfire detection.
Higher confidence values indicate more reliable wildfire observations.
""")

# ==========================
# KPI Cards
# ==========================

col1, col2, col3 = st.columns(3)

col1.metric("Average Confidence", f"{df['confidence'].mean():.2f}")
col2.metric("Maximum Confidence", f"{df['confidence'].max():.0f}")
col3.metric("Minimum Confidence", f"{df['confidence'].min():.0f}")

st.divider()

# ==========================
# Histogram
# ==========================

st.subheader("Confidence Distribution")

fig = px.histogram(
    df,
    x="confidence",
    nbins=20,
    title="Distribution of Wildfire Detection Confidence"
)

fig.update_layout(
    xaxis_title="Confidence",
    yaxis_title="Number of Wildfires"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Box Plot
# ==========================

st.subheader("Confidence Spread")

fig = px.box(
    df,
    y="confidence",
    title="Box Plot of Detection Confidence"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Confidence by Satellite
# ==========================

st.subheader("Confidence by Satellite")

fig = px.box(
    df,
    x="satellite",
    y="confidence",
    color="satellite",
    title="Confidence Levels by Satellite"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Confidence Statistics
# ==========================

st.subheader("Confidence Statistics")

st.dataframe(
    df["confidence"].describe().to_frame(),
    use_container_width=True
)

st.divider()

# ==========================
# Top 20 Highest Confidence
# ==========================

st.subheader("Top 20 Highest Confidence Records")

top20 = df.sort_values("confidence", ascending=False).head(20)

st.dataframe(
    top20[
        [
            "acq_date",
            "satellite",
            "brightness",
            "confidence",
            "frp"
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
• Average confidence is **{df['confidence'].mean():.2f}**.

• Most wildfire detections have relatively high confidence.

• Terra and Aqua satellites provide consistently reliable observations.

• High-confidence detections are generally associated with stronger wildfire activity.
""")