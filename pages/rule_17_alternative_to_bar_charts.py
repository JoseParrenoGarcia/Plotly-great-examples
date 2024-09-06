import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (travel_gdp_share_data, life_expectancy_data)
from utils.bar_chart_examples.travel_gdp_share_plot import (
    travel_gdp_share_plot_bar_chart,
    travel_gdp_share_plot_dot_chart)
from utils.bar_chart_examples.life_expectancy_plot import (
    life_expectancy_bar_chart)



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

life_expectancy_df = life_expectancy_data()
# life_expectancy_df = life_expectancy_df[life_expectancy_df['country'].isin(['Russia', 'Spain'])]
life_expectancy_df = life_expectancy_df[life_expectancy_df['country'].isin(['Spain'])] # germany, russia and spain
life_expectancy_chart_bar = life_expectancy_bar_chart(df=life_expectancy_df)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
dot_plot_tab, timeseries_area_plot_tab = st.tabs(["🔵 Dot plots", "🕒 Timeseries"])

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
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.plotly_chart(travel_gdp_share_chart_bar)

    st.divider()
    st.write('**Dot chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L86)")

    st.plotly_chart(travel_gdp_share_chart_dot)

with timeseries_area_plot_tab:
    st.dataframe(life_expectancy_df)
    st.plotly_chart(life_expectancy_chart_bar)




