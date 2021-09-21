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
            images = self.scrap(initial_scrap)
            images_list = ImageList(images=images)
            images_list_json = images_list.dict()
            images_list_json_data = jsonable_encoder(images_list_json)

            logger.info(f"Json: {images_list}")
            logger.info(f"Ilosc zdjec: {len(images)}")

            callback_response = send_to_master(images_list_json_data)
            logger.info(f"Wynik zapytania do callbacka -> {callback_response.status_code}")

            if callback_response.status_code != 200:
                logger.error("Nie udalo się przeslac zdjec")
            else:
                logger.info(f"Przesłano {len(images)}")
        except Exception as e:
            logger.error(e)
