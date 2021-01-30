import tweepy
import datetime
from nltk.tokenize import TweetTokenizer

# API Key/Secret
auth = tweepy.OAuthHandler("<API Key>",
                           "<API Key Secret>")

# Access Token/Secret
auth.set_access_token("<Access Token>",
                      "<Access Token Secret>")

api = tweepy.API(auth)

targetHandle = ["Insert Twitter handle here!"]

stopDate = datetime.datetime(2020, 1, 1, 0, 0, 0)
textFile = open("Tweet_IDs.txt", "w")

all_tweets = []
covid_tweet_IDs = []
tokenizer = TweetTokenizer()


def get_handle_tweets(handle):
    for tweet in tweepy.Cursor(api.user_timeline, id=handle).items():
        if tweet.created_at > stopDate:
            all_tweets.append(tweet)
        if tweet.created_at == stopDate:
            return

    return


def get_covid_tweets(all_tweets):
    count = 0
    for tweet in all_tweets:
        tweet_tokens = tokenizer.tokenize(tweet.text)
        for token in tweet_tokens:
            if count == 0:
                covid_tweet_IDs.append(tweet.user.name + "\n")
                count += 1
            if "covid" in token.lower():
                covid_tweet_IDs.append(tweet.id_str)
    return


for handle in targetHandle:
    get_handle_tweets(handle)
    get_covid_tweets(all_tweets)

# COVID Tweet IDs are written to a text file to be put through Hydrator to retrieve metadata
# and exported into CSVs for each respective handle.

for tweet_ID in covid_tweet_IDs:
    textFile.write(tweet_ID + "\n")

textFile.close()


