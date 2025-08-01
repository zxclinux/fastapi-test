import boto3
from PIL import Image
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        tmp_path = f"/tmp/{os.path.basename(key)}"
        s3.download_file(bucket, key, tmp_path)

        with Image.open(tmp_path) as img:
            img.thumbnail((128, 128))
            thumb_path = f"/tmp/thumb_{os.path.basename(key)}"
            img.save(thumb_path)

        dest_bucket = bucket + "-resized"
        s3.upload_file(thumb_path, dest_bucket, f"thumb_{key}")
