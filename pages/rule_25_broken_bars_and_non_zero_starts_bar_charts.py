import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    mountain_or_structure_heights_data,

)

# ---------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------
st.set_page_config(
    layout="wide",
)

pages_format()

# ---------------------------------------------------------------------
# Data read
# ---------------------------------------------------------------------
mountain_or_structure_heights_df = mountain_or_structure_heights_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
st.write('hello')

st.dataframe(mountain_or_structure_heights_df)

# sex at birth ratio
