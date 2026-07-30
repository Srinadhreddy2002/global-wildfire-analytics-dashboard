import streamlit as st

st.title("❓ Analytical Questions")

st.markdown("""
This project explores the NASA FIRMS wildfire dataset through the following analytical questions.
""")

questions = [
    "1. How has the number of wildfire occurrences changed over time?",
    "2. Which months recorded the highest number of wildfire occurrences?",
    "3. How is Fire Radiative Power (FRP) distributed among wildfire events?",
    "4. What is the distribution of wildfire detection confidence levels?",
    "5. How does Fire Radiative Power (FRP) relate to Brightness?",
    "6. How are wildfire detections distributed between Day and Night?",
    "7. Which satellite detected the highest number of wildfire events?",
    "8. Does wildfire brightness vary with confidence level?",
    "9. How does Fire Radiative Power (FRP) vary across different confidence levels?",
    "10. Where are the major wildfire hotspots located based on geographic coordinates?"
]

for question in questions:
    st.markdown(f"### {question}")

st.info("""
Each analytical question is explored in the corresponding dashboard page using
interactive Plotly visualizations and summary insights.
""")