import random

from fastapi import APIRouter

from ..core.db import Image
from ..schemas.images import ImageDBOut, ImageStats

cenzo_router = APIRouter()


@cenzo_router.get("/", response_model=list[ImageDBOut])
async def cenzo_last_10_images():
    images = await Image.objects.order_by("-id").limit(10).all()
    images_list = []
    for i in images:
        image = ImageDBOut(url=i.public_url)
        images_list.append(image)
    return images_list

@cenzo_router.get("/random", response_model=ImageDBOut)
async def cenzo_random():
    last_image = await Image.objects.get()
    random_id = random.randint(1, last_image.id)
    random_image = await Image.objects.get(id=random_id)
    image = ImageDBOut(url=random_image.public_url)
    return image


@cenzo_router.get("/stats")
async def cenzo_stats():
    cenzo_count = await Image.objects.count()
    return ImageStats(count=cenzo_count)