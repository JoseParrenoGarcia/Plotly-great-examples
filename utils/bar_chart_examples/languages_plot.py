import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def languages_bar_chart_plot(df):
    df = df.query("observation_rank <= 10").copy()

    fig = go.Figure()

    fig.add_trace(
        go.Bar(x=df['language'],
               y=df['Observation'],
               marker_color='darkblue',
               showlegend=False,
            )
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Top 10 languages spoken in England',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="English is still the main language, spoken by 92% of the population",
                xref="paper",
                yref="paper",
                x=-0.085, y=1.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
        ],
        font=dict(family="Helvetica Neue", size=10),
        yaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=1,
                   showgrid=False,
                   ),
        xaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=1,
                   ),
        margin=dict(t=100, pad=0),
        height=450,
        width=750,
    )

    return fig

def languages_stacked_bar_chart(df):
    first_chart_data = (df
                        .groupby('language_group')
                        .agg({'Observation': 'sum'})
                        .sort_values('Observation', ascending=False)
                        .reset_index())

    second_chart_data = (df
                         .query("language_group == 'All other languages'")
                         .sort_values('Observation', ascending=False))

    # Create the first bar chart
    fig = make_subplots(rows=1, cols=2)

    fig.add_trace(
        go.Bar(
            x=first_chart_data['language_group'],
            y=first_chart_data['Observation'],
            name='main_languages',
            # text=[f'{obs / 1e6:.0f}m' for obs in first_chart_data['Observation']],
            # texttemplate='%{text}',
            # textposition='inside',
            showlegend=False,
            # marker_color=['darkblue' if main_languages == 'English' else 'green'],
            marker_line=dict(color='black', width=1),
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(
            x=second_chart_data['language'],
            y=second_chart_data['Observation'],
            name='other_languages',
            # text=[f'{obs / 1e6:.0f}m' for obs in first_chart_data['Observation']],
            # texttemplate='%{text}',
            # textposition='inside',
            showlegend=False,
            # marker_color=['darkblue' if main_languages == 'English' else 'green'],
            marker_line=dict(color='black', width=1),
        ),
        row=1, col=2
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Languages Spoken in England',
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        # barmode='stack',
        font=dict(family="Helvetica Neue", size=10),
        # yaxis1=dict(visible=False),
        # xaxis1=dict(visible=False),
        # yaxis2=dict(visible=False),
        # xaxis2=dict(visible=False),
        margin=dict(t=100, pad=0),
        height=450,
        width=750,
    )

    return fig
