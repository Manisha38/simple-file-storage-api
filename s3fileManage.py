import boto3
import settings
import json
from botocore.client import ClientError


def getClient():
	client = boto3.client('s3', 
                  aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY, 
                  aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY, 
                  region_name=settings.REGION_NAME
            )
	return client


def aws_fCreate(name):
	try:
		client = getClient()
		response = client.put_object(Bucket=settings.bucketname,Key=name)
	except ClientError as e:
		if e.response['Error']['Code'] =='NoSuchBucket':
			return "Bucket does not exists"
	if response['ResponseMetadata']['HTTPStatusCode']==200:
		return "Created File"


def aws_fOpen(name):
	try:
		s3 = boto3.resource('s3')
		obj = s3.Object(settings.bucketname,name)
		string = obj.get()['Body'].read().decode('utf-8')
		return string
	except ClientError as e:
		responseCode = e.response['Error']['Code'] 
		if responseCode=='404' or responseCode=='NoSuchKey':
			return "File does not exists"
	

def aws_fRename(old_name,new_name):
	s3 = boto3.resource('s3')
	bucket = settings.bucketname
	try:
		response=s3.Object(bucket,new_name).copy_from(CopySource=bucket+'/'+old_name)
		s3.Object(bucket,old_name).delete()
		if response['ResponseMetadata']['HTTPStatusCode']==200:
			return "File name changed"

	except ClientError as e:
		if e.response['Error']['Code'] == 'NoSuchKey':
			return 'File does not exists'
		elif e.response['Error']['Code'] == 'NoSuchBucket':
			return 'Bucket does not exists'


def aws_fgetAttr(name):
	try:
		client = getClient()
		response = client.head_object(Bucket=settings.bucketname, Key =name)
	except ClientError as e:
		if e.response['Error']['Code']=='404':
			return "File not found"
	file_attrs = {}
	file_attrs['LastModified'] = response['LastModified'].strftime("%Y %m %d %H:%M:%S")
	file_attrs['Size'] = response['ContentLength']
	file_attrs['Type'] = response['ContentType']
	return json.dumps(file_attrs)


def aws_fDelete(name):
	s3 = boto3.resource('s3')
	obj = s3.Object(settings.bucketname, name)
	response = obj.delete()
	return "Deleted file"

