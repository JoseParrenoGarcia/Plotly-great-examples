import plotly.graph_objects as go
from altair import layer


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
            range=[0, 101],
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

def neighbouring_countries_abacus_chart(df):
    fig = go.Figure()

    median_value = df['percentage'].median()
    df = df[df['country'] != 'Median']

    fig.add_trace(
        go.Scatter(
            y=df['country'],
            x=df['percentage'],
            mode='markers+text',
            marker=dict(color='rgb(0, 51, 153)', size=25),
            text=df['percentage'].round(1),
            textfont=dict(color='white'),
        )
    )

    # Add horizontal lines for each country
    for country in df['country']:
        fig.add_shape(
            type='line',
            x0=0,
            y0=country,
            x1=100,
            y1=country,
            line=dict(color='lightgrey', width=1),
            layer="below"
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
            dict(
                text="% who believe that parts of neighbouring countries 'really belong to us'",
                xref="paper", yref="paper",
                x=0, y=1.09,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
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
            range=[0, 100],
            showticklabels=False,
            showline=False,
        ),
        yaxis=dict(
            title='',
            showline=False,
        ),
        font=dict(family="Helvetica Neue"),
        margin=dict(t=100, pad=0),
        height=600,
        width=1000,
    )

    fig.add_vline(
        x=median_value,
        line=dict(color='lightgrey', dash='dot', width=2),
        annotation_text='Median',
        annotation_position='bottom right',
        layer='below',
    )

    fig.add_vline(
        x=0,
        line=dict(color='lightgrey', width=4),
        annotation_text='  0',
        annotation_position='bottom right',
    )

    fig.add_vline(
        x=100,
        line=dict(color='lightgrey', width=4),
        annotation_text='100  ',
        annotation_position='bottom left',
    )

    return fig