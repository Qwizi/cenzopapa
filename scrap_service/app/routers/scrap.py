import httpx
from fastapi import APIRouter
from starlette.background import BackgroundTasks

from app.services.scrap import ScrapService
from app.services.wykop import WykopScrapService
from app.utils.service_result import handle_result

scrap_router = APIRouter()


@scrap_router.post("/scrap/")
def scrap_sites(background_tasks: BackgroundTasks, initial_scrap: bool = False):
    sites = [
        WykopScrapService(client=httpx.Client(), site_name="Wykop", site_url="https://www.wykop.pl")
    ]

    result = ScrapService(background_tasks, sites=sites).run_sites_scrap(initial_scrap)
    return handle_result(result)
