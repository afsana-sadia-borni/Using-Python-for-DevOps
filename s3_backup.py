"""summary_line
This is a script to backup from local to Aws s3
boto3:- used to do AWS tasks using python 
"""
"""
treminal : aws configure 
"""
import boto3
s3=boto3.resource("s3")
def show_bucket():
    for bucket in s3.buckets.all():
        print(bucket.name)
def create_bucket(s3):
    s3.create_bucket(Bucket="local_to_aws_s3_bucket",
                     CreateBuucketConfiguration={
                         'LocationConstraint : 'us-east-2',
                     },) #bucket name create 
    print("bucket created successfully")

create_bucket(s3)
show_bucket(s3)