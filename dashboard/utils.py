import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv("data/wildfire_data.csv")

    df["acq_date"] = pd.to_datetime(df["acq_date"])

    df["year"] = df["acq_date"].dt.year
    df["month"] = df["acq_date"].dt.month_name()

    return df