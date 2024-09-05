import plotly.graph_objects as go

def travel_gdp_share_plot_bar_chart(df):

    # Create the bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['ISO_Code'],
                y=df['y2023'],
                marker_color=[
                    'rgb(255, 204, 0)' if iso_code == 'Avg.' else 'rgb(0, 51, 153)' for iso_code in df['ISO_Code']
                ],
                text=df['y2023'].round(1),
                textposition='outside'
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='The tourism trap',
            y=0.9,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="10 countries are more heavily reliant on international tourism than the global average",
                xref="paper",
                yref="paper",
                x=0, y=1.25,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            # Second paragraph annotation
            dict(
                text="Travel and tourism share of GDP in the EU-27 and the UK in 2023",
                xref="paper", yref="paper",
                x=0, y=1.10,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: Statista, <a href='https://www.statista.com/statistics/1228395/travel-and-tourism-share-of-gdp-in-the-eu-by-country/'>Share of travel and tourism's total contribution to GDP report</a>",
                xref="paper", yref="paper",
                x=0, y=-0.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=12),
                align="left"
            )
        ],
        images=[
            dict(
                source="https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
                xref="paper", yref="paper",
                x=1, y=1.15,
                sizex=0.2, sizey=0.2,
                xanchor="right", yanchor="bottom",
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
        width=1000,
    )

    # Show the plot
    return fig