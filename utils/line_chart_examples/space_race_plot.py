import plotly.graph_objects as go

def space_race_line_chart(df):
    fig = go.Figure()

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

    start_us = 30
    us_color = 'rgb(10, 49, 97)'
    fig.add_vline(x=start_us, line=dict(color=us_color, width=2))

    start_soviet = -30
    soviet_color = 'rgb(204, 0, 0)'
    fig.add_vline(x=start_soviet, line=dict(color=soviet_color, width=2))

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
            marker=dict(color=soviet_color)
        )
    )

    for year in soviet_data['Year']:
        fig.add_shape(
            type="line",
            x0=start_soviet,
            y0=year,
            x1=start_soviet - 40,
            y1=year,
            line=dict(color=soviet_color, width=2)
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
            marker=dict(color=us_color)
        )
    )

    for year in us_data['Year']:
        fig.add_shape(
            type="line",
            x0=start_us,
            y0=year,
            x1=start_us + 40,
            y1=year,
            line=dict(color=us_color, width=2)
        )

    # Add annotations for both
    both_data = df[df['Country'] == 'U.S. & USSR']
    for index, row in both_data.iterrows():
        fig.add_annotation(
            x=0,
            y=row['Year'] + 0.5,
            text=str(row['text_to_show']),
            ax=0,
            ay=-50,
            showarrow=True,
            arrowhead=0,
            arrowcolor='white',
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
        images=[
            dict(
                source="https://upload.wikimedia.org/wikipedia/commons/f/f5/Flag_of_the_United_States_%281912-1959%29.svg",
                xref="paper", yref="paper",
                x=0.6, y=0.92,
                sizex=0.05, sizey=0.08,
                xanchor="right",
                yanchor="bottom",
            ),
            dict(
                source="https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_the_Soviet_Union.svg",
                xref="paper", yref="paper",
                x=0.45, y=0.92,
                sizex=0.05, sizey=0.08,
                xanchor="right",
                yanchor="bottom",
            ),
        ],
        font=dict(family="Helvetica Neue", size=12),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=1000,
        width=1200,
    )

    return fig
