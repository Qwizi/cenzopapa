from scrap.utils import ScrapService


def scrap_images(days: int = 7, years: int = None):
    scrap_service = ScrapService()
    scrap_service.scrap(days=days, years=years)
