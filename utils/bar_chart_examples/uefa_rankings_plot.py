import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

def uefa_ranking_slope_chart_plotly_express(df):
    df = df.sort_values(['season', 'ranking'], ascending=True)

    fig = px.bar(
        df,
        x='club',
        y='ranking',
        color='season',
        text='ranking',
        title='How Peter Lim destroyed a historical club'
    )

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1550,
        barmode='group'
    )

    return fig


def uefa_ranking_slope_chart(df):
    # Add dummy categories for spacing
    season_order=['2012-13', '2013-14', '2023-24', '2024-25']
    df = df[['club', 'season', 'ranking', 'text_column']].copy()
    dummy_before = pd.DataFrame({'club': [''], 'season': ['2012-13'], 'ranking': [None], 'text_column': ['']})
    dummy_after = pd.DataFrame({'club': [''], 'season': ['2024-25'], 'ranking': [None], 'text_column': ['']})
    df = pd.concat([dummy_before, df, dummy_after], ignore_index=True)
    df['season'] = pd.Categorical(df['season'], categories=season_order, ordered=True)

    df['text_column'] = df.apply(
        lambda x: '' if x['season'] == '2023-24' and x['club'] == 'Sevilla' else x['text_column'],
        axis=1
    )
    df['text_column'] = df.apply(
        lambda x: '' if x['season'] == '2013-14' and x['club'] == 'Barcelona' else x['text_column'],
        axis=1
    )
    df['text_column'] = df.apply(
        lambda x: '' if x['season'] == '2013-14' and x['club'] == 'Atleti' else x['text_column'],
        axis=1
    )


    fig = go.Figure()

    # Iterate over each club
    for club in df['club'].unique():
        club_data = df[df['club'] == club]

        if club == 'Valencia':
            color = 'orange'
            line_width = 4
            marker_size = 8
            colour_ = color
        else:
            color = 'lightgrey'
            line_width = 2
            marker_size = 6
            colour_ = 'grey'

        fig.add_trace(go.Scatter(
            x=club_data['season'],
            y=club_data['ranking'],
            mode='lines+markers+text',
            name=club,
            text=club_data['text_column'],
            textposition=['middle left' if season == '2013-14' else 'middle right' for season in club_data['season']],
            textfont=dict(color=colour_),
            marker=dict(color=color, size=marker_size),
            line=dict(color=color, width=line_width)
        ))

    # Update the overall layout
    fig.update_layout(
        title=dict(
            text='How Peter Lim destroyed a historical club',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            dict(
                text="Valencia CF went from 8th to 94th in the world in a space of 10 years.",
                xref="paper",
                yref="paper",
                x=0, y=1.09,
                showarrow=False,
                font=dict(size=14),
                align="left"
            ),
            dict(
                text="Uefa rankings for season 2013-14 and 2023-24",
                xref="paper",
                yref="paper",
                x=0, y=1.02,
                showarrow=False,
                align="left"
            ),
        ],
        yaxis=dict(visible=False,
                   showgrid=False,
                   ),
        xaxis=dict(visible=False,
                   categoryorder='array',
                   categoryarray=season_order,
                   ),
        font=dict(family="Helvetica Neue", size=12),
        yaxis_autorange='reversed',  # Rankings are usually better when lower
        showlegend=False,
        margin=dict(t=120, pad=0),
        height=800,
        width=700,
    )

    return fig
