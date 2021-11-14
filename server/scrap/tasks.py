from images.models import Image
from scrap.utils import ScrapService


def scrap_images(days: int = 365, years: int = 2):
    scrap_service = ScrapService()
    images = scrap_service.scrap(days=days, years=years)
    for image in images:
        if not Image.objects.filter(remote_image_url=image['remote_image_url']).exists():
            new_image = Image.objects.create(
                remote_image_url=image['remote_image_url'],
                posted_at=image['posted_at'],
                width=image['width'],
                height=image['height'],
                public_url=image['remote_image_url'],
                author_id=1,
            )
            print(new_image)

