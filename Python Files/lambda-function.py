import json
import boto3
import twitter_to_es

s3 = boto3.client('s3')

def manual_function(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        resp = s3.get_object(Bucket=bucket, Key=key)
              
    except Exception as e:
        print(e)
        print('Error getting object')
        raise e
    
    try:
        s3_content = resp['Body'].read()
        if s3_content.endswith(',\n'):
            s3_content = s3_content[:-2]
        tweets_str = '['+s3_content+']'
        tweets = json.loads(tweets_str)
   
    except Exception as e:
        print(e)
        print('Error loading json from object')
        raise e
   
    try:
        twitter_to_es.load(tweets)

    except Exception as e:
        print(e)
        print('Error loading data into ElasticSearch')
        raise e    
