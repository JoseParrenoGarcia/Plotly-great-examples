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

    with st.container(border=True):
        st.write('**Dot chart**')
        st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L86)")

        st.plotly_chart(travel_gdp_share_chart_dot)

with timeseries_area_plot_tab:
    st.subheader('Bar charts are not great for timeseries plots')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/6/16/rule-17-not-too-many-bars)")
    st.write('')

    with st.container(border=True):
        st.write('**Bar chart**')
        st.markdown("🔗 [To see the code which generated this plot, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/1f5bbef0f5d881ff5309155883037af68603a167/utils/bar_chart_examples/life_expectancy_plot.py#L12)")

        st.plotly_chart(life_expectancy_chart_bar)

    with st.container(border=True):
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




