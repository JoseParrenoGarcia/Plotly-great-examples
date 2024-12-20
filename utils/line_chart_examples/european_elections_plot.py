import plotly.graph_objects as go
import plotly.express as px

def european_elections_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='SEATS_PERCENT_EU',
                 color='political_spectrum',
                 title='European elections')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig


def european_elections_line_chart(df):

    fig = go.Figure()

    for spectrum in df['political_spectrum'].unique():
        fig.add_trace(
            go.Scatter(x=df[df['political_spectrum'] == spectrum]['Year'],
                       y=df[df['political_spectrum'] == spectrum]['SEATS_PERCENT_EU'],
                       mode='lines',
                       name=spectrum,
                       showlegend=False,
                       line=dict(color=df[df['political_spectrum'] == spectrum]['color'].values[0], width=2)
                       )
        )

        if spectrum == 'Center':
            textposition = 'bottom right',
        else:
            textposition = 'middle right',

        fig.add_trace(
            go.Scatter(x=df[(df['political_spectrum'] == spectrum) & (df['Year'] == df['Year'].max())]['Year'],
                       y=df[(df['political_spectrum'] == spectrum) & (df['Year'] == df['Year'].max())]['SEATS_PERCENT_EU'],
                       mode='markers+text',
                       name=spectrum,
                       showlegend=False,
                       marker=dict(color=df[df['political_spectrum'] == spectrum]['color'].values[0], size=6),
                       text=spectrum,
                       textposition=textposition,
                       textfont=dict(family="Helvetica Neue", color=df[df['political_spectrum'] == spectrum]['color'].values[0], size=12),
                       )
        )

    fig.update_layout(
        title=dict(
            text="Europe is moving to the right",
            font=dict(family="Helvetica Neue", size=20),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='The right-wing parties have increased their presence in the European Parliament<br>over the last 40 years',
                xref="paper",
                yref="paper",
                x=-0.1, y=1.2,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=15),
                align="left"
            ),
            dict(
                text='Percentage of seats in the European Parliament',
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
            range=[df['Year'].min(), df['Year'].max() + 7],
            tickvals=[1979, 1984, 1989, 1994, 1999, 2004, 2009, 2014, 2019, 2024],
            ticktext=['1979', '1984', '1989', '1994', '1999', '2004', '2009', '2014', '2019', '2024'],
            showticklabels=True,
            ticks='outside',
            tickwidth=2,
            tickcolor='lightgrey'
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