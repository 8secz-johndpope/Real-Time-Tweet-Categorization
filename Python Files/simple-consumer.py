import boto3
import time
import json
import botocore
import s3

## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis")
shard_id = "shardId-000000000000" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]

s3 = boto3.resource("s3")
print s3
bucket = s3.Bucket("dic-twitter-bucket")##

s3.meta.client.head_bucket(Bucket = 'firehose-s3-es');


while 1==1:
     out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
     shard_it = out["NextShardIterator"]
     s3.Object('firehose-se-es','twitter').put(Body=put(out))
     print out;
     time.sleep(1.0)