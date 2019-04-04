import tweepy  # this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler
import json

# provide your access details below
consumer_key = 'luCMgoolgODpFH9rxcvLbRqYt'
consumer_secret = 'lW9fERVDfcgoq3aqVDYpbUNGkKUUFquwpQYrLvlaXzeekpvkgZ'
access_token  = '750950262098059268-riOExqjYPhUTJAe4OHW9F7aYfK2ljuQ'
access_token_secret = 'GE4K0zqwyBi50k5Ma3xFSP44zYd1HiM5ncL1gGaDscu5K'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener



class Listener(StreamListener):


    def on_data(self, data):
        j = json.loads(data)
        if not j['retweeted'] and 'RT @' not in j['text']:#prevent tweets that is RT
         t = {
          "created_at":j["created_at"],# retrive the time when the tweet is v
          "text": j["text"] #retrive the tweet text
          }
         with open('tweets.json', 'a') as f:  # store created_at , text in json format
            f.write(str(t))
            f.write("\n")
            print(t)
            #f.write(",")

        return(True)

    def on_status(self, status):
        print(status.text)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth=auth, listener=Listener(),wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

stream.filter(track=['مكه' ])# keyword search






