import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    driving_women_data
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
driving_women_data_df = driving_women_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(physical_distance_tab,
 other_distances_tab,
 )  = st.tabs(
    ["📊 Physical distance",
     "🚩 Other types of distance",
     ]
)

with physical_distance_tab:
    st.subheader('Physical distance')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")
    # st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/workforce_by_sector_plot.py)")

    with st.expander("Expand to see the data"):
        st.dataframe(driving_women_data_df, hide_index=True)
