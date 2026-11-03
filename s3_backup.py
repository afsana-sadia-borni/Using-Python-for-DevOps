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


def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket="bucket_name",
                     CreateBuucketConfiguration={
                         'LocationConstraint' : region,
                     },) #bucket name create 
    print("bucket created successfully")
#backup file upload in s3
def upload_backup(s3, file_name, bucket_name, key_name):
    data=open(file_name, 'rb')#read binary hocche
    s3.Bucket(bucket_name).put_object(key=key_name)
    print("backup uploaded successfuully!!!")







bucket_name="python_for_devops"
region="us-east-2"
#create_bucket(s3)
#show_bucket(s3)
file_name="/Users/apple/Documents/cpu/backups/backup_2026-10-31.tar.gz" #paste backup path
key="my_backup.tar.gz"
upload_backup(s3, file_name, bucket_name, key )