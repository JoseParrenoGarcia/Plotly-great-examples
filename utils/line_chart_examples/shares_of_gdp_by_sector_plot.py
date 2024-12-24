import plotly.graph_objects as go

def shares_of_gdp_by_sector_plot(df, type='line'):
    fig = go.Figure()

    for sector in ['Share_of_agriculture_in_GDP',
                   'Share_of_industry_in_GDP',
                   'Share_of_services_in_GDP',
                   ]:

        if sector == 'Share_of_services_in_GDP':
            t = 'Services'
            c = 'rgb(93, 173, 226)'
        elif sector == 'Share_of_industry_in_GDP':
            t = 'Industry'
            c = 'rgb(236, 112, 99)'
        else:
            t = 'Agriculture'
            c = 'rgb(69, 179, 157)'

        if type=='line':
            x_ = -0.07
            fig.add_trace(
                go.Scatter(x=df['Year'],
                           y=df[sector],
                           mode='lines',
                           name=sector,
                           line=dict(width=2.5, color=c),
                           showlegend=False,
                           )
            )

            fig.add_trace(
                go.Scatter(x=df[df['Year'] == df['Year'].max()]['Year'],
                           y=df[df['Year'] == df['Year'].max()][sector],
                           mode='markers+text',
                           name=t,
                           showlegend=False,
                           marker=dict(size=6.5, color=c),
                           text=t,
                           textposition='middle right',
                           textfont=dict(family="Helvetica Neue", size=14, color=c),
                           )
            )


        else:
            x_ = -0.08
            fig.add_trace(
                go.Scatter(x=df['Year'],
                           y=df[sector],
                           mode='lines',
                           name=t,
                           line=dict(width=2, color=c),
                           stackgroup='one',
                           fillcolor=c,
                           showlegend=True,
                           )
            )


    fig.update_layout(
        title=dict(
            text='Spain is becoming a service economy',
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Agriculture is losing importance in the Spanish economy, represeting only a 3.47% of GDP in 2011',
                xref="paper",
                yref="paper",
                x=x_, y=1.23,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text='Share of services in GDP (%)',
                xref="paper",
                yref="paper",
                x=x_, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max() + 19],
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
        margin=dict(t=250, r=100, pad=0),
        height=800,
        width=1000,
    )

    return fig