import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

def progress_against_target_bar_chart_basic(df, sort_by='category'):
    color_mapping = {
        'Above target': 'green',
        'On target': 'gold',
        'Below target': 'red',
    }
    df['color'] = df['category'].map(color_mapping)

    df = df.sort_values(by=['progress'], ascending=[True])


    if sort_by== 'category':
        fig = px.bar(df,
                     x='progress',
                     y='department',
                     orientation='h',
                     color='category',
                     color_discrete_map=color_mapping
                     )

    else:
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=df['progress'],
            y=df['department'],
            orientation='h',
            marker_color=df['color'],
            showlegend=False,
        ))

        for category, color in color_mapping.items():
            fig.add_trace(go.Scatter(
                x=[None], y=[None],
                mode='markers',
                marker=dict(size=10, color=color),
                legendgroup=category,
                showlegend=True,
                name=category
            ))

    fig.update_layout(
        title='Progress against target',
        height=550,
        width=600,
    )

    return fig

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

        if category == 'Above target':
            color_ = 'rgb(72, 201, 176)'
        elif category == 'On target':
            color_ = 'rgb(244, 208, 63)'
        else:
            color_ = 'rgb(236, 112, 99)'

        fig.add_trace(
            go.Bar(
                x=category_df['progress'],
                y=category_df['department'],
                orientation='h',
                marker_color=color_,
                showlegend=False,
            ),
            row=i + 1,
            col=1
        )

        # Add scatter trace for target values
        fig.add_trace(
            go.Scatter(
                x=category_df['target'],
                y=category_df['department'],
                mode='markers',
                marker=dict(line_color='grey', line_width=2, symbol='line-ns', size=15,),
                showlegend=True if i == 0 else False,
                name='Yearly target',
            ),
            row=i + 1,
            col=1
        )

        # Add scatter trace for text values
        category_df['text'] = category_df.apply(
            lambda x: f"<span style='color: {color_};'>{x['progress']}</span> vs {x['target']}",
            axis=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=[100] * len(category_df),
                y=category_df['department'],
                mode='text',
                text=category_df['text'],
                textposition='middle right',
                showlegend=False,
            ),
            row=i + 1,
            col=1
        )

        fig.add_annotation(
            xref='paper',
            yref='y' + str(i + 1),
            xanchor='right',
            x=-0.3,  # Position to the left of the plot
            y=category_df['category'].iloc[len(category_df) // 2],  # Centered vertically
            text=category,
            showarrow=False,
            font=dict(size=12)
        )

    # Update the layout
    fig.update_layout(
        title=dict(text='Progress against target',
                   y=0.98,
                   x=0,
                   xanchor='left',
                   yanchor='top',
                   font=dict(family="Helvetica Neue", size=18),
                   ),
        font=dict(family="Helvetica Neue"),
        showlegend=True,
        legend=dict(
            orientation='h',
            x=0,
            y=-0.05,
            xanchor='right',
            yanchor='top',
            font=dict(color='grey')
        ),
        height=50 * len(category),  # Adjust height based on the number of continents
        width=800,
        margin=dict(l=250),
    )

    fig.add_annotation(
        xref='paper',
        yref='paper',
        xanchor='left',
        x=-0.45,
        y=1.095,
        text='10 of 15 departments are close to achieving or above their yearly targets. 5 are struggling.',
        showarrow=False,
        font=dict(family="Helvetica Neue", size=14),
        align='left',
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
            range=[0, 140],
            row=i + 1,
            col=1
        )

    return fig