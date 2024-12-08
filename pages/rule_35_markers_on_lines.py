import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    UK_elections_data,
    kids_before_marriage_data,
    ireland_population,
    # european_elections_data
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
ireland_population_df = ireland_population()
# european_elections_data_df = european_elections_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(uneven_intervals_tab,
 not_a_lot_of_data_tab,
 important_events_tab,
 colours_with_meaning_tab,
 )  = st.tabs(
    ["📈 Uneven intervals",
     "🚶‍♀️ Not a lot of data",
     "⏱️ Important events tab",
     "📏 Colours with meaning",
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
#
# with colour_hierarchy_tab:
#     st.subheader('Colour hierarchy through colours')
#
#     st.write('')
#     st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")
#
#     # with st.expander("Expand to see the data"):
#     #     st.dataframe(alcohol_consumption_data_df, hide_index=True)

