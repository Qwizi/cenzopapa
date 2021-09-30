import logging

from fastapi import APIRouter
from starlette.background import BackgroundTasks

from app.schemas.images import ImageList
from ..core.db import Image

from ..services.main import FireStoreService, FireStorageService
from ..utils.firebase import db, bucket

logger = logging.getLogger(__name__)
process_images_router = APIRouter()


async def process(images_list):
    for image in images_list.images:
        image_exists = await Image.objects.filter(remote_image_url=image.remote_image_url).exists()
        if not image_exists:
            firestorage_service = FireStorageService(bucket)
            filename, extension, public_url = firestorage_service.upload(image)
            if filename and extension and public_url:
                new_image = await Image.objects.create(
                    filename=filename,
                    extension=extension,
                    public_url=public_url,
                    remote_image_url=image.remote_image_url
                )
                logger.info(new_image)


@process_images_router.post("/")
async def process_images(images_list: ImageList, background_tasks: BackgroundTasks):
    background_tasks.add_task(process, images_list)

    return None
