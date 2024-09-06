import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import travel_gdp_share_data
from utils.bar_chart_examples.travel_gdp_share_plot import (
    travel_gdp_share_plot_bar_chart,
    travel_gdp_share_plot_dot_chart)



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
travel_gdp_share_chart_bar = travel_gdp_share_plot_bar_chart(df=travel_gdp_share_df)
travel_gdp_share_chart_dot = travel_gdp_share_plot_dot_chart(df=travel_gdp_share_df)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
dot_plot_tab, timeseries_area_plot_tab = st.tabs(["🔵 Dot plots", "🕒 Timeseries area plots"])

with dot_plot_tab:
    st.subheader('Dot plots can be an elegant alternative to bar charts')
    st.write('When you need to compare a large number of datapoints, bars can be quite heavy. '
             'The end of each bar, so critical for understanding the charts '
             'meaning, can become blurred by proximity to its neighbours. Dot charts '
             'make it easier for your audience to pinpoint each category’s value. '
             'They are also less visually overwhelming.')

    st.write('You can see below a well designed bar chart following all best practices. It is '
             'still very legible and easy to understand. However, the dot plot is more minimalist '
             'and makes the audience focus thr attention on the data points. This reduces the use '
             'of "ink" and helps redue cognitive load of comparing the end of each bar chart.')

    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/6/16/rule-17-not-too-many-bars)")

    st.divider()
    st.write('**Bar chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/your-username/your-repo)")

    st.plotly_chart(travel_gdp_share_chart_bar)

    st.divider()
    st.write('**Dot chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/your-username/your-repo)")

    st.plotly_chart(travel_gdp_share_chart_dot)




