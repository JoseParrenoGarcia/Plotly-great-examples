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
               text=[f'{obs / 1e3:,.0f}k' for obs in df['Observation']],
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
                        .groupby('language_group', as_index=False)
                        .agg({'Observation': 'sum'})
                        .assign(language_group_text=lambda x: x['language_group'].str.replace(' ', '<br>'))
                        .sort_values('Observation', ascending=False)
                        .reset_index())

    second_chart_data = (df
                         .query("language_group == 'All other languages'")
                         .query("observation_rank <= 10")
                         .sort_values(['Observation'], ascending=False))

    # Create the first bar chart
    fig = make_subplots(rows=1, cols=2, column_widths=[0.3, 0.7])

    fig.add_trace(
        go.Bar(
            x=first_chart_data['language_group_text'],
            y=first_chart_data['Observation'],
            name='main_languages',
            text=[f'{obs / 1e6:.0f}m' for obs in first_chart_data['Observation']],
            texttemplate='%{text}',
            textposition='outside',
            showlegend=False,
            marker_color=['rgb(52, 152, 219)' if lang == 'English' else 'rgb(115, 198, 182)' for lang in first_chart_data['language_group_text']],
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(
            x=second_chart_data['language'],
            y=second_chart_data['Observation'],
            name='other_languages',
            text=[f'{obs / 1e3:.0f}k' for obs in second_chart_data['Observation']],
            texttemplate='%{text}',
            textposition='outside',
            showlegend=False,
            marker_color='rgb(115, 198, 182)',
        ),
        row=1, col=2
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='English is still, of course, the main language in England',
            y=0.98,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        annotations=[
            # Second paragraph annotation
            dict(
                text="Nigels Farage statement that he heard no English spoken on a train journey is likely to be untrue",
                xref="paper", yref="paper",
                x=-0.03, y=1.25,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
        ],
        font=dict(family="Helvetica Neue", size=12),
        yaxis1=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        yaxis2=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        xaxis1=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        xaxis2=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        margin=dict(t=100, pad=0),
        height=450,
        width=800,
    )

    return fig
