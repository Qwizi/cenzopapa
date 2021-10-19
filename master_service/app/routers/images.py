from fastapi import APIRouter
from fastapi_crudrouter import OrmarCRUDRouter

from app.utils.service_result import handle_result
from ..core.db import Image
from ..schemas import ImageStats
from ..services.images import ImageService

images_router = APIRouter()

crud_images_router = OrmarCRUDRouter(
    schema=Image,
    create_route=False,
    delete_one_route=False,
    update_route=False,
    delete_all_route=False,
    prefix="images",
    paginate=10
)


@images_router.get("/random", response_model=Image, response_model_exclude_none=True)
async def random():
    results = await ImageService.get_random_image()
    return handle_result(results)


@images_router.get("/count", response_model=ImageStats)
async def count():
    images_count = await ImageService.get_images_count()
    return handle_result(images_count)
