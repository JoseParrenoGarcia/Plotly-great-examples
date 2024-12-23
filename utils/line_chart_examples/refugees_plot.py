import plotly.graph_objects as go
import plotly.express as px

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
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in ['Iraq', 'Syria', 'Afghanistan'] else row['color_greyscale'], axis=1)
            elif type == 'Sudan_subsahara':
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in ['Sudan & South Sudan', 'Subharan Africa'] else row['color_greyscale'], axis=1)
            elif type == 'Myanmar':
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in ['Myanmar'] else row['color_greyscale'], axis=1)
            elif type == 'Bos_Ukr':
                df_aux.loc[:, 'color'] = df_aux.apply(lambda row: row['color_rgb'] if row['countries_to_display'] in ['Bosnia and Herzegovina', 'Ukraine'] else row['color_greyscale'], axis=1)
            else:
                df_aux.loc[:, 'color'] = df_aux['color_rgb']


            fig.add_trace(
                go.Scatter(x=df_aux['Year'],
                           y=df_aux['Refugees'],
                           mode='lines',
                           name=country,
                           stackgroup='one',
                           showlegend=True,
                           line=dict(width=2, color=df_aux['color'].values[0]),
                           )
            )

            # fig.add_trace(
            #     go.Scatter(x=df_aux[df_aux['Year'] == df_aux['Year'].max()]['Year'],
            #                y=df_aux[df_aux['Year'] == df_aux['Year'].max()]['Refugees'],
            #                text=df_aux[df_aux['Year'] == df_aux['Year'].max()]['Refugees'].apply(lambda x: f"{x // 1000000}m"),
            #                mode='markers+text',
            #                showlegend=False,
            #                marker=dict(size=8),
            #                textfont=dict(family="Helvetica Neue", size=14),
            #                textposition='middle right',
            #                )
            # )

    fig.update_layout(
        title=dict(
            text='Highest level of refugees in known history',
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='32 million people are currently displaced worldwide. This is equivalent to the population of Saudi Arabia.',
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