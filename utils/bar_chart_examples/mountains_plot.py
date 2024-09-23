import plotly.graph_objects as go

def mountain_bar_chart_plot(df):
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['Name'],
                y=df['Total Height (km)'],
                marker_color='darkblue',
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='The biggest structures on Earth',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="There are also massive structure below sea-level",
                xref="paper",
                yref="paper",
                x=-0.085, y=1.20,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
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
