import plotly.graph_objects as go
from plotly.subplots import make_subplots

def workforce_by_sector_subplots_bar_charts(df):
    list_of_categories = df['sector'].unique().tolist()
    list_of_categories.sort()

    fig = make_subplots(rows=1, cols=4, shared_yaxes=True,
                        subplot_titles=list_of_categories
                        )

    for i, feature in enumerate(list_of_categories):
        row = i + 1

        if row == 1:
            aux_df = df[df['sector'] == feature].sort_values('percentage').copy()
        else:
            aux_df = df[df['sector'] == feature].copy()


        # Add bar chart to the subplot
        fig.add_trace(
            go.Bar(
                y=aux_df['country'],
                x=aux_df['percentage'],
                text=aux_df['percentage'].round(0),
                textposition='auto',
                orientation='h',
                showlegend=False,
            ),
            row=1, col=row
        )

        # Update the layout for each subplot
        fig.update_xaxes(
            visible=False,
            row=1, col=row
        )
        fig.update_yaxes(
            title_text='',
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            showgrid=False,
            tickfont=dict(weight='bold'),
            row=1, col=row
        )

    # Adjust the y position of the subplot titles
    for annotation in fig['layout']['annotations']:
        annotation['y'] = annotation['y'] + 0.05  # Adjust this value as needed

    # Update the overall layout
    fig.update_layout(
        title=dict(
            text='Distribution of workforce by country per sector (as a percentange)',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        font=dict(family="Helvetica Neue", size=10),
        barmode='group',
        margin=dict(t=120, pad=0),
        height=500,
        width=1200,
    )

    return fig


