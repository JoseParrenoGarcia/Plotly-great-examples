import plotly.graph_objects as go

def island_distance_line_chart(df):
    df = df.sort_values('Km_rank', ascending=True)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df['x_island'],
            y=df['Km_rank'],
            mode='markers+text',
            text=df['Island'],
            showlegend=False,
            textposition='middle left',
            marker=dict(size=10, color='rgb(17, 122, 101)'),

        )
    )

    fig.add_trace(
        go.Scatter(
            x=df['x_landmass'],
            y=df['Km_rank'],
            mode='markers+text',
            text=df['Closest landmass'],
            showlegend=False,
            textposition='middle right',
            marker=dict(size=10, color='rgb(17, 122, 101)'),
        )
    )

    for index, row in df.iterrows():
        fig.add_shape(
            type='line',
            x0=row['x_island'],
            y0=row['Km_rank'],
            x1=row['x_landmass'],
            y1=row['Km_rank'],
            line=dict(color='rgb(133, 193, 233)', width=2, dash='dash'),
            layer='below',
        )
        fig.add_annotation(
            x=(row['x_island'] + row['x_landmass']) / 2,
            y=row['Km_rank'] - 0.1,
            text=str(row['Km']) + ' km',
            showarrow=False,
            xanchor='center',
            yanchor='bottom'
        )

    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=-1_200,
        x1=-750,
        y0=0.5,
        y1=1.5,
        fillcolor="lightgrey",
        opacity=0.5,
        layer="below",
        line_width=0,
    )

    fig.add_annotation(
        x=(-1_200 + -750) / 2,
        y=(0.5 + 1.5) / 2,
        text='Islands',
        showarrow=False,
        xanchor='center',
        font=dict(color='black')
    )

    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=750,
        x1=1_200,
        y0=0.5,
        y1=1.5,
        fillcolor="lightgrey",
        opacity=0.5,
        layer="below",
        line_width=0,
    )

    fig.add_annotation(
        x=(1_200 + 750) / 2,
        y=(0.5 + 1.5) / 2,
        text='Closest landmasses',
        showarrow=False,
        xanchor='center',
        font=dict(color='black')
    )



    # Update layout
    fig.update_layout(
        title=dict(
            text='Closest landmasses to different islands',
            font=dict(family="Helvetica Neue", size=24),
        ),
        xaxis=dict(
            showticklabels=False,
            showgrid=False,
            position=0,
            zeroline=False,
            range=[-1500, 1500],
        ),
        yaxis=dict(
            title='',
            showgrid=False,
            visible=False,
        ),
        yaxis_autorange='reversed',
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=1000,
        width=1200,
    )

    return fig
