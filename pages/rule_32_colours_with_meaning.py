import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    smoking_rates_data,
    new_books_data,
    alcohol_consumption_data,
    european_elections_data
)

from utils.line_chart_examples.books_per_capita_plot import books_per_capita_plotly_express_line_chart, books_per_capita_line_plot
from utils.line_chart_examples.european_elections_plot import european_elections_plotly_express_line_chart
from utils.line_chart_examples.alcohol_consumption_plot import alcohol_consumption_plotly_express_line_chart, alcohol_consumption_line_chart

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
smoking_rates_data_df = smoking_rates_data()
new_books_data_df = new_books_data()
alcohol_consumption_data_df = alcohol_consumption_data()
european_elections_data_df = european_elections_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(hero_line_tab,
 colour_hierarchy_tab,
 colours_with_meaning_tab,
 )  = st.tabs(
    ["📈 Hero lines",
     "🚶‍♀️ Colour hierarchy",
     "📏 Colours with meaning",
     ]
)

with hero_line_tab:
    st.subheader('Hero lines')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/6/10/rule-32-every-line-should-be-a-different-colour)")

    with st.expander("Expand to see the data"):
        st.dataframe(new_books_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(books_per_capita_plotly_express_line_chart(new_books_data_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(books_per_capita_line_plot(new_books_data_df))

with colour_hierarchy_tab:
    st.subheader('Colour hierarchy through colours')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/6/10/rule-32-every-line-should-be-a-different-colour)")

    with st.expander("Expand to see the data"):
        st.dataframe(alcohol_consumption_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(alcohol_consumption_plotly_express_line_chart(alcohol_consumption_data_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(alcohol_consumption_line_chart(alcohol_consumption_data_df))

with colours_with_meaning_tab:
    st.subheader('Political parties')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/6/10/rule-32-every-line-should-be-a-different-colour)")

    with st.expander("Expand to see the data"):
        st.dataframe(european_elections_data_df, hide_index=True)

    # st.write('')
    # with st.container(border=True):
    #     st.plotly_chart(european_elections_plotly_express_line_chart(european_elections_data_df))

