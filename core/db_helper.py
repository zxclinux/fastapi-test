import boto3
from core.config import settings

dynamodb = boto3.resource("dynamodb", region_name=settings.aws.aws_region)
table = dynamodb.Table(settings.db.dynamo_table)

def save_metadata(metadata: dict):
    table.put_item(Item=metadata)

def get_metadata(image_id: str):
    response = table.get_item(Key={"imageid": image_id})
    return response.get("Item")