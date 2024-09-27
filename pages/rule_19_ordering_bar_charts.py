import streamlit as st
from utils.pages_format import pages_format
from utils.load_data import (
    favourite_animal_data,
    favourite_weekday_data,
    smoking_rate_data,
    housing_data
)

from utils.bar_chart_examples.favourite_animal_plot import favourite_animal_bar_chart_plot
from utils.bar_chart_examples.favourite_weekday_plot import favourite_weekday_bar_chart_plot
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

    explanation_text = """
        Moving an outlier category (like "Other") to the end of the bar chart can be beneficial for several reasons:
        - **Clarity**: Placing the outlier category at the end helps in clearly distinguishing it from the main categories, making the chart easier to read and understand.
        - **Focus**: It allows viewers to focus on the primary data categories first, without being distracted by the outlier.
        - **Comparison**: It facilitates better comparison among the main categories by keeping them grouped together.
        - **Visual Appeal**: Enhances the visual appeal of the chart by maintaining a logical order, which can be more aesthetically pleasing.
        - **Data Integrity**: Ensures that the outlier does not skew the perception of the data distribution among the main categories.
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/27/rule-19-arrange-your-bars-from-largest-to-smallest)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write('')
    st.plotly_chart(favourite_animal_bar_chart_plot(favourite_animal_df))


with ordinal_categories_tab:
    st.subheader('Certain types of data should be ordered naturally, not from highest to lowest')

    explanation_text = """
        When dealing with ordinal categories (such as days of the week or positive to negative categories), it is important to maintain their natural order instead of simply ordering from highest to lowest for several reasons:
        - **Contextual Understanding**: Ordinal categories have a specific sequence that provides context. For example, days of the week follow a natural progression from Monday to Sunday.
        - **Comparative Analysis**: Maintaining the order allows for easier comparison within the context of the category. For instance, seeing the progression of values across the days of the week can reveal trends that might be lost if the order is changed.
        - **Data Integrity**: Preserving the natural order ensures that the data is represented accurately and meaningfully, maintaining the integrity of the information being conveyed.
        - **User Expectations**: Viewers expect ordinal categories to follow a logical sequence. Disrupting this order can lead to confusion and misinterpretation of the data.
        - **Trend Identification**: Keeping the order helps in identifying patterns and trends that are inherent to the sequence of the categories, which might be obscured if the order is altered.
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/27/rule-19-arrange-your-bars-from-largest-to-smallest)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write('')
    st.plotly_chart(favourite_weekday_bar_chart_plot(favourite_weekday_df))

with groupings_tab:
    st.subheader('Grouped categories break the higher to lower order between groups, but you keep it intra-group')

    explanation_text = """
        When visualizing data for countries, it is beneficial to group them by continent before ordering from high to low for several reasons:
        - **Contextual Clarity**: Grouping by continent provides a clear context, making it easier to understand regional patterns and comparisons.
        - **Comparative Analysis**: It allows for better comparison within each continent, highlighting regional differences and similarities.
        - **Data Integrity**: Preserving the grouping ensures that the data is represented accurately, maintaining the integrity of the information.
        - **User Expectations**: Viewers often expect geographical data to be grouped by regions, which aligns with their mental models and expectations.
        - **Trend Identification**: Grouping helps in identifying trends and patterns specific to each continent, which might be obscured if the data is ordered solely by value.
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/12/rule-18-dont-use-multi-coloured-bars)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b4fc56427486fb67e1938090481b77ca94ad7667/utils/bar_chart_examples/smoking_rates_plot.py#L5)")
    st.write('')

    ### GROUPING BY GEO - no need for colour
    st.plotly_chart(smoking_rates_plot(smoking_rate_df))

with distributions_tab:
    st.subheader('Maintaining X-axis Order in Distributions')

    explanation_text = """
        When plotting a distribution, it is crucial to keep the x-axis ordered based on the x-axis values rather than ordering by the y-axis feature for several reasons:
        - **Contextual Accuracy**: The x-axis values represent the natural order of the data points. Changing this order can misrepresent the distribution.
        - **Trend Identification**: Keeping the x-axis in its natural order helps in identifying trends and patterns that are inherent to the data.
        - **Data Integrity**: Preserving the x-axis order ensures that the data is represented accurately and meaningfully, maintaining the integrity of the information being conveyed.
        - **User Expectations**: Viewers expect the x-axis to follow a logical sequence. Disrupting this order can lead to confusion and misinterpretation of the data.
        - **Comparative Analysis**: Maintaining the x-axis order allows for easier comparison within the context of the distribution, revealing insights that might be lost if the order is changed.
        """
    st.markdown(explanation_text)

    st.write('')
    st.markdown("🌐 [Original article used for inspiration](https://www.addtwodigital.com/add-two-blog/2021/7/27/rule-19-arrange-your-bars-from-largest-to-smallest)")
    st.markdown("🔗 [To see the code which generated these plots, navigate to the repo](https://github.com/JoseParrenoGarcia/Plotly-great-examples/blob/b75ca0485b4bb1cb71c8d4d7d4e41b1b36dd6cb5/utils/bar_chart_examples/travel_gdp_share_plot.py#L3)")

    st.write('')
    st.plotly_chart(housing_bar_chart_plot(housing_df))



