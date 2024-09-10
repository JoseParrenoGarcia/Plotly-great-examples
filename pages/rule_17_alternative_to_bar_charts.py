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

neighbouring_countries_df = neighbouring_countries_ownership()
neighbouring_countries_bar = neighbouring_countries_bar_chart(df=neighbouring_countries_df)
neighbouring_countries_abacus = neighbouring_countries_abacus_chart(df=neighbouring_countries_df)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
dot_plot_tab, abacus_plot_tab, timeseries_area_plot_tab,  = st.tabs(
    ["🔵 Dot plot",
     "🧮 Abacus plot",
     "🕒 Timeseries",
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

with abacus_plot_tab:
    st.subheader('Another way to represent comparisons is through Abacus plots')
    st.write('Similar to dot plots, if we have a horizontal bar chart with lots of categories, '
             'and where our aim to compare values between them, the bar chart can become a bit heavy '
             'from a cognitive load point of view.')

    st.write('Even though the bar chart below has an OK design, your mind actually scans the whole bar '
             'chart until you get to the displayed data point at the end of it. That doesnt happen with the '
             'abacus dot plot, because you are immediately drawn to the dot.')

    st.write('In addition, because we want to show percentages, the bar chart has this wierd look of being shrinked. '
             'We could have expanded the bar charts so that the range was between 0 to 67, and not 0 to 100, but then '
             'the % representation might have been a bit skewed. Again, the abacus dot plot lends well into have '
             'this fixed comparison range.')

    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/5/17/rule-16-if-in-doubt-use-a-bar-chart)")
    st.write("")
    st.write("")

    st.write('**Bar chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/e22e99d15bc296435d0df6ae8e81f4485e953aeb/utils/bar_chart_examples/neighbouring_countries_plot.py#L5)")
    st.write("")

    st.plotly_chart(neighbouring_countries_bar)

    st.write("")
    st.write("")
    st.write('**Dot chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/e22e99d15bc296435d0df6ae8e81f4485e953aeb/utils/bar_chart_examples/neighbouring_countries_plot.py#L77)")
    st.write("")

    st.plotly_chart(neighbouring_countries_abacus)




