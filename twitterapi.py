from credentials import *
import pymysql, tweepy
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_secret'])

api = tweepy.API(auth)


class TwitterUser:
    def __init__(self, handle):
        self.handle = handle

    def get_recent_tweets(self):
        tweetnum = int(input("input the number of tweets "))
        tweet = api.user_timeline(screen_name=self.handle, count=tweetnum)[0:tweetnum]
        for entry in tweet:
            print(entry.text)

user = TwitterUser("realDonaldTrump")
user.get_recent_tweets()

