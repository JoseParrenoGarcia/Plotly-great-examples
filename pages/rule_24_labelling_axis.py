import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    gdp_by_country_data,
    boys_names_data,
)

from utils.bar_chart_examples.gdp_country_plot import gdp_by_country_bar_chart_plot
from utils.bar_chart_examples.boys_name_plot import boys_names_bar_chart_plot

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
gdp_by_country_df = gdp_by_country_data()
boys_names_df = boys_names_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(long_yaxis_tab,
 long_xaxis_tab,
 axis_removal_tab,
 icons_tab,
 )  = st.tabs(
    ["⬆️ Long yAxis labels",
     "➡️ Long xAxis labels",
     "❌ Axis removal",
     "🖼️ Icons on axis",
     ]
)

with long_yaxis_tab:
    st.subheader('xxx')

    explanation_text = """
    xxx
    """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    st.plotly_chart(gdp_by_country_bar_chart_plot(gdp_by_country_df))

with long_xaxis_tab:
    # https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesenglandandwalesbabynamesstatisticsboys
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    st.plotly_chart(boys_names_bar_chart_plot(boys_names_df))
    st.dataframe(boys_names_df)

    # st.write("## Use also abbreviations for weekdays")

with axis_removal_tab:
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    # use baby names
    st.write("## Long yAxis labels")

with icons_tab:
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/2/rule-22-no-rounded-pointed-or-decorated-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")


    # use industry icons (https://www.ethnicity-facts-figures.service.gov.uk/work-pay-and-benefits/employment/employment-by-sector/latest/#download-the-data)
    st.write("## Long yAxis labels")

    # use country icons (maybe with the GDP data)

