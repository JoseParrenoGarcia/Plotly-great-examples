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
from utils.bar_chart_examples.ons_data_subplots import ons_data_subplots_bar_charts

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

    explanation_text = """
        ###### Effective Use of Colours in Bar Charts
        - **Clarity and Focus**: Using colours sparingly in bar charts helps maintain clarity and focus. Minimal colour variety ensures that the viewer is not overwhelmed by too many colours.
        - **Appropriate Use of Same Colour**: In some cases, using the same colour for all bars is appropriate, especially when you do not want to emphasize any particular category.
        - **Effective Highlighting**: When highlighting is necessary, using simple contrasting colours can be very effective. This approach ensures that the highlighted data stands out without overwhelming the viewer.
        """
    st.markdown(explanation_text)

    explanation_text = """
        ###### Examples of effective colour use
        - **Two Colours and One Pattern Fill**: In the examples below, we use only two colours and one pattern fill to convey our message.
        - **Clear but Non-Intrusive Contrast**: Choosing colours with clear but non-intrusive contrast, such as grey for the majority and a distinct colour for highlights, ensures that the highlighted data stands out.
        - **Enhanced Interpretability**: This approach makes the chart easier to interpret and more visually appealing.
        """
    st.markdown(explanation_text)

    st.write('')
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
    st.subheader('One colour highlighted bars & subplots are great for multi-dimensional comparisons')
    explanation_text = """

    Highlighting the Uruguay bar with a distinct color while keeping all other countries in grey, and organizing these visualizations into subplots, offers several advantages for multi-dimensional comparisons:

    1. **Clarity and Focus**: By using a single color to highlight Uruguay, the viewer's attention is immediately drawn to this specific country. This makes it easier to compare Uruguay's performance across different dimensions without being distracted by other data points.
    2. **Consistency**: Using the same color for Uruguay across all subplots ensures consistency. This helps the viewer quickly identify Uruguay in each subplot, facilitating a more straightforward comparison across multiple metrics.
    3. **Reduced Visual Clutter**: Keeping all other countries in grey minimizes visual clutter. This approach simplifies the chart, making it easier to interpret the data and focus on the highlighted country.
    4. **Effective Use of Subplots**: Organizing the data into subplots allows for the simultaneous comparison of multiple dimensions. Each subplot represents a different metric, and the consistent highlighting of Uruguay across these subplots enables a comprehensive view of its performance relative to other countries.
    5. **Enhanced Comparability**: The combination of highlighting and subplots makes it easier to spot trends, patterns, and outliers. For instance, if Uruguay consistently performs well or poorly across different metrics, this will be immediately apparent.
    In summary, this approach leverages color and layout to enhance the readability and interpretability of complex data, making it easier to draw meaningful insights from multi-dimensional comparisons.
    """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.plotly_chart(ons_data_subplots_bar_charts(ons_data_df))










