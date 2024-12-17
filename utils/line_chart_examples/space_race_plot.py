import plotly.graph_objects as go

def space_race_line_chart(df):
    fig = go.Figure()

    start_us = 30
    fig.add_vline(x=start_us, line=dict(color="black", width=2))

    start_soviet = -30
    fig.add_vline(x=start_soviet, line=dict(color="black", width=2))

    # Add annotations for the Soviet Union
    soviet_data = df[df['Country'] == 'Soviet Union']
    fig.add_trace(
        go.Scatter(
            x=[start_soviet-50] * len(soviet_data),
            y=soviet_data['Year'],
            text=soviet_data['text_to_show'],
            mode='text',
            showlegend=False,
            textposition='middle left'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[start_soviet-40] * len(soviet_data),
            y=soviet_data['Year'],
            mode='markers',
            showlegend=False,
            marker=dict(color='black')
        )
    )

    for index, row in soviet_data.iterrows():
        fig.add_annotation(
            x=start_soviet,
            y=row['Year'],
            ax=start_soviet-10,
            ay=0,  # Same y-coordinate to make it horizontal
            showarrow=True,
            arrowhead=0
        )

    # Add annotations for the US
    us_data = df[df['Country'] == 'United States']
    fig.add_trace(
        go.Scatter(
            x=[start_us + 50] * len(us_data),
            y=us_data['Year'],
            text=us_data['text_to_show'],
            mode='text',
            showlegend=False,
            textposition='middle right'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[start_us + 40] * len(us_data),
            y=us_data['Year'],
            mode='markers',
            showlegend=False,
            marker=dict(color='black')
        )
    )

    for index, row in us_data.iterrows():
        fig.add_annotation(
            x=start_us,
            y=row['Year'],
            ax=start_us + 10,
            ay=0,  # Same y-coordinate to make it horizontal
            showarrow=True,
            arrowhead=0
        )

    # Add scatter plot for years
    years = list(range(1957, 1976))
    fig.add_trace(
        go.Scatter(
            x=[0] * len(years),
            y=years,
            mode='text',
            text=[str(year) for year in years],
            showlegend=False,
            textposition='middle center'
        )
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text='Space Race Timeline',
            font=dict(family="Helvetica Neue", size=24),
        ),
        xaxis=dict(
            showticklabels=False,
            showgrid=False,
            range=[-700, 700],
            position=0,
            zeroline=False,
        ),
        yaxis=dict(
            range=[1956, 1976],
            title='',
            showgrid=False,
            visible=False,
        ),
        font=dict(family="Helvetica Neue", size=12),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=1000,
        width=1200,
    )

    return fig
