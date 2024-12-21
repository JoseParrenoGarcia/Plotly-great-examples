import plotly.graph_objects as go

def human_height_line_plot(df, line_width, hero_line=None):
    if hero_line is None:
        rest_of_countries = df['Entity'].unique()
    else:
        rest_of_countries = [country for country in df['Entity'].unique() if country not in hero_line]

    fig = go.Figure()

    for country in rest_of_countries:
        fig.add_trace(
            go.Scatter(x=df[df['Entity'] == country]['Year'],
                       y=df[df['Entity'] == country]['height'],
                       mode='lines',
                       name=country,
                       showlegend=False,
                       line=dict(color='rgba(204, 209, 209, 0.5)', width=line_width)
                       )
        )

    if hero_line is not None:
        for country in hero_line:
            fig.add_trace(
                go.Scatter(x=df[df['Entity'] == country]['Year'],
                           y=df[df['Entity'] == country]['height'],
                           mode='lines',
                           name=country,
                           showlegend=False,
                           line=dict(color='purple', width=line_width*3)
                           )
            )

            fig.add_trace(
                go.Scatter(x=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['Year'],
                           y=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['height'],
                           mode='markers+text',
                           name=country,
                           showlegend=False,
                           marker=dict(color='purple', size=line_width*3*2),
                           text=country,
                           textposition='middle right',
                           textfont=dict(family="Helvetica Neue", color='purple', size=12),
                           )
            )

    # Update layout
    fig.update_layout(
        title=dict(
            text="More wellfare, more height.",
            font=dict(family="Helvetica Neue", size=20),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Europeans are taller compared to the rest of the world.<br>But, East Asian countries like South Korea and Japan are catching up.',
                xref="paper",
                yref="paper",
                x=-0.1, y=1.12,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=15),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max()+25],
        ),
        yaxis=dict(
            title='',
            showline=True,
            zeroline=False,
            showgrid=False,
            linecolor='lightgrey',
            linewidth=2,
            ticksuffix="  ",

        ),
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=150, pad=0),
        height=700,
        width=700,
    )

    return fig