 import boto3
 import datetime
 s3 = boto3.client('s3')
 
 files = s3.list_objects_v2(Bucket='my-bucket')['Contents']
 old_files = [{'Key': file['Key']} for file in files if file['LastModified'] < datetime.now() - timedelta(days=2)]
 s3.delete_objects(Bucket='my-bucket', Delete={'Objects': old_files}) 
