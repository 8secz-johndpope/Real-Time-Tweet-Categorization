import boto3
import json
import config
import listStreams
import twitterReshardStream
import createRole

role = createRole.create_role('firehose_delivery_role','firehose-policy.json')
print role

#streamList = listStreams.list_streams(10)
#twitterReshardStream.update_shard_count(streamList['StreamNames'][0],config.shardCount,config.scalingType)
