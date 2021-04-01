import tweepy
import time
consumer_key = 'gYiM4AXsBCzTf4sIWv32O1Y2U'
consumer_secret = 'QU295F6Ptvi22vVRCSt56uvaXSv3WLdnFzocnSDUMZfs0hY4lJ'
access_token = '2977685302-GhcXlmTycUcvRL2TUqTsa2PUpD24d7fxihDOL2W'
access_token_secret = 'ZXJhJpIxeesf1GjXReu1y5z7v7OrmYHAJ6gD6zeKPIrBp'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user)

search = ['manish','jha']

nrTweets = 50

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(3)

    except tweepy.error.TweepError as e:
        print(e.reason)

    except tweepy.error.RateLimitError as r:

        print(r.reason)

    except StopIteration:
        print('Stopped Favouriting')
        break

