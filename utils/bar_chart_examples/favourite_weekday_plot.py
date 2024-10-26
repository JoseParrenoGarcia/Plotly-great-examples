import plotly.graph_objects as go
import plotly.express as px

def favourite_weekday_bar_chart_plot_plotly_express(df):
    df = df.sort_values('Favorite %', ascending=False)

    fig = px.bar(data_frame=df,
                 x='Day',
                 y='Favorite %',
                 text='Favorite %',
                 title='Looking forward to the weekend.',)

    fig.update_layout(height=600,
        width=700,)

    return fig

def favourite_weekday_bar_chart_plot(df):
    # Define the categorical order
    # categories = [day_ for day_ in df['Day'] if day_ != 'No preference'] + ['No preference']
    # df['SortOrder'] = df['Day'].apply(lambda x: 1 if x == 'No preference' else 0)
    df = df.sort_values(by=['Day_Number'], ascending=True).reset_index(drop=True)

    fig = go.Figure(
        data=[
            go.Bar(
                x=df['Day'],
                y=df['Favorite %'],
                marker_color=[
                    'lightgrey' if day_ == 'No preference' else 'darkblue' for day_ in df['Day']
                ],
                text=df['Favorite %'].round(1),
                textposition='outside'
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Looking forward to the weekend.',
            y=0.9,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Americans love Friday and Saturday the most. Tuesday the least.",
                xref="paper",
                yref="paper",
                x=0, y=1.25,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            # Second paragraph annotation
            dict(
                text="% who say this is their favourite day",
                xref="paper", yref="paper",
                x=0, y=1.10,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: YouGov, <a href='https://today.yougov.com/society/articles/34696-most-and-least-favorite-day-week-poll'>Published in YouGov US blog</a>",
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