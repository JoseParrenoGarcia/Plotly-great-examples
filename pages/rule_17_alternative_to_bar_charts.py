import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (
    travel_gdp_share_data,
    life_expectancy_data,
    neighbouring_countries_ownership,
)
from utils.bar_chart_examples.travel_gdp_share_plot import (
    travel_gdp_share_plot_bar_chart,
    travel_gdp_share_plot_dot_chart
)
from utils.bar_chart_examples.life_expectancy_plot import (
    life_expectancy_bar_chart,
    life_expectancy_scatter_plot,
    life_expectancy_bar_chart_multiple_countries,
    life_expectancy_scatter_plot_multiple_countries,
)
from utils.bar_chart_examples.neighbouring_countries_plot import (
    neighbouring_countries_bar_chart,
    neighbouring_countries_abacus_chart,
)



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
life_expectancy_df_russia = life_expectancy_df[life_expectancy_df['country'].isin(['Russia'])]
life_expectancy_chart_bar = life_expectancy_bar_chart(df=life_expectancy_df_russia)
life_expectancy_scatter_plot = life_expectancy_scatter_plot(df=life_expectancy_df_russia)

life_expectancy_df_multiple = life_expectancy_df[life_expectancy_df['country'].isin([
    'Russia', 'Spain', 'Germany', 'Brazil', 'Argentina', 'Japan']
)]
life_expectancy_chart_bar_multiple = life_expectancy_bar_chart_multiple_countries(df=life_expectancy_df_multiple)
life_expectancy_scatter_plot_multiple = life_expectancy_scatter_plot_multiple_countries(df=life_expectancy_df_multiple)

neighbouring_countries_df = neighbouring_countries_ownership()
neighbouring_countries_bar = neighbouring_countries_bar_chart(df=neighbouring_countries_df)
neighbouring_countries_abacus = neighbouring_countries_abacus_chart(df=neighbouring_countries_df)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
dot_plot_tab, timeseries_area_plot_tab, abacus_plot_tab = st.tabs(
    ["🔵 Dot plot",
     "🕒 Timeseries",
     "🧮 Abacus plot",
     ]
)

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

    st.write('**Bar chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.plotly_chart(travel_gdp_share_chart_bar)

    st.write('**Dot chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L86)")

    st.plotly_chart(travel_gdp_share_chart_dot)

with timeseries_area_plot_tab:
    st.subheader('Bar charts are not great for timeseries plots')
    st.write('Bar charts can be used for timeseries, but, when you have lots of bars representing a crowded and long timeseries, '
             'the mind can struggle to understand the important trends. The change over time story is less '
             'clear as you have the cognitive load of too much ink and spaces between bars. In addition, '
             'you head tends to automatically compare the ends of bars, bringing you away from processing a trend.')

    st.write('Whilst I have tried to keep the bar chart as clean as possible, the line plot is clearer. '
             'The line plot makes it easier to see the trend over time. The line plot is also more '
             'space efficient, as it does not need to leave space for the bars. This makes the line plot '
             'more compact and easier to read. In the line chart, I have also highlighted the annotated years with '
             'bolder markers, and used a dashed line for estimated years.')

    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/6/16/rule-17-not-too-many-bars)")

    st.write('**Bar chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/1f5bbef0f5d881ff5309155883037af68603a167/utils/bar_chart_examples/life_expectancy_plot.py#L12)")

    st.plotly_chart(life_expectancy_chart_bar)

    st.write('**Line chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/1f5bbef0f5d881ff5309155883037af68603a167/utils/bar_chart_examples/life_expectancy_plot.py#L132)")

    st.plotly_chart(life_expectancy_scatter_plot)

    st.divider()

    st.subheader('This is even worse when you have multiple categories')
    st.write('The moment that you have different categories, a timeseries using a bar chart breaks. It '
             'is impossible to compare different categories as the bars are trying to all '
             'fit into the tiny space reserved for each year. The colours are hard to distinguish.')

    st.write("The line chart however is much clearer. "
             "Whilst the colouring might not be the best for this example, it is actually possible to see the differences "
             "between a couple of trends or easy to answer which country has the lower life expectancy.")

    st.write('**Bar chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/1f5bbef0f5d881ff5309155883037af68603a167/utils/bar_chart_examples/life_expectancy_plot.py#L278)")

    st.plotly_chart(life_expectancy_chart_bar_multiple)

    st.write('**Line chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/1f5bbef0f5d881ff5309155883037af68603a167/utils/bar_chart_examples/life_expectancy_plot.py#L327)")

    st.plotly_chart(life_expectancy_scatter_plot_multiple)

with abacus_plot_tab:
    st.write(neighbouring_countries_df)
    st.plotly_chart(neighbouring_countries_bar)
    st.plotly_chart(neighbouring_countries_abacus)




