import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    fertility_rates_data,
)

from utils.line_chart_examples.fertility_rates_plots import fertility_rates_plotly_express_line_chart, fertility_rates_line_plot

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
    st.subheader('Too many lines')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/5/4/rule-31-line-charts-shouldnt-have-too-many-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(fertility_rates_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(fertility_rates_plotly_express_line_chart(fertility_rates_data_df))

with sparse_tab:
    st.subheader('Line sparsity')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/5/4/rule-31-line-charts-shouldnt-have-too-many-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(fertility_rates_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(fertility_rates_plotly_express_line_chart(fertility_rates_data_df[fertility_rates_data_df['Country Name'].isin(['France', 'United Kingdom', 'Germany', 'Italy'])]))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(fertility_rates_plotly_express_line_chart(fertility_rates_data_df[fertility_rates_data_df['Country Name'].isin(['Niger', 'Korea, Rep.', 'United States', 'World'])]))

with grey_out_tab:
    st.subheader('Grey out to provide context')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/5/4/rule-31-line-charts-shouldnt-have-too-many-lines)")

    with st.expander("Expand to see the data"):
        st.dataframe(fertility_rates_data_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(fertility_rates_line_plot(
            df=fertility_rates_data_df,
            title='Gulf states have seen fertility rates plummet since the 1960s',
            countries_to_highlight=['Kuwait', 'Bahrain', 'United Arab Emirates', 'Saudi Arabia', 'Oman']
        )

        )

    st.write('')
    with st.container(border=True):
        st.plotly_chart(fertility_rates_line_plot(
            df=fertility_rates_data_df,
            title='In sub-saharan Africa, fertility rates have remained high',
            countries_to_highlight=['Niger', 'Somalia', 'Congo, Dem. Rep.', 'Mali']
        )

        )


# with other_distances_tab:
#     st.subheader('Other distances')
#
#     st.write('')
#     st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2022/1/28/rule-30-a-line-chart-should-only-show-change-over-time)")
#
#     with st.expander("Expand to see the data"):
#         st.dataframe(political_view_survey_data_df, hide_index=True)

