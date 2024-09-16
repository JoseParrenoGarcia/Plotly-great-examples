import plotly.graph_objects as go

def housing_bar_chart_plot(df):
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['price_grouped'],
                y=df['count'],
                marker_color='darkblue',
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Even luxury house prices in Boston have outliers',
            y=0.9,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Luxury house prices in Boston are centered around 3 US millions",
                xref="paper",
                yref="paper",
                x=-0.07, y=1.29,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
        ],
        font=dict(family="Helvetica Neue"),
        yaxis=dict(title="Price (in millions)"),
        xaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=3,
                   ),
        margin=dict(t=200, pad=0),
        height=600,
        width=700,
    )

    # Show the plot
    return fig