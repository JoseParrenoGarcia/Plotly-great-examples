import plotly.graph_objects as go

def employmeny_by_industry_bar_chart_plot(df):
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['Value'],
                y=df['Industry'],
                marker_color='darkblue',
                orientation='h',
                text=df['Value'].astype(str) + '%',
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='The world of work',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="UK employment (% of population in each sector - 2021)",
                xref="paper",
                yref="paper",
                x=-0.48, y=1.20,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            dict(
                x=-0.48,
                y=-0.15,
                text="Source: UK Gov., <a href='https://www.ethnicity-facts-figures.service.gov.uk/work-pay-and-benefits/employment/employment-by-sector/latest/#download-the-data'>Employmeny by sector statistics</a>",
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
                   griddash='dot'),
        xaxis=dict(title="", visible=False),
        margin=dict(t=150, pad=0),
        height=600,
        width=800,
    )

    return fig
