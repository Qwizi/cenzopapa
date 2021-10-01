from fastapi import APIRouter

from app.utils.service_result import handle_result
from ..schemas.images import ImageDBOut, ImageStats
from ..services.image import ImageService

images_router = APIRouter()


@images_router.get("/", response_model=list[ImageDBOut])
async def last_10_images():
    results = await ImageService.get_last_10_images()
    return handle_result(results)


@images_router.get("/random", response_model=ImageDBOut)
async def random():
    results = await ImageService.get_random_image()
    return handle_result(results)


@images_router.get("/stats", response_model=ImageStats)
async def stats():
    results = await ImageService.get_images_count()
    return handle_result(results)