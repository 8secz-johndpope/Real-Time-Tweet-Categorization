import boto3
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "<Enter valid token here>"
consumer_secret = "<Enter valid token here>"
access_token = "<Enter valid token here>"
access_token_secret = "<Enter valid token here>"
DeliveryStreamName = 'twitter-stream'

client = boto3.client('firehose')

class DataListener(StreamListener):

    def get_data(self, data):
        print data
        response = client.put_record(
            DeliveryStreamName=DeliveryStreamName,
                Record={
                    'Data': json.dumps(data)
        }
    )
        return True

if __name__ == '__main__':

    dl = DataListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    datastream = Stream(auth, dl)
