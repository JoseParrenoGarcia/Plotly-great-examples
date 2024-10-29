import plotly.graph_objects as go
import plotly.express as px

def gdp_by_country_bar_chart_plot_plotly_express(df):
    df = df.sort_values('GDP', ascending=False)

    fig = px.bar(
        df,
        x='Country',
        y='GDP',
        title='Countries with the highest GDP measured in US trillions (2023)'
    )

    fig.update_yaxes(tickformat=',.0f')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=500,
        width=600,
    )

    return fig


def gdp_by_country_bar_chart_plot(df, add_context=True):
    if add_context:
        x_ = df['Country_with_emoji']
    else:
        x_ = df['Country']


    fig = go.Figure(
        data=[
            go.Bar(
                x=x_,
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
                x=-0.085,
                y=-0.2,
                text="Source: DataBank, <a href='https://databank.worldbank.org/reports.aspx?source=2&series=NY.GDP.MKTP.CD&country=&_gl=1*1jzomxe*_gcl_au*MTA2MTc2ODI5OS4xNzI2NDYxOTk4#'>World development indicators</a>",
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
                   # type='category'
                   ),
        margin=dict(t=150, pad=0),
        height=600,
        width=700,
    )

    if add_context:
        fig.add_shape(
            type="rect",
            xref="x",
            yref="y",
            x0='India<br>🇮🇳',
            y0=25_000_000_000_000,
            x1='Canada<br>🇨🇦',
            y1=30_000_000_000_000,
            fillcolor="lightgrey",
            opacity=0.5,
            layer="below",
            line_width=0,
        )

        fig.add_annotation(
            x='China<br>🇨🇳',
            y=df[df['Country'] == 'US']['GDP'].values[0],  # Slightly above the y-value
            text='The 🇺🇸 GDP is 27 trillion dollars. If you dont know<br>how many zeros that is, '
                 'here it goes: <b>27,000,000,000,000</b>.',
            xref="x",
            yref="y",
            showarrow=True,
            arrowhead=0,
            ax=355,
            ay=0,
            arrowcolor='lightgrey',
            arrowwidth=1,
            borderpad=10,
            font=dict(family="Helvetica Neue", size=12),
            align='left',
        )

    return fig
