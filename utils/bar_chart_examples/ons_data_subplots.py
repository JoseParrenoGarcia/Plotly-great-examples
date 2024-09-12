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

    fig = make_subplots(rows=3, cols=2,
                        subplot_titles=(
                            'GDP per Capita',
                            'CO2 Emissions per Capita',
                            'Child Mortality',
                            'Air Pollution (Nitrogen oxide (NOx))',
                            'Gov Health Expenditure',
                            'Population in Extreme Poverty')
                        )

    features = [
        'GDP_per_capita',
        'CO2_emissions_per_capita',
        'Child_mortality',
        'Air_pollution_NOx',
        'Gov_health_expenditure',
        'Population_in_poverty',
    ]

    titles = [
        'GDP per Capita', 'CO2 Emissions per Capita', 'Child Mortality',
        'Air Pollution', 'Gov Health Expenditure', 'Population in Extreme Poverty'
    ]

    subtitles = [
        "GDP per capita in USD", "CO2 emissions per capita in metric tons",
        "Child mortality rate per 1000 live births", "Air pollution in PM2.5",
        "Government health expenditure as % of GDP", "Population in extreme poverty (%)"
    ]

    for i, feature in enumerate(features):
        row = i // 2 + 1
        col = i % 2 + 1

        # Sort the DataFrame by the current feature
        sorted_df = ons_data_df.sort_values(by=feature, ascending=True)

        # Define bar colors
        marker_color_ = ['rgba(85, 181, 229, 1)' if c_ == 'Uruguay' else 'lightgrey' for c_ in sorted_df['Entity']]

        if feature == 'GDP_per_capita':
            text_ = [f"<b>${val / 1000:,.1f}k</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(sorted_df[feature], sorted_df['Entity'])]
        elif feature == 'Child_mortality':
            text_ = [f"<b>{val:.2f}</b>" if c_ == 'Uruguay' else '' for val, c_ in zip(sorted_df[feature], sorted_df['Entity'])]
        else:
            text_ = ['' for _ in sorted_df['Entity']]

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

        # Update the layout for each subplot
        fig.update_xaxes(
            title_text=subtitles[i],
            showline=True,
            linecolor='lightgrey',
            linewidth=1,
            row=row, col=col
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
        height=1200, width=1200,
        title_text="ONS Data Subplots",
        font=dict(family="Helvetica Neue"),
        margin=dict(t=100, pad=0),
    )

    return fig