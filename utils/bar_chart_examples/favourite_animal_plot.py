import plotly.graph_objects as go
import plotly.express as px

def favourite_animal_bar_chart_plot_plotly_express(df):
    df = df.sort_values('Percentage', ascending=False)

    fig = px.bar(data_frame=df,
                 x='Animal',
                 y='Percentage',
                 text='Percentage',
                 title='The Tiger is the favourite animal',)

    fig.update_layout(height=600,
        width=700,)

    return fig


def favourite_animal_bar_chart_plot(df, other_ordering=True):

    if other_ordering:
        # Define the categorical order
        df['SortOrder'] = df['Animal'].apply(lambda x: 1 if x == 'Other' else 0)
        df = df.sort_values(by=['SortOrder', 'Percentage'], ascending=[True, False]).reset_index(drop=True)
    else:
        df = df.sort_values('Percentage', ascending=False)

    fig = go.Figure(
        data=[
            go.Bar(
                x=df['Animal'],
                y=df['Percentage'],
                marker_color=[
                    'lightgrey' if animal == 'Other' else 'darkblue' for animal in df['Animal']
                ],
                text=df['Percentage'].round(1),
                textposition='outside'
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Tiger king',
            y=0.9,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="According to <i>Animal Planet</i> viewers, the tiger is the best beast.",
                xref="paper",
                yref="paper",
                x=0, y=1.25,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            # Second paragraph annotation
            dict(
                text="% who say this is their favourite animal",
                xref="paper", yref="paper",
                x=0, y=1.10,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: Animal Planet, <a href='https://www.manchestereveningnews.co.uk/news/greater-manchester-news/tiger-is-worlds-favourite-animal-1131562'>Published in the Manchester news</a>",
                xref="paper", yref="paper",
                x=0, y=-0.18,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=12),
                align="left"
            )
        ],
        font=dict(family="Helvetica Neue"),
        yaxis=dict(title="", visible=False),
        xaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=3,
                   type='category'
                   ),
        margin=dict(t=180, pad=0),
        height=600,
        width=700,
    )

    # Show the plot
    return fig