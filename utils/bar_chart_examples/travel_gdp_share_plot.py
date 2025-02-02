import plotly.graph_objects as go
import plotly.express as px

def travel_gdp_share_plotly_express_bar_chart(df):
    df = df.rename(columns={'ISO_Code': 'Country ISO code',
                            'y2023': 'Tourism percentage over GDP'})
    fig = px.bar(df,
                 x='Country ISO code',
                 y='Tourism percentage over GDP',
                 title='The tourism trap<br>'
                       '<sup>10 countries are more heavily reliant on international tourism than the global average</sup>', )

    # Minor layout customization
    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig


def travel_gdp_share_plot_bar_chart(df):

    # Create the bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['ISO_Code_with_emoji'],
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
            y=1,
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
                x=0, y=1.18,
                showarrow=False,
                font=dict(size=18),
                align="left"
            ),
            # Second paragraph annotation
            dict(
                text="Travel and tourism share of GDP in the EU-27 and the UK in 2023",
                xref="paper", yref="paper",
                x=0, y=1.07,
                showarrow=False,
                font=dict(size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: Statista, <a href='https://www.statista.com/statistics/1228395/travel-and-tourism-share-of-gdp-in-the-eu-by-country/'>Share of travel and tourism's total contribution to GDP report</a>",
                xref="paper", yref="paper",
                x=0, y=-0.19,
                showarrow=False,
                font=dict(size=12),
                align="left"
            )
        ],
        images=[
            dict(
                source="https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
                xref="paper", yref="paper",
                x=1, y=1.05,
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
        margin=dict(t=100, pad=0),
        height=600,
        width=1000,
    )

    # Show the plot
    return fig


def travel_gdp_share_plot_dot_chart(df):
    # Calculate the average value
    avg_value = df[df['ISO_Code'] != 'Avg.']['y2023'].mean()

    # Filter out the 'Avg.' category
    df_filtered = df[df['ISO_Code'] != 'Avg.']

    # Create the dot plot
    fig = go.Figure()

    # Add scatter plot for dots
    fig.add_trace(
        go.Scatter(
            x=df_filtered['ISO_Code_with_emoji'],
            y=df_filtered['y2023'],
            mode='markers+text',
            marker=dict(
                color=['rgb(255, 204, 0)' if y > avg_value else 'rgb(0, 51, 153)' for y in df_filtered['y2023']],
                size=18
            ),
            text=df_filtered['y2023'].round(1),
            textposition='top center'
        )
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='The tourism trap',
            y=1,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="10 countries are more heavily reliant on international tourism than the global average",
                xref="paper", yref="paper",
                x=0, y=1.18,
                showarrow=False,
                font=dict(size=18),
                align="left"
            ),
            # Second paragraph annotation
            dict(
                text="Travel and tourism share of GDP in the EU-27 and the UK in 2023",
                xref="paper", yref="paper",
                x=0, y=1.07,
                showarrow=False,
                font=dict(size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: Statista, <a href='https://www.statista.com/statistics/1228395/travel-and-tourism-share-of-gdp-in-the-eu-by-country/'>Share of travel and tourism's total contribution to GDP report</a>",
                xref="paper", yref="paper",
                x=0, y=-0.19,
                showarrow=False,
                font=dict(size=12),
                align="left"
            )
        ],
        images=[
            dict(
                source="https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
                xref="paper", yref="paper",
                x=1, y=1.05,
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
                   type='category',
                   ),
        margin=dict(t=100, pad=0),
        height=600,
        width=1000,
    )

    # Add horizontal line for average
    fig.add_hline(
        y=avg_value,
        line=dict(color='grey', dash='dot', width=0.5),
        annotation_text=f'Average: {avg_value:.1f}%',
        annotation_position='top right', layer="below",
    )

    # Add vertical lines
    for i, row in df_filtered.iterrows():
        fig.add_shape(
            type='line',
            x0=row['ISO_Code_with_emoji'],
            y0=0,
            x1=row['ISO_Code_with_emoji'],
            y1=row['y2023'],
            line=dict(color='lightgrey', width=2),
            layer="below",
        )

    return fig