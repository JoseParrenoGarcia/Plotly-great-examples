import streamlit as st
from utils.pages_format import pages_format

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


# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(long_yaxis_tab,
 long_xaxis_tab,
 axis_removal_tab,
 icons_tab,
 )  = st.tabs(
    ["🎨 Long yAxis labels",
     "🏢 Long xAxis labels",
     "🦎 Axis removal",
     "🫐 Icons on axis",
     ]
)

with long_yaxis_tab:
    # https://databank.worldbank.org/reports.aspx?source=2&series=NY.GDP.MKTP.CD&country=&_gl=1*1jzomxe*_gcl_au*MTA2MTc2ODI5OS4xNzI2NDYxOTk4#
    st.write("## Long yAxis labels")

with long_xaxis_tab:
    # https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesenglandandwalesbabynamesstatisticsboys
    st.write("## Long xAxis labels")
    st.write("## Use also abbreviations for weekdays")

with axis_removal_tab:
    # use baby names
    st.write("## Long yAxis labels")

with icons_tab:
    # use industry icons (https://www.ethnicity-facts-figures.service.gov.uk/work-pay-and-benefits/employment/employment-by-sector/latest/#download-the-data)
    st.write("## Long yAxis labels")

    # use country icons (maybe with the GDP data)

