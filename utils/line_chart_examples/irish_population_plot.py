import plotly.graph_objects as go
import plotly.express as px

def irish_population_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='Population',
                 markers=True,
                 title='Evoution of the Irish population')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def irish_population_line_chart(df):

    color='rgb(255,136,62)'

    fig = go.Figure()

    for year in [1845, 1972]:
        population_value = df[df['Year'] == year]['Population'].values[0]

        fig.add_trace(
            go.Scatter(x=df[df['Year'] == year]['Year'],
                       y=df[df['Year'] == year]['Population'],
                       text=df[df['Year'] == year]['Population'].astype(str) + 'm',
                       mode='markers+text',
                       showlegend=False,
                       marker=dict(size=8, color=color),
                       textfont=dict(family="Helvetica Neue", size=14, color=color),
                       textposition='top center',
                       )
        )

        if year == 1845:
            t = "   <b>(1845 - 1852)</b><br>   The great famine <a href='https://en.wikipedia.org/wiki/Great_Famine_(Ireland)'>🔗</a>"
        else:
            t = "   <b>(1972)</b><br>   Ireland joins the EU <a href='https://ireland.representation.ec.europa.eu/about-us/irelands-eu-membership_en#:~:text=in%20the%20EU-,Ireland%20in%20the%20EU,referendum%20held%20on%2010%20May.'>🔗</a>"

        fig.add_shape(
            type="line",
            x1=year,
            x0=year,
            y0=2,
            y1=population_value,
            line=dict(color="grey", width=1, dash="dash"),
        )

        fig.add_trace(
            go.Scatter(x=[year],
                       y=[2],
                       text=[t],
                       mode='text',
                       showlegend=False,
                       textfont=dict(family="Helvetica Neue", size=14, color='grey'),
                       textposition='middle right',
                       )
        )


    fig.add_trace(
        go.Scatter(x=df['Year'],
                   y=df['Population'],
                   mode='lines',
                   showlegend=False,
                   line=dict(width=2, color=color),
                   )
    )

    fig.update_layout(
        title=dict(
            text="The Great Famine had a huge impact on the Irish population",
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Irelands population dropped by half in the 1840s, and has yet to recover more than 100 years later.',
                xref="paper",
                yref="paper",
                x=-0.06, y=1.23,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text='Population of Ireland (millions)',
                xref="paper",
                yref="paper",
                x=-0.06, y=1.08,
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
            range=[0, df['Population'].max() * 1.1],

        ),
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=250, r=100, pad=0),
        height=800,
        width=1000,
    )

    return fig