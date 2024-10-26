import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (
    favourite_animal_data,
    favourite_weekday_data,
    smoking_rate_data,
    housing_data
)

from utils.bar_chart_examples.favourite_animal_plot import favourite_animal_bar_chart_plot, favourite_animal_bar_chart_plot_plotly_express
from utils.bar_chart_examples.favourite_weekday_plot import favourite_weekday_bar_chart_plot, favourite_weekday_bar_chart_plot_plotly_express
from utils.bar_chart_examples.smoking_rates_plot import smoking_rates_plot
from utils.bar_chart_examples.housing_plot import housing_bar_chart_plot

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
smoking_rate_df = smoking_rate_data()
housing_df = housing_data()

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
    st.subheader('Pushing an outlier category to the end of the bar chart')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/27/rule-19-arrange-your-bars-from-largest-to-smallest)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/favourite_animal_plot.py)")

    with st.expander("Expand to see the data"):
        st.dataframe(favourite_animal_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(favourite_animal_bar_chart_plot_plotly_express(favourite_animal_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(favourite_animal_bar_chart_plot(favourite_animal_df, other_ordering=False))


    st.write('')
    with st.container(border=True):
        st.plotly_chart(favourite_animal_bar_chart_plot(favourite_animal_df))


with ordinal_categories_tab:
    st.subheader('Certain types of data should be ordered naturally, not from highest to lowest')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/27/rule-19-arrange-your-bars-from-largest-to-smallest)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/favourite_weekday_plot.py)")

    with st.expander("Expand to see the data"):
        st.dataframe(favourite_weekday_df, hide_index=True)

    st.write('')
    with st.container(border=True):
        st.plotly_chart(favourite_weekday_bar_chart_plot_plotly_express(favourite_weekday_df))

    st.write('')
    with st.container(border=True):
        st.plotly_chart(favourite_weekday_bar_chart_plot(favourite_weekday_df))

with groupings_tab:
    st.subheader('Grouped categories break the higher to lower order between groups, but you keep it intra-group')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/smoking_rates_plot.py)")
    st.write('')

    ### GROUPING BY GEO - no need for colour
    with st.container(border=True):
        st.plotly_chart(smoking_rates_plot(smoking_rate_df))

with distributions_tab:
    st.subheader('Maintaining X-axis Order in Distributions')

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/27/rule-19-arrange-your-bars-from-largest-to-smallest)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/main/utils/bar_chart_examples/housing_plot.py)")

    st.write('')
    with st.container(border=True):
        st.plotly_chart(housing_bar_chart_plot(housing_df))



