from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json
import os
from textblob import TextBlob
elasticSearch_init = Elasticsearch(hosts=['localhost'], port=9200)


def main():
    
    consumerInit = KafkaConsumer("tweetstream", auto_offset_reset='earliest')

    for msg_data in consumerInit:
        jsonMsg_data = json.loads(msg_data.value)
        tweetBody = TextBlob(jsonMsg_data["text"])
        pol_value = tweetBody.sentiment.polarity
        tweet_label = ""
        if pol_value > 0:
            tweet_label = 'positive'
        elif pol_value < 0:
            tweet_label = 'negative'
        elif pol_value == 0:
            tweet_label = 'neutral'
        print("The sentiment is:", tweet_label)

        #add text and sentiment info to elasticsearch
        es_Message = {"authorName": jsonMsg_data["user"]["screen_name"],
                       "dateCreated": jsonMsg_data["created_at"],
                       "msg": jsonMsg_data["text"],
                       "polarity_Value": pol_value,
                       "label": tweet_label}

        try:
            elasticSearch_init.index(index="elastictweet",
                     doc_type="_doc",
                     body=es_Message)

        except Exception as e:
            print(e)

        print('\n')


if __name__ == "__main__":
    main()