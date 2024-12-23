import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    sector_growth_data,
    refugees_data,
    distributions_data,
    fertility_rates_stacked_area_data,
    inflation_rates_data
)

from utils.line_chart_examples.fertility_rates_area_plot import fertility_rates_line_chart
from utils.line_chart_examples.hong_kong_inflation_rates import hk_inflation_rates_line_chart
from utils.line_chart_examples.shares_of_gdp_by_sector_plot import shares_of_gdp_by_sector_plot
from utils.line_chart_examples.overlapping_distribution_plot import overlapping_distribution_line_chart
from utils.line_chart_examples.refugees_plot import refugees_plotly_express_line_chart, refugees_line_chart

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
distributions_data_df = distributions_data()
fertility_rates_stacked_area_data_df = fertility_rates_stacked_area_data()
inflation_rates_data_df = inflation_rates_data()

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
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts)")

    with st.expander("Expand to see the data"):
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(fertility_rates_stacked_area_data_df, hide_index=True)

        with col2:
            st.dataframe(inflation_rates_data_df, hide_index=True)

    # st.write('')
    # with st.container(border=True):
    #     st.plotly_chart(fertility_rates_plotly_express_line_chart(fertility_rates_stacked_area_data_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(fertility_rates_line_chart(fertility_rates_stacked_area_data_df, type='line'))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(fertility_rates_line_chart(fertility_rates_stacked_area_data_df, type='area'))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(hk_inflation_rates_line_chart(inflation_rates_data_df, type='line'))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(hk_inflation_rates_line_chart(inflation_rates_data_df, type='area'))


with overlapping_timeseries_tab:
    st.subheader('Overlapping timeseries')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts)")

    with st.expander("Expand to see the data"):
        st.dataframe(distributions_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(overlapping_distribution_line_chart(distributions_data_df, type='line'))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(overlapping_distribution_line_chart(distributions_data_df, type='area'))

with walkthrough_tab:
    st.subheader('Walkthrough timeseries')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts)")

    with st.expander("Expand to see the data"):
        st.dataframe(refugees_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(refugees_plotly_express_line_chart(refugees_data_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(refugees_line_chart(refugees_data_df, type='total'))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(refugees_line_chart(refugees_data_df, type='Iraq_Syria'))


with stacked_100_tab:
    st.subheader('100% stacked timeseries')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2024/2/23/rule-41-avoid-area-charts)")

    with st.expander("Expand to see the data"):
        st.dataframe(sector_growth_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(shares_of_gdp_by_sector_plot(sector_growth_data_df, type='line'))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(shares_of_gdp_by_sector_plot(sector_growth_data_df, type='stacked'))
