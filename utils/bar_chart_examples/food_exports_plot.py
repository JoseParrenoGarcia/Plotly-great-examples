import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def food_exports_subplots_dot_charts_plotly_express(df, colour='Food'):
    if colour=='Food':
        df = df.sort_values('Food', ascending=False)
        x_ = 'Country'
    else:
        df = df.sort_values('Country', ascending = False)
        x_ = 'Food'

    fig = px.bar(
        df,
        x=x_,
        y='percentage',
        color=colour,
        title='How the Netherlands feeds the world'
    )

    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=750,
        barmode='group'
    )

    return fig

def food_exports_subplots_dot_charts(df):
    list_of_categories = df['Food'].unique().tolist()
    list_of_categories.sort()

    food_to_emoji = {
        'Cucumbers': '🥒',
        'Eggs': '🥚',
        'Mushrooms': '🍄',
        'Onions': '🧅',
        'Peppers': '🌶️',
        'Potatoes': '🥔',
        'Tomatoes': '🍅'
    }

    subplot_titles = [f"{category} {food_to_emoji.get(category, '')}" for category in list_of_categories]

    fig = make_subplots(rows=1, cols=7, shared_yaxes=True,
                        subplot_titles=subplot_titles
                        )

    for i, feature in enumerate(list_of_categories):
        row = i + 1

        if row == 1:
            aux_df = df[df['Food'] == feature].sort_values('percentage', ascending=False).copy()
        else:
            aux_df = df[df['Food'] == feature].copy()


        # Add bar chart to the subplot

        fig.add_trace(
            go.Scatter(
                y=aux_df['Country'],
                x=[1] * len(aux_df),
                mode='markers+text',
                text=[f"{val}%" for val in aux_df['percentage'].round(0)],
                textposition=['top center' if val < 10 else 'middle center' for val in aux_df['percentage']],
                textfont=dict(color=['grey' if val < 10 else 'white' for val in aux_df['percentage']]),
                marker=dict(size=aux_df['percentage']*3,
                            color=['rgb(0, 61, 165)' if country == 'Netherlands 🇳🇱' else 'darkgrey' for country in aux_df['Country']]),
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
            showline=False,
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
            text='How the Netherlands feeds the world',
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


def food_exports_stacked_bar_chart(df):
    df = df.sort_values(['Food', 'percentage'], ascending=[True, True])

    fig = go.Figure()

    for Food in df['Food'].unique():
        aux_df = df[df['Food'] == Food].copy()

        fig.add_trace(
            go.Bar(
                x=aux_df['percentage'],
                y=aux_df['Country'],
                orientation='h',
                name=Food,
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
            text='How the Netherlands feeds the world',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        uniformtext_minsize=8, uniformtext_mode='hide'
    )

    return fig

def food_exports_stacked_bar_chart2(df):
    df = df.sort_values(['Country', 'percentage'], ascending=[True, True])

    fig = go.Figure()

    for Country in df['Country'].unique():
        aux_df = df[df['Country'] == Country].copy()

        fig.add_trace(
            go.Bar(
                x=aux_df['percentage'],
                y=aux_df['Food'],
                orientation='h',
                name=Country,
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
            text='How the Netherlands feeds the world',
            y=0.95,
            x=0,
            xanchor='left',
            yanchor='top',
            font=dict(family="Helvetica Neue", size=24),
        ),
        uniformtext_minsize=8, uniformtext_mode='hide'
    )

    return fig