import boto3    
from glob import glob

s3 = boto3.resource('s3')

for file in glob(f'coleta/*.json'):
    s3object = s3.Object('tiktokbrands-bucket', file)
    s3object.put(
    Body=(file))

# class classS3:
#     def __init__(self, bucket_name):
#         self.bucket_name = bucket_name
#         self.s3 = boto3.resource('s3')
#         self.client = boto3.client('s3')

#     def upload_file(self, file_name):
#         s3object = s3.Object(self.bucket_name, file_name)
#         s3object.put(
#         Body=(file_name))