import plotly.graph_objects as go

def sex_ratio_at_birth_bar_chart_plot(df):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(x=df['Entity'],
               y=df['ratio'],
               marker_color='darkblue',
               text=df['ratio'],
               showlegend=False,
            )
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Number of male born babies for every 100 female babies',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        font=dict(family="Helvetica Neue", size=10),
        yaxis=dict(title="",
                   visible=False,
                   ),
        xaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=3,
                   ),
        margin=dict(t=60, pad=0),
        height=450,
        width=750,
    )

    hist_avg = df['ratio_avg'].min().round(0)
    fig.add_hline(y=hist_avg, line_color="darkgrey", line_width=1, line_dash='dash',
                  annotation_text=f'Historical average - {hist_avg}', annotation_position='top right',
                  annotation_font_size=14)

    return fig


def sex_ratio_at_birth_dot_plot(df):
    df = df.sort_values('ratio_rank', ascending=False).copy()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=df['ratio'],
                   y=df['Entity_text'],
                   mode='markers+text',
                   marker=dict(color='darkblue', size=18),
                   text=df['ratio'],
                   textposition='middle right',
                   showlegend=False,
                   )
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Number of male born babies for every 100 female babies',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        font=dict(family="Helvetica Neue", size=10),
        yaxis=dict(title="",
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=3,
                   ),
        xaxis=dict(title="",
                   visible=False,
                   ),
        margin=dict(t=60, pad=0),
        height=450,
        width=750,
    )

    hist_avg = df['ratio_avg'].min().round(0)
    fig.add_vline(x=hist_avg, line_color="darkgrey", line_width=1, line_dash='dash',
                  annotation_text=f'   Historical average - {str(hist_avg)}', annotation_position='top right',)

    return fig

def sex_ratio_at_birth_bar_deviation_plot(df):
    return df
