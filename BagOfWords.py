import pandas as pd
import numpy as np
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("Harvested_COVID_Tweets.csv")

tweet_list = []
processed_tweets = []
temp_string = ""
tokenizer = TweetTokenizer(strip_handles=True)


for index, row in df.iterrows():
    tweet_list.append(row['text'])

for i in range(len(tweet_list)):
    tokens = tokenizer.tokenize(tweet_list[i])
    for token in tokens:
        if "http" not in token:
            temp_string += token + ' '

    processed_tweets.append(temp_string)

# This does not perform any real function -remove
for i in range(5):
    tokens = tokenizer.tokenize(processed_tweets[i])
    for token in tokens:
        print(token)


tweet_tokens = np.array(processed_tweets)
count = CountVectorizer()
bag_of_words = count.fit_transform(tweet_tokens)
feature_names = count.get_feature_names()

df = pd.DataFrame(bag_of_words.toarray(), columns=feature_names)
df.to_csv("BagOfWords.csv")

