import boto3
bucket_name = 'your-s3-bucket-name'

def load_data(bucket_name, prefix):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    management_string = ""

    try:
        for obj in bucket.objects.filter(Prefix=prefix):
            if obj.key.endswith('.txt'):
                response = obj.get()
                content = response['Body'].read().decode('utf-8')
                management_string += content
    except Exception as e:
        print(f"Error: Failed to load files from S3 bucket: {e}")
        return None

    return management_string

def process_files(bucket_name):
    name_data = load_data(bucket_name, 'name/')
    tld_data = load_data(bucket_name, 'tld/')

    if name_data is None or tld_data is None:
        print("Error: Missing files in the S3 bucket.")
        return

    # Perform your desired operations with the management string
    print("Loaded name data:")
    print(name_data)
    print("Loaded TLD data:")
    print(tld_data)
    
process_files(bucket_name)