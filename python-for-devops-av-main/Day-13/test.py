import boto3

client = boto3.client('s3')

response = client.get_bucket_acl(
   Bucket='chandresh-demo-boto3',
   
) 
print(response)