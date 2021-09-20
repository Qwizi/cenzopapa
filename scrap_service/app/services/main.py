import abc
import json
import logging

import httpx

from app.utils.app_exceptions import AppException
from app.utils.service_result import ServiceResult

logger = logging.getLogger(__name__)

class HttpxClientMixin:
    def __init__(self, client: httpx.Client):
        self.client = client


class SiteMixin(HttpxClientMixin, abc.ABC):
    images = []

    def __init__(self, client: httpx.Client, site_name, site_url):
        self.site_name = site_name
        self.site_url = site_url
        super().__init__(client)

    @abc.abstractmethod
    def scrap(self, initial_scrap=False):
        pass

    def send_to_master(self, data):
        return httpx.post(f"http://master_service:8000/api/v1/process_images/", json=data)

    def send_images_to_process(self, initial_scrap=False):
        logger.info(f"Pobieranie danych rozpoczete")
        images = self.scrap(initial_scrap)
        images_models = json.dumps(images, indent=4, sort_keys=True, default=str)
        if images:
            response = self.send_to_master(images_models)
            if response.status_code != 200:
                logger.error("Nie udalo się przeslac zdjec")
            logger.info("Zdjecia zostaly przeslane")
