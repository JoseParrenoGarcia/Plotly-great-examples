import plotly.graph_objects as go

def political_distance_line_chart(df):
    fig = go.Figure()

    for index, row in df.iterrows():
        fig.add_shape(
            type='line',
            x0=row['right'],
            x1=row['left'],
            y0=row['Topic'],
            y1=row['Topic'],
            line=dict(color='darkgrey', width=2),
        )
        fig.add_annotation(
            x=(row['right'] + row['left']) / 2,
            y=index + 0.15,
            text=str(row['difference']) + '% points',
            showarrow=False,
            xanchor='center',
            yanchor='bottom'
        )

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

    fig.add_annotation(
        x=23,
        y=6,
        text='Right wingers',
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-50,
        arrowcolor='rgb(93, 173, 226)',
        arrowwidth=1,
        font=dict(color='rgb(93, 173, 226)'),
    )

    fig.add_annotation(
        x=60,
        y=6,
        text='Left wingers',
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-50,
        arrowcolor='rgb(236, 112, 99)',
        arrowwidth=1,
        font=dict(color='rgb(236, 112, 99)'),
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
            tickfont=dict(size=14),
        ),
        yaxis=dict(
            title='',
            showgrid=True,
            visible=True,
            showline=True,
            tickfont=dict(size=14),
        ),
        font=dict(family="Helvetica Neue", size=12),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=600,
        width=700,
    )

    return fig
