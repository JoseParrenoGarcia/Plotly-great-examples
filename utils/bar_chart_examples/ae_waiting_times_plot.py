import plotly.graph_objects as go

def AE_waiting_times_bar_chart_plot(df):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(x=df['text_col'],
               y=df['percentage_4_hours_or_less'],
               marker_color='darkblue',
               text=df['percentage_4_hours_or_less'],
               showlegend=False,
               textposition='outside',
            )
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Percentage of patients in A&E departments in England waiting 4 hours or less',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        font=dict(family="Helvetica Neue", size=10),
        yaxis=dict(title="",
                   range=[0, 100],
                   dtick=25,
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
        margin=dict(t=60, pad=0),
        height=450,
        width=750,
    )

    target = 95
    fig.add_hline(y=target, line_color="darkgrey", line_width=1, line_dash='dash',
                  annotation_text=f'Target - {target}%', annotation_position='top right',
                  annotation_font_size=14)

    return fig


def AE_waiting_times_dot_plot(df):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=df['text_col'],
                   y=df['percentage_4_hours_or_less'],
                   marker=dict(color='darkblue', size=10),
                   mode='lines+markers+text',
                   textposition='top center',
                   text=df['percentage_4_hours_or_less'],
                   showlegend=False,
                )
    )

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='Percentage of patients in A&E departments in England waiting 4 hours or less',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=18),
        ),
        font=dict(family="Helvetica Neue", size=10),
        yaxis=dict(title="",
                   range=[df['percentage_4_hours_or_less'].min() - 2, 100],
                   showline=True,
                   linecolor='lightgrey',
                   linewidth=1,
                   showgrid=False,
                   ),
        xaxis=dict(title="",
                   showline=False,
                   ),
        margin=dict(t=60, pad=0),
        height=450,
        width=750,
    )

    target = 95
    fig.add_hline(y=target, line_color="darkgrey", line_width=1, line_dash='dash',
                  annotation_text=f'Target - {target}%', annotation_position='top right',
                  annotation_font_size=14)

    return fig