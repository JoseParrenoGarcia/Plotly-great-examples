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

    def _add_annotation_to_area_plot(fig, year, ystart, t, pos, yend=32_000_000, c='grey'):
        fig.add_shape(
            type="line",
            x1=year,
            x0=year,
            y0=ystart,
            y1=yend,
            line=dict(color=c, width=1, dash="dash"),
        )

        fig.add_trace(
            go.Scatter(x=[year],
                       y=[yend],
                       text=[t],
                       mode='markers+text',
                       showlegend=False,
                       marker=dict(size=8, color='rgba(0,0,0,0)'),
                       textfont=dict(color=c),
                       textposition=pos,
                       )
        )

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
                title_='Wars in the Middle East are one of the worst problems in humankind.'
                h1='Syria and Afganishtan are the countries with the highest number of refugees.'

                country_list = ['Iraq', 'Syria', 'Afghanistan']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

                if country == 'Afghanistan':
                    t = "<b>(2001)</b><br>The Taliban collapse <a href='https://www.cfr.org/timeline/us-war-afghanistan'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 2001]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=2001, t=t, pos='middle left', ystart=ystart, c=c)

                    t = "<b>(2021)</b><br>Talibans regain control <a href='https://www.cfr.org/timeline/us-war-afghanistan'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 2021]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=2021, t=t, pos='middle left', ystart=ystart, c=c)

                if country == 'Iraq':
                    t = "<b>(2006-2008)</b><br>Iraqi Civil War <a href='https://en.wikipedia.org/wiki/Iraqi_civil_war_(2006–2008)'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 2006]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=2006, t=t, pos='middle right', ystart=ystart, yend=28_000_000, c=c)

                if country == 'Syria':
                    t = "<b>(2011-present)</b><br>Syrian Civil War<br><a href='https://en.wikipedia.org/wiki/Syrian_civil_war'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 2011]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=2011, t=t, pos='middle right', ystart=ystart, yend=23_000_000, c=c)


            elif type == 'Sudan_subsahara':
                title_='Civil war in South Sudan and neighbouring countries are not covered enough in the media.'
                h1 = 'After South Sudans independence in 2011, the country has been in a civil war.'

                country_list = ['Sudan & South Sudan', 'Subharan Africa']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

                if country == 'Sudan & South Sudan':
                    t = "<b>(2013-2020)</b><br>South Sudanese civil war <a href='https://en.wikipedia.org/wiki/South_Sudanese_Civil_War'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 2013]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=2013, t=t, pos='middle left', ystart=ystart, c=c)

                if country == 'Subharan Africa':
                    t = "<b>(1994)</b><br>Rwanda genocide <a href='https://en.wikipedia.org/wiki/Rwandan_genocide'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 1994]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=1994, t=t, pos='middle right', ystart=ystart, yend=28_000_000, c=c)

            elif type == 'Myanmar':
                title_='The Rohingya crisis.'
                h1 = 'The Myanmar government launched a military campaign in 2017 against the Muslim ethnic minority Rohingya.'

                country_list = ['Myanmar']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

                if country == 'Myanmar':
                    t = "<b>(2017-present)</b><br>Massive waves of violence started in Rakhine State <a href='https://www.unrefugees.org/news/rohingya-refugee-crisis-explained/#RohingyainBangladesh'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 2017]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=2017, t=t, pos='middle left', ystart=ystart, c=c)

            elif type == 'Bos_Ukr':
                title_='Criminal Russia is forcing people in Ukraine to flee their homes.'
                h1 = 'Ukraine is now the biggest refugee crisis in Europe since the war in Bosnia'

                country_list = ['Bosnia and Herzegovina', 'Ukraine']
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in country_list else row['color_greyscale'], axis=1)

                if country == 'Bosnia and Herzegovina':
                    t = "<b>(1992-1995)</b><br>Bosnian war <a href='https://en.wikipedia.org/wiki/Bosnian_War'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 1992]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=1992, t=t, pos='middle right', ystart=ystart, c=c)

                if country == 'Ukraine':
                    t = "<b>(2021-present)</b><br>Russia invades Ukraine <a href='https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine'>🔗</a>"
                    ystart = df_aux[df_aux['Year'] == 2021]['cumulative_refugees'].values[0]
                    c = df_aux['color'].values[0]
                    _add_annotation_to_area_plot(fig=fig, year=2021, t=t, pos='middle left', ystart=ystart, c=c)

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
                elif (c == 'Bosnia and Herzegovina') or (c == 'Iraq'):
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

            remaining_countries = [country for country in list_of_countries if country not in country_list]
            for c in remaining_countries:
                specific_country_df = df_aux[(df_aux['countries_to_display'] == c) & (df_aux['Year'] == df_aux['Year'].max())]

                if (c == 'Ukraine') or (c =='Syria') or (c =='Subharan Africa'):
                    textpos = 'bottom right'
                elif (c == 'Bosnia and Herzegovina') or (c == 'Iraq') or (c == 'Myanmar') or (c == 'Everywhere else'):
                    textpos = 'top right'
                else:
                    textpos = 'middle right'

                fig.add_trace(
                    go.Scatter(x=specific_country_df['Year'],
                               y=specific_country_df['cumulative_refugees'],
                               text=c,
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