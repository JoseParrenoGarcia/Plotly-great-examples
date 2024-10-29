import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (
    gdp_per_capita_data,
    co2_emissions_per_capita_data,
    child_mortality_data,
    air_pollution_data,
    gov_health_expenditure_data,
    population_in_extreme_poverty_data,
    smoking_rate_data,
    progress_against_target_synthetic_data,
    covid_data,
)

from utils.bar_chart_examples.gdp_per_capita_plot import gdp_per_capita_bar_chart_plot, gdp_per_capita_bar_chart_plotly_express
from utils.bar_chart_examples.ons_data_subplots_plot import ons_data_subplots_bar_charts
from utils.bar_chart_examples.smoking_rates_plot import smoking_rates_plot, smoking_rates_plotly_express
from utils.bar_chart_examples.progress_against_target_plot import progress_against_target_bar_chart, progress_against_target_bar_chart_basic
from utils.bar_chart_examples.covid_plot import covid_bar_chart_plot

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
smoking_rate_df = smoking_rate_data()
progress_against_target_synthetic_df = progress_against_target_synthetic_data()

gdp_per_capita_df = gdp_per_capita_data()
co2_emissions_per_capita_df = co2_emissions_per_capita_data()
child_mortality_df = child_mortality_data()
air_pollution_df = air_pollution_data()
gov_health_expenditure_df = gov_health_expenditure_data()
population_in_extreme_poverty_df = population_in_extreme_poverty_data()

covid_df = covid_data()

ons_data_df  = (
    gdp_per_capita_df
    .merge(co2_emissions_per_capita_df, on=['Entity', 'Code'], how='outer')
    .merge(child_mortality_df, on=['Entity', 'Code'], how='outer')
    .merge(air_pollution_df, on=['Entity', 'Code'], how='outer')
    .merge(gov_health_expenditure_df, on=['Entity', 'Code'], how='outer')
    .merge(population_in_extreme_poverty_df, on=['Entity', 'Code'], how='outer')
)

columns_to_fill = [
    'GDP per capita',
    'Annual CO₂ emissions (per capita)',
    'Under-five mortality rate',
    'Nitrogen oxide (NOx)',
    'Domestic general government health expenditure (GGHE-D) as percentage of general government expenditure (GGE) (%)',
    '$2.15 a day - Share of population in poverty'
]
ons_data_df[columns_to_fill] = ons_data_df[columns_to_fill].fillna(0)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(colouring_tab,
 # subplots_tab,
 long_tail_highlights_tab,
 grouping_tab,
 )  = st.tabs(
    ["🎨 Colouring",
     # "🏢 Subplots",
     "🦎 Long tail highlights",
     "🫐 Grouping",
     ]
)

with colouring_tab:
    st.subheader('Colours in bar charts should be used sparingly')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py)")

    with st.expander('Expand to see the data'):
        st.dataframe(gdp_per_capita_df, hide_index=True)

    with st.container(border=True):
        st.write('**Plotly express**')
        st.plotly_chart(gdp_per_capita_bar_chart_plotly_express(df=gdp_per_capita_df))

    with st.container(border=True):
        st.write('**No highlighting**')
        st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='no', remove_xaxis=True))

    with st.container(border=True):
        st.write('**Highlighting a specific bar**')
        st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='Uruguay'))

    with st.container(border=True):
        st.write('**Highlighting the minimum or the maximum**')
        st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='min'))

    with st.container(border=True):
        st.write('**Highlighting a data quality issue**')
        st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='data_issue'))

    with st.container(border=True):
        st.write('**Highlighting a benchmark**')
        st.plotly_chart(gdp_per_capita_bar_chart_plot(df=gdp_per_capita_df, highlight='data_issue', add_median=True))

with grouping_tab:
    st.subheader('Grouping categories isnt just about colour')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.write('')

    ### GROUPING BY GEO - no need for colour
    with st.container(border=True):
        st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/smoking_rates_plot.py)")

        with st.expander('Expand to see the data'):
            st.dataframe(smoking_rate_df, hide_index=True)

        st.write('**Plotly basic - ordering by smoking rate**')
        st.plotly_chart(smoking_rates_plotly_express(smoking_rate_df, sort_by='smoking_rate'))

        st.write('**Plotly basic - ordering by continent**')
        st.plotly_chart(smoking_rates_plotly_express(smoking_rate_df))

        st.write('**Plotly advanced**')
        st.plotly_chart(smoking_rates_plot(smoking_rate_df))

    # ### PROGRESS AGAINST TARGET
    with st.container(border=True):
        st.write('')
        st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/progress_against_target_plot.py)")
        st.write('')

        with st.expander('Expand to see the data'):
            st.dataframe(progress_against_target_synthetic_df, hide_index=True)

        st.write('**Plotly basic - ordering by progress against target**')
        st.plotly_chart(progress_against_target_bar_chart_basic(progress_against_target_synthetic_df, sort_by='progress'))

        st.write('**Plotly basic - ordering by progress against target by category**')
        st.plotly_chart(progress_against_target_bar_chart_basic(progress_against_target_synthetic_df, sort_by='category'))

        st.write('**Plotly advanced**')
        st.plotly_chart(progress_against_target_bar_chart(progress_against_target_synthetic_df))

with long_tail_highlights_tab:
    st.subheader('Highlighting a very small long tail')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/covid_plot.py)")
    st.write('')

    with st.container(border=True):
        st.dataframe(covid_df, hide_index=True)

    with st.container(border=True):
        st.write('**Simple plot**')
        st.plotly_chart(covid_bar_chart_plot(covid_df, simple_plot=True))

    with st.container(border=True):
        st.write('**Highlighting**')
        st.plotly_chart(covid_bar_chart_plot(covid_df))









