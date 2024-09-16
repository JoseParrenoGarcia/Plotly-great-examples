import plotly.graph_objects as go

def gdp_by_country_bar_chart_plot(df):
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['Country'],
                y=df['GDP'],
                marker_color='darkblue',
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='The rich list',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Countries with the highest GDP measured in US trillions (2023)",
                xref="paper",
                yref="paper",
                x=-0.085, y=1.20,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                x='China',
                y=df[df['Country'] == 'US']['GDP'].values[0],  # Slightly above the y-value
                text='The 🇺🇸 GDP is 27 trillion dollars. If you dont know<br>how many zeros that is, '
                     'here it goes: <b>27,000,000,000,000</b>.<br>That is 10 trillion '
                     'more than China 🇨🇳.',
                xref="x",
                yref="y",
                showarrow=True,
                arrowhead=0,
                ax=350,
                ay=0,
                arrowcolor='lightgrey',
                arrowwidth=1,
                borderpad=10,
                font=dict(family="Helvetica Neue", size=12),
                align='left',
            )
        ],
        shapes=[
            dict(
                type="rect",
                xref="x",
                yref="y",
                x0='India',
                y0=24_000_000_000_000,
                x1='Canada',
                y1=30_000_000_000_000,
                fillcolor="lightgrey",
                opacity=0.5,
                layer="below",
                line_width=0,
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
