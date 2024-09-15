import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def smoking_rates_plot(df):
    continent_order = ['Asia', 'Oceania', 'Africa', 'Europe', 'South America', 'North America']
    df['continent'] = pd.Categorical(df['continent'], categories=continent_order, ordered=True)
    df = df.sort_values(by=['continent', 'smoking_rate'], ascending=[True, True])
    continents = df['continent'].unique()

    # Create subplots
    fig = make_subplots(
        rows=len(continents),
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.02
    )

    # Add bars for each continent
    for i, continent in enumerate(continents):
        continent_df = df[df['continent'] == continent]
        fig.add_trace(
            go.Bar(
                x=continent_df['smoking_rate'],
                y=continent_df['country'],
                orientation='h',
                text=continent_df['smoking_rate'],
                textposition='inside',
                textangle=0,
                textfont=dict(color='black'),
                marker_color='lightgrey',
            ),
            row=i + 1,
            col=1
        )

        fig.add_annotation(
            xref='paper',
            yref='y' + str(i + 1),
            xanchor='right',
            x=-0.45,  # Position to the left of the plot
            y=continent_df['country'].iloc[len(continent_df) // 2],  # Centered vertically
            text=continent,
            showarrow=False,
            font=dict(size=12)
        )

    # Update the layout
    fig.update_layout(
        # title='Smoking Rates by Country and Continent',
        title=dict(text='Smoking still sticks around',
                   y=0.98,
                   x=0,
                   xanchor='left',
                   yanchor='top',
                   font=dict(family="Helvetica Neue", size=18),
                   ),
        font=dict(family="Helvetica Neue"),
        showlegend=False,
        height=150 * len(continents),  # Adjust height based on the number of continents
        width=600,
        margin=dict(l=250),
    )

    for i in range(len(continents)):
        fig.update_yaxes(
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            ticklabelposition='outside',
            ticklen=7,
            tickcolor='white',
            row=i + 1,
            col=1
        )

        fig.update_xaxes(
            showticklabels=False,
            showline=False,
            zeroline=False,
            row=i + 1,
            col=1
        )

    fig.add_annotation(
        xref='paper',
        yref='paper',
        xanchor='left',
        x=-0.70,
        y=1.065,
        text='% of smoking population in the top 5 most populated countries by continent',
        showarrow=False,
        font=dict(family="Helvetica Neue", size=14),
        align='left',
    )

    fig.add_annotation(
        xref='paper',
        yref='paper',
        xanchor='left',
        x=-0.45,
        y=-0.05,
        text="Source: World Bank, <a href='https://ourworldindata.org'>Our World in Data</a>",
        showarrow=False,
        font=dict(family="Helvetica Neue", size=12),
        align='left',
    )

    return fig