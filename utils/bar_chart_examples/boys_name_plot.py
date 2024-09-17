import plotly.graph_objects as go

def boys_names_bar_chart_plot(df):
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['Count'],
                y=df['Name'],
                marker_color='darkblue',
                orientation='h',
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Most popular boy names in the UK',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Count of baby names (2023)",
                xref="paper",
                yref="paper",
                x=-0.155, y=1.20,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                x=-0.155,
                y=-0.15,
                text="Source: ONS, <a href='https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesenglandandwalesbabynamesstatisticsboys'>Baby name statistics</a>",
                showarrow = False,
                ax=0,
                ay=-130,
                xref = "paper", yref = "paper",
                font=dict(family="Helvetica Neue", size=12),
                align = "left"
            )
        ],
        font=dict(family="Helvetica Neue"),
        yaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=1,
                   gridcolor='lightgrey',
                   gridwidth=1,
                   griddash='dot'
                   ),
        xaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=3,
                   ),
        margin=dict(t=150, pad=0),
        height=600,
        width=700,
    )

    return fig
