import tweepy
def connect(consumer_key, consumer_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Successfully Logged In")
        return api
    except:
        print("Login Failed")