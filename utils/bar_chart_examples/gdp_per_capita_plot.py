import plotly.graph_objects as go
import pandas as pd
import numpy as np

def gdp_per_capita_bar_chart_plot(df, highlight='Uruguay'):
    df = df.sort_values('GDP per capita', ascending=True)

    if highlight=='Uruguay':
        marker_color_ = ['rgba(85, 181, 229, 1)' if c_ == 'Uruguay' else 'lightgrey' for c_ in df['Entity']]
        text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(df['GDP per capita'], df['Entity'])]
        pattern_shape_ = ['' for _ in df['Entity']]
        title_text = 'Uruguay flies high'
        subtitle_text = "Uruguay's GDP per capita is amongst the highest in South America (2020)"

    elif highlight=='min':
        marker_color_ = ['rgba(239, 51, 64, 1)' if c_ == df['Entity'].iloc[0] else 'lightgrey' for c_ in df['Entity']]
        text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == df['Entity'].iloc[0] else '' for val, c_ in zip(df['GDP per capita'], df['Entity'])]
        pattern_shape_ = ['' for _ in df['Entity']]
        title_text = 'Venezuela hits rock bottom'
        subtitle_text = "The country with the lowest GDP per capita in South America (2020)"

    elif highlight == 'median':
        median_ = df['GDP per capita'].median()
        uruguay_gdp = df.loc[df['Entity'] == 'Uruguay', 'GDP per capita'].values[0]
        diff = uruguay_gdp - median_
        perct_diff = diff / median_

        median_row = pd.DataFrame({
            'Entity': ['Median'],
            'GDP per capita': [median_]
        })

        df = pd.concat([df, median_row], ignore_index=True).sort_values('GDP per capita', ascending=True)

        marker_color_ = [
            'darkgrey' if c_ == 'Median' else
            'rgba(85, 181, 229, 1)' if c_ == 'Uruguay' else
            'lightgrey'
            for c_ in df['Entity']
        ]

        text_ = [
            f"<b>${val / 1000:,.1f}k</b>" if c_ in ['Median', 'Uruguay'] else ''
            for val, c_ in zip(df['GDP per capita'], df['Entity'])
        ]

        pattern_shape_ = ['' for _ in df['Entity']]

        title_text = f'Uruguay is {np.round(100*perct_diff, 0)}% above the median'
        subtitle_text = f"This is a difference of ${diff/1000:,.1f}k"

    elif highlight == 'data_issue':
        marker_color_ = ['rgba(85, 181, 229, 1)' if c_ == 'Paraguay' else 'lightgrey' for c_ in df['Entity']]
        pattern_shape_ = ['/' if c_ == 'Paraguay' else '' for c_ in df['Entity']]
        text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == 'Paraguay' else '' for val, c_ in zip(df['GDP per capita'], df['Entity'])]
        title_text = 'Data Quality Issue'
        subtitle_text = "Paraguay's data has a quality issue (2020)"

    else:
        marker_color_ = ['lightgrey' for _ in df['Entity']]
        pattern_shape_ = ['' for _ in df['Entity']]
        text_ = ['' for _ in df['Entity']]
        title_text = ''
        subtitle_text = ''


    fig = go.Figure(
        data=[
            go.Bar(
                y=df['Entity'],
                x=df['GDP per capita'],
                marker_color=marker_color_,
                marker_pattern_shape=pattern_shape_ if highlight == 'data_issue' else None,
                orientation='h',
                text=text_,
                textposition='outside',
                showlegend=False,
            )
        ]
    )

    # Update the layout
    fig.update_layout(
        title=dict(
            text=title_text,
            y=0.98,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        annotations=[
            # Second paragraph annotation
            dict(
                text=subtitle_text,
                xref="paper", yref="paper",
                x=0, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            # Footer annotation
            dict(
                text="Source: World Bank, <a href='https://ourworldindata.org'>Our World in Data</a>",
                xref="paper", yref="paper",
                x=0, y=-0.15,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=12),
                align="left"
            ),
        ],
        xaxis=dict(
            title='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
        ),
        yaxis=dict(
            title='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
        ),
        legend=dict(
            x=1,
            y=0,
            xanchor='right',
            yanchor='bottom',
            orientation='h'
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=100, pad=0),
        height=500,
        width=600,
    )

    if highlight == 'median':
        fig.add_vline(x=median_, line_dash='dot', line_color='darkgrey', line_width=1,
                  annotation_text='Median GDP per capita', annotation_position='bottom right',
                      layer='below')

    # Add custom legend item for the filled pattern
    if highlight == 'data_issue':
        fig.add_trace(go.Scatter(
            x=[None], y=[None],
            mode='markers',
            marker=dict(
                size=10,
                symbol='square',
                color='rgba(85, 181, 229, 1)',
            ),
            legendgroup='Data Quality Issue',
            showlegend=True,
            name='Data Quality Issue'
        ))

    return fig




