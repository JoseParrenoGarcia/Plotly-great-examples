import plotly.graph_objects as go
from plotly.subplots import make_subplots

def smoking_rates_plot(df):
    # df = df.sort_values(by=['continent', 'smoking_rate'], ascending=[True, True])
    #
    # # Create the bar chart
    # fig = go.Figure()
    #
    # # Add bars for each continent
    # for continent in df['continent'].unique():
    #     continent_df = df[df['continent'] == continent]
    #     fig.add_trace(go.Bar(
    #         x=continent_df['smoking_rate'],
    #         y=continent_df['country'],
    #         orientation='h',
    #         text=continent_df['smoking_rate'],
    #         textposition='inside',
    #         textangle=0,
    #     ))
    #
    #     fig.add_trace(go.Bar(
    #         x=[0],  # Dummy value
    #         y=[continent],  # Position at the first country of the continent
    #         orientation='h',
    #         yaxis='y2',
    #         showlegend=False,
    #         marker=dict(color='rgba(0,0,0,0)')  # Invisible bar
    #     ))
    #
    # # Update the layout
    # fig.update_layout(
    #     barmode='stack',
    #     xaxis=dict(title='',
    #                showticklabels=False,
    #                showline=False),
    #     yaxis=dict(title='',
    #                showline=True,
    #                linecolor='lightgrey',
    #                linewidth=1,
    #                ),
    #     yaxis2=dict(title='',
    #                 anchor="free",
    #                 overlaying="y",
    #                 autoshift=True,
    #                 ),
    #     title='Smoking Rates by Country and Continent',
    #     font=dict(family="Helvetica Neue"),
    #     showlegend=False,
    #     height=900,
    #     width=800,
    #     margin=dict(l=150),
    # )
    #
    # return fig

    df = df.sort_values(by=['continent', 'smoking_rate'], ascending=[True, True])
    continents = df['continent'].unique()

    # Create subplots
    fig = make_subplots(
        rows=len(continents),
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.005
    )

    # Add bars for each continent
    for i, continent in enumerate(continents):
        continent_df = df[df['continent'] == continent]
        fig.add_trace(
            go.Bar(
                x=continent_df['smoking_rate'],
                y=continent_df['country'],
                orientation='h',
                text=continent_df['smoking_rate'],
                textposition='inside',
                textangle=0,
            ),
            row=i + 1,
            col=1
        )

        # Add an invisible bar trace for the continent name
        fig.add_trace(
            go.Bar(
                x=[0],  # Dummy value
                y=[continent],  # Position at the continent level
                orientation='h',
                showlegend=False,
                marker=dict(color='rgba(0,0,0,0)')  # Invisible bar
            ),
            row=i + 1,
            col=1
        )

    # Update the layout
    fig.update_layout(
        title='Smoking Rates by Country and Continent',
        font=dict(family="Helvetica Neue"),
        showlegend=False,
        height=300 * len(continents),  # Adjust height based on the number of continents
        width=800,
        margin=dict(l=150),
    )

    return fig