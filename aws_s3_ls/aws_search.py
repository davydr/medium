import boto3
import sys

# Check if a search string is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <search-string>")
    sys.exit(1)

search_string = sys.argv[1]

# Create an S3 client
s3_client = boto3.client('s3')

# Enumerate all S3 buckets
response = s3_client.list_buckets()

# Define exclusion patterns
excluded_buckets = ['cloudtrail', 'logs', 'backup']

for bucket in response['Buckets']:
    bucket_name = bucket['Name']

    # Check if the bucket name matches any of the exclusion patterns
    if not any(excluded in bucket_name for excluded in excluded_buckets):
        print(f"Searching in bucket: {bucket_name}")

        # List objects in the bucket
        paginator = s3_client.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket_name)

        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    if search_string in obj['Key']:
                        print(f"Found {search_string} in {obj['Key']}")

    else:
        print(f"Skipping excluded bucket: {bucket_name}")
