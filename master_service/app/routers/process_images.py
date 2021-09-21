from fastapi import APIRouter
from starlette.background import BackgroundTasks

from app.schemas.images import ImageList

from ..services.main import FireStoreService, FireStorageService
from ..utils.firebase import db, bucket

process_images_router = APIRouter()


def process(images_list):
    for image in images_list.images:
        firestore_service = FireStoreService(db)
        image_exists = firestore_service.exists("images", "remote_image_url", "==",
                                                image.remote_image_url)
        if not image_exists:
            firestorage_service = FireStorageService(bucket)
            filename, extension, public_url = firestorage_service.upload(image)
            new_image = firestore_service.add("images", image, filename, extension, public_url)
            print(new_image)


@process_images_router.post("/")
async def process_images(images_list: ImageList, background_tasks: BackgroundTasks):
    background_tasks.add_task(process, images_list)

    return None
