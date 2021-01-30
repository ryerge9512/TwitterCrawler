import pandas as pd

# Reads-in all hydrated Tweet data CSVs and concatenates into a single aggregated data CSV.

def read_covid_spreadsheets(local_covid_spreadsheets, local_df):
    count = 1

    for spreadsheet in local_covid_spreadsheets:
        if count != 0:
            local_df = pd.read_csv(spreadsheet, usecols=["created_at", "hashtags", "text", "user_name"])
            count -= 1
        else:
            tempdf = pd.read_csv(spreadsheet, usecols=["created_at", "hashtags", "text", "user_name"])
            local_df = pd.concat([local_df, tempdf])

    return local_df


covid_spreadsheets = ['CBSNY_Covid_tweets.csv', 'CityOfRochester_Covid_tweets.csv', 'Montefiore_Covid_tweets.csv',
                      'News8WROC_Covid_tweets.csv', 'News10ABC_Covid_tweets.csv', 'News12LI_Covid_tweets.csv',
                      'NewsChannel9_Covid_tweets.csv', 'nycgov_Covid_tweets.csv', 'NYDOH_Covid_tweets.csv',
                      'WBFO-NPR_Covid_tweets.csv']

pd.set_option("max_columns", None)
pd.set_option("max_rows", None)
df = read_covid_spreadsheets(covid_spreadsheets, pd.DataFrame)

df.to_csv("Harvested_COVID_Tweets.csv")

