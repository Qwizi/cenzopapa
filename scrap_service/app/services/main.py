import abc
import logging

import httpx
from fastapi.encoders import jsonable_encoder

from app.schemas.images import ImageList

logger = logging.getLogger(__name__)


def send_to_master(data):
    return httpx.post(f"http://master_service:8000/api/v1/process_images/", json=data,
                      headers={"Content-Type": "application/json; charset=utf-8"})


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

    def send_images_to_process(self, initial_scrap=False):
        try:
            logger.info(f"Pobieranie danych rozpoczete")
            self.scrap(initial_scrap)
        except Exception as e:
            logger.error(e)
