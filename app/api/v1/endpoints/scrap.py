from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from scrapp.site_manager import site_manager
router = APIRouter()


@router.post("/scrap/")
def scrap(background_tasks: BackgroundTasks):
    sites = site_manager.get_sites()
    for site in sites:
        background_tasks.add_task(site['site_class'].run)
    return JSONResponse()
