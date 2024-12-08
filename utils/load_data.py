import pandas as pd
import pycountry
import pycountry_convert as pc
import numpy as np
import re

def _get_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except KeyError:
        return None

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

south_america_country_to_emoji = {
        'Argentina': '🇦🇷', 'Bolivia': '🇧🇴', 'Brazil': '🇧🇷', 'Chile': '🇨🇱', 'Colombia': '🇨🇴',
        'Ecuador': '🇪🇨', 'Guyana': '🇬🇾', 'Paraguay': '🇵🇾', 'Peru': '🇵🇪', 'Suriname': '🇸🇷',
        'Uruguay': '🇺🇾', 'Venezuela': '🇻🇪'
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

    iso_to_emoji = {
        'HR': '🇭🇷', 'PT': '🇵🇹', 'GR': '🇬🇷', 'ES': '🇪🇸', 'MT': '🇲🇹', 'CY': '🇨🇾',
        'DE': '🇩🇪', 'AT': '🇦🇹', 'IT': '🇮🇹', 'SI': '🇸🇮', 'NL': '🇳🇱', 'EE': '🇪🇪',
        'FR': '🇫🇷', 'GB': '🇬🇧', 'LU': '🇱🇺', 'LV': '🇱🇻', 'HU': '🇭🇺', 'FI': '🇫🇮',
        'SE': '🇸🇪', 'BG': '🇧🇬', 'DK': '🇩🇰', 'RO': '🇷🇴', 'BE': '🇧🇪', 'CZ': '🇨🇿',
        'LT': '🇱🇹', 'SK': '🇸🇰', 'PL': '🇵🇱', 'IE': '🇮🇪'
    }

    # Append the average row to the original DataFrame
    travel_gdp_share_df = (pd.concat([travel_gdp_share_df, average_row]
                                     , ignore_index=True)
                           .assign(**{'ISO_Code': lambda x: x['Country'].map(country_to_iso),})
                           .assign(ISO_Code_with_emoji=lambda x: x['ISO_Code'].map(lambda y: f"{y}<br>{iso_to_emoji.get(y, '')}"))
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
                         .assign(Entity_emoji=lambda x: x['Entity'].map(lambda y: f"{y} {south_america_country_to_emoji.get(y, '') }"))
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

def smoking_rate_data():
    country_pop_df = (pd.read_csv('data/country-population-2022.csv', delimiter=';')
                      .rename(columns={'2022': 'population',
                                       'Country Name': 'country'})
                      .assign(continent=lambda x: x['Country Code'].apply(_get_continent))
                      )

    smoking_rate_df = (pd.read_csv('data/smoking-rates-by-country-2024.csv')
                       .rename(columns={'smokingRatesByCountry_rateBothPct2022': 'smoking_rate'}))

    merged_df = pd.merge(country_pop_df, smoking_rate_df, on='country')
    merged_df['rank_by_population_over_continent'] = (merged_df
                                                      .groupby('continent')['population']
                                                      .transform(lambda x: x.rank(method='dense', ascending=False)))
    merged_df = merged_df.query("rank_by_population_over_continent <= 5")
    merged_df = merged_df[['continent', 'country', 'population', 'smoking_rate']]

    continent_ordering = {
        'Africa': 1,
        'Asia': 2,
        'Europe': 3,
        'Oceania': 4,
        'North America': 5,
        'South America': 6,
    }
    merged_df['continent_ordering'] = merged_df['continent'].map(continent_ordering)

    return merged_df

def progress_against_target_synthetic_data():
    df = (pd.read_csv('data/department_targets.csv')
          .assign(progress=lambda x: x['progress'].round(1),
                  # diff=lambda x: (x['progress'] - x['target']).round(1),
                  # diff_perct=lambda x: (((x['progress']-x['target']) / x['target']) * 100).round(1),
                  )
          )

    return df


def covid_data():
    entities_to_filter = ['Brazil', 'UK', 'US', 'France', 'Sweden', 'Germany', 'Russia', 'India', 'Spain', 'New Zealand', 'Spain', 'China']
    df = (pd.read_csv('data/covid.csv')
          .query("Day == '2021-05-24'")
          .query("Entity in @entities_to_filter")
          .rename(columns={'Total confirmed deaths due to COVID-19 per 100,000 people': 'Deaths'})
          .drop(columns=["Cumulative excess deaths per 100,000 people (central estimate)",
                         "Cumulative excess deaths per 100,000 people (95% CI, lower bound)",
                         "Cumulative excess deaths per 100,000 people (95% CI, upper bound)",
                         "Day",])
          .assign(Deaths=lambda x: x['Deaths'].round(2))
          .reset_index()
          )

    return df


def favourite_weekday_data():
    # https://today.yougov.com/society/articles/34696-most-and-least-favorite-day-week-poll
    data = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Don't know", "N/A"],
        "Least Favorite": [38, 8, 4, 2, 3, 3, 6, 2, 34],
        "Least Favorite %": ["58%", "12%", "6%", "3%", "5%", "5%", "9%", "3%", "28%"],
        "Favorite": [4, 2, 5, 4, 21, 25, 10, 2, 28],
        "Favorite %": [6, 3, 7, 6, 29, 35, 14, 3, 0]
    }

    day_to_number = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }

    day_abbreviation = {
        "Monday": "Mo",
        "Tuesday": "Tu",
        "Wednesday": "We",
        "Thursday": "Th",
        "Friday": "Fr",
        "Saturday": "Sa",
        "Sunday": "Su",
        "No preference": "NA"
    }

    return (pd.DataFrame(data)
            .assign(Day_Number=lambda df: df['Day'].map(day_to_number).fillna(8).astype(int))
            .assign(Day=lambda df: df.apply(lambda row: 'No preference' if row['Day_Number'] == 8 else row['Day'], axis=1))
            .assign(Day_Abbreviation=lambda df: df['Day'].map(day_abbreviation))
            .groupby(['Day', 'Day_Number', 'Day_Abbreviation'], as_index=False)
            .agg({'Favorite %': 'sum'})
            )

def favourite_animal_data():
    data = {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Animal": ["Tiger", "Dog", "Dolphin", "Horse", "Lion", "Snake", "Elephant", "Chimpanzee", "Orang-utan", "Whale"],
        "Percentage": [21.0, 20.0, 13.0, 10.0, 9.0, 8.0, 6.0, 5.0, 4.5, 3.5]
    }

    return (pd.DataFrame(data)
            .assign(Animal=lambda df: df['Animal'].where(df['Percentage'] >= 8, 'Other'))
            .groupby('Animal', as_index=False)
            .agg({'Percentage': 'sum'})
            )

def synthetic_satisfaction_data():
    data = {
        "satisfaction": ["very satisfied", "satisfied", "neutral", "dissatisfied", "very dissatisfied"],
        "percentage": [25.0, 35.0, 20.0, 10.0, 10.0]
    }

    return pd.DataFrame(data)

def housing_data():
    df = (pd.read_csv('data/Housing.csv')
          .assign(price_grouped=lambda x: np.round(x['price'], -5))
          .groupby('price_grouped')['area']
          .size()
          .reset_index(name='count')
          )

    return df

def gdp_by_country_data():
    def _is_valid_country(country_name):
        try:
            pycountry.countries.lookup(country_name)
            return True
        except LookupError:
            return False

    country_to_emoji = {
        'US': '🇺🇸',
        'China': '🇨🇳',
        'Germany': '🇩🇪',
        'Japan': '🇯🇵',
        'India': '🇮🇳',
        'UK': '🇬🇧',
        'France': '🇫🇷',
        'Italy': '🇮🇹',
        'Brazil': '🇧🇷',
        'Canada': '🇨🇦'
    }

    df = (pd.read_csv('data/gdp_by_country_2023.csv')
          .rename(columns={'Country Name': 'Country',
                           'Country Code': 'Code',
                           '2023 [YR2023]': 'GDP',
                           })
          .query("GDP != '..'")
          .assign(GDP=lambda x: pd.to_numeric(x['GDP'], errors='coerce').round(0))
          .query("Country.map(@_is_valid_country)")
          .replace({'Country': {'United Kingdom': 'UK',
                                'United States': 'US',
                                }})
          .assign(GDP_Rank=lambda x: x['GDP'].rank(ascending=False, method='dense'))
          .query("GDP_Rank <= 10")
          .assign(Country_with_emoji=lambda x: x['Country'].map(lambda y: f"{y}<br>{country_to_emoji.get(y, '')}"))
          .sort_values('GDP_Rank')
          )

    return df

def boys_names_data():
    df = (pd.read_csv('data/boynames2022.csv', sep=';')
          .query("Rank <= 10")
          .sort_values('Rank', ascending=False)
          )

    return df

def employment_by_sector_data():
    df = (pd.read_csv('data/employment-by-sector-UK.csv', sep=',')
          .query("Time == 2021")
          .query("Ethnicity == 'All'")
          .replace({'Industry': {'A - Agriculture, forestry and fishing': 'Agriculture, forestry and fishing  -  🎣  ',
                                'B,D,E - Energy and water': 'Energy and water  -  ⚡️ ',
                                'C -Manufacturing': 'Manufacturing  -  🏭  ',
                                'F - Construction': 'Construction  -  🏗️  ',
                                'G,I -Distribution, hotels and restaurants': 'Distribution, hotels and restaurants  -  🍽️  ',
                                'H,J -Transport and communication': 'Transport and communication  -  🚚  ',
                                'K,L,M,N_-_Banking_and_finance': 'Banking and finance  -  💰  ',
                                'O,P,Q - Public admin, education and health': 'Public admin, education and health  -  🏥  ',
                                'R,S,T,U - Other services': 'Other services  -  🛠  ',
                                }})
          .assign(Industry_without_emoji=lambda x: x['Industry'].str.replace(
        r'[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002702-\U000027B0\U000024C2-\U0001F251]', '', regex=True))
          .assign(Industry_without_emoji=lambda x: x['Industry_without_emoji'].str.replace(' -  ', ''))
          .assign(Value=lambda x: x['Value'].astype(float))
          .sort_values('Value', ascending=True)
          .drop(columns=['Measure', 'Time_type', 'Ethnicity', 'SIC', 'Denominator', 'Numerator', 'CI'])
          )

    return df

def mountain_or_structure_heights_data():
    # Data for the dataframe
    data = {
        "Type": ["Mountain", "Mountain", "Mountain", "Mountain",
                 "Volcano", "Volcano", "Volcano", "Volcano",
                 "Ocean Trench", "Ocean Trench", "Ocean Trench", "Ocean Trench",
                 "Man-Made Structure", "Man-Made Structure", "Man-Made Structure", "Man-Made Structure",
                 "Cave", "Cave", "Cave", "Cave",
                 "Mine", "Mine", "Mine", "Mine",
                 "River", "River", "River",
                 "Waterfall", "Waterfall", "Waterfall",
                 "Canyon", "Canyon", "Canyon", "Canyon",
                 "Lake", "Lake", "Lake"],

        "Name": ["Mount Everest", "Mauna Kea", "K2", "Denali",
                 "Ojos del Salado", "Mount Kilimanjaro", "Nevado Ojos del Salado", "Mount Vesuvius",
                 "Mariana Trench", "Tonga Trench", "Puerto Rico Trench", "Java Trench",
                 "Burj Khalifa", "Shanghai Tower", "Abraj Al-Bait Clock Tower", "CN Tower",
                 "Veryovkina Cave", "Krubera Cave", "Sarma Cave", "Snezhnaya Cave",
                 "Mponeng Gold Mine", "TauTona Mine", "Kola Superdeep Borehole", "Savuka Gold Mine",
                 "Amazon River", "Nile River", "Yangtze River",
                 "Angel Falls", "Tugela Falls", "Tres Hermanas Falls",
                 "Grand Canyon", "Yarlung Tsangpo Canyon", "Kali Gandaki Gorge", "Cotahuasi Canyon",
                 "Baikal Lake", "Caspian Sea", "Lake Tanganyika"],

        "Total Height (km)": [8.848, 10.2, 8.611, 6.19,
                              6.893, 5.895, 6.893, 1.281,
                              -11, -10.882, -8.64, -7.725,
                              0.828, 0.632, 0.601, 0.553,
                              -2.212, -2.197, -1.83, -1.75,
                              -4, -3.9, -12.262, -3.7,
                              6.992, 6.65, 6.3,
                              0.979, 0.948, 0.914,
                              1.83, 5.382, 6, 3.354,
                              -1.642, -1.025, -1.471],

        "Height vs Sea Level (km)": [8.848, 4.2, 8.611, 6.19,
                                     6.893, 5.895, 6.893, 1.281,
                                     -11, -10.882, -8.64, -7.725,
                                     0.828, 0.632, 0.601, 0.553,
                                     -2.212, -2.197, -1.83, -1.75,
                                     -4, -3.9, -12.262, -3.7,
                                     6.992, 6.65, 6.3,
                                     0.979, 0.948, 0.914,
                                     1.83, 5.382, 6, 3.354,
                                     -1.642, -1.025, -1.471]
    }

    return (pd.DataFrame(data)
            .assign(Height_Rank=lambda x: x.groupby('Type')['Total Height (km)'].rank(ascending=False, method='dense'),
                    total_height=lambda x: np.round(x['Total Height (km)'], 1),
                    height_sea_level=lambda x: np.round(x["Height vs Sea Level (km)"], 1),
                    diff_sea_level_height=lambda x: np.round(x['height_sea_level'] - x['total_height'], 1),
                    starting_point=lambda x: np.where(((x['diff_sea_level_height'] == 0) & (x['total_height'] > 0)), 0,
                                                np.where(((x['diff_sea_level_height'] == 0) & (x['total_height'] < 0)),
                                                         x['total_height'], x['diff_sea_level_height'])),
                    text_for_starting_point=lambda x: np.where(x['starting_point'] < 0, x['starting_point'].astype(str) + 'km', ''),
                    )
            .query('Name != "Nevado Ojos del Salado"')
            .query("Type.isin(['Mountain', 'Volcano', 'Ocean Trench', 'Canyon',' Waterfall'])")
            .query("Height_Rank <= 3")
            .sort_values(['starting_point', 'total_height'], ascending=False)
            )

def sex_ratio_data():
    df = (pd.read_csv('data/sex-ratio-at-birth.csv', sep=',')
          .query("Year == 2017")
          .dropna(subset=['Code'])
          .rename(columns={'Sex ratio - Sex: all - Age: 0 - Variant: estimates': 'ratio'})
          .assign(ratio_avg=lambda x: x['ratio'].mean(),)
          )

    country_pop_df = (pd.read_csv('data/country-population-2022.csv', delimiter=';')
                      .rename(columns={'2022': 'population',
                                       'Country Code': 'Code',})
                      .drop(columns=['Country Name'])
                      )

    country_to_emoji = {
        'China': '🇨🇳',
        'Azerbaijan': '🇦🇿',
        'Vietnam': '🇻🇳',
        'India': '🇮🇳',
        'Uzbekistan': '🇺🇿',
        'Angola': '🇦🇴',
        'Kenya': '🇰🇪',
        'Zimbabwe': '🇿🇼',
        'Mozambique': '🇲🇿',
        'Malawi': '🇲🇼',
        'Zambia': '🇿🇲'
    }

    return_df = (pd.merge(df, country_pop_df, on='Code')
                 .assign(population_rank=lambda x: x['population'].rank(ascending=False, method='dense'))
                 .query("population_rank <= 100")
                 .assign(ratio_rank=lambda x: x['ratio'].rank(ascending=False, method='dense'),
                         ratio=lambda x: x['ratio'].round(0))
                 .query("(ratio_rank <= 5) | (ratio_rank >= 95)")
                 .assign(Entity_text=lambda x: x['Entity'].map(lambda y: f"{y} {country_to_emoji.get(y, '')}"))
                 .sort_values('ratio_rank')
                 )

    return return_df

def AE_waiting_times_data():
    df = (pd.read_csv('data/AE_percentage_waiting_times.csv', sep=';')
          .assign(year_clean=lambda x: x['Year'].str.split('-').str[0].astype(int),
                  quarter_clean=lambda x: x['Quarter'].str.split(':').str[0],
                  text_col=lambda x: x['quarter_clean'] + ' ' + x['year_clean'].astype(str),
                  percentage_4_hours_or_less=lambda x: x['Percentage in 4 hours or less (all)'].str.replace('%', '').astype(float),
                  )
          .query("year_clean >= 2018")
          .query("year_clean <= 2022")
          )
    return df

def speaking_languages_data():
    strings_to_replace = ['Other European language (EU):',
                          '(English or Welsh in Wales)',
                          'Other European language (non EU):',
                          'Tagalog or',
                          'or Farsi',
                          '(with Sylheti and Chatgaya)',
                          'South Asian language:',
                          'African language:',
                          'East Asian language:',
                          'West or Central Asian language:'
                          ' ',
                          ]
    pattern = '|'.join(map(re.escape, strings_to_replace))

    df = (pd.read_csv('data/languages.csv', sep=',')
          .rename(columns={'Main language (detailed) (95 categories)': 'language', })
          .assign(language=lambda x: x['language'].str.replace(pattern, '', regex=True),
                  language_group=lambda x: np.where(x['language'].str.contains('English'), 'English', 'All other languages'),
                  )
          .groupby(['language', 'language_group'], as_index=False)
          .agg({'Observation': 'sum'})
          .assign(observation_rank=lambda x: x['Observation'].rank(ascending=False, method='dense'),)
          .query("language != 'Does not apply'")
          .sort_values('observation_rank')
          )

    return df

def percentage_of_global_food_exports_data():
    country_to_emoji = {
        'Netherlands': '🇳🇱',
        'USA': '🇺🇸',
        'China': '🇨🇳',
        'France': '🇫🇷',
        'Germany': '🇩🇪'
    }

    # Define the data
    data = {
        'Country': ['USA', 'China', 'France', 'Germany', 'Netherlands'],
        'Potatoes': [5, 6, 15, 9, 18],
        'Onions': [7, 14, 2, 1, 19],
        'Cucumbers': [2, 2, 1, 1, 21],
        'Tomatoes': [3, 2, 4, 1, 20],
        'Mushrooms': [2, 10, 2, 2, 15],
        'Peppers': [4, 1, 1, 1, 20],
        'Eggs': [5, 4, 1, 7, 23]
    }

    return (pd.DataFrame(data)
            .melt(id_vars=['Country'], var_name='Food', value_name='percentage')
            .assign(Country=lambda x: x['Country'].map(lambda y: f"{y} {country_to_emoji.get(y, '')}"))
            .sort_values('percentage', ascending=True)
            )

def uefa_clubs_rankings_data():
    rename_dict = {
        'pk-d--flex': 'ranking',
        'pk-identifier': 'club',
        'pk-identifier (2)': 'country',
        'ag-cell-value': '09/10',
        'ag-cell-value (2)': '10/11',
        'ag-cell-value (3)': '11/12',
        'ag-cell-value (4)': '12/13',
        'ag-cell-value (5)': '13/14',
        'ag-cell-value (6)': 'total_points',
        'ag-cell-value (7)': 'coefficient',
    }

    df_13_14 = (pd.read_csv('data/uefa-2013-14.csv', sep=','))
    df_13_14.rename(columns=rename_dict, inplace=True)
    df_13_14['season'] = '2013-14'

    df_23_24 = (pd.read_csv('data/uefa-2023-24.csv', sep=','))
    df_23_24.rename(columns=rename_dict, inplace=True)
    df_23_24['season'] = '2023-24'

    return_df = (pd.concat([df_13_14, df_23_24], ignore_index=True)
                 .query("country == 'Spain'")
                 .query("ranking <= 94")
                 .query("club not in ['Getafe', 'Levante', 'Malaga', 'Athletic Club', 'Osasuna', 'Granada']")
                 )

    return_df['text_column'] = return_df.apply(
        lambda row: f"  {row['ranking']} - {row['club']}" if row['season'] == '2023-24' else (
            f"{row['club']} - {row['ranking']}  " if row['season'] == '2013-14' else row['club']
        ),
        axis=1
    )

    return return_df

def workforce_by_sector_data():
    rename_dict = {
        'ref_area.label': 'country',
        'source.label': 'label',
        'indicator.label': 'indicator',
        'classif1.label': 'sector',
        'classif2.label': 'skill',
        'time': 'year',
    }

    strings_to_replace = ['Economic activity (Aggregate):',]
    pattern = '|'.join(map(re.escape, strings_to_replace))

    country_to_emoji = {
        'Netherlands': '🇳🇱',
        'Spain': '🇪🇸',
        'Brazil': '🇧🇷',
        'Indonesia': '🇮🇩',
        'South Africa': '🇿🇦',
        'Nigeria': '🇳🇬',
        'USA': '🇺🇸',
        'Thailand': '🇹🇭',
        'Vietnam': '🇻🇳',
        'India': '🇮🇳'
    }

    df = (pd.read_csv('data/workforce-by-sector1.csv', sep=';'))
    df.rename(columns=rename_dict, inplace=True)
    df = (df
          .query("year == 2019")
          .assign(sector=lambda x: x['sector'].str.replace(pattern, '', regex=True))
          .assign(sector=lambda x: x['sector'].str.replace('Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 'Services'))
          .assign(sector=lambda x: x['sector'].str.replace('Public Administration, Community, Social and other Services and Activities', 'Services'))
          .query('country in ["Netherlands", "Spain", "Brazil", "Indonesia", "South Africa", "Nigeria", "United States of America", "Thailand", "Viet Nam", "India"]')
          .assign(country=lambda x: x['country'].str.replace('United States of America', 'USA'))
          .assign(country=lambda x: x['country'].str.replace('Viet Nam', 'Vietnam'))
          .query('sector.str.contains("Agriculture|Services|Industry|Construction|Manufacturing")')
          .groupby(['country', 'sector'], as_index=False)
          .agg({'obs_value': 'sum'})
          .assign(total_obs_value_by_country=lambda x: x.groupby('country')['obs_value'].transform('sum'))
          .assign(percentage=lambda x: np.round((x['obs_value'] / x['total_obs_value_by_country']) * 100, 1))
          .assign(country=lambda x: x['country'].map(lambda y: f"{y} {country_to_emoji.get(y, '')}"))
          )

    return df

def driving_women_data():
    df = (pd.read_csv('data/driving-women.csv', sep=';')
          .drop(columns=['Unnamed: 10'])
          .melt(id_vars=['Year', 'Sex'], var_name='age_group', value_name='percentage')
          )

    df['percentage'] = pd.to_numeric(df['percentage'], errors='coerce')

    return df

def space_race_data():
    df = (pd.read_csv('data/timeline-space-race.csv', sep=';'))

    return df

def island_distances_data():
    df = (pd.read_csv('data/island-distances.csv', sep=';'))

    return df

def political_view_survey_data():
    df = (pd.read_csv('data/political-view-survey.csv', sep=';'))

    return df

def fertility_rates_data():
    df = (pd.read_csv('data/fertility_rates1.csv', sep=','))

    return df