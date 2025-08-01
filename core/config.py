import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class DBConfig(BaseModel):
    dynamo_table: str = os.getenv("DYNAMO_TABLE", "image_info")

class AWSConfig(BaseModel):
    aws_region: str = os.getenv("AWS_REGION", "eu-north-1")
    s3_bucket: str = os.getenv("S3_BUCKET", "mybucket399839194361")

class Settings(BaseModel):
    run: RunConfig = RunConfig()
    db: DBConfig = DBConfig()
    aws: AWSConfig = AWSConfig()

settings = Settings()
