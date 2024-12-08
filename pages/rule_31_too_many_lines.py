import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    fertility_rates_data,
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
fertility_rates_data_df = fertility_rates_data()
# space_race_data_df = space_race_data()
# island_distances_data_df = island_distances_data()
# political_view_survey_data_df = political_view_survey_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(too_many_tab,
 sparse_tab,
 grey_out_tab,
 segment_tab,
 )  = st.tabs(
    ["📈 Too many lines",
     "⏱️ Too sparse",
     "🚶‍♀️ Greying out",
     "📏 Segment grouping",
     ]
)

with too_many_tab:
    st.subheader('Timeline')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/5/4/rule-31-line-charts-shouldnt-have-too-many-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(fertility_rates_data_df, hide_index=True)

# with timeseries_tab:
#     st.subheader('Time series')
#
#     st.write('')a
#     st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")
#     # st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/workforce_by_sector_plot.py)")
#
#     with st.expander("Expand to see the data"):
#         st.dataframe(driving_women_data_df, hide_index=True)
#
# with physical_distance_tab:
#     st.subheader('Physical distances')
#
#     st.write('')
#     st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")
#
#     with st.expander("Expand to see the data"):
#         st.dataframe(island_distances_data_df, hide_index=True)
#
# with other_distances_tab:
#     st.subheader('Other distances')
#
#     st.write('')
#     st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")
#
#     with st.expander("Expand to see the data"):
#         st.dataframe(political_view_survey_data_df, hide_index=True)

