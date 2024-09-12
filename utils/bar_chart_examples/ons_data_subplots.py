import plotly.graph_objects as go
from plotly.subplots import make_subplots

def ons_data_subplots_bar_charts(ons_data_df):
    column_rename_mapping = {
        'GDP per capita': 'GDP_per_capita',
        'Annual CO₂ emissions (per capita)': 'CO2_emissions_per_capita',
        'Under-five mortality rate': 'Child_mortality',
        'Nitrogen oxide (NOx)': 'Air_pollution_NOx',
        'Domestic general government health expenditure (GGHE-D) as percentage of general government expenditure (GGE) (%)': 'Gov_health_expenditure',
        '$2.15 a day - Share of population in poverty': 'Population_in_poverty'
    }

    ons_data_df = (ons_data_df.rename(columns=column_rename_mapping))
    columns_to_fill = ['GDP_per_capita', 'CO2_emissions_per_capita', 'Child_mortality', 'Air_pollution_NOx', 'Gov_health_expenditure', 'Population_in_poverty']
    ons_data_df[columns_to_fill] = ons_data_df[columns_to_fill].fillna(0)

    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=[
            'GDP per capita',
            'Gov. health expenditure (as % of total)',
            'Child mortality rate',
            'Population in extreme poverty (<$2.15 p/day)',
            'CO2 Emissions (per capita)',
            'Air pollution (NOx)',
        ], vertical_spacing=0.1)

    features = [
        'GDP_per_capita',
        'Gov_health_expenditure',
        'Child_mortality',
        'Population_in_poverty',
        'CO2_emissions_per_capita',
        'Air_pollution_NOx',
    ]

    for i, feature in enumerate(features):
        row = i // 2 + 1
        col = i % 2 + 1

        print(f'{feature}: {row}x{col}')

        # Sort the DataFrame by the current feature
        zero_value_entities = ons_data_df[ons_data_df[feature] == 0]['Entity'].tolist()
        print(zero_value_entities)
        print('')
        sorted_df = ons_data_df[ons_data_df[feature] > 0].sort_values(by=feature, ascending=True).copy()

        # Define bar colors
        marker_color_ = ['rgba(85, 181, 229, 1)' if c_ == 'Uruguay' else 'lightgrey' for c_ in sorted_df['Entity']]

        if feature == 'GDP_per_capita':
            text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(sorted_df[feature], sorted_df['Entity'])]
        elif feature == 'Air_pollution_NOx':
            text_ = [f"<b>{val / 1000:,.1f}k</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(sorted_df[feature], sorted_df['Entity'])]
        elif feature in ['Child_mortality', 'CO2_emissions_per_capita']:
            text_ = [f"<b>{val:.2f}</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(sorted_df[feature], sorted_df['Entity'])]
        elif feature in ['Gov_health_expenditure', 'Population_in_poverty']:
            text_ = [f"<b>{val:.2f}%</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(sorted_df[feature], sorted_df['Entity'])]
        else:
            text_ = ['' for _ in sorted_df['Entity']]

        if feature == 'Gov_health_expenditure':
            range_ = [0, 26]
        else:
            range_ = [None, None]

        # Add bar chart to the subplot
        fig.add_trace(
            go.Bar(
                y=sorted_df['Entity'],
                x=sorted_df[feature],
                marker_color=marker_color_,
                orientation='h',
                text=text_,
                textposition='outside',
                showlegend=False,
            ),
            row=row, col=col
        )

        # Update the font, size, and alignment of the subplot titles
        for annotation in fig['layout']['annotations']:
            annotation['font'] = dict(family="Helvetica Neue", size=14)

        # Update the layout for each subplot
        fig.update_xaxes(
            title_text='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            row=row, col=col,
            range=range_,
        )
        fig.update_yaxes(
            title_text='',
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            showgrid=False,
            row=row, col=col
        )

    # Update the overall layout
    fig.update_layout(
        title=dict(
            text="Uruguay is one of the most succesful countries in South America",
            font=dict(family="Helvetica Neue", size=24)  # Change font family and size here
        ),
        font=dict(family="Helvetica Neue"),
        barmode='group',
        margin=dict(t=100, pad=0),
        height=1000,
        width=800,
    )

    fig.add_annotation(
        text = "Source: World Bank, <a href='https://ourworldindata.org'>Our World in Data</a>",
        xref="paper", yref="paper",
        x=0, y=-0.07,
        showarrow=False,
        font=dict(family="Helvetica Neue", size=12, color="grey"),
        align='left',

    )

    return fig