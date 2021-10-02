from fastapi import APIRouter
from fastapi_pagination import Page

from app.utils.service_result import handle_result
from ..core.db import Image
from ..services.image import ImageService

images_router = APIRouter()


@images_router.get("/", response_model=Page[Image], response_model_exclude_none=True)
async def last_10_images():
    results = await ImageService.get_last_10_images()
    return handle_result(results)


@images_router.get("/random", response_model=Image, response_model_exclude_none=True)
async def random():
    results = await ImageService.get_random_image()
    return handle_result(results)