from datetime import datetime
from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    remote_image_url: str
    created_at: datetime
    height: int
    width: int


class ImageList(BaseModel):
    images: List[Image]
