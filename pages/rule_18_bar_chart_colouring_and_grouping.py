import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (
    gdp_per_capita_data,
    co2_emissions_per_capita_data,
    child_mortality_data,
    air_pollution_data,
    gov_health_expenditure_data,
    population_in_extreme_poverty_data
)

from utils.bar_chart_examples.gdp_per_capita_plot import gdp_per_capita_bar_chart_plot

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
gdp_per_capita_df = gdp_per_capita_data()

co2_emissions_per_capita_df = co2_emissions_per_capita_data()
child_mortality_df = child_mortality_data()
air_pollution_df = air_pollution_data()
gov_health_expenditure_df = gov_health_expenditure_data()
population_in_extreme_poverty_df = population_in_extreme_poverty_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
colouring_tab, grouping_tab, subplots_tab  = st.tabs(
    ["🎨 Colouring",
     "🫐 Grouping",
     "🏢 Subplots"
     ]
)

# highlighting a small bar

with colouring_tab:
    st.subheader('xxxx')
    st.write('xxx')

    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.write('**Highlighting a specific bar**')
            st.divider()
            st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='Uruguay'))

    with col2:
        with st.container(border=True):
            st.write('**Highlighting the minimum or the maximum**')
            st.divider()
            st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='min'))

    with col1:
        with st.container(border=True):
            st.write('**Highlighting a data quality issue**')
            st.divider()
            st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='data_issue'))

    with col2:
        with st.container(border=True):
            st.write('**Highlighting a benchmark**')
            st.divider()
            st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='median'))

    # st.write(gdp_per_capita_df)
    # st.write(co2_emissions_per_capita_df)
    # st.write(child_mortality_df)
    # st.write(air_pollution_df)
    # st.write(gov_health_expenditure_df)
    # st.write(population_in_extreme_poverty_df)


    st.write('**Bar chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")






