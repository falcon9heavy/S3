import boto3

## read from ~/.aws/credentials

BUCKET_NAME = 's3-csv-test-bucket'

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(f'Bucket Name --> {bucket.name}')

my_bucket = s3.Bucket(BUCKET_NAME)
for my_bucket_object in my_bucket.objects.all():
    print(f'Bucket Content --> {my_bucket_object.key}')

s3 = boto3.client('s3')
with open('iocs.csv', 'wb') as f:
    s3.download_fileobj('s3-csv-test-bucket', 'iocs.csv', f)

#s3 = boto3.client('s3')
#s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')





#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html