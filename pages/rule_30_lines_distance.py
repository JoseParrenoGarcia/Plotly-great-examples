import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    driving_women_data,
    space_race_data,
    island_distances_data,
    political_view_survey_data
)

from utils.line_chart_examples.driving_women_plot import driving_women_line_chart
from utils.line_chart_examples.space_race_plot import space_race_line_chart

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
driving_women_data_df = driving_women_data()
space_race_data_df = space_race_data()
island_distances_data_df = island_distances_data()
political_view_survey_data_df = political_view_survey_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(timeseries_tab,
 timeline_tab,
 physical_distance_tab,
 other_distances_tab,
 )  = st.tabs(
    ["📈 Timeseries",
     "⏱️ Timeline",
     "🚶‍♀️ Physical distance",
     "📏 Other types of distance",
     ]
)

with timeline_tab:
    st.subheader('Timeline')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")

    with st.expander("Expand to see the data"):
        st.dataframe(space_race_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(space_race_line_chart(space_race_data_df))

with timeseries_tab:
    st.subheader('Time series')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")

    with st.expander("Expand to see the data"):
        st.dataframe(driving_women_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(driving_women_line_chart(driving_women_data_df))

with physical_distance_tab:
    st.subheader('Physical distances')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")

    with st.expander("Expand to see the data"):
        st.dataframe(island_distances_data_df, hide_index=True)

with other_distances_tab:
    st.subheader('Other distances')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")

    with st.expander("Expand to see the data"):
        st.dataframe(political_view_survey_data_df, hide_index=True)

