import plotly.graph_objects as go

def political_distance_line_chart(df):
    # df = df.sort_values('Km_rank', ascending=True)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df['left'],
            y=df['Topic'],
            mode='markers',
            showlegend=False,
            marker=dict(size=10, color='rgb(236, 112, 99)'),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df['right'],
            y=df['Topic'],
            mode='markers',
            showlegend=False,
            marker=dict(size=10, color='rgb(93, 173, 226)'),
        )
    )

    fig.add_vline(x=100, line=dict(color='black', width=1))

    # Update layout
    fig.update_layout(
        title=dict(
            text='Policies that differentiate left and right wingers the most',
            font=dict(family="Helvetica Neue", size=24),
        ),
        xaxis=dict(
            showticklabels=True,
            showgrid=True,
            position=0,
            zeroline=False,
            range=[0, 100],
            tickvals=[20, 40, 60, 80, 100],
            tickmode='array',
            ticktext=['20%', '40%', '60%', '80%', '100%'],
        ),
        yaxis=dict(
            title='',
            showgrid=True,
            visible=True,
            showline=True,
        ),
        font=dict(family="Helvetica Neue", size=16),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=500,
        width=700,
    )

    return fig
