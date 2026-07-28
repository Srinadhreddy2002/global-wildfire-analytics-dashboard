import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

# -----------------------------
# Load Dataset
# -----------------------------
df = load_data()

st.title("📅 Monthly Wildfire Analysis")

st.markdown("""
This page analyzes how wildfire occurrences vary across different months.
It helps identify seasonal wildfire patterns.
""")

# -----------------------------
# Wildfires by Month
# -----------------------------
monthly = (
    df.groupby("month_name")
    .size()
    .reset_index(name="Wildfires")
)

# Correct month order
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Convert to ordered categorical
monthly["month_name"] = pd.Categorical(
    monthly["month_name"],
    categories=month_order,
    ordered=True
)

# Sort by month
monthly = monthly.sort_values("month_name")

# -----------------------------
# KPI Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Months", monthly.shape[0])
col2.metric("Highest Wildfires", f"{monthly['Wildfires'].max():,}")
col3.metric("Lowest Wildfires", f"{monthly['Wildfires'].min():,}")

st.divider()

# -----------------------------
# Monthly Bar Chart
# -----------------------------
fig = px.bar(
    monthly,
    x="month_name",
    y="Wildfires",
    title="Wildfires by Month",
    color="Wildfires",
    color_continuous_scale="Oranges",
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Monthly Pie Chart
# -----------------------------
fig = px.pie(
    monthly,
    names="month_name",
    values="Wildfires",
    title="Monthly Wildfire Distribution",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Monthly Summary Table
# -----------------------------
st.subheader("📋 Monthly Summary")

st.dataframe(monthly, use_container_width=True)

# -----------------------------
# Insights
# -----------------------------
highest = monthly.loc[monthly["Wildfires"].idxmax()]
lowest = monthly.loc[monthly["Wildfires"].idxmin()]

st.subheader("💡 Key Insights")

st.success(f"""
🔥 Highest wildfire month: **{highest['month_name']}**
with **{highest['Wildfires']:,}** wildfire detections.

🌿 Lowest wildfire month: **{lowest['month_name']}**
with **{lowest['Wildfires']:,}** wildfire detections.
""")

st.info("""
The monthly analysis reveals seasonal wildfire trends.
Understanding these patterns helps governments and disaster management
authorities prepare resources during high-risk periods.
""")