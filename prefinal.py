import tweepy
import logging
import time
import random
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()

FILE_NAME = 'lastseen.txt'

def retrieve_lastseen(file_name):
    f_read = open(file_name, 'r')
    lastseen = int(f_read.read().strip())
    f_read.close()
    return lastseen

def store_lastseen(lastseen, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(lastseen))
    f_write.close()
    return

def fav_retweet(api):
    logger.info('Retrieving tweets...')
    lastseen = retrieve_lastseen(FILE_NAME)
    mentions = api.mentions_timeline(lastseen,tweet_mode='extended')
    for mention in reversed(mentions):
        logger.warning(str(mention.id) + ' - ' + mention.full_text)
        lastseen = mention.id
        store_lastseen(lastseen, FILE_NAME)
        if '#hopzy' in mention.full_text.lower():
            # logger.info('Hopzy at your service')
            # logger.info('Please DM us your concern')
            api.update_status(
                f'@{mention.user.screen_name}\n Hopzy at your service \n Please DM us your concern')
            logger.info('Replied to the hashtag #hopzy')

        if mention.in_reply_to_status_id is not None or mention.user.id == api.me().id:
            return

        if not mention.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                mention.favorite()
                logger.info(f"Liked tweet by {mention.user.name}")
            except Exception as e:
                logger.error("Error on fav", exc_info=True)

        if not mention.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                mention.retweet()
                logger.info(f"Retweeted tweet by {mention.user.name}")
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

# while True:
#     fav_retweet(api)
#     logger.info("Waiting...")
#     time.sleep(30)


def fav_retweet_user(api, user_handle,nrTweets):
    search = f"{user_handle}"
    logger.info(f'Retrieving tweets mentioning {user_handle}...')
    tweets = api.search(q=search, lang ="en")
    for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    #     tweet.favorite()
    #     logger.info(f'Tweet from {user_handle} is liked')
    #     time.sleep(5)
    #     tweet.retweet
    #     logger.info(f'Tweet from {user_handle} is retweeted')
    # # for tweet in tweets:
    #     if tweet.in_reply_to_status_id is not None or tweet.user.id == api.me().id:
    #         # This tweet is a reply or I'm its author so, ignore it
    #         return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                logger.info(f"Liked a tweet mentioning {user_handle}")
            except tweepy.error.TweepError as e:
                logger.warning(e.reason)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                logger.info(f"Retweeted a tweet mentioning {user_handle}")
            except tweepy.error.TweepError as e:
                logger.warning(e.reason)

# while True:
#     fav_retweet_user(api, "@iamsrk",50)
#     logger.info("Waiting...")
#     time.sleep(30)

def retweet_tweets_with_hashtag(api, need_hashtags):
    if type(need_hashtags) is list:
        search_query = f"{need_hashtags} -filter:retweets"
        tweets = api.search(q=search_query, lang ="en", tweet_mode='extended')
        for tweet in tweets:
            hashtags = [i['text'].lower() for i in tweet.__dict__['entities']['hashtags']]
            try:
                need_hashtags = [hashtag.strip('#') for hashtag in need_hashtags]
                need_hashtags = list(need_hashtags)
                if set(hashtags) & set(need_hashtags):
                    if tweet.user.id != api.me().id:
                        api.retweet(tweet.id)
                        logger.info(f"Retweeted tweet from {tweet.user.name}")
                        time.sleep(5)
            except tweepy.TweepError:
                logger.error("Error on retweet", exc_info=True)
    else:
        logger.error("Hashtag search terms needs to be of type list", exc_info=True)
        return

while True:
        retweet_tweets_with_hashtag(api, ['#nifty','#banknifty','#stockmarket','manjha'])
        logger.info("Waiting..."),
        time.sleep(30)