import streamlit as st
import plotly.express as px
from utils import load_data

# Load data
df = load_data()

st.title("📌 Key Insights Dashboard")

st.markdown("""
This page summarizes the most important findings from the Global Wildfire Analytics project.
""")

# ==========================
# KPI Cards
# ==========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Wildfires", f"{len(df):,}")
col2.metric("Average Brightness", f"{df['brightness'].mean():.2f}")
col3.metric("Average Confidence", f"{df['confidence'].mean():.2f}")
col4.metric("Average FRP", f"{df['frp'].mean():.2f}")

st.divider()

# ==========================
# Satellite Contribution
# ==========================

st.subheader("Wildfires by Satellite")

sat = (
    df["satellite"]
    .value_counts()
    .reset_index()
)

sat.columns = ["Satellite", "Wildfires"]

fig = px.pie(
    sat,
    names="Satellite",
    values="Wildfires",
    title="Satellite Contribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Monthly Distribution
# ==========================

st.subheader("Monthly Wildfire Distribution")

month = (
    df.groupby("month_name")
    .size()
    .reset_index(name="Wildfires")
)

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

month["month_name"] = month["month_name"].astype(str)

fig = px.bar(
    month,
    x="month_name",
    y="Wildfires",
    color="Wildfires",
    title="Monthly Wildfire Count",
    color_continuous_scale="Oranges"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Brightness vs FRP
# ==========================

st.subheader("Brightness vs Fire Radiative Power")

fig = px.scatter(
    df,
    x="brightness",
    y="frp",
    color="confidence",
    title="Brightness vs FRP",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# Project Summary
# ==========================

st.subheader("Project Summary")

st.info("""
This dashboard analyzed NASA FIRMS wildfire observations using Python,
Pandas, Plotly and Streamlit.

Major findings include:

• Wildfire occurrences are distributed globally.

• Terra and Aqua satellites contributed most wildfire detections.

• Fire Radiative Power (FRP) is strongly related to wildfire intensity.

• Higher brightness values generally correspond to higher FRP.

• Most wildfire detections have high confidence levels.

• Geographic visualization clearly identifies wildfire hotspots.

• Monthly analysis helps understand seasonal wildfire behaviour.

This dashboard provides valuable insights for wildfire monitoring,
environmental studies and disaster management.
""")

st.divider()

# ==========================
# Final Conclusion
# ==========================

st.success("""
### ✅ Conclusion

The Global Wildfire Analytics Dashboard successfully explores wildfire
patterns using NASA FIRMS data.

Interactive visualizations reveal temporal trends, satellite performance,
geographical hotspots, wildfire intensity and confidence levels.

The dashboard can assist researchers, environmental agencies and decision-makers
in understanding wildfire behaviour and supporting future disaster preparedness.
""")