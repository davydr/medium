import boto3
from contextlib import closing

# Create a client for S3 and Polly
s3 = boto3.client('s3')
polly = boto3.client('polly')

# Fixed bucket name and voice ID
bucket_name = 'fixed-bucket-name' #Chgange this to your bucket name
voice_id = 'Danielle' # Change this to any voice
folder_path = 'ssml/done/'  # Folder path in the S3 bucket

# Ask the user for the name of the SSML file in the S3 bucket
input_file_name = input("Enter the name of the SSML file in the S3 bucket: ")
full_input_path = folder_path + input_file_name  # Full path to the file in S3
output_file_name = input("Enter the desired name for the output MP3 file (without extension): ") + ".mp3"

# Retrieve the SSML text from the S3 file
s3_object = s3.get_object(Bucket=bucket_name, Key=full_input_path)
ssml_text = s3_object['Body'].read().decode('utf-8')

# Synthesize speech using Polly
response = polly.synthesize_speech(
    TextType='ssml',
    Text=ssml_text,
    OutputFormat='mp3',
    VoiceId=voice_id
)

# The response's 'AudioStream' is a streaming body, so we need to read it with a context manager
with closing(response['AudioStream']) as stream:
    # Save the audio stream to the specified output file
    with open(output_file_name, 'wb') as file:
        file.write(stream.read())

print(f"Audio file saved as {output_file_name}")
