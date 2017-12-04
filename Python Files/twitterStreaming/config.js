'use strict';

var config = module.exports = {
 firehose : {
  DeliveryStreamName: 'manualstream', 
  S3DestinationConfiguration: {
    BucketARN: 'arn:aws:s3:::dic-bucket1234',
    RoleARN: 'arn:aws:iam::958809247975:role/firehose_delivery_role',
    BufferingHints: {
      IntervalInSeconds: 300,
      SizeInMBs: 5
    },
    CompressionFormat: 'UNCOMPRESSED', /* 'UNCOMPRESSED | GZIP | ZIP | Snappy' */
    EncryptionConfiguration: {
      NoEncryptionConfig: 'NoEncryption'
    },
    Prefix: 'twitter/data'
  }
  },
  twitter: {
      consumer_key: '',
      consumer_secret: '',
      access_token: '',
      access_token_secret: ''
 },
 locations: ['-127.33,23.34,-55.52,49.56'], 
 waitBetweenDescribeCallsInSeconds: 2,
 recordsToWritePerBatch: 100,
 waitBetweenPutRecordsCallsInMilliseconds: 50,
 region: 'us-east-1'   
};
