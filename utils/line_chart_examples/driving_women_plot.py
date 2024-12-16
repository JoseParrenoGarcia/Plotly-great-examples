import plotly.graph_objects as go

def driving_women_line_chart(df, add_context=True):
    df = df.sort_values(['Year', 'Sex'], ascending=False)

    fig = go.Figure()

    for sex in df['Sex'].unique():
        df_aux = df[df['Sex'] == sex]

        if sex == 'Males':
            color = 'rgb(46, 134, 193)'
        else:
            color = 'rgb(236, 112, 99)'

        fig.add_trace(
            go.Scatter(
                x=df_aux['Year'],
                y=df_aux['percentage'],
                name=sex,
                mode='lines',
                showlegend=False,
                line=dict(color=color),
            )
        )

        scatter_dot_df = df_aux[df_aux['Year'] == 2023]
        fig.add_trace(
            go.Scatter(
                x=scatter_dot_df['Year'],
                y=scatter_dot_df['percentage'],
                name=sex,
                mode='markers+text',
                text=scatter_dot_df['percentage'].astype(str) + '% ' + scatter_dot_df['Sex'],
                textposition='middle right',
                showlegend=False,
                marker=dict(color=color),
                textfont=dict(color=color,),
            )
        )


    # Customize the layout
    fig.update_layout(
        title=dict(
            text='The drive for equality',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Only 29% of women drove in 1975. Now, it is over 70%.",
                xref="paper",
                yref="paper",
                x=-0.080, y=1.23,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text="Driving licence holders by gender (UK, %)",
                xref="paper",
                yref="paper",
                x=-0.080, y=1.10,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            dict(
                x=-0.080,
                y=-0.2,
                text="Source: GOV.UK, <a href='https://assets.publishing.service.gov.uk/media/66ce14751aaf41b21139cf8e/nts0201.ods'>Full car driving licence holders by age and sex group</a>",
                showarrow = False,
                ax=0,
                ay=-130,
                xref = "paper", yref = "paper",
                font=dict(family="Helvetica Neue", size=12),
                align = "left"
            )
        ],
        font=dict(family="Helvetica Neue"),
        yaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=1,
                   gridcolor='lightgrey',
                   gridwidth=1,
                   griddash='dot',
                   ),
        xaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=3,
                   range=[1975, 2030],
                   ),
        margin=dict(t=150, pad=0),
        height=600,
        width=700,
    )

    return fig
