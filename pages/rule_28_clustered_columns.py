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
(non_zero_starts_tab,
 hidden_differences_tab,
 small_or_big_drops_tab,
 dominating_category_tab,
 )  = st.tabs(
    ["0️⃣️ Non-zero starts",
     "🫣️ Hidden differences",
     "💧 Small or big drops",
     "🐘️ Dominating category",
     ]
)

st.write('hello')