import plotly.graph_objects as go
from plotly.subplots import make_subplots

def food_exports_subplots_bar_charts(df):
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


