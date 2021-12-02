from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from time import sleep

import requests
from bs4 import BeautifulSoup

from images.models import Image


class ScrapService(object):
    site_url = "https://wykop.pl/multimedia-tag/cenzopapa"

    def __init__(self):
        self.client = requests.session()

    @staticmethod
    def get_sleep_values():
        return [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3]

    @staticmethod
    def get_datetime(days: int = 1, years: int = None) -> datetime:
        if not years:
            return datetime.now() - timedelta(days=days)
        return datetime.now() - timedelta(days=days * years)

    @staticmethod
    def __create_new_image(image):
        image_exists = Image.objects.filter(url=image['url']).exists()
        new_image = None
        print(image)
        if not image_exists:
            new_image = Image.objects.create(
                posted_at=make_aware(image['posted_at']),
                width=image['width'],
                height=image['height'],
                url=image['url'],
                author_id=1,
            )
        return new_image

    def __check_time(self, datetime_time_el, days=7, years=None):
        return datetime_time_el <= self.get_datetime(days, years)

    def __get_scrap_image(self, image):
        img_el = image.find("img")
        time_el = image.find("time")
        datetime_time_el = time_el.attrs['datetime']
        datetime_time_el = datetime.strptime(datetime_time_el[:-6], '%Y-%m-%dT%H:%M:%S')
        height = int(float(img_el.get("data-height", 600)))
        width = int(float(img_el.get("data-width", 400)))

        return {
            "posted_at": datetime_time_el,
            "height": height,
            "width": width,
            "url": img_el['src']
        }

    def scrap(self, days: int = 1, years: int = None):
        page_number = 0
        repeat = True
        while repeat:
            page_number += 1
            url = f"{self.site_url}/strona/{page_number}"
            response = self.client.get(url)
            if response.status_code == 503:
                repeat = False
            bs = BeautifulSoup(response.text, 'html.parser')
            scrape_images = bs.find_all("div", class_="rel image")
            if not scrape_images:
                repeat = False
            else:
                for image in scrape_images:
                    img_dict = self.__get_scrap_image(image)
                    if self.__check_time(img_dict['posted_at'], days=days, years=years):
                        repeat = False
                    new_image = self.__create_new_image(img_dict)
                    print(new_image)
            sleep(2)
