from kafka import KafkaProducer
import kafka
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# Twitter API Config
consumerKey = "XeAKgeWYtWBVDTcGXEaiiWHCo"
consumerSecret = "bR4hcPi5sRsx7XZj5GwlOUfFp9lEaPVRa4DjGC5XJ9zXGnLocq"
accessToken = "828503191822102528-qhmoTavuoO9GKQl1Wtp0GGBHN6CeL1G"
accessSecret = "wwz6dJBk1F0F9YbE2TB5uPmf8m8REPuhgbrm7u5i0DCth"

# Twitter API Authentication
authentication = OAuthHandler(consumerKey, consumerSecret)
authentication.set_access_token(accessToken, accessSecret)

api_initilization = tweepy.API(authentication)


# Twitter Stream Listener
class KafkaProducerListener(StreamListener):
    def __init__(self):

        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def on_data(self, inputData):
        # Producer produces data for consumer
        # Data comes from Twitter
        self.producer.send("tweetstream", inputData.encode('utf-8'))
        print(inputData)
        return True

    def extract_error(self, stat):
        print(stat)
        return True


# Twitter Stream Config
twitterStreaming = Stream(authentication, KafkaProducerListener())

# Produce Data that has trump hashtag (Tweets)
twitterStreaming.filter(track=['#trump', '#coronavirus'])