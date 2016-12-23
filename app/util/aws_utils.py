import boto3
import boto3.session
import os

def upload_to_s3(filename, username):
    session = boto3.session.Session(region_name='ap-south-1')
    s3client = session.client('s3', config=boto3.session.Config(signature_version='s3v4'))
    data= open(filename)
    print 'uploading file {} to S3'.format(filename)
    print s3client.put_object(Bucket='atharva', Body=data, ACL='private', Key=os.path.basename(filename))