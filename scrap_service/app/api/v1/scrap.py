from fastapi import APIRouter
from starlette.background import BackgroundTasks
from starlette.responses import JSONResponse

from app.api.v1.site_manager import site_manager

scrap_router = APIRouter()


@scrap_router.post("/scrap/")
async def home(background_tasks: BackgroundTasks):
    sites = site_manager.get_sites()
    for site in sites:
        background_tasks.add_task(site['site_class'].run)
    return JSONResponse()
