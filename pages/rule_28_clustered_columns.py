import streamlit as st
from utils.pages_format import pages_format

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


# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(many_categories_tab,
 comparing_2_groups_tab,
 )  = st.tabs(
    ["📊 Many categories",
     "👥 Comparing 2 groups",
     ]
)

st.write('hello')