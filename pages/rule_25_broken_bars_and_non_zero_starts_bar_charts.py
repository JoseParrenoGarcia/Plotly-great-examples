import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    mountain_or_structure_heights_data,
    sex_ratio_data,
    AE_waiting_times_data,
    speaking_languages_data,

)

from utils.bar_chart_examples.mountains_plot import mountain_bar_chart_plot, mountain_bar_chart_plot_plotly_express
from utils.bar_chart_examples.sex_ratio_at_birth_plot import (
    sex_ratio_at_birth_bar_chart_plot,
    sex_ratio_at_birth_dot_plot,
    sex_ratio_at_birth_bar_deviation_plot
)
from utils.bar_chart_examples.ae_waiting_times_plot import (AE_waiting_times_bar_chart_plot, AE_waiting_times_dot_plot)
from utils.bar_chart_examples.languages_plot import (languages_bar_chart_plot, languages_stacked_bar_chart)

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
mountain_or_structure_heights_df = mountain_or_structure_heights_data()
sex_ratio_df = sex_ratio_data()
AE_waiting_times_df = AE_waiting_times_data()
speaking_languages_df = speaking_languages_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(non_zero_starts_tab,
 hidden_differences_tab,
 small_or_big_drops_tab,
 dominating_category_tab,
 )  = st.tabs(
    ["0️⃣️ Non-zero starts",
     "🫣️ Hidden differences",
     "💧 Small or big drops",
     "🐘️ Dominating category",
     ]
)

with non_zero_starts_tab:
    st.subheader('Sometimes a chart needs to start at a non-zero value')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/9/26/rule-25-always-start-your-bar-charts-at-zero)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/mountains_plot.py)")

    with st.expander('Expand see to dataframe'):
        st.dataframe(mountain_or_structure_heights_df, hide_index=True)

    with st.container(border=True):
        st.plotly_chart(mountain_bar_chart_plot_plotly_express(mountain_or_structure_heights_df))

    with st.container(border=True):
        st.plotly_chart(mountain_bar_chart_plot(mountain_or_structure_heights_df))

with hidden_differences_tab:
    st.subheader('Starting at zero will hide differences')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/sex_ratio_at_birth_plot.py)")

    with st.container(border=True):
        st.plotly_chart(sex_ratio_at_birth_bar_chart_plot(sex_ratio_df))

        # Dot plot
        st.plotly_chart(sex_ratio_at_birth_dot_plot(sex_ratio_df))

        # Deviation plot
        st.plotly_chart(sex_ratio_at_birth_bar_deviation_plot(sex_ratio_df))

with small_or_big_drops_tab:
    st.subheader('Small or big drops in a timeseries are not well represented with a bar chart')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/ae_waiting_times_plot.py)")

    with st.container(border=True):
        st.plotly_chart(AE_waiting_times_bar_chart_plot(AE_waiting_times_df))
        st.plotly_chart(AE_waiting_times_dot_plot(AE_waiting_times_df))

with dominating_category_tab:
    st.subheader('How to deal with a dominating category?')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/languages_plot.py)")

    with st.container(border=True):
        st.plotly_chart(languages_bar_chart_plot(speaking_languages_df))
        st.plotly_chart(languages_stacked_bar_chart(speaking_languages_df))





# sex at birth ratio: https://ourworldindata.org/gender-ratio#:~:text=This%20is%20what%20the%20World,107%20boys%20per%20100%20girls.
# percentage waiting times: https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/
# speaking languages: https://www.ons.gov.uk/datasets/TS024/editions/2021/versions/1