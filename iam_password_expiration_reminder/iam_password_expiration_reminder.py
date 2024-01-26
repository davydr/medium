import boto3
import csv
import io
import datetime
import holidays
import json

def is_weekend_or_holiday(date):
    us_holidays = holidays.UnitedStates()
    return date.weekday() >= 5 or date in us_holidays

def get_user_arn_mapping(s3_bucket, s3_key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
    mapping_str = response['Body'].read().decode('utf-8')
    return json.loads(mapping_str)

def lambda_handler(event, context):
    iam = boto3.client('iam')
    sns = boto3.client('sns')

    # Load IAM user to SNS ARN mapping from S3
    user_arn_mapping = get_user_arn_mapping('your-s3-bucket-name', 'your-s3-key.json')

    # Generate and retrieve the credential report
    iam.generate_credential_report()
    response = iam.get_credential_report()
    report = csv.DictReader(io.StringIO(response['Content'].decode('utf-8')))
    
    for row in report:
        username = row['user']
        if 'password_next_rotation' in row and username in user_arn_mapping:
            next_rotation_str = row['password_next_rotation']
            if next_rotation_str:
                next_rotation = datetime.datetime.strptime(next_rotation_str, '%Y-%m-%dT%H:%M:%S+00:00')
                if next_rotation - datetime.datetime.now() < datetime.timedelta(days=7):  # Within 7 days
                    if not is_weekend_or_holiday(datetime.datetime.now()):
                        # Send SNS Notification
                        sns.publish(
                            TopicArn=user_arn_mapping[username], 
                            Message=f"Password for user {username} will expire soon.",
                            Subject='Password Expiration Alert'
                        )

    return "Password expiration check complete"
