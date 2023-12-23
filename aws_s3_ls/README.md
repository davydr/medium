# AWS Blog on Medium  
1) AWS Search (Linux/Mac/Windows uses aws cli, but python uses boto3). Each script searches through all of your buckets on your account. It searhces for one string or file name. You can exclude buckets that are big to reduce your search time  
   1.1) aws_search.sh  (run it like './aws_search.sh filename.txt')  
   1.2) aws_search.ps1 is for windows computers (run it like '.\aws_search.ps1 filename.txt')  
   1.3) aws_search.py is for python (run it like 'python aws_search.py filename.txt')  

2) perform an aws s3 ls command and only give the file names or look for one file
   Linux and Mac
     
   ```
   aws s3 ls s3://myBucket --recursive | awk 'NF>1{print $4}' | grep .
   ```
   ```
   aws s3 ls s3://myBucket --recursive | grep 'foo.txt'
   ```
     
   Windows:  
   ```
   aws s3 ls s3://myBucket --recursive | ForEach-Object { if ($_ -match '^\S+\s+\S+\s+\S+\s+(.+)$') { $matches[1] } }
   ```
   ```
   aws s3 ls s3://myBucket --recursive | Select-String 'foo.txt'
   ```

 
   
Please see aws cli instructions if you are just starting out:  
https://github.com/davydr/medium/blob/main/README.md  
