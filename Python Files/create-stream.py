# Simple script to create a kinesis stream
# create-stream.py
import boto3
shardsNum = 1

client = boto3.client('kinesis')
response = client.create_stream(
   StreamName='twitter',
   ShardCount=shardsNum
)
