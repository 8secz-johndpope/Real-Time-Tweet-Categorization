import boto3

def list_streams(limit = 10,startStream = ''):
	kinesis = boto3.client('kinesis')

	response = kinesis.list_streams(
		Limit = limit
		#ExclusiveStartStreamName = startStream
	)
	return response
