import praw
import pandas as pd
import datetime as dt

def get_date(created):
    return dt.datetime.fromtimestamp(created)

def Reddit_Scrape(subreddit):

    reddit = praw.Reddit(client_id='E1O1C_RP0Jl7Dg', \
                     client_secret='SGqD7mfZ2p_cvbw8bJgAVPOtzv8', \
                     user_agent='reddit_scrape', \
                     username='web_scrapper', \
                     password='Password!')

    subreddit1 = reddit.subreddit(subreddit)

    hot_subreddit = subreddit1.hot(limit = 200)

    topics_dict = { "title":[], \
                    "id":[], "url":[], \
                    "score":[], \
                    "created": [], \
                    "comms_num": [], \
                    "body":[]}

    for submission in hot_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["id"].append(submission.id)
        topics_dict["score"].append(submission.score)
        topics_dict["url"].append(submission.url)
        topics_dict["created"].append(submission.created)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["body"].append(submission.selftext)

    
    
    data = pd.DataFrame(topics_dict)

    _timestamp = data["created"].apply(get_date)
    
    data = data.assign(timestamp = _timestamp)

    data.to_csv('%s.csv' % (subreddit), index=False) 

    

    
