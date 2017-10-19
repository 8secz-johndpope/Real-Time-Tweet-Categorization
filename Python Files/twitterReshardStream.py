import boto3

def update_shard_count(streamName, shardCount, scalingType):
	kinesis = boto3.client('kinesis')
	print streamName + '\n' 
	print shardCount 
	print '\n' + scalingType + '\n'
	response = kinesis.update_shard_count(
		StreamName = streamName,
		TargetShardCount = shardCount,
		ScalingType = scalingType
	)
