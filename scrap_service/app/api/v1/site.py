import json
from abc import abstractmethod, ABC
from datetime import datetime

import httpx

from app.core.config import settings
from .models import ImageProcessModel, ImageModel


class Site(ABC):
    site_name: str
    site_url: str
    session: any

    def run(self):
        images = self.scrap_images(initial_scrap=False)
        images_models = json.dumps(images, indent=4, sort_keys=True, default=str)
        #print(images_models)
        response = httpx.post(f"http://master_service:8000/api/v1/process_images/", json=images_models)
        print(response)
        return 123

    @abstractmethod
    def scrap_images(self, initial_scrap=False):
        pass
