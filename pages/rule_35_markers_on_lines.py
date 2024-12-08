import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    UK_elections_data,
    kids_before_marriage_data,
    ireland_population_data,
    contraceptive_use_data
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
UK_elections_data_df = UK_elections_data()
kids_before_marriage_data_df = kids_before_marriage_data()
ireland_population_df = ireland_population_data()
contraceptive_use_data_df = contraceptive_use_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(uneven_intervals_tab,
 not_a_lot_of_data_tab,
 important_events_tab,
 replacement_for_legend_tab,
 )  = st.tabs(
    ["📈 Uneven intervals",
     "🚶‍♀️ Not a lot of data",
     "⏱️ Important events",
     "📏 Replacement for legend",
     ]
)

with uneven_intervals_tab:
    st.subheader('Uneven intervals')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(UK_elections_data_df, hide_index=True)

with not_a_lot_of_data_tab:
    st.subheader('Not a lot of data')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(kids_before_marriage_data_df, hide_index=True)

with important_events_tab:
    st.subheader('Important events')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(ireland_population_df, hide_index=True)

with replacement_for_legend_tab:
    st.subheader('Colour hierarchy through colours')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(contraceptive_use_data_df, hide_index=True)

