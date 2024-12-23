import plotly.graph_objects as go
import plotly.express as px

def refugees_plotly_express_line_chart(df):
    fig = px.line(df,
                  x='Year',
                  y='Refugees',
                  color='countries_to_display',
                  title='Refugees by country')

    # Minor layout customization
    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

# def refugees_line_chart(df, type='line'):
#     fig = go.Figure()
#
#     fig.update_layout(
#         title='Refugees by country',
#         xaxis_title='Year',
#         yaxis_title='Number of refugees',
#         template='plotly_white'
#     )
#
#     if type == 'area':
#         fig.update_traces(mode='lines+markers', fill='tozeroy')
#
#     return fig