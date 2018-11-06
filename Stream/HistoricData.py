import tweepy
import csv
import jsonpickle
import os
import Stream.TwitterStream as TwitterStream
import Stream.ProcessCompanyKeywords as ProcessKeywords
from Stream.ProcessCompanyKeywords import Tweet
from Stream.StoreDetails import save_dill, load_dill
from datetime import datetime, timedelta
import sys

def query_search(query, api, fName, maxTweets=10000000, tweetsPerQry=100):
    sinceId = None
    max_id = -1

    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    with open(fName, 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=query, count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=query, count=tweetsPerQry,
                                                since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                            '\n')
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break


def tweet_info(json):
    tweet_instance = Tweet(json)
    return tweet_instance


def api_finder():
    #consumer_key = "JO5NRAceQeIyGmwTE12fXeasD"
    #consumer_secret = "7vhI1GCLhSRAsWJbdzjiMqCm3x658QvXlnaFpmOIol9MvIkYfg"

    consumer_key = "JO5NRAceQeIyGmwTE12fXeasD"
    consumer_secret = "7vhI1GCLhSRAsWJbdzjiMqCm3x658QvXlnaFpmOIol9MvIkYfg"


    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api


if __name__ == '__main__':

    api = TwitterStream.login() #login as Maria

    keyword_list = []

    keyword_list.extend(ProcessKeywords.find_company('nike').keywords)
    keyword_list.extend(ProcessKeywords.find_company('apple').keywords)
    keyword_list.extend(ProcessKeywords.find_company('tesla').keywords)
    keyword_list.extend(ProcessKeywords.find_company('netflix').keywords)
    keyword_list.extend(ProcessKeywords.find_company('google').keywords)

    for keyword in keyword_list:
        query_search(keyword, api, keyword, maxTweets=10000000, tweetsPerQry=100)



