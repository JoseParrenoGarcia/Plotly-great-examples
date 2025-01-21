import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def fertility_rates_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='Fertility_Rate',
                 color='Country Name',
                 title='Fertility rates (children per woman)')

    # Minor layout customization
    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def fertility_rates_line_plot(df, title, countries_to_highlight):
    fig = go.Figure()

    for country in df['Country Name'].unique():
        if country not in countries_to_highlight:
            fig.add_trace(
                go.Scatter(x=df[df['Country Name'] == country]['Year'],
                           y=df[df['Country Name'] == country]['Fertility_Rate'],
                           mode='lines',
                           name=country,
                           showlegend=False,
                           line=dict(color='rgba(204, 209, 209, 0.5)', width=1)
                           )
            )

    for country in countries_to_highlight:
        if country in df['Country Name'].unique():
            fig.add_trace(
                go.Scatter(x=df[df['Country Name'] == country]['Year'],
                           y=df[df['Country Name'] == country]['Fertility_Rate'],
                           mode='lines',
                           name=country,
                           showlegend=False,
                           line=dict(color='purple', width=2)
                           )
            )

            if country == 'United Arab Emirates':
                text='UAE'
                textposition = 'middle right'
            elif country == 'Congo, Dem. Rep.':
                text='Congo'
                textposition = 'middle right'
            elif country == 'Somalia':
                text = 'Somalia'
                textposition = 'top right'
            else:
                text=country
                textposition='middle right'

            fig.add_trace(
                go.Scatter(x=df[(df['Country Name'] == country) & (df['Year'] == df['Year'].max())]['Year'],
                           y=df[(df['Country Name'] == country) & (df['Year'] == df['Year'].max())]['Fertility_Rate'],
                           mode='markers+text',
                           name=country,
                           showlegend=False,
                           marker=dict(color='purple', size=6),
                           text=text,
                           textposition=textposition,
                           textfont=dict(family="Helvetica Neue", color='purple', size=12),
                           )
            )

    # Update layout
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Children per woman",
                xref="paper",
                yref="paper",
                x=-0.085, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max()+8],
            tickvals=[1980, 1990, 2000, 2010, 2020],
            ticktext=['1980', '1990', '2000', '2010', '2020'],
        ),
        yaxis=dict(
            title='',
            showline=True,
            showgrid=False,
            linecolor='lightgrey',
            linewidth=2,
            ticksuffix="  ",
        ),
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=150, r=100, pad=0),
        height=700,
        width=700,
    )

    return fig

def fertility_rates_lines_by_group(df):
    def _individual_plot(df, continent):
        df_continent = df[df['continent'] == continent]
        last_year = df_continent['Year'].max()
        df_last_year = df_continent[df_continent['Year'] == last_year]
        max_fertility_country = df_last_year.loc[df_last_year['Fertility_Rate'].idxmax()]
        min_fertility_country = df_last_year.loc[df_last_year['Fertility_Rate'].idxmin()]

        countries_to_highlight = [max_fertility_country['Country Name'], min_fertility_country['Country Name']]
        rest_of_countries = [country for country in df_continent['Country Name'].unique() if country not in countries_to_highlight]

        fig = go.Figure()

        for country in rest_of_countries:
            fig.add_trace(
                go.Scatter(x=df_continent[df_continent['Country Name'] == country]['Year'],
                           y=df_continent[df_continent['Country Name'] == country]['Fertility_Rate'],
                           mode='lines',
                           name=country,
                           showlegend=False,
                           line=dict(color='rgba(204, 209, 209, 0.5)', width=1)
                           )
                )

        for country in countries_to_highlight:
            if country in df['Country Name'].unique():
                fig.add_trace(
                    go.Scatter(x=df_continent[df_continent['Country Name'] == country]['Year'],
                               y=df_continent[df_continent['Country Name'] == country]['Fertility_Rate'],
                               mode='lines',
                               name=country,
                               showlegend=False,
                               line=dict(color='purple', width=2)
                               )
                )

                fig.add_trace(
                    go.Scatter(x=df_continent[(df_continent['Country Name'] == country) & (df_continent['Year'] == df_continent['Year'].max())]['Year'],
                               y=df_continent[(df_continent['Country Name'] == country) & (df_continent['Year'] == df_continent['Year'].max())]['Fertility_Rate'],
                               mode='markers+text',
                               name=country,
                               showlegend=False,
                               marker=dict(color='purple', size=6),
                               text=country,
                               textposition='bottom left',
                               textfont=dict(family="Helvetica Neue", color='purple', size=12),
                               )
                )

        return fig

    fig = make_subplots(rows=1, cols=5, shared_yaxes=True,
                        # subplot_titles=("Asia", "Europe", "Africa", "North America", 'S')
                        )

    asia_fig = _individual_plot(df=df, continent='Asia')
    for trace in asia_fig.data:
        fig.add_trace(trace, row=1, col=1)

    europe_fig = _individual_plot(df=df, continent='Europe')
    for trace in europe_fig.data:
        fig.add_trace(trace, row=1, col=2)

    africa_fig = _individual_plot(df=df, continent='Africa')
    for trace in africa_fig.data:
        fig.add_trace(trace, row=1, col=3)

    north_america_fig = _individual_plot(df=df, continent='North America')
    for trace in north_america_fig.data:
        fig.add_trace(trace, row=1, col=4)

    south_america_fig = _individual_plot(df=df, continent='South America')
    for trace in south_america_fig.data:
        fig.add_trace(trace, row=1, col=5)

    # Update layout
    fig.update_layout(
        title=dict(
            text='Fertility rates are down across the world, but to different degrees.',
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            dict(
                text="Children per woman",
                xref="paper",
                yref="paper",
                x=-0.04, y=1.06,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            dict(
                text="<i>Highlighting the countries with the highest and lowest fertility rate by continent</i>",
                xref="paper",
                yref="paper",
                x=-0.04, y=1.13,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14, color='purple'),
                align="left"
            ),
        ],
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=150, r=100, pad=0),
        height=700,
    )

    for col in range(1, 6):
        fig.update_xaxes(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max() + 2],
            dtick=20,
            row=1,
            col=col
        )

        fig.update_yaxes(
            showline=True,
            showgrid=True,
            linecolor='lightgrey',
            linewidth=2,
            row=1,
            col=col
        )

    fig.update_yaxes(title='', ticksuffix="  ", row=1, col=1)

    return fig
