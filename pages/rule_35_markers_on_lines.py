import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    UK_elections_data,
    kids_before_marriage_data,
    ireland_population_data,
    driving_women_data,
    new_books_data
)

from utils.line_chart_examples.driving_women_plot import driving_women_line_chart, driving_women_plotly_express
from utils.line_chart_examples.books_per_capita_plot import books_per_capita_plotly_express_line_chart, books_per_capita_line_plot
from utils.line_chart_examples.uk_elections_plot import uk_elections_plotly_express_line_chart, uk_elections_line_chart


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
UK_elections_data_df = UK_elections_data()
kids_before_marriage_data_df = kids_before_marriage_data()
ireland_population_df = ireland_population_data()
new_books_data_df = new_books_data()

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

    st.write('')
    with st.container(border=True):
        st.plotly_chart(uk_elections_plotly_express_line_chart(UK_elections_data_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(uk_elections_line_chart(UK_elections_data_df))


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
    st.subheader('Markers acting as legend')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-35-add-data-markers-to-your-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(driving_women_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(driving_women_plotly_express(driving_women_data_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(driving_women_line_chart(driving_women_data_df))

    with st.expander("Expand to see the data"):
        st.dataframe(new_books_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(books_per_capita_plotly_express_line_chart(new_books_data_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(books_per_capita_line_plot(new_books_data_df))


