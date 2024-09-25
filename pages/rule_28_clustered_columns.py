import streamlit as st
from utils.pages_format import pages_format

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


# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(many_categories_tab,
 outlier_categories_tab,
 comparing_2_groups_tab,
 )  = st.tabs(
    ["📊 Many categories",
     "📊 Outlier category",
     "👥 Comparing 2 groups",
     ]
)

with many_categories_tab:
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    # https://rshiny.ilo.org/dataexplorer44/?lang=en&id=EMP_TEMP_ECO_OCU_NB_A

with outlier_categories_tab:
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    # percentage_of_global_food_exports

with comparing_2_groups_tab:
    st.subheader('xxx')

    explanation_text = """
        xxx
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/8/18/rule-24-label-your-bars-and-axes)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/gdp_per_capita_plot.py#L5)")

    # https://www.uefa.com/nationalassociations/uefarankings/club/?year=2025


