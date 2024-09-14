import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def progress_against_target_bar_chart(df):
    progress_order = ['Above target', 'On target', 'Below target']
    df['category'] = pd.Categorical(df['category'], categories=progress_order, ordered=True)
    df = df.sort_values(by=['category', 'progress'], ascending=[True, True])
    category = df['category'].unique()

    # Create subplots
    fig = make_subplots(
        rows=len(category),
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.02
    )

    for i, category in enumerate(category):
        category_df = df[df['category'] == category]
        fig.add_trace(
            go.Bar(
                x=category_df['progress'],
                y=category_df['department'],
                orientation='h',
                text=category_df['progress'],
                textposition='inside',
                textangle=0,
                textfont=dict(color='black'),
                marker_color='lightgrey',
            ),
            row=i + 1,
            col=1
        )

        # Update the layout
        fig.update_layout(
            # title='Smoking Rates by Country and Continent',
            title=dict(text='xxxx',
                       y=0.98,
                       x=0,
                       xanchor='left',
                       yanchor='top',
                       font=dict(family="Helvetica Neue", size=18),
                       ),
            font=dict(family="Helvetica Neue"),
            showlegend=False,
            height=75 * len(category),  # Adjust height based on the number of continents
            width=600,
            margin=dict(l=250),
        )

        for i in range(len(category)):
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

            return fig