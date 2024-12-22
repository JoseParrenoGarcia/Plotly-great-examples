import plotly.graph_objects as go
import plotly.express as px

def fertility_rates_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='Fertility Rate',
                 title='Fertility rates soared in Romania forced by communist dictator Ceaucescu')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def fertility_rates_line_chart(df, type='line'):
    color='rgb(0, 43, 127)'

    fig = go.Figure()

    for year in [1967, 1989]:
        population_value = df[df['Year'] == year]['Fertility Rate'].values[0]

        if year==1967:
            pos='top left'
        else:
            pos='top right'

        fig.add_trace(
            go.Scatter(x=df[df['Year'] == year]['Year'],
                       y=df[df['Year'] == year]['Fertility Rate'],
                       text=df[df['Year'] == year]['Fertility Rate'],
                       mode='markers+text',
                       showlegend=False,
                       marker=dict(size=8, color=color),
                       textfont=dict(family="Helvetica Neue", size=14, color=color),
                       textposition=pos,
                       )
        )

        if year == 1967:
            t = "<b>(1967)</b><br>Decree 770 <a href='https://en.wikipedia.org/wiki/Decree_770'>🔗</a>"
        else:
            t = "<b>(1989)</b><br>Trial and execution of Ceaucescu <a href='https://en.wikipedia.org/wiki/Trial_and_execution_of_Nicolae_and_Elena_Ceaușescu'>🔗</a>"

        fig.add_shape(
            type="line",
            x1=year,
            x0=year,
            y0=population_value,
            y1=4,
            line=dict(color="grey", width=1, dash="dash"),
        )

        fig.add_trace(
            go.Scatter(x=[year],
                       y=[4],
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
                       y=df['Fertility Rate'],
                       mode='lines',
                       showlegend=False,
                       line=dict(width=2, color=color),
                       )
        )
    else:
        fig.add_trace(
            go.Scatter(x=df['Year'],
                       y=df['Fertility Rate'],
                       mode='lines',
                       fill='tozeroy',
                       showlegend=False,
                       line=dict(width=2, color=color),
                       )
        )

    fig.update_layout(
        title=dict(
            text='Fertility rates soared in Romania forced by communist dictator Ceaucescu',
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Decree 770 was a law that banned contraception and abortion in Romania',
                xref="paper",
                yref="paper",
                x=-0.07, y=1.23,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text='Number of births per woman',
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
            range=[0, 4.4],

        ),
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=250, r=100, pad=0),
        height=800,
        width=1000,
    )

    return fig