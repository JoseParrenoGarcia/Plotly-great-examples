import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    gdp_by_country_data,
    boys_names_data,
    favourite_weekday_data,
    employment_by_sector_data,
)

from utils.bar_chart_examples.gdp_country_plot import gdp_by_country_bar_chart_plot, gdp_by_country_bar_chart_plot_plotly_express
from utils.bar_chart_examples.boys_name_plot import boys_names_bar_chart_plot
from utils.bar_chart_examples.favourite_weekday_plot import favourite_weekday_bar_chart_plot
from utils.bar_chart_examples.emplyoment_by_industry_plot import employment_by_industry_bar_chart_plot, employment_by_industry_bar_chart_plotly_express

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
favourite_weekday_df = favourite_weekday_data()
employment_by_sector_df = employment_by_sector_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(long_yaxis_tab,
 long_xaxis_tab,
 icons_tab,
 abbreviations_tab,

 )  = st.tabs(
    ["⬆️ Long yAxis labels",
     "➡️ Long xAxis labels",
     "🖼️ Icons on axis",
     "🔤 Abbreviations",
     ]
)

with long_yaxis_tab:
    st.subheader('You cant understand labels such as trillions in the yaxis')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/gdp_country_plot.py)")

    with st.container(border=True):
        st.dataframe(gdp_by_country_df)

    with st.container(border=True):
        st.plotly_chart(gdp_by_country_bar_chart_plot_plotly_express(gdp_by_country_df))

    with st.container(border=True):
        st.plotly_chart(gdp_by_country_bar_chart_plot(gdp_by_country_df, add_context=False))

    with st.container(border=True):
        st.plotly_chart(gdp_by_country_bar_chart_plot(gdp_by_country_df))

with long_xaxis_tab:
    st.subheader('For long texts in the xaxis, a horizontal plot is your best option.')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/emplyoment_by_industry_plot.py)")

    with st.container(border=True):
        st.dataframe(employment_by_sector_df)

    with st.container(border=True):
        st.plotly_chart(employment_by_industry_bar_chart_plotly_express(employment_by_sector_df))

    with st.container(border=True):
        st.plotly_chart(employment_by_industry_bar_chart_plot(employment_by_sector_df, with_emojis=False))


with abbreviations_tab:
    st.subheader('You cant use abbreviations carefully')
    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/favourite_weekday_plot.py)")

    with st.container(border=True):
        st.plotly_chart(favourite_weekday_bar_chart_plot(favourite_weekday_df))

with icons_tab:
    st.subheader('Icons on axis can help understand labels more easily')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/2/rule-22-no-rounded-pointed-or-decorated-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/emplyoment_by_industry_plot.py)")

    with st.container(border=True):
        st.plotly_chart(employment_by_industry_bar_chart_plot(employment_by_sector_df))

