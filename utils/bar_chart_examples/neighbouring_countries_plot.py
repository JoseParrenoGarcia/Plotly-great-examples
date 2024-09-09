import plotly.graph_objects as go


def neighbouring_countries_bar_chart(df):
    fig = go.Figure(
        data=[
            go.Bar(
                y=df['country'],
                x=df['percentage'],
                marker_color=[
                    'rgba(0, 51, 153, 0.3)' if c_ == 'Median' else 'rgb(0, 51, 153)' for c_ in df['country']
                ],
                orientation='h',
                text=df['percentage'].round(1),
                textposition='inside',
                textangle=0,
            )
        ]
    )

    # Update the layout
    fig.update_layout(
        title=dict(
            text='Eastern European countries believe that parts of their territory belong to them.',
            y=0.98,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        annotations=[
            # Second paragraph annotation
            dict(
                text="% who believe that parts of neighbouring countries 'really belong to us'",
                xref="paper", yref="paper",
                x=0, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: Pew Research Center, <a href='https://www.pewresearch.org/global/2020/02/09/nato-seen-favorably-across-member-states/#are-there-parts-of-neighboring-countries-that-really-belong-to-us'>NATO 2020 report</a>",
                xref="paper", yref="paper",
                x=0, y=-0.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=12),
                align="left"
            ),
        ],
        xaxis=dict(
            title='',
            tickmode='linear',
            dtick=20,
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
        ),
        yaxis=dict(
            title='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=100, pad=0),
        height=600,
        width=1000,
    )

    return fig