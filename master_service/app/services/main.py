import logging
import os
import uuid

import httpx
from firebase_admin import firestore

from app.schemas.images import Image
from ..schemas.images import ImageDBModel
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


class FireStoreMixin:
    def __init__(self, db):
        self.db = db


class FireStorageMixin:
    def __init__(self, bucket):
        self.bucket = bucket


class FireBaseMixin(FireStoreMixin, FireStorageMixin):
    pass


class FireStoreService(FireStoreMixin):
    @staticmethod
    def get_result(stream):
        s = None
        for r in stream:
            s = r.to_dict()
        return s

    def exists(self, collection: str = 'images', column_name: str = 'remote_image_url', operator: str = "==",
               value: str = "none", limit: int = 1):
        query = self.db.collection(collection).where(column_name, operator, value).limit(limit).stream()
        if self.get_result(query):
            return True
        return False

    def get_last(self, collection: str, order_id="id"):
        last_collection_ref = self.db.collection(collection)
        query = last_collection_ref.order_by(order_id, direction=firestore.Query.DESCENDING).limit(1).stream()
        return self.get_result(query)

    def add(self, collection: str, image: Image, filename, extension, public_url):
        last_img = self.get_last(collection)
        data = {
            "id": last_img['id'] + 1 if last_img is not None else 1,
            "filename": f"{filename}",
            "extension": extension,
            "public_url": public_url
        }
        data.update(image.dict())
        self.db.collection(collection).add(data)
        new_image = self.get_result(self.db.collection(collection).where("id", "==", data["id"]).limit(1).stream())
        new_image_model = ImageDBModel.parse_obj(new_image)
        return new_image_model


class FireStorageService(FireStorageMixin):

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
                blob = self.bucket.blob(full_filename)
                blob.upload_from_filename(path)
                blob.make_public()
                self.remove_file_from_temp(path)
                if filename and extension and blob.public_url:
                    return filename, extension, blob.public_url
                return None, None, None
        except Exception as exc:
            logger.error(exc)

