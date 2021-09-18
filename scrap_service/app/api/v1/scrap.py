from datetime import datetime

from fastapi import APIRouter
from starlette.background import BackgroundTasks
from starlette.responses import JSONResponse

from app.api.v1.models import ImageProcessModel, ImageModel
from app.api.v1.site_manager import site_manager

import httpx

from app.core.config import settings

scrap_router = APIRouter()


@scrap_router.post("/scrap/")
async def home(background_tasks: BackgroundTasks):
    sites = site_manager.get_sites()
    for site in sites:
        background_tasks.add_task(site['site_class'].run)
    return JSONResponse()


@scrap_router.get("/test/")
def test():
    images = ImageProcessModel(images=[ImageModel(remote_image_url="asdasd", created_at=datetime.now())])
    response = httpx.post("http://master_service:8000/api/v1/process_images/", data={
        "images": images.dict()
    })
    print(response.content)
    return True

