import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (
    favourite_animal_data,
    favourite_weekday_data
)

from utils.bar_chart_examples.favourite_animal import favourite_animal_bar_chart_plot

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
favourite_animal_df = favourite_animal_data()
favourite_weekday_df = favourite_weekday_data()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
(other_tab,
 ordinal_categories_tab,
 groupings_tab,
 distributions_tab,
 )  = st.tabs(
    ["🧩 Other segment",
     "🔢 Ordinal categories",
     "🫐 Groupings",
     "📊 Distributions",
     ]
)

with other_tab:
    st.subheader('xxxx')

    explanation_text = """
            xxx
            """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write('')
    st.plotly_chart(favourite_animal_bar_chart_plot(favourite_animal_df))


with ordinal_categories_tab:
    st.subheader('xxxx')

    explanation_text = """
            xxx
            """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write('')
    st.dataframe(favourite_weekday_df)

with groupings_tab:
    st.subheader('xxxx')

    explanation_text = """
                xxx
                """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write('')
    # display our geo group data

with distributions_tab:
    st.subheader('xxxx')

    explanation_text = """
                    xxx
                    """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write('')
    # display housing data


