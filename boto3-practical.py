import boto3

client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket='lahiru-demo-boto3-001'
)
print(response)