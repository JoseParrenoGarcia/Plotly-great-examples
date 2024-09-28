import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (
    travel_gdp_share_data,
    life_expectancy_data,
    neighbouring_countries_ownership,
)
from utils.bar_chart_examples.travel_gdp_share_plot import (
    travel_gdp_share_plot_bar_chart,
    travel_gdp_share_plot_dot_chart,
    travel_gdp_share_plotly_express_bar_chart
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
dot_plot_tab, timeseries_area_plot_tab,  = st.tabs(
    ["🔵 Dot plot",
     "🕒 Timeseries",
     ]
)

with dot_plot_tab:
    st.subheader('Dot plots can be an elegant alternative to bar charts')
    st.write("""
        - **Reduced Visual Clutter**: When you need to compare a large number of data points, bars can be quite heavy. The end of each bar, so critical for understanding the chart's meaning, can become blurred by proximity to its neighbours.
        - **Pinpoint Accuracy**: Dot charts make it easier for your audience to pinpoint each category’s value. They are also less visually overwhelming.
        - **Minimalist Design**: Dot plots are more minimalist and make the audience focus their attention on the data points. This reduces the use of "ink" and helps reduce the cognitive load of comparing the end of each bar chart.
        - **Space Efficiency**: Dot plots often take up less space than bar charts, making them more suitable for dashboards or reports with limited space.
        - **Ease of Comparison**: Dot plots make it easier to compare multiple categories at a glance, as the dots are aligned along a common axis.
        - **Highlighting Trends**: Dot plots can more effectively highlight trends or patterns in the data, especially when combined with lines connecting the dots.
        - **Versatility**: Dot plots can be used for both small and large datasets, whereas bar charts can become cluttered with too many bars.
        - **Avoiding Misinterpretation**: Dot plots reduce the risk of misinterpreting the length of bars, which can sometimes be misleading in bar charts.
        """)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/6/16/rule-17-not-too-many-bars)")
    st.write('')

    with st.container(border=True):
        st.write('**Plotly express bar chart**')
        st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")
        st.plotly_chart(travel_gdp_share_plotly_express_bar_chart(df=travel_gdp_share_df))

    with st.container(border=True):
        st.write('**Bar chart**')
        st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

        st.plotly_chart(travel_gdp_share_chart_bar)
        st.write(travel_gdp_share_df)

    with st.container(border=True):
        st.write('**Dot chart**')
        st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L86)")

        st.plotly_chart(travel_gdp_share_chart_dot)

with timeseries_area_plot_tab:
    st.subheader('Bar charts are not great for timeseries plots')
    st.write("""
        - **Visual Overload**: Bar charts can become visually overwhelming when representing a crowded and long timeseries. The cognitive load of too much ink and spaces between bars can make it difficult to discern important trends.
        - **Trend Clarity**: Line plots make it easier to see trends over time. The continuous nature of line plots helps in understanding the change over time more clearly.
        - **Space Efficiency**: Line plots are more space-efficient as they do not need to leave space for the bars. This makes them more compact and easier to read.
        - **Highlighting Key Points**: Line plots can effectively highlight key points with markers and different line styles (e.g., dashed lines for estimated years), making it easier to focus on important data points.
        - **Reduced Cognitive Load**: Line plots reduce the cognitive load by simplifying the visual representation, allowing the viewer to process trends more easily.
        """)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/6/16/rule-17-not-too-many-bars)")
    st.write('')

    st.write('**Bar chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/1f5bbef0f5d881ff5309155883037af68603a167/utils/bar_chart_examples/life_expectancy_plot.py#L12)")

    st.plotly_chart(life_expectancy_chart_bar)

    st.write('**Line chart**')
    st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/1f5bbef0f5d881ff5309155883037af68603a167/utils/bar_chart_examples/life_expectancy_plot.py#L132)")

    st.plotly_chart(life_expectancy_scatter_plot)

# with abacus_plot_tab:
#     st.subheader('Another way to represent comparisons is through Abacus plots')
#     st.write("""
#         - **Reduced Cognitive Load**: Similar to dot plots, abacus plots reduce cognitive load by drawing immediate attention to the data points rather than the entire bar.
#         - **Immediate Focus**: The viewer's attention is immediately drawn to the dot, making it easier to interpret the data.
#         - **Fixed Comparison Range**: Abacus plots lend themselves well to fixed comparison ranges, making it easier to compare percentages or other metrics.
#         - **Space Efficiency**: Abacus plots often take up less space than bar charts, making them more suitable for dashboards or reports with limited space.
#         - **Avoiding Misinterpretation**: Abacus plots reduce the risk of misinterpreting the length of bars, which can sometimes be misleading in bar charts.
#         """)
#
#     st.write("")
#     st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/5/17/rule-16-if-in-doubt-use-a-bar-chart)")
#     st.write("")
#
#     st.write('**Bar chart**')
#     st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/e22e99d15bc296435d0df6ae8e81f4485e953aeb/utils/bar_chart_examples/neighbouring_countries_plot.py#L5)")
#     st.write("")
#
#     st.plotly_chart(neighbouring_countries_bar)
#
#     st.write("")
#     st.write("")
#     st.write('**Dot chart**')
#     st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/e22e99d15bc296435d0df6ae8e81f4485e953aeb/utils/bar_chart_examples/neighbouring_countries_plot.py#L77)")
#     st.write("")
#
#     st.plotly_chart(neighbouring_countries_abacus)




