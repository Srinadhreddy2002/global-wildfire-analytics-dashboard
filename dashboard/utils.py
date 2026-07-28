import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(__file__)
    csv_path = os.path.join(BASE_DIR, "data", "wildfire_data.csv")

    df = pd.read_csv(csv_path)

    df["acq_date"] = pd.to_datetime(df["acq_date"])

    df["year"] = df["acq_date"].dt.year
    df["month"] = df["acq_date"].dt.month
    df["month_name"] = df["acq_date"].dt.month_name()

    return df