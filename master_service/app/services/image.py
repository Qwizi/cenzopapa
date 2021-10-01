import logging
import sys
from random import randint

from ormar import NoMatch

from ..schemas.images import ImageDBOut, ImageStats
from ..utils.app_exceptions import AppException
from ..utils.service_result import ServiceResult
from ..core.db import Image

logger = logging.getLogger(__name__)


class ImageService:
    @staticmethod
    async def get_last_10_images():
        images = await Image.objects.order_by("-id").limit(10).fields(["public_url"]).all()
        images_list = []
        for i in images:
            image = ImageDBOut(url=i.public_url)
            images_list.append(image)
        if not images:
            return ServiceResult(AppException.AppError("Images list is empty"))
        if not images_list:
            return ServiceResult(AppException.AppError("ImagesDBOut list is empty"))
        return ServiceResult(images_list)

    @staticmethod
    async def get_random_image():
        try:
            last_image = await Image.objects.get()
            random_id = randint(1, last_image.id)
            random_image = await Image.objects.get(id=random_id)
            image = ImageDBOut(url=random_image.public_url)
            return ServiceResult(image)
        except NoMatch:
            logger.error("Image not found")
            return ServiceResult(AppException.ImageError("Image not found"))
        except:
            logger.error(f"Unexpected error {sys.exc_info()[0]}")
            raise

    @staticmethod
    async def get_images_count():
        try:
            count = await Image.objects.count()
            if not count:
                return ServiceResult(AppException.ImageError("Somethink went wrong"))
            return ServiceResult(ImageStats(count=count))
        except Exception:
            logger.error(f"Somethink went wrong")
            return ServiceResult(AppException.ImageError("Somethink went wrong"))
