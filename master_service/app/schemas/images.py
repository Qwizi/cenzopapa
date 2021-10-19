import uuid
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Image(BaseModel):
    remote_image_url: str
    created_at: datetime
    height: int
    width: int


class ImageList(BaseModel):
    images: List[Image]


class ImageDBModel(Image):
    id: int
    filename: Optional[UUID] = Field(default_factory=uuid4)
    extension: Optional[str] = None
    public_url: str


class ImageDBOut(BaseModel):
    url: str


class ImageStats(BaseModel):
    count: int
