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

# Mapping of countries to continents
country_to_continent = {
    'Argentina': 'South America',
    'Bolivia': 'South America',
    'Brazil': 'South America',
    'Chile': 'South America',
    'Colombia': 'South America',
    'Ecuador': 'South America',
    'Guyana': 'South America',
    'Paraguay': 'South America',
    'Peru': 'South America',
    'Suriname': 'South America',
    'Uruguay': 'South America',
    'Venezuela': 'South America'
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
                          .query("year <= 2080")
                          )

    return life_expectancy_df

def neighbouring_countries_ownership():
    data = [
        ('Canada', 25),
        ('US', 19),
        ('Hungary', 67),
        ('Greece', 60),
        ('Bulgaria', 58),
        ('Poland', 48),
        ('Slovakia', 46),
        ('Spain', 37),
        ('Italy', 36),
        ('France', 33),
        ('Czech Rep.', 31),
        ('Lithuania', 30),
        ('Germany', 30),
        ('Netherlands', 24),
        ('UK', 23),
        ('Turkey', 58),
        ('Russia', 53),
        ('Ukraine', 47),
        ('Sweden', 13),
    ]

    df = pd.DataFrame(data, columns=['country', 'percentage'])

    median_percentage = df['percentage'].median()
    median_row = pd.DataFrame({
        'country': ['Median'],
        'percentage': [median_percentage]
    })

    return pd.concat([df, median_row], ignore_index=True).sort_values('percentage', ascending=True)

def gdp_per_capita_data():
    gdp_per_capita_df = (pd.read_csv('data/gdp-per-capita-maddison.csv')
                         .assign(Continent=lambda x: x['Entity'].map(country_to_continent))
                         .query("Continent == 'South America'")
                         .query("Year == 2020")
                         .drop(columns=['Year', 'Continent'])
                         )

    return gdp_per_capita_df

def co2_emissions_per_capita_data():
    co2_emissions_df = (pd.read_csv('data/co-emissions-per-capita.csv')
                        .assign(Continent=lambda x: x['Entity'].map(country_to_continent))
                        .query("Continent == 'South America'")
                        .query("Year == 2020")
                        .drop(columns=['Year', 'Continent'])
                        )

    return co2_emissions_df

def child_mortality_data():
    child_mortality_df = (pd.read_csv('data/child-mortality.csv')
                          .assign(Continent=lambda x: x['Entity'].map(country_to_continent))
                          .query("Continent == 'South America'")
                          .query("Year == 2020")
                          .drop(columns=['Year', 'Continent'])
                          )

    return child_mortality_df

def air_pollution_data():
    air_pollution_df = (pd.read_csv('data/air-pollution.csv')
                        .assign(Continent=lambda x: x['Entity'].map(country_to_continent))
                        .query("Continent == 'South America'")
                        .query("Year == 2020")
                        .drop(columns=['Year', 'Continent'])
                      )

    return air_pollution_df

def gov_health_expenditure_data():
    gov_health_expenditure_df = (
        pd.read_csv('data/health-expenditure-government-expenditure.csv')
        .assign(Continent=lambda x: x['Entity'].map(country_to_continent))
        .query("Continent == 'South America'")
        .query("Year == 2020")
        .drop(columns=['Year', 'Continent'])
    )

    return gov_health_expenditure_df

def population_in_extreme_poverty_data():
    specific_cases = {
        'Argentina (urban)': 'Argentina',
    }

    population_in_extreme_poverty_df = (
        pd.read_csv('data/share-of-population-in-extreme-poverty.csv')
        .assign(Entity=lambda x: x['Entity'].replace(specific_cases))
        .assign(Continent=lambda x: x['Entity'].map(country_to_continent))
        .query("Continent == 'South America'")
        .query("Year == 2020")
        .drop(columns=['Year', 'Continent'])
        .assign(Code=lambda x: x.apply(lambda row: 'ARG' if row['Entity'] == 'Argentina' and pd.isna(row['Code']) else row['Code'], axis=1))
    )

    return population_in_extreme_poverty_df