import streamlit as st

st.title("❓ Analytical Questions & Answers")

qa = [
    (
        "1. How has the number of wildfire occurrences changed over time?",
        "Wildfire occurrences fluctuate over the years, with some years recording significantly higher activity than others."
    ),
    (
        "2. Which months recorded the highest number of wildfire occurrences?",
        "The monthly analysis shows that the highest number of wildfire events occurred during the peak fire season."
    ),
    (
        "3. How is Fire Radiative Power (FRP) distributed among wildfire events?",
        "Most wildfire events have low to moderate FRP values, while a smaller number of events exhibit extremely high FRP."
    ),
    (
        "4. What is the distribution of wildfire detection confidence levels?",
        "The majority of wildfire detections fall into the high-confidence category, indicating reliable satellite observations."
    ),
    (
        "5. How does Fire Radiative Power (FRP) relate to Brightness?",
        "Higher brightness values generally correspond to higher FRP, suggesting more intense fires."
    ),
    (
        "6. How are wildfire detections distributed between Day and Night?",
        "Wildfires are detected during both day and night, with the distribution depending on satellite observation times."
    ),
    (
        "7. Which satellite detected the highest number of wildfire events?",
        "One satellite recorded more wildfire detections than the other, reflecting its coverage and observation frequency."
    ),
    (
        "8. Does wildfire brightness vary with confidence level?",
        "Higher-confidence wildfire detections generally exhibit higher brightness values."
    ),
    (
        "9. How does FRP vary across different confidence levels?",
        "High-confidence wildfire events tend to have higher FRP values than low-confidence detections."
    ),
    (
        "10. Where are the major wildfire hotspots located?",
        "The geographic analysis identifies wildfire hotspots concentrated in specific latitude and longitude regions."
    ),
]

for question, answer in qa:
    st.subheader(question)
    st.write(answer)
    st.markdown("---")