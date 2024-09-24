import streamlit as st
from utils.pages_format import pages_format

from utils.load_data import (
    mountain_or_structure_heights_data,
    sex_ratio_data,
    AE_waiting_times_data,

)

from utils.bar_chart_examples.mountains_plot import mountain_bar_chart_plot
from utils.bar_chart_examples.sex_ratio_at_birth_plot import (
    sex_ratio_at_birth_bar_chart_plot,
    sex_ratio_at_birth_dot_plot,
    sex_ratio_at_birth_bar_deviation_plot
)
from utils.bar_chart_examples.ae_waiting_times import (AE_waiting_times_bar_chart_plot, AE_waiting_times_dot_plot)

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

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(non_zero_starts_tab,
 hidden_differences_tab,
 small_or_big_drops_tab,
 icons_tab,
 )  = st.tabs(
    ["0️⃣️ Non-zero starts",
     "🫣️ Hidden differences",
     "💧 Small or big drops",
     "🖼️ Icons on axis",
     ]
)

with non_zero_starts_tab:
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    st.plotly_chart(mountain_bar_chart_plot(mountain_or_structure_heights_df))

with hidden_differences_tab:
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    st.plotly_chart(sex_ratio_at_birth_bar_chart_plot(sex_ratio_df))

    # Dot plot
    st.plotly_chart(sex_ratio_at_birth_dot_plot(sex_ratio_df))

    # Deviation plot
    st.plotly_chart(sex_ratio_at_birth_bar_deviation_plot(sex_ratio_df))

with small_or_big_drops_tab:
    st.subheader('xxx')

    explanation_text = """
            xxx
            """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    st.plotly_chart(AE_waiting_times_bar_chart_plot(AE_waiting_times_df))
    st.plotly_chart(AE_waiting_times_dot_plot(AE_waiting_times_df))
    # st.dataframe(AE_waiting_times_df)



# sex at birth ratio: https://ourworldindata.org/gender-ratio#:~:text=This%20is%20what%20the%20World,107%20boys%20per%20100%20girls.
# percentage waiting times: https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/
# speaking languages: https://www.ons.gov.uk/datasets/TS024/editions/2021/versions/1