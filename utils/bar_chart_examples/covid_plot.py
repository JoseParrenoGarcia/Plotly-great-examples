import plotly.graph_objects as go
import pandas as pd
import numpy as np

def covid_bar_chart_plot(df):
    df = df.sort_values('Deaths', ascending=True).reset_index()

    # if highlight=='Uruguay':
    #     marker_color_ = ['rgba(85, 181, 229, 1)' if c_ == 'Uruguay' else 'lightgrey' for c_ in df['Entity']]
    #     text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(df['GDP per capita'], df['Entity'])]
    #     pattern_shape_ = ['' for _ in df['Entity']]
    #     title_text = 'Uruguay flies high'
    #     subtitle_text = "Uruguay's GDP per capita is amongst the highest in South America (2020)"

    fig = go.Figure(
        data=[
            go.Bar(
                y=df['Entity'],
                x=df['Deaths'],
                marker_color='rgb(18, 22, 122)',
                orientation='h',
                text=[f'<b>{deaths:,.1}</b>' if entity == 'China' else '' for deaths, entity in zip(df['Deaths'], df['Entity'])],
                textposition='outside',
                showlegend=False,
            )
        ]
    )

    # Find the y-coordinate of the China entity
    china_index = df[df['Entity'] == 'China'].index[0]
    y0 = china_index - 0.5
    y1 = china_index + 0.5

    fig.add_shape(
        type="rect",
        x0=0,
        x1=df['Deaths'].max(),
        y0=y0,
        y1=y1,
        fillcolor="rgba(18, 22, 122, 0.3)",
        opacity=0.5,
        layer="below",
        line_width=0,
    )

    # Update the layout
    fig.update_layout(
        title=dict(
            text='Did China manage to contain Covid?',
            y=0.98,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        annotations=[
            # Second paragraph annotation
            dict(
                text='Although Covid originated in China, it seems they managed to contain the virus',
                xref="paper", yref="paper",
                x=-0.20, y=1.20,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            dict(
                text='Cumulative deaths per 100k people as of July 2021',
                xref="paper", yref="paper",
                x=-0.20, y=1.10,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=12),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: World Bank, <a href='https://ourworldindata.org'>Our World in Data</a>",
                xref="paper", yref="paper",
                x=-0.20, y=-0.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=12),
                align="left"
            ),
        ],
        xaxis=dict(
            dtick=50,
            showgrid=True,
        ),
        yaxis=dict(
            title='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        legend=dict(
            x=1,
            y=0,
            xanchor='right',
            yanchor='bottom',
            orientation='h'
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=100, pad=0),
        height=500,
        width=630,
    )

    return fig




