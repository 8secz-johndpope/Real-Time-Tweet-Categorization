import boto3
import json
from TwitterAPI import TwitterAPI

consumer_key = "<Enter valid token here>"
consumer_secret = "<Enter valid token here>"
access_token = "<Enter valid token here>"
access_token_secret = "<Enter valid token here>"
DeliveryStreamName = 'twitter-stream'

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

firehose = boto3.client('firehose')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})

for item in r:
        firehose.put_record(DeliveryStreamName=DeliveryStreamName, Record={
                    'Data': json.dumps(data)
        }
    )
