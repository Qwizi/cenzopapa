from images.models import Image
from scrap.utils import ScrapService


def scrap_images(days: int = 7, years: int = None):
    scrap_service = ScrapService()
    images = scrap_service.scrap(days=days, years=years)
    remote_image_urls = []
    for image in images:
        remote_image_urls.append(image['remote_image_url'])
    images_exists = Image.objects.filter(remote_image_url__in=remote_image_urls).values("remote_image_url")
    if not images_exists:
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
    print(remote_image_urls)

