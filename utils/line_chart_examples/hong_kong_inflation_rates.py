import plotly.graph_objects as go

def hk_inflation_rates_line_chart(df, type='line'):
    color='rgb(0, 43, 127)'

    fig = go.Figure()

    for year in [1997, 2003]:
        population_value = df[df['Year'] == year]['Inflation Rate'].values[0]

        fig.add_trace(
            go.Scatter(x=df[df['Year'] == year]['Year'],
                       y=df[df['Year'] == year]['Inflation Rate'],
                       text=df[df['Year'] == year]['Inflation Rate'],
                       mode='markers+text',
                       showlegend=False,
                       marker=dict(size=8, color=color),
                       textfont=dict(family="Helvetica Neue", size=14, color=color),
                       textposition='middle right',
                       )
        )

        if year == 1997:
            t = "<b>(1998)</b><br>Asian financial<br>crisis <a href='https://en.wikipedia.org/wiki/1997_Asian_financial_crisis'>🔗</a>"
        else:
            t = "<b>(2003)</b><br>2003 protests,<br>with 500k marchers <a href='https://en.wikipedia.org/wiki/Hong_Kong_1_July_marches#:~:text=The%20Hong%20Kong%201%20July,of%20Basic%20Law%20Article%2023.u'>🔗</a>"

        fig.add_shape(
            type="line",
            x1=year,
            x0=year,
            y0=population_value,
            y1=12,
            line=dict(color="grey", width=1, dash="dash"),
        )

        fig.add_trace(
            go.Scatter(x=[year],
                       y=[12],
                       text=[t],
                       mode='markers+text',
                       showlegend=False,
                       marker=dict(size=20, color='rgba(0,0,0,0)'),
                       textfont=dict(family="Helvetica Neue", size=14, color='grey'),
                       textposition='middle right',
                       )
        )

    if type=='line':
        fig.add_trace(
            go.Scatter(x=df['Year'],
                       y=df['Inflation Rate'],
                       mode='lines',
                       showlegend=False,
                       line=dict(width=2, color=color),
                       )
        )
    else:
        fig.add_trace(
            go.Scatter(x=df['Year'],
                       y=df['Inflation Rate'],
                       mode='lines',
                       fill='tozeroy',
                       showlegend=False,
                       line=dict(width=2, color=color),
                       )
        )

    fig.update_layout(
        title=dict(
            text='Price drops in Hong Kong',
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='The asian financial crisis trigegered 5 years of deflation and the first series od demonstrations.',
                xref="paper",
                yref="paper",
                x=-0.07, y=1.23,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text='Inflation rate (%)',
                xref="paper",
                yref="paper",
                x=-0.07, y=1.08,
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
        showlegend=False,
        margin=dict(t=250, r=100, pad=0),
        height=800,
        width=1000,
    )

    return fig