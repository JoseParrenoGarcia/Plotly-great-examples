import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    human_height_data,
    market_stocks_data,
)

from utils.line_chart_examples.faang_stocks_plot import faang_stocks_line_chart
from utils.line_chart_examples.human_heights_plot import human_height_line_plot

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
human_height_data_df = human_height_data()
market_stocks_data_df = market_stocks_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(lines_with_lots_of_change_tab,
 too_many_lines_tab,
 benchmark_tab,
 )  = st.tabs(
    ["📈 Lines with lots of change",
     "🚶‍♀️ Too many lines",
     "📏 Benchmark lines",
     ]
)

with lines_with_lots_of_change_tab:
    st.subheader('Lines with lots of change')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-36-line-thickness)")

    with st.expander("Expand to see the data"):
        st.dataframe(market_stocks_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(faang_stocks_line_chart(market_stocks_data_df, line_width=6))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(faang_stocks_line_chart(market_stocks_data_df, line_width=3))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(faang_stocks_line_chart(market_stocks_data_df, line_width=1))

with too_many_lines_tab:
    st.subheader('Too many lines')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-36-line-thickness)")

    with st.expander("Expand to see the data"):
        st.dataframe(human_height_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(human_height_line_plot(human_height_data_df,
                                               line_width=6))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(human_height_line_plot(human_height_data_df,
                                               line_width=3))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(human_height_line_plot(human_height_data_df,
                                               line_width=1))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(human_height_line_plot(human_height_data_df,
                                               line_width=1,
                                               hero_line=['Vietnam', 'Denmark', 'South Korea', 'Japan']))

with benchmark_tab:
    st.subheader('Benchmark lines')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2023/1/5/rule-36-line-thickness)")

    with st.expander("Expand to see the data"):
        st.dataframe(human_height_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(human_height_line_plot(human_height_data_df,
                                               line_width=1,
                                               hero_line=['Vietnam', 'Denmark', 'South Korea', 'Japan'],
                                               benchmark_line=True
                                               ))


