import logging

from ..core.db import Image
from ..services.main import FireStorageMixin

logger = logging.getLogger(__name__)


class ProcessImageService(FireStorageMixin):
    async def process(self, images_list):
        try:
            for image in images_list.images:
                image_exists = await Image.objects.filter(remote_image_url=image.remote_image_url).exists()
                if not image_exists:
                    filename, extension, public_url = self.bucket.upload(image)
                    if filename and extension and public_url:
                        new_image = await Image.objects.create(
                            filename=filename,
                            extension=extension,
                            public_url=public_url,
                            remote_image_url=image.remote_image_url
                        )
                        logger.info(new_image)

        except Exception as exc:
            logger.error("Somethink went wrong")
            pass

