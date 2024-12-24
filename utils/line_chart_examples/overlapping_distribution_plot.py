import plotly.graph_objects as go

def overlapping_distribution_line_chart(df, type='line'):
    fig = go.Figure()

    for tag in df['tag'].unique():
        df_aux = df[df['tag']==tag]
        if type=='line':
            fig.add_trace(
                go.Scatter(x=df_aux['x'],
                           y=df_aux['y'],
                           mode='lines',
                           showlegend=False,
                           # line=dict(width=2, color=color),
                           )
            )
        else:
            fig.add_trace(
                go.Scatter(x=df_aux['x'],
                           y=df_aux['y'],
                           mode='lines',
                           fill='tozeroy',
                           showlegend=False,
                           # line=dict(width=2, color=color),
                           )
            )

    fig.update_layout(
        title=dict(
            text='3 different and overlapping distributions',
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Line vs area charts',
                xref="paper",
                yref="paper",
                x=-0.07, y=1.23,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text='Density',
                xref="paper",
                yref="paper",
                x=-0.07, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
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
            # range=[0, 4.4],

        ),
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=250, r=100, pad=0),
        height=800,
        width=1000,
    )

    return fig
