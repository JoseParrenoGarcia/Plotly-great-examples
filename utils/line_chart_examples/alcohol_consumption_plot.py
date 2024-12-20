import plotly.graph_objects as go
import plotly.express as px

def alcohol_consumption_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='alcohol_consumption',
                 color='Country',
                 title='Alcohol consumption in litres per capita per year')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def alcohol_consumption_line_chart(df):

    def _plot_lines(fig, df, countries, color):
        for country in countries:
            fig.add_trace(
                go.Scatter(x=df[df['Country'] == country]['Year'],
                           y=df[df['Country'] == country]['alcohol_consumption'],
                           mode='lines',
                           name=country,
                           showlegend=False,
                           line=dict(color=color, width=2)
                           )
            )

            # if (country == 'Tanzania') or (country == 'Egypt, Arab Rep.'):
            #     textposition = 'bottom right'
            # # elif country == 'Poland':
            # #     textposition = 'top right'
            # else:
            #     textposition = 'middle right'

            fig.add_trace(
                go.Scatter(x=df[(df['Country'] == country) & (df['Year'] == df['Year'].max())]['Year'],
                           y=df[(df['Country'] == country) & (df['Year'] == df['Year'].max())]['alcohol_consumption'],
                           mode='markers+text',
                           name=country,
                           showlegend=False,
                           marker=dict(color=color, size=6),
                           text=country,
                           textposition='middle right',
                           textfont=dict(family="Helvetica Neue", color=color, size=12),
                           )
            )

    european_consumers = ["Romania", "Poland", "Latvia", "Georgia"]
    african_countries = ['Uganda', 'Tanzania', 'Cameroon', 'Benin']
    muslim_countries = ['United Arab Emirates', 'Bahrain', 'Algeria', 'Egypt, Arab Rep.']
    rest_of_countries = [country for country in df['Country'].unique() if country not in european_consumers + african_countries + muslim_countries]

    fig = go.Figure()

    for country in rest_of_countries:
        fig.add_trace(
            go.Scatter(x=df[df['Country'] == country]['Year'],
                       y=df[df['Country'] == country]['alcohol_consumption'],
                       mode='lines',
                       name=country,
                       showlegend=False,
                       line=dict(color='rgba(204, 209, 209, 0.5)', width=1)
                       )
        )

    _plot_lines(fig, df, european_consumers, 'red')
    _plot_lines(fig, df, african_countries, 'orange')
    _plot_lines(fig, df, muslim_countries, 'green')


    # Update layout
    fig.update_layout(
        title=dict(
            text="Drinking patterns around the world",
            font=dict(family="Helvetica Neue", size=20),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Traditional <b><span style="color:red;">hard-drinking countries</span></b> still consume a lot,'
                     '<br>but <b><span style="color:orange;">African countries</span></b> are increasing their alcohol consumption.'
                     '<br>Most <b><span style="color:green;">Muslim countries</span></b> stay sober.',
                xref="paper",
                yref="paper",
                x=-0.1, y=1.2,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=15),
                align="left"
            ),
            dict(
                text='Annual alcohol consumption (litres per person)',
                xref="paper",
                yref="paper",
                x=-0.1, y=1.07,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=13),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max()+7],
            tickvals=[2000, 2005, 2010, 2015, 2020],
            ticktext=['2000', '2005', '2010', '2015', '2020'],
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
        margin=dict(t=250, r=100, pad=0),
        height=900,
        width=700,
    )

    return fig
