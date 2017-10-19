import boto3
import uuid

def create_bucket(bucket):
	s3 = boto3.client('s3')
	bucketName = bucket.format(uuid.uuid4())
	s3.create_bucket(
		Bucket = bucketName
	)

def list_buckets():
	s3 = boto3.client('s3')
	response = s3.list_buckets()
	return response
