import streamlit as st
from utils.pages_format import pages_format
import pandas as pd

# ---------------------------------------------------------------------
# HOME PAGE - CONFIGURATION
# ---------------------------------------------------------------------
st.set_page_config(
    layout="wide",
)

pages_format()

# ---------------------------------------------------------------------
# Data read
# ---------------------------------------------------------------------
travel_gdp_share_df = (
    pd.read_csv('data/travel_gdp_share_statista.csv', delimiter=';')
    .assign(
        **{
            '2019': lambda x: x['2019'].str.rstrip('%').astype(float),
            '2023': lambda x: x['2023'].str.rstrip('%').astype(float),
        }
    )
    .rename(columns={'2019': 'y2019', '2023': 'y2023'})
)

st.write(travel_gdp_share_df)



