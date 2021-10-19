import abc
import logging
from datetime import datetime, timedelta

import httpx
from fastapi.encoders import jsonable_encoder

from app.schemas.images import ImageList

logger = logging.getLogger(__name__)


def send_to_master(data):
    return httpx.post(f"http://master_service:8000/process_images/", json=data,
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

    @staticmethod
    def get_datetime(days: int = 1, years: int = None) -> datetime:
        if not years:
            return datetime.now() - timedelta(days=days)
        return datetime.now() - timedelta(days=days * years)

    def send_images_to_process(self, days, years):
        try:
            logger.info(f"Pobieranie danych rozpoczete")
            self.scrap(days, years)
        except Exception as e:
            logger.error(e)
