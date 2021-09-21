from fastapi import APIRouter

from app.schemas.images import ImageList

process_images_router = APIRouter()


@process_images_router.post("/")
async def process_images(images: ImageList):
    print(images)
    return "123"
