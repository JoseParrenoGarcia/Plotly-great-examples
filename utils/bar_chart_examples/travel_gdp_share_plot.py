import plotly.graph_objects as go

def travel_gdp_share_plot(df):

    # Create the bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                x=df['ISO_Code'],
                y=df['y2023'],
                marker_color='darkblue',
                text=df['y2023'].round(1),
                textposition='outside'
            )
        ]
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Tourism trap<br><sub>First, keep all the bars the same colour - unless there is a single bar or group of bars that you want to call out. This could be the highest performer, the audience’s own country, or an average.</sub>',
            y=0.9,  # Position of the title (closer to the top)
            x=0.01,  # Left-align the title
            xanchor='left',
            yanchor='top',
            font=dict(size=24),
            pad=dict(t=10)
        ),
        xaxis_title="",
        yaxis_title="",
        yaxis=dict(visible=False),
        xaxis=dict(showgrid=False,),
        margin=dict(t=200),  # Increase top margin to make space for the title
        height=600
    )

    # Show the plot
    return fig