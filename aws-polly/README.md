Change lines 9, 10 and 11 for your S3 files  

If you want a list of AWS Polly voices use a command like this:  
```aws polly describe-voices --language-code en-US

If you just have local file you want to convert to mp3 use this command
```aws polly synthesize-speech --text-type ssml --text file://greeting-script.txt --output-format mp3 --voice-id "Danielle" "polly-audio-$(date +%Y%m%d-%H%M%S).mp3  
