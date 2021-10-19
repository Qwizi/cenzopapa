from starlette.background import BackgroundTasks

from ..services.main import SiteMixin
from ..utils.app_exceptions import AppException
from ..utils.service_result import ServiceResult


class ScrapService:

    def __init__(self, background_tasks: BackgroundTasks, sites, initial_scrap=False):
        self.background_tasks = background_tasks
        self.sites = sites
        self.initial_scrap = initial_scrap
        
    def run_sites_scrap(self, days, years):
        result = []
        if not self.sites:
            return ServiceResult(AppException.ScrapFailed({"detail": "List of sites is empty"}))
        for site in self.sites:
            if not isinstance(site, SiteMixin):
                return ServiceResult(AppException.ScrapFailed({"detail": "Site is not a instance of SiteMixin"}))
            self.background_tasks.add_task(site.send_images_to_process, days, years)
            result.append({
                "site": site.site_name
            })
        return ServiceResult(result)
            
