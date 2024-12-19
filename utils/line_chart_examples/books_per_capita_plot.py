import plotly.graph_objects as go
import plotly.express as px

def books_per_capita_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='book_titles_per_capita',
                 color='Entity',
                 title='UK amongst the top 10 countries with most books published per capita, but still behind Scandinavian countries')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def books_per_capita_line_plot(df):
    hero_line = ["United Kingdom"]
    scandinavian_countries = ['Iceland', 'Norway', 'Sweden', 'Denmark', 'Finland']
    rest_of_countries = [country for country in df['Entity'].unique() if country not in hero_line + scandinavian_countries]

    fig = go.Figure()

    for country in rest_of_countries:
        fig.add_trace(
            go.Scatter(x=df[df['Entity'] == country]['Year'],
                       y=df[df['Entity'] == country]['book_titles_per_capita'],
                       mode='lines',
                       name=country,
                       showlegend=False,
                       line=dict(color='rgba(204, 209, 209, 0.5)', width=1)
                       )
        )

        if country in ['Netherlands', 'Spain']:
            fig.add_trace(
                go.Scatter(x=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['Year'],
                           y=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['book_titles_per_capita'],
                           mode='markers+text',
                           name=country,
                           showlegend=False,
                           marker=dict(color='rgba(204, 209, 209, 0.5)', size=6),
                           text=country,
                           textposition='middle right',
                           textfont=dict(family="Helvetica Neue", color='rgba(204, 209, 209, 1)', size=12),
                           )
            )

    for country in scandinavian_countries:
        fig.add_trace(
            go.Scatter(x=df[df['Entity'] == country]['Year'],
                       y=df[df['Entity'] == country]['book_titles_per_capita'],
                       mode='lines',
                       name=country,
                       showlegend=False,
                       line=dict(color='rgba(174, 214, 241, 0.8)', width=2)
                       )
        )

        fig.add_trace(
            go.Scatter(x=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['Year'],
                       y=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['book_titles_per_capita'],
                       mode='markers+text',
                       name=country,
                       showlegend=False,
                       marker=dict(color='rgba(174, 214, 241, 0.8)', size=6),
                       text=country,
                       textposition='middle right',
                       textfont=dict(family="Helvetica Neue", color='rgba(174, 214, 241, 1)', size=12),
                       )
        )

    for country in hero_line:
        fig.add_trace(
            go.Scatter(x=df[df['Entity'] == country]['Year'],
                       y=df[df['Entity'] == country]['book_titles_per_capita'],
                       mode='lines',
                       name=country,
                       showlegend=False,
                       line=dict(color='purple', width=2)
                       )
        )

        fig.add_trace(
            go.Scatter(x=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['Year'],
                       y=df[(df['Entity'] == country) & (df['Year'] == df['Year'].max())]['book_titles_per_capita'],
                       mode='markers+text',
                       name=country,
                       showlegend=False,
                       marker=dict(color='purple', size=6),
                       text='UK',
                       textposition='middle right',
                       textfont=dict(family="Helvetica Neue", color='purple', size=12),
                       )
        )

    # Update layout
    fig.update_layout(
        title=dict(
            text="How many books are published per million inhabitants?",
            font=dict(family="Helvetica Neue", size=20),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='UK amongst the top 10 countries with most books published per capita,<br>but still behind Scandinavian countries',
                xref="paper",
                yref="paper",
                x=-0.13, y=1.12,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=15),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max()+7],
            tickvals=[1960, 1970, 1980, 1990],
            ticktext=['1960', '1970', '1980', '1990'],
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
        margin=dict(t=150, r=100, pad=0),
        height=700,
        width=700,
    )

    return fig