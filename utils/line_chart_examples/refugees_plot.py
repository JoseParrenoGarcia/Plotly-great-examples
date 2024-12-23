import plotly.graph_objects as go
import plotly.express as px
from numpy.core.defchararray import title


def refugees_plotly_express_line_chart(df):
    fig = px.line(df,
                  x='Year',
                  y='Refugees',
                  color='countries_to_display',
                  title='Refugees by country')

    # Minor layout customization
    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def refugees_line_chart(df, type='total'):
    fig = go.Figure()

    if type=='total':
        title_ = 'Highest level of refugees in known history'
        h1= '32 million people are currently displaced worldwide. This is equivalent to the population of Saudi Arabia.'

        df_aux = df.groupby('Year').sum().reset_index()

        fig.add_trace(
            go.Scatter(x=df_aux['Year'],
                       y=df_aux['Refugees'],
                       mode='lines',
                       fill='tozeroy',
                       showlegend=False,
                       line=dict(width=2, color='purple'),
                       )
        )

        fig.add_trace(
            go.Scatter(x=df_aux[df_aux['Year'] == df_aux['Year'].max()]['Year'],
                       y=df_aux[df_aux['Year'] == df_aux['Year'].max()]['Refugees'],
                       text=df_aux[df_aux['Year'] == df_aux['Year'].max()]['Refugees'].apply(lambda x: f"{x // 1000000}m"),
                       mode='markers+text',
                       showlegend=False,
                       marker=dict(size=8, color='purple'),
                       textfont=dict(family="Helvetica Neue", size=14, color='purple'),
                       textposition='middle right',
                       )
        )

    else:
        list_of_countries = ['Syria', 'Iraq', 'Afghanistan',
                             'Sudan & South Sudan', 'Subharan Africa',
                             'Myanmar',
                             'Ukraine', 'Bosnia and Herzegovina',
                             'Everywhere else']

        for country in list_of_countries:
            df_aux = df[df['countries_to_display'] == country]

            if type == 'Ir_Sy_Af':
                title_='Refugees from Iraq, Syria and Afghanistan'
                h1=type

                country_list = ['Iraq', 'Syria', 'Afghanistan']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

            elif type == 'Sudan_subsahara':
                title_='Refugees from Sudan and Subharan Africa'
                h1 = type

                country_list = ['Sudan & South Sudan', 'Subharan Africa']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

            elif type == 'Myanmar':
                title_='Refugees from Myanmar'
                h1 = type

                country_list = ['Myanmar']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

            elif type == 'Bos_Ukr':
                title_='Refugees from Bosnia and Herzegovina and Ukraine'
                h1 = type

                country_list = ['Bosnia and Herzegovina', 'Ukraine']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

            else:
                title_='Refugees by country'
                h1 = type

                country_list = list_of_countries
                df_aux.loc[:, 'color'] = df_aux['color_rgb']


            fig.add_trace(
                go.Scatter(x=df_aux['Year'],
                           y=df_aux['Refugees'],
                           mode='lines',
                           name=country,
                           stackgroup='one',
                           showlegend=False,
                           line=dict(width=2, color=df_aux['color'].values[0]),
                           )
            )

            for c in country_list:
                specific_country_df = df_aux[(df_aux['countries_to_display'] == c) & (df_aux['Year'] == df_aux['Year'].max())]

                if (c == 'Ukraine') or (c =='Syria'):
                    textpos = 'bottom right'
                elif (c == 'Bosnia and Herzegovina') or () or (c == 'Iraq'):
                    textpos = 'top right'
                else:
                    textpos = 'middle right'

                fig.add_trace(
                    go.Scatter(x=specific_country_df['Year'],
                               y=specific_country_df['cumulative_refugees'],
                               text=specific_country_df['text_to_show'],
                               mode='markers+text',
                               showlegend=False,
                               marker=dict(size=8, color=df_aux['color'].values[0]),
                               textfont=dict(family="Helvetica Neue", size=14, color=df_aux['color'].values[0]),
                               textposition=textpos,
                               )
                )

    fig.update_layout(
        title=dict(
            text=title_,
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text=h1,
                xref="paper",
                yref="paper",
                x=-0.08, y=1.23,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text='Refugee population by country of origin',
                xref="paper",
                yref="paper",
                x=-0.08, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max() + 15],
            tickvals=[1980, 1990, 2000, 2010, 2020],
            ticktext=['1980', '1990', '2000', '2010', '2020'],

        ),
        yaxis=dict(
            title='',
            showline=True,
            zeroline=False,
            showgrid=False,
            linecolor='lightgrey',
            linewidth=2,
            ticksuffix="  ",
            # range=[0, 4.4],

        ),
        font=dict(family="Helvetica Neue", size=14),
        margin=dict(t=250, r=100, pad=0),
        height=800,
        width=1000,
    )

    return fig