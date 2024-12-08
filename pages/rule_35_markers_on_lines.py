import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    UK_elections_data,
    # new_books_data,
    # alcohol_consumption_data,
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
# new_books_data_df = new_books_data()
# alcohol_consumption_data_df = alcohol_consumption_data()
# european_elections_data_df = european_elections_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(uneven_intervals_tab,
 colour_hierarchy_tab,
 colour_equal_importance_tab,
 colours_with_meaning_tab,
 )  = st.tabs(
    ["📈 Uneven intervals",
     "🚶‍♀️ Colour hierarchy",
     "⏱️ Colours of equal importance",
     "📏 Colours with meaning",
     ]
)

with uneven_intervals_tab:
    st.subheader('Uneven intervals')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(UK_elections_data_df, hide_index=True)

# with hero_line_tab:
#     st.subheader('Hero lines')
#
#     st.write('')
#     st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")
#
#     # with st.expander("Expand to see the data"):
#     #     st.dataframe(new_books_data_df, hide_index=True)

with colour_equal_importance_tab:
    st.subheader('Equal importance colours')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    # with st.expander("Expand to see the data"):
    #     st.dataframe(smoking_rates_data_df, hide_index=True)

with colour_hierarchy_tab:
    st.subheader('Colour hierarchy through colours')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    # with st.expander("Expand to see the data"):
    #     st.dataframe(alcohol_consumption_data_df, hide_index=True)

