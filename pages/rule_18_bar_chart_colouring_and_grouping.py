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

ons_data_df  = (
    gdp_per_capita_df
    .merge(co2_emissions_per_capita_df, on=['Entity', 'Code'], how='outer')
    .merge(child_mortality_df, on=['Entity', 'Code'], how='outer')
    .merge(air_pollution_df, on=['Entity', 'Code'], how='outer')
    .merge(gov_health_expenditure_df, on=['Entity', 'Code'], how='outer')
    .merge(population_in_extreme_poverty_df, on=['Entity', 'Code'], how='outer')
)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(colouring_tab,
 grouping_tab,
 subplots_tab,
 percentage_tab,
 long_tail_highlights_tab)  = st.tabs(
    ["🎨 Colouring",
     "🫐 Grouping",
     "🏢 Subplots",
     "Percentage plots",
     "Long tail highlights", # highlighting a small bar
     ]
)

with colouring_tab:
    st.subheader('Colours in bar charts should be used sparingly')
    st.write('It is standard best practice to try to keep colour variety in plots to a minimum.  This is '
             'not an exception for bar charts. There might be instances where keeping the same colour is what the chart requires '
             '(for example, if you dont to provide more importance to a category). '
             'However, if you do need to highlight something, single-colour bar charts can be a bit dull.')

    st.write("In the examples below, you will see how we used only 2 colours and 1 pattern fill to convey our message. "
             "Ideally, colours should be chosen so the contrast is clear but non-intrusive. For example, grey is a good colour to use. " 
             "In the examples below, we highlighted bars based on country colours but contrasting them with grey. ")

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

with subplots_tab:
    st.subheader('xxx')
    st.write('xxx')

    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write(ons_data_df)









