import plotly.graph_objects as go

def space_race_line_chart(df):
    fig = go.Figure()

    # Add annotations for the Soviet Union
    soviet_data = df[df['Country'] == 'Soviet Union']
    # for index, row in soviet_data.iterrows():
    #     fig.add_annotation(
    #         x=-200,
    #         y=row['Year'],
    #         text=row['text_to_show'],
    #         align='right',
    #         showarrow=False,
    #         arrowhead=0,
    #         ax=0,
    #         ay=0,
    #     )

    fig.add_trace(
        go.Scatter(
            x=[-35] * len(soviet_data),
            y=soviet_data['Year'],
            text=soviet_data['text_to_show'],
            mode='text',
            showlegend=False,
            textposition='middle left'
        )
    )

    # us_data = df[df['Country'] == 'United States']
    # for index, row in us_data.iterrows():
    #     fig.add_annotation(
    #         x=20,
    #         y=row['Year'],
    #         text=row['text_to_show'],
    #         align='left',
    #         showarrow=True,
    #         arrowhead=0,
    #         ax=100,
    #         ay=0,
    #     )
    #
    # both_data = df[df['Country'] == 'U.S. & USSR']
    # for index, row in both_data.iterrows():
    #     fig.add_annotation(
    #         x=0,
    #         y=row['Year'] + 0.2,
    #         text=row['Event'],
    #         showarrow=True,
    #         arrowhead=0,
    #         ax=0,
    #         ay=-50,
    #     )

    fig.add_vline(x=20, line=dict(color="black", width=2))
    fig.add_vline(x=-20, line=dict(color="black", width=2))

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
        title='Space Race Timeline',
        xaxis=dict(
            showticklabels=False,
            showgrid=False,
            range=[-600, 600],
            position=0,
            zeroline=False,
        ),
        yaxis=dict(
            range=[1956, 1976],
            title='',
            showgrid=False,
            visible=False,
        ),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=1000,
        width=1000,
    )

    return fig
