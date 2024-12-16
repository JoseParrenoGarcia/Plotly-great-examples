import plotly.graph_objects as go

def space_race_line_chart(df):
    fig = go.Figure()

    # Add annotations for the Soviet Union
    soviet_data = df[df['Country'] == 'Soviet Union']
    for index, row in soviet_data.iterrows():
        fig.add_annotation(
            x=-20,  # Position to the left of the y-axis
            y=row['Year'],
            text=row['Event'],
            showarrow=True,
            arrowhead=2,
            ax=-100,  # Length of the arrow
            ay=0,
        )

    us_data = df[df['Country'] == 'United States']
    for index, row in us_data.iterrows():
        fig.add_annotation(
            x=20,  # Position to the left of the y-axis
            y=row['Year'],
            text=row['Event'],
            showarrow=True,
            arrowhead=2,
            ax=100,  # Length of the arrow
            ay=0,
        )

    both_data = df[df['Country'] == 'U.S. & USSR']
    for index, row in both_data.iterrows():
        fig.add_annotation(
            x=0,  # Position to the left of the y-axis
            y=row['Year'],
            text=row['Event'],
            showarrow=True,
            arrowhead=2,
            ax=0,  # Length of the arrow
            ay=0,
        )

    fig.add_vline(x=20, line=dict(color="black", width=2))
    fig.add_vline(x=-20, line=dict(color="black", width=2))

    # Update layout
    fig.update_layout(
        title='Space Race Timeline',
        xaxis=dict(
            showticklabels=False,
            showgrid=False,
            range=[-300, 300],
            position=0,
            zeroline=False,
            # zerolinewidth=2,
            # zerolinecolor='black'
        ),
        yaxis=dict(
            range=[1957, 1975],
            # dtick=1,
            title='',
            showgrid=False,
            visible=False,
        ),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=1000,
        width=700,
    )

    return fig
