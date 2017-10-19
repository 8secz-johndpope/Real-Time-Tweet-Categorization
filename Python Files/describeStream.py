import boto3

def describe_stream(streamName):
	kinesis = boto3.client('kinesis')
	response = kinesis.describe_stream(
		SteamName = streamName,	
	)
	return response
