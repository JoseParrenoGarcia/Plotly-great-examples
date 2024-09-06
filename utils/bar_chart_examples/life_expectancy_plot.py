import plotly.graph_objects as go

def life_expectancy_bar_chart(df):
    fig = go.Figure()

    # Add bars to the chart
    for country in df['country'].unique():
        country_data = df[df['country'] == country]
        fig.add_trace(go.Bar(
            x=country_data['year'],
            y=country_data['life_expectancy'],
            name=country,
        ))

    # Update the layout
    fig.update_layout(
        title=dict(
            text='Average life expectancy in Russia (',
            y=0.9,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        xaxis=dict(
            title='Year',
            tickmode='linear',
            dtick=20,
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
        ),
        yaxis=dict(
            title='Life Expectancy',
            tickmode='linear',
            dtick=10,
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=180, pad=0),
        height=600,
        width=1000,
    )

    return fig
