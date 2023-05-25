import boto3

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

bucket_name = 'nameo-data'

# List objects in the bucket
objects = s3_client.list_objects_v2(Bucket=bucket_name)
for obj in objects['Contents']:
    print(obj['Key'])

# Upload a file to the bucket
s3_client.upload_file('local-file.txt', bucket_name, 'remote-file.txt')

# Download a file from the bucket
s3_client.download_file(bucket_name, 'remote-file.txt', 'local-file.txt')

# Delete a file from the bucket
s3_client.delete_object(Bucket=bucket_name, Key='remote-file.txt')
