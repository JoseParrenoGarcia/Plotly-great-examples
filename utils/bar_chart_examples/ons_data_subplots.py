import plotly.graph_objects as go
from plotly.subplots import make_subplots

def ons_data_subplots_bar_charts(ons_data_df):
    fig = make_subplots(rows=3, cols=2, shared_yaxes=True, subplot_titles=(
        'GDP per Capita', 'CO2 Emissions per Capita', 'Child Mortality',
        'Air Pollution', 'Gov Health Expenditure', 'Population in Extreme Poverty'))

    # features = [
    #     'GDP per capita', 'CO2 emissions per capita', 'Child mortality',
    #     'Air pollution', 'Gov health expenditure', 'Population in extreme poverty'
    # ]

    return ons_data_df