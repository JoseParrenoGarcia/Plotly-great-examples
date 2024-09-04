import streamlit as st
import pandas as pd
from utils.pages_format import pages_format
from utils.load_data import travel_gdp_share_data
from utils.bar_chart_examples.travel_gdp_share_plot import travel_gdp_share_plot



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
travel_gdp_share_df = travel_gdp_share_data()
travel_gdp_share_chart = travel_gdp_share_plot(df=travel_gdp_share_df)

st.write(travel_gdp_share_df)
st.plotly_chart(travel_gdp_share_chart)



