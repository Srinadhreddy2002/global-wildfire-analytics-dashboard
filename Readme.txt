# 🔥 Global Wildfire Analytics Dashboard

## 📌 Project Overview

The **Global Wildfire Analytics Dashboard** is an interactive data visualization project developed using **Streamlit**, **Plotly**, and **Pandas**. It analyzes NASA FIRMS wildfire data to identify wildfire patterns, seasonal trends, fire intensity, confidence levels, satellite observations, and geographical distribution.

The dashboard provides an easy-to-use interface for exploring wildfire incidents through multiple interactive pages.

---

## 🎯 Objectives

- Analyze global wildfire occurrences.
- Visualize monthly wildfire trends.
- Study Fire Radiative Power (FRP).
- Examine wildfire detection confidence.
- Compare wildfire detections from different satellites.
- Display wildfire locations geographically.
- Present key insights through interactive dashboards.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Jupyter Notebook

---

## 📂 Project Structure

```
global-wildfire-analytics-dashboard/
│
├── dashboard/
│   ├── app.py
│   ├── utils.py
│   ├── requirements.txt
│   ├── data/
│   │   └── wildfire_data.csv
│   └── pages/
│       ├── 1_Overview.py
│       ├── 2_Monthly_Analysis.py
│       ├── 3_FRP_Analysis.py
│       ├── 4_Confidence_Analysis.py
│       ├── 5_Satellite_Analysis.py
│       ├── 6_Geographic_Analysis.py
│       └── 7_Key_Insights.py
│
├── notebook/
│   └── Final_Project.ipynb
│
└── README.md
```

---

## 📊 Dashboard Pages

### 🏠 Home
Introduces the project and provides navigation to all dashboard pages.

### 📈 Overview
- Total Records
- Total Columns
- Satellites Used
- Average Confidence
- Dataset Preview

### 📅 Monthly Analysis
- Monthly wildfire frequency
- Seasonal wildfire trends

### 🔥 FRP Analysis
- Average FRP
- Maximum FRP
- Minimum FRP
- Distribution of Fire Radiative Power

### 🎯 Confidence Analysis
- Average Confidence
- Maximum Confidence
- Minimum Confidence
- Confidence Distribution

### 🛰 Satellite Analysis
- Wildfires detected by Terra and Aqua satellites
- Satellite comparison

### 🌍 Geographic Analysis
- Global wildfire distribution
- Latitude and longitude visualization

### 📌 Key Insights
- Overall wildfire statistics
- Average Brightness
- Average Confidence
- Average FRP
- Satellite contribution

---

## 📊 Dataset

**Source:** NASA FIRMS (Fire Information for Resource Management System)

The dataset includes:

- Latitude
- Longitude
- Brightness
- Scan
- Track
- Acquisition Date
- Acquisition Time
- Satellite
- Instrument
- Confidence
- Version
- Bright T31
- Fire Radiative Power (FRP)
- Day/Night

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Srinadhreddy2002/global-wildfire-analytics-dashboard.git
```

Move into the project folder

```bash
cd global-wildfire-analytics-dashboard/dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📷 Dashboard Features

- Interactive sidebar navigation
- KPI Cards
- Monthly trend analysis
- Fire intensity analysis
- Confidence analysis
- Satellite comparison
- Geographic visualization
- Interactive Plotly charts
- Clean and responsive Streamlit interface

---

## 📈 Key Insights

- More than **66,000 wildfire records** were analyzed.
- Terra satellite recorded more wildfire detections than Aqua.
- Confidence values indicate reliable wildfire detections.
- Fire Radiative Power varies significantly across wildfire events.
- Monthly analysis helps identify seasonal wildfire patterns.
- Geographic visualization highlights wildfire-prone regions.

---

## 🔮 Future Enhancements

- Real-time NASA FIRMS API integration
- Country-wise wildfire filters
- Time-series forecasting
- Machine learning-based wildfire prediction
- Deployment on Streamlit Community Cloud

---

## 👨‍💻 Author

**Srinadh Reddy**

Master's Student – Data Science

University of Europe for Applied Sciences

---

## 📄 License

This project was developed for academic purposes as part of the **Data Visualization** course.
