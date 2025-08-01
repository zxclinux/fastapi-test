from pydantic import BaseModel

class ImageMetadata(BaseModel):
    imageid: str
    filename: str
    size: int
    url: str
