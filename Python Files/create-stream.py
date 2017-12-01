# Simple script to create a kinesis stream
# create-stream.py
import boto3
shardsNum = raw_input("Number of shards:")

client = boto3.client('kinesis')
response = client.create_stream(
   StreamName='twitter',
   ShardCount=shardsNum
)
