import streamlit as st
from utils.pages_format import pages_format

# ---------------------------------------------------------------------
# HOME PAGE - CONFIGURATION
# ---------------------------------------------------------------------
st.set_page_config(
    layout="wide",
)

pages_format()

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
st.header("Welcome to the Awesome Plotly with Code App")
st.write("In this app I aim to cover best data visualisation practices using Plotly. For each plot, "
         "I will direct you to my GitHub repository where you can find the code to reproduce the plot. "
         "I assume you have some basic knowledge of Python and Plotly, therefore, I wont go into commenting"
         "or explaining the related Plotly code (tip: if you want to understand it, copy and paste it into ChatGPT "
         "and ask it to explain it to you). ")

st.write("Many of these examples and plots have had inspiration from a company called **AddTwoDigital**. They have an amazing blog, which is well worth the read.")
st.write("I have no affiliation with them, but as I said, their content is amazing. I have permission from Adam Frost to "
         "recreate some of their contents using Plotly. I know they mostly use DataWrapper (I need to try DataWrappers python API) "
         "but I am a big fan of Plotly and I wanted to try to recreate this stunning visuals using Plotly. ")

st.divider()

st.write("I hope you enjoy the app and find it useful. If you have any questions or suggestions, please let me know. ")

st.markdown("🌐 [AddTwoDigital blog](https://www.addtwodigital.com/blog)")

