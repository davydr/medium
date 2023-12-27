Change lines 9, 10 and 11 for your S3 files. Set the folder path to "" if your files are directly in your bucket   

If you want a list of AWS Polly voices use a command like this:  
```aws polly describe-voices --language-code en-US```  

If you just have local file you want to convert to mp3 use this command  
```aws polly synthesize-speech --text-type ssml --text file://greeting-script.txt --output-format mp3 --voice-id "Danielle" "polly-audio-$(date +%Y%m%d-%H%M%S).mp3```  

There is no way to send AWS Polly a location of a s3 file directly with the CLI. You have to use something like this python code for the SDK to manipulate S3 with Polly  
