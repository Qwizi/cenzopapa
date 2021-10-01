import logging
import os
import uuid

import httpx
from firebase_admin import firestore

from app.schemas.images import Image
from .watermark import WatermarkService
from ..schemas.images import ImageDBModel
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


class FireStorageMixin:
    def __init__(self, bucket):
        self.bucket = bucket

class FireStorageService(FireStorageMixin):
    def __init__(self, bucket, watermark_service: WatermarkService):
        super().__init__(bucket)
        self.watermark_service = watermark_service

    @staticmethod
    def get_filename_extension(url):
        path = urlparse(url).path
        extension = str(os.path.splitext(path)[1])
        filename = str(uuid.uuid4())
        full_filename = f"{filename}{extension}"
        return filename, extension, full_filename

    @staticmethod
    def remove_file_from_temp(path):
        if os.path.exists(path):
            os.remove(path)

    def download(self, image: Image):
        try:
            response = httpx.get(image.remote_image_url)
            response.raise_for_status()
            if response.status_code != 200:
                logger.error("Error response status code")
            else:
                filename, extension, full_filename = self.get_filename_extension(image.remote_image_url)
                path = f"app/temp/{full_filename}"
                file = open(path, "wb")
                file.write(response.content)
                file.close()
                return path
        except httpx.RequestError as exc:
            logger.error(f"An error occurred while requesting {exc.request.url!r}.")
        except httpx.HTTPStatusError as exc:
            logger.error(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")

    def upload(self, image: Image):
        try:
            if image and image.remote_image_url != "":
                path = self.download(image)
                filename, extension, full_filename = self.get_filename_extension(image.remote_image_url)
                self.watermark_service.add_watermark(path)
                blob = self.bucket.blob(full_filename)
                blob.upload_from_filename(path)
                blob.make_public()
                self.remove_file_from_temp(path)
                if filename and extension and blob.public_url:
                    return filename, extension, blob.public_url
                return None, None, None
        except Exception as exc:
            logger.error(exc)
            raise
