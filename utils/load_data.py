import pandas as pd

# Mapping of country names to ISO country codes
country_to_iso = {
    'Croatia': 'HR',
    'Portugal': 'PT',
    'Greece': 'GR',
    'Spain': 'ES',
    'Malta': 'MT',
    'Cyprus': 'CY',
    'Germany': 'DE',
    'Austria': 'AT',
    'Italy': 'IT',
    'Slovenia': 'SI',
    'Netherlands': 'NL',
    'Estonia': 'EE',
    'France': 'FR',
    'United Kingdom': 'GB',
    'Luxembourg': 'LU',
    'Latvia': 'LV',
    'Hungary': 'HU',
    'Finland': 'FI',
    'Sweden': 'SE',
    'Bulgaria': 'BG',
    'Denmark': 'DK',
    'Romania': 'RO',
    'Belgium': 'BE',
    'Czechia': 'CZ',
    'Lithuania': 'LT',
    'Slovakia': 'SK',
    'Poland': 'PL',
    'Ireland': 'IE',
    'Average': 'Avg.'
}

def travel_gdp_share_data():
    travel_gdp_share_df = (
        pd.read_csv('data/travel_gdp_share_statista.csv', delimiter=';')
        .assign(
            **{
                '2019': lambda x: x['2019'].str.rstrip('%').astype(float),
                '2023': lambda x: x['2023'].str.rstrip('%').astype(float),
            }
        )
        .rename(columns={'2019': 'y2019', '2023': 'y2023', 'Characteristic': 'Country'})
    )

    # Create a new DataFrame for the average row
    average_row = pd.DataFrame({
        'Country': ['Average'],
        'y2019': [None],
        'y2023': [travel_gdp_share_df['y2023'].mean()],
    })

    # Append the average row to the original DataFrame
    travel_gdp_share_df = (pd.concat([travel_gdp_share_df, average_row]
                                     , ignore_index=True)
                           .assign(**{'ISO_Code': lambda x: x['Country'].map(country_to_iso),})
                           .sort_values(by='y2023', ascending=False)
                           )
    return travel_gdp_share_df

def life_expectancy_data():
    life_expectancy_df = (pd.read_csv('data/life_expectancy.csv')
                          .melt(id_vars=['country'], var_name='year', value_name='life_expectancy')
                          .assign(year=lambda x: x['year'].astype(int))
                          .query("year >= 1900")
                          )

    return life_expectancy_df
