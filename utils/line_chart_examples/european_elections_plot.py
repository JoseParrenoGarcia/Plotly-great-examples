import plotly.graph_objects as go
import plotly.express as px

def european_elections_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='SEATS_PERCENT_EU',
                 color='GROUP_ID',
                 title='xxxx')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig