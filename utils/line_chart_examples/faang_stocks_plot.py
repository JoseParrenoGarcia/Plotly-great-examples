import plotly.graph_objects as go

def faang_stocks_line_chart(df, line_width):

    fig = go.Figure()

    for stock in df['stock'].unique():
        fig.add_trace(
            go.Scatter(x=df[df['stock'] == stock]['Date'],
                       y=df[df['stock'] == stock]['Open'],
                       mode='lines',
                       name=stock,
                       showlegend=False,
                       line=dict(width=line_width, color='darkblue')
                       )
        )

        fig.add_trace(
            go.Scatter(x=df[(df['stock'] == stock) & (df['Date'] == df['Date'].max())]['Date'],
                       y=df[(df['stock'] == stock) & (df['Date'] == df['Date'].max())]['Open'],
                       mode='markers+text',
                       name=stock,
                       showlegend=False,
                       marker=dict(size=line_width*3, color='darkblue'),
                       text=stock,
                       textposition='top center',
                       textfont=dict(family="Helvetica Neue", size=12, color='darkblue'),
                       )
        )

    fig.update_layout(
        title=dict(
            text="Meta stock soaring",
            font=dict(family="Helvetica Neue", size=20),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Meta has been the best performing stock in the last 6 months',
                xref="paper",
                yref="paper",
                x=-0.1, y=1.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=15),
                align="left"
            ),
            dict(
                text='Opening trading prices for Meta',
                xref="paper",
                yref="paper",
                x=-0.1, y=1.07,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=13),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
        ),
        yaxis=dict(
            title='',
            showline=True,
            zeroline=False,
            showgrid=False,
            linecolor='lightgrey',
            linewidth=2,
            ticksuffix="  ",

        ),
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=600,
        width=700,
    )

    return fig