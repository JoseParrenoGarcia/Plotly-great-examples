import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    sector_growth_data,
    refugees_data,
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
sector_growth_data_df = sector_growth_data()
refugees_data_df = refugees_data()
# ireland_population_df = ireland_population_data()
# contraceptive_use_data_df = contraceptive_use_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(single_timeseries_tab,
 overlapping_timeseries_tab,
 walkthrough_tab,
 stacked_100_tab,
 )  = st.tabs(
    ["📈 Single timeseries",
     "🚶‍♀️ Overlapping timeseries",
     "⏱️ Walthrough timeseries",
     "📏 100% stacked timeseries",
     ]
)

with single_timeseries_tab:
    st.subheader('Single timeseries')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts")

    # with st.expander("Expand to see the data"):
    #     st.dataframe(market_stocks_data_df, hide_index=True)

with overlapping_timeseries_tab:
    st.subheader('Overlapping timeseries')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts")

    with st.expander("Expand to see the data"):
        st.dataframe(sector_growth_data_df, hide_index=True)

with walkthrough_tab:
    st.subheader('Walkthrough timeseries')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts")

    with st.expander("Expand to see the data"):
        st.dataframe(refugees_data_df, hide_index=True)

with stacked_100_tab:
    st.subheader('100% stacked timeseries')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts")

    # with st.expander("Expand to see the data"):
    #     st.dataframe(human_height_data_df, hide_index=True)

