import streamlit as st
import plotly.express as px
from utils import load_data

# Load dataset
df = load_data()

st.title("📅 Monthly Wildfire Analysis")

st.markdown("""
This page analyzes how wildfire occurrences vary across different months.
It helps identify seasonal wildfire patterns.
""")

# --------------------------
# Wildfires by Month
# --------------------------

monthly = (
    df.groupby("month_name")
    .size()
    .reset_index(name="Wildfires")
)

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly["month_name"] = px.Categorical(
    monthly["month_name"],
    categories=month_order,
    ordered=True
)

monthly = monthly.sort_values("month_name")

fig = px.bar(
    monthly,
    x="month_name",
    y="Wildfires",
    title="Wildfires by Month",
    color="Wildfires",
    color_continuous_scale="Oranges"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------
# Pie Chart
# --------------------------

fig = px.pie(
    monthly,
    names="month_name",
    values="Wildfires",
    title="Monthly Wildfire Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------
# Dataset
# --------------------------

st.subheader("Monthly Summary")

st.dataframe(monthly, use_container_width=True)

# --------------------------
# Key Insights
# --------------------------

st.subheader("Insights")

highest = monthly.loc[monthly["Wildfires"].idxmax()]
lowest = monthly.loc[monthly["Wildfires"].idxmin()]

st.success(f"""
🔥 Highest wildfire month: **{highest['month_name']}**
with **{highest['Wildfires']:,}** wildfire detections.

🌿 Lowest wildfire month: **{lowest['month_name']}**
with **{lowest['Wildfires']:,}** wildfire detections.

The monthly analysis helps identify seasonal wildfire activity and supports
future wildfire monitoring and disaster preparedness.
""")