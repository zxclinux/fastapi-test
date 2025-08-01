import boto3
import uuid
from core.config import settings

s3 = boto3.client("s3", region_name=settings.aws.aws_region)

def upload_file(file) -> dict:
    image_id = str(uuid.uuid4())
    key = f"uploads/{image_id}_{file.filename}"

    s3.upload_fileobj(file.file, settings.aws.s3_bucket, key)

    return {
        "imageid": image_id,
        "filename": file.filename,
        "size": file.size,
        "url": f"https://{settings.aws.s3_bucket}.s3.{settings.aws.aws_region}.amazonaws.com/{key}"
    }
