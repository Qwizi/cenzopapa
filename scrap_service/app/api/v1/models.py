import datetime

from pydantic import BaseModel

class ImageModel(BaseModel):
    remote_image_url: str
    created_at: datetime.datetime

class ImageProcessModel(BaseModel):
    images: list[ImageModel]

