import json
import csv
import tweepy
import re
import pandas as pd


consumer_key = "hrfDn07ZIftyGxqwj2ACnvpQT"
consumer_secret = "TBeGi5SMzRnFz91OIGZXxZdIIiaacZmHdnlNrwTz82Xy20MrKx"
access_token = "15432383-uKuMl9YxbQWKLDPiERYm7woexk0YeCB6wnoSMYHgP"
access_token_secret = "IdORj2aKJP6ejhqlqLyWo8cnznfCgXGWbhjlGPvrTzE6r"

def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)
    data=[]
    for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(15):
        row=[]
        row.append(tweet.user.screen_name)
        row.append(tweet.user.created_at)
        row.append(tweet.full_text.encode('utf-8'))
        row.append(str(tweet.created_at))
        row.append(str([hashtag['text'] for hashtag in tweet._json['entities']['hashtags']]))
        row.append(tweet.user.followers_count)
        row.append(tweet.user.friends_count)
        data.append(row)
    return data

    
hashtag_phrase = input('Hashtag Phrase ')
with open('%s.csv' % (hashtag_phrase),'w',newline='') as f:
    write=csv.writer(f)
    write.writerow(['UserName','User_Created','Tweet_text','Tweet_Data','Tweet_Hashtags','User_FollowCount','User_FriendCount'])
    data=search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
    for row in data:
        write.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])



