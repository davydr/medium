In order to use most aws command line tools you need  
1) Establish an account that has access keys
2) Use these access keys to perform actions with the cli

You can make the account using IAM on the aws console (console.aws.com) and give the account limited or all access on your account  
These access keys are like a username and password combination  
AWS_ACCESS_KEY_ID == username    
AWS_SECRET_ACCESS_KEY == password  

You should protect both of them like they are credentials   

You can follow these steps to add aws cli to your computer  
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html  

You can follow these ssteps to add your keys to your computer:   
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html  

After loading the aws tool on your computer these are an example of configuring your keys on your computer  
>> aws configure  

AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE  
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY  
Default region name [None]: us-west-2  
Default output format [None]: json  

You'll see these example under "Configuring using AWS CLI commands" under the "Long-term credentials' tab  

If you have multiple accounts or keys you need to create a profile for every set of keys you add to your computer  
