import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def workforce_by_sector_subplots_bar_charts_plotly_express(df):
    df = df.sort_values(['sector', 'percentage'], ascending=False)

    fig = px.bar(
        df,
        x='country',
        y='percentage',
        color='sector',
        text='percentage',
        title='Distribution of workforce by country per sector (as a percentage)'
    )

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1550,
        barmode='group'
    )

    return fig

def workforce_by_sector_stacked_bar_chart(df):
    df = df.sort_values(['sector', 'percentage'], ascending=[True, True])

    fig = go.Figure()

    for sector in df['sector'].unique():
        aux_df = df[df['sector'] == sector].copy()

        fig.add_trace(
            go.Bar(
                x=aux_df['percentage'],
                y=aux_df['country'],
                orientation='h',
                name=sector,
                text=aux_df['percentage'],
                textposition='auto',
            )
        )

    fig.update_layout(
        barmode='stack',
        font=dict(family="Helvetica Neue", size=10),
        height=600,
        width=750,
        title=dict(
            text='Distribution of workforce by country per sector (as a percentage)',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        uniformtext_minsize=8, uniformtext_mode='hide'
    )

    return fig


def workforce_by_sector_subplots_bar_charts(df):
    list_of_categories = df['sector'].unique().tolist()
    list_of_categories.sort()

    fig = make_subplots(rows=1, cols=4, shared_yaxes=True,
                        subplot_titles=list_of_categories,
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
                marker=dict(color='darkblue'),
                text=aux_df['percentage'].round(0),
                textposition='auto',
                orientation='h',
                showlegend=False,
            ),
            row=1, col=row
        )

        # Update the layout for each subplot
        fig.update_xaxes(
            # range=[0, 100],
            visible=False,
            row=1,
            col=row
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
            text='Distribution of workforce by country per sector (as a percentage)',
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


