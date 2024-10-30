import plotly.graph_objects as go
import numpy as np

def replace_spaces_with_br(text):
    return text.replace(' ', '<br>')

def mountain_bar_chart_plot(df):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(x=df['Name'],
               y=df['starting_point'],
               marker_color='darkblue',
               text=df['text_for_starting_point'],
               textposition='outside',
               showlegend=False,
            )
    )

    df_aux = df.query("height_sea_level > 0")
    fig.add_trace(
        go.Bar(x=df_aux['Name'],
               y=df_aux['total_height'],
               marker_color='darkblue',
               text=df['total_height'].astype(str) + 'km',
               showlegend=False,
               textposition='inside',
               )
    )

    df['wrapped_name'] = df['Name'].apply(replace_spaces_with_br)
    df['position_of_y_name'] = np.where((df['height_sea_level'] > 0) & (df['diff_sea_level_height'] < 0),
                                        df['height_sea_level'] + 1.5,
                                        np.where((df['height_sea_level'] > 0) & (df['diff_sea_level_height'] == 0), -1.5, 1.5)
                                        )
    fig.add_trace(
        go.Scatter(
            x=df['Name'],
            y=df['position_of_y_name'],
            # y=[df['height_sea_level'] if height > 0 else 1.5 for height in df['total_height']],
            mode='text',
            text=df['wrapped_name'],
            textposition='middle center',
            showlegend=False,
            hoverinfo='skip'
        )
    )

    mauna_kea_starting_point = df.loc[df['Name'] == 'Mauna Kea', 'starting_point'].values[0]
    mauna_kea_text = df.loc[df['Name'] == 'Mauna Kea', 'text_for_starting_point'].values[0]

    # Customize the layout
    fig.update_layout(
        title=dict(
            text='The biggest natural structures on Earth',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Below sea-level there is much more to be discovered",
                xref="paper",
                yref="paper",
                x=0, y=1.25,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=18),
                align="left"
            ),
            dict(
                text="Total height and position measured from sea level",
                xref="paper",
                yref="paper",
                x=0, y=1.1,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
            dict(
                x='Mauna Kea',
                y=mauna_kea_starting_point - 0.5,
                text=mauna_kea_text,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=10),
                align="center"
            ),
        ],
        font=dict(family="Helvetica Neue", size=10),
        yaxis=dict(title="",
                   visible=False,
                   ),
        xaxis=dict(title="",
                   visible=False,
                   ),
        margin=dict(t=150, pad=0),
        height=600,
        width=750,
        barmode='stack',
    )

    fig.add_hline(y=0, line_color="lightgrey", line_width=2)
    fig.add_hline(y=df['height_sea_level'].min(), line_color="lightgrey", line_width=1, line_dash='dash',
                  annotation_text='Lowest point below sea level', annotation_position='bottom left')
    fig.add_hline(y=df['height_sea_level'].max(), line_color="lightgrey", line_width=1, line_dash='dash',
                  annotation_text='Highest point above sea level', annotation_position='top left'
                  )

    fig.add_annotation(
        x='Puerto Rico Trench',
        y=5.5,  # Slightly above the y-value
        text='<b><i>Mauna Kea</i></b> is actually<br>the highest natural<br>structure on Earth<br>with 10.2km',
        xref="x",
        yref="y",
        showarrow=False,
        borderpad=10,
        font=dict(family="Helvetica Neue", size=10),
        align='center',
    )

    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0='Java Trench',
        y0=3.8,
        x1='Tonga Trench',
        y1=7.2,
        fillcolor="lightgrey",
        opacity=0.5,
        layer="below",
        line_width=0,
    )

    return fig
