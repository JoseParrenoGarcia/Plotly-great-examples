import plotly.graph_objects as go
import plotly.express as px

def kids_before_marriage_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='year',
                 y='percentage',
                 markers=True,
                 title='Kids before marriage (%)')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def kids_before_marriage_line_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=df['year'],
                   y=df['percentage'],
                   text=df['percentage'].astype(str) + '%',
                   mode='lines+markers+text',
                   showlegend=False,
                   line=dict(width=5),
                   marker=dict(size=36),
                   textfont=dict(family="Helvetica Neue", size=13, color='white'),
                   textposition='middle center'
                   )
    )

    fig.update_layout(
        title=dict(
            text="Times have changed.",
            font=dict(family="Helvetica Neue", size=22),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='Less than 50% of people believe you need to be married before having kids.',
                xref="paper",
                yref="paper",
                x=-0.065, y=1.225,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text='% who agree that people who want children should get married',
                xref="paper",
                yref="paper",
                x=-0.065, y=1.10,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            # range=[df['election'].min(), df['election'].max() + 19],
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
        height=800,
        width=1000,
    )

    return fig