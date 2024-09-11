import plotly.graph_objects as go

def gdp_per_capita_bar_chart_plot(df, highlight='Uruguay'):
    df = df.sort_values('GDP per capita', ascending=True)

    if highlight=='Uruguay':
        marker_color_ = ['rgba(85, 181, 229, 1)' if c_ == 'Uruguay' else 'lightgrey' for c_ in df['Entity']]
        text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(df['GDP per capita'], df['Entity'])]
        title_text = 'Uruguay flies high'
        subtitle_text = "Uruguay's GDP per capita is amongst the highest in South America (2020)"

    elif highlight=='min':
        marker_color_ = ['rgba(239, 51, 64, 1)' if c_ == df['Entity'].iloc[0] else 'lightgrey' for c_ in df['Entity']]
        text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == df['Entity'].iloc[0] else '' for val, c_ in zip(df['GDP per capita'], df['Entity'])]
        title_text = 'Venezuela hits rock bottom'
        subtitle_text = "The country with the lowest GDP per capita in South America (2020)"

    else:
        pass


    fig = go.Figure(
        data=[
            go.Bar(
                y=df['Entity'],
                x=df['GDP per capita'],
                marker_color=marker_color_,
                orientation='h',
                text=text_,
                textposition='outside',
            )
        ]
    )

    # Update the layout
    fig.update_layout(
        title=dict(
            text=title_text,
            y=0.98,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        annotations=[
            # Second paragraph annotation
            dict(
                text=subtitle_text,
                xref="paper", yref="paper",
                x=0, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: World Bank, <a href='https://ourworldindata.org'>Our World in Data</a>",
                xref="paper", yref="paper",
                x=0, y=-0.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=12),
                align="left"
            ),
        ],
        xaxis=dict(
            title='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
        ),
        yaxis=dict(
            title='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=100, pad=0),
        height=500,
        width=600,
    )

    return fig




