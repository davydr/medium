#!/bin/bash

# Script to search for a file or file string in all S3 buckets, excluding large log buckets
#!/bin/bash

# Script to search for a specified file pattern in all S3 buckets,
# excluding specified buckets.

# Check if a search string is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <search-string>"
    exit 1
fi

# The search string is taken from the first command line argument
SEARCH_STRING=$1

for bucket in $(aws s3 ls | awk '{print $3}'); do
    # Check if the bucket name matches any of the exclusion patterns
    if [[ $bucket != *"cloudtrail"* && $bucket != *"logs"* && $bucket != *"backup"* ]]; then
        echo "Searching in bucket: $bucket"
        aws s3 ls "s3://$bucket/" --recursive | grep "$SEARCH_STRING"
    else
        echo "Skipping excluded bucket: $bucket"
    fi
done
