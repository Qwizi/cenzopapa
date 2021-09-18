import json
from typing import List

from fastapi import APIRouter, Body
from fastapi.openapi.models import RequestBody
from starlette.requests import Request
from starlette.responses import Response

from .models import ImageModel, ImageProcessModel

process_images_router = APIRouter()


@process_images_router.post('/')
async def process_images(request: Request):
    images = await request.json()
    img = json.loads(images)
    for image in img:
        imageModel = ImageModel(remote_image_url=image["remote_image_url"], created_at=image['created_at'])
        print(imageModel)
    return 123
