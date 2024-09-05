import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import travel_gdp_share_data
from utils.bar_chart_examples.travel_gdp_share_plot import travel_gdp_share_plot_bar_chart



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
travel_gdp_share_df = travel_gdp_share_data()
travel_gdp_share_chart = travel_gdp_share_plot_bar_chart(df=travel_gdp_share_df)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
dot_plot_tab, timeseries_area_plot_tab = st.tabs(["🔵 Dot plots", "🕒 Timeseries area plots"])

with dot_plot_tab:
    st.subheader('Dot plots can be an elegant alternative to bar charts')

    st.write('**Whilst this is well designed bar chart**')

    bullet_points = """
    - Not too many categories, but enough for experts to have a detailed view
    - Carefully chosen colour: 1 colour for countries and 1 for the average. In addition, we have replicated the RGB colours used in the EU flag
    - The *Avg.* category helps divide the countries to get a clear view of our definition of high vs low
    - Numbers only with 1 decimal point so that it doesn't get too cluttered
    - Chart has yaxis removed, it doesn't add value to have the range of values. We already show them in each bar.
    - Clear title, definition of the chart and footer with the source
    """
    st.markdown(bullet_points)

    st.plotly_chart(travel_gdp_share_chart)

    st.divider()

    st.write('**Dot plots can be elegant and provide a minimalist view**')

    st.plotly_chart(travel_gdp_share_chart)




