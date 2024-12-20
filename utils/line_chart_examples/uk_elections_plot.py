import plotly.graph_objects as go
import plotly.express as px

def uk_elections_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='election',
                 y='votes',
                 color='party',
                 markers=True,
                 title='UK elections')

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig


def uk_elections_line_chart(df):

    fig = go.Figure()

    for party in df['party'].unique():

        if (party == 'Labour') or (party == 'Lib. dems.'):
            line_size = 3
        else:
            line_size = 2

        fig.add_trace(
            go.Scatter(x=df[df['party'] == party]['election'],
                       y=df[df['party'] == party]['votes'],
                       mode='lines+markers',
                       name=party,
                       showlegend=False,
                       line=dict(color=df[df['party'] == party]['color'].values[0], width=line_size),
                       marker=dict(color=df[df['party'] == party]['color'].values[0], size=line_size * 2),
                       )
        )

        fig.add_trace(
            go.Scatter(x=df[(df['party'] == party) & (df['election'] == df['election'].max())]['election'],
                       y=df[(df['party'] == party) & (df['election'] == df['election'].max())]['votes'],
                       mode='markers+text',
                       name=party,
                       showlegend=False,
                       marker=dict(color=df[df['party'] == party]['color'].values[0], size=line_size * 2),
                       text=party,
                       textposition='middle right',
                       textfont=dict(family="Helvetica Neue", color=df[df['party'] == party]['color'].values[0], size=12),
                       )
        )

    fig.update_layout(
        title=dict(
            text="Labour vs Liberal votes",
            font=dict(family="Helvetica Neue", size=20),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text='<b><span style="color:rgba(203, 67, 53, 1);">Labour</span></b> and <b><span style="color:rgba(240, 178, 122, 1);">Liberal</span></b> vote is mirrored. Both parties fight for the same voters.',
                xref="paper",
                yref="paper",
                x=-0.13, y=1.4,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=16),
                align="left"
            ),
            dict(
                text='Number of votes in each election.',
                xref="paper",
                yref="paper",
                x=-0.13, y=1.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=13),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['election'].min(), df['election'].max() + 19],
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
        height=600,
        width=700,
    )

    return fig
