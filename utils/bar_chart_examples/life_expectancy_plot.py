import plotly.graph_objects as go
import plotly.express as px

def life_expectancy_plotly_express_bar_chart(df):
    fig = px.bar(df,
                 x='year',
                 y='life_expectancy',
                 title='Average life expectancy in Russia', )

    # Minor layout customization
    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig


def life_expectancy_bar_chart(df):
    fig = go.Figure()

    fig.add_vline(
        x=2023,
        line=dict(color='lightgrey', dash='dot', width=2),
        annotation_text='Predicted life expectancy after 2022',
        annotation_position='top right',
    )

    # Add bars to the chart
    for country in df['country'].unique():
        country_data = df[df['country'] == country]
        fig.add_trace(go.Bar(
            x=country_data['year'],
            y=country_data['life_expectancy'],
            name=country,
            marker=dict(
                color=['rgba(0, 51, 153, 0.5)' if year >= 2023 else 'rgb(0, 51, 153)' for year in country_data['year']]
            )
        ))

    txt_ = "<b>1917 - 1922.</b> Russian civil war <a href='https://en.wikipedia.org/wiki/Russian_Civil_War'>🔗</a>"
    fig.add_annotation(
        x=1920,
        y=40,  # Slightly above the y-value
        text=txt_,
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-230,
        arrowcolor='lightgrey',
        arrowwidth=1,
        borderpad=5,
        align='left',
        xanchor='left',
    )

    txt_ = "<b>1933.</b> Stalinist collectivisation <a href='https://en.wikipedia.org/wiki/Collectivization_in_the_Soviet_Union'>🔗</a>"
    fig.add_annotation(
        x=1933,
        y=40,  # Slightly above the y-value
        text=txt_,
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-200,
        arrowcolor='lightgrey',
        arrowwidth=1,
        borderpad=5,
        align='left',
        xanchor='left',
    )

    txt_ = "<b>1941 - 1945.</b> WWII <a href='https://en.wikipedia.org/wiki/Soviet_Union_in_World_War_II'>🔗</a>"
    fig.add_annotation(
        x=1943,
        y=40,  # Slightly above the y-value
        text=txt_,
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-170,
        arrowcolor='lightgrey',
        arrowwidth=1,
        borderpad=5,
        align='left',
        xanchor='left',
    )

    txt_ = "Life expectancy measured in years"
    fig.add_annotation(
        x=-0.02,
        y=1.07,
        text=txt_,
        showarrow=False,
        ax=0,
        ay=-130,
        xref="paper", yref="paper",
        font=dict(size=14),
        align="left"
    )

    txt_ = "Source: Gapminder, <a href='https://www.gapminder.org/data/'>Life expectancy</a>"
    fig.add_annotation(
        x=-0.02,
        y=-0.10,
        text=txt_,
        showarrow = False,
        ax=0,
        ay=-130,
        xref = "paper", yref = "paper",
        font=dict(family="Helvetica Neue", size=12),
        align="left"
    )

    # Update the layout
    fig.update_layout(
        title=dict(
            text='Average life expectancy in Russia',
            y=0.98,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        xaxis=dict(
            title='',
            tickmode='linear',
            dtick=20,
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
        ),
        yaxis=dict(
            title=None,
            tickmode='linear',
            dtick=10,
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=100, pad=0),
        height=600,
        width=1000,
    )

    return fig


def life_expectancy_scatter_plot(df):
    fig = go.Figure()

    for country in df['country'].unique():
        prior_2022_country_data = (df[df['country'] == country].query("year <= 2023"))
        fig.add_trace(go.Scatter(
            x=prior_2022_country_data['year'],
            y=prior_2022_country_data['life_expectancy'],
            mode='lines',
            line=dict(
                dash='solid',
                color='rgb(0, 51, 153)'
            ),
            showlegend=False,
        ))

        post_2022_country_data = (df[df['country'] == country].query("year >= 2023"))
        fig.add_trace(go.Scatter(
            x=post_2022_country_data['year'],
            y=post_2022_country_data['life_expectancy'],
            mode='lines',
            line=dict(dash='dot',
                      color='rgba(0, 51, 153, 0.5)'
                      ),
            showlegend=False,
        ))

        def _highlight_years(df, specific_years):
            specific_years_data = df[(df['country'] == country) & (df['year'].isin(specific_years))]
            fig.add_trace(go.Scatter(
                x=specific_years_data['year'],
                y=specific_years_data['life_expectancy'],
                mode='lines+markers',
                line=dict(width=5.5, color='rgb(0, 51, 153)', ),
                marker=dict(
                    size=8,
                    color='white',
                    line=dict(color='rgb(0, 51, 153)', width=4)
                ),
                showlegend=False,
            ))

        _highlight_years(df, [1917, 1918, 1919, 1920, 1921, 1922])
        _highlight_years(df, [1933])
        _highlight_years(df, [1941, 1942, 1943, 1944, 1945])

    txt_ = "<b>1917 - 1922.</b> Russian civil war <a href='https://en.wikipedia.org/wiki/Russian_Civil_War'>🔗</a>"
    fig.add_annotation(
        x=1920,
        y=40,  # Slightly above the y-value
        text=txt_,
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-260,
        arrowcolor='lightgrey',
        arrowwidth=1,
        borderpad=5,
        align='left',
        xanchor='left',
    )

    txt_ = "<b>1933.</b> Stalinist collectivisation <a href='https://en.wikipedia.org/wiki/Collectivization_in_the_Soviet_Union'>🔗</a>"
    fig.add_annotation(
        x=1933,
        y=40,  # Slightly above the y-value
        text=txt_,
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-230,
        arrowcolor='lightgrey',
        arrowwidth=1,
        borderpad=5,
        align='left',
        xanchor='left',
    )

    txt_ = "<b>1941 - 1945.</b> WWII <a href='https://en.wikipedia.org/wiki/Soviet_Union_in_World_War_II'>🔗</a>"
    fig.add_annotation(
        x=1943,
        y=40,  # Slightly above the y-value
        text=txt_,
        showarrow=True,
        arrowhead=0,
        ax=0,
        ay=-200,
        arrowcolor='lightgrey',
        arrowwidth=1,
        borderpad=5,
        align='left',
        xanchor='left',
    )

    txt_ = "Life expectancy measured in years"
    fig.add_annotation(
        x=-0.02,
        y=1.07,
        text=txt_,
        showarrow=False,
        ax=0,
        ay=-130,
        xref="paper", yref="paper",
        font=dict(size=14),
        align="left"
    )

    txt_ = "Source: Gapminder, <a href='https://www.gapminder.org/data/'>Life expectancy</a>"
    fig.add_annotation(
        x=-0.02,
        y=-0.10,
        text=txt_,
        showarrow=False,
        ax=0,
        ay=-130,
        xref="paper", yref="paper",
        font=dict(family="Helvetica Neue", size=12),
        align="left"
    )

    fig.add_vline(
        x=2023,
        line=dict(color='lightgrey', dash='dot', width=2),
        annotation_text='Predicted life expectancy after 2022',
        annotation_position='top right',
    )

    # Update the layout
    fig.update_layout(
        title=dict(
            text='Average life expectancy in Russia',
            y=0.98,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        xaxis=dict(
            title='',
            tickmode='linear',
            dtick=20,
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
        ),
        yaxis=dict(
            title=None,
            tickmode='linear',
            dtick=10,
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=100, pad=0),
        height=600,
        width=1000,
    )

    return fig