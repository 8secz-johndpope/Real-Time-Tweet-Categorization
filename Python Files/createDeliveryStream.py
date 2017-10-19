import boto3

def create_delivery_stream(deliveryStream,streamType,streamARN,roleARN):
	firehose = boto3.client('firehose')	
	response = fireshose.create_delivery_stream(
		DeliveryStreamName = deliveryStream,
		DeliveryStreamType = streamType,
		KinesisStreamSourceConfiguration ={
			'KinesisStreamARN': streamARN,
			'RoleARN' : roleARN
		},
		S3DestinationConfiguration = {
			'RoleARN': ,
			'BucketARN': bucketARN,
		} 	
	)
	return response
