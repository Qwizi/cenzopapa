import random
from datetime import datetime, timedelta
from time import sleep

import requests
from bs4 import BeautifulSoup


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

    def scrap(self, days: int = 1, years: int = None):
        page_number = 0
        repeat = True
        while repeat:
            images = []
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
                    img_el = image.find("img")
                    time_el = image.find("time")
                    datetime_time_el = time_el.attrs['datetime']
                    datetime_time_el = datetime.strptime(datetime_time_el[:-6], '%Y-%m-%dT%H:%M:%S')
                    height = int(float(img_el.get("data-height", 600)))
                    width = int(float(img_el.get("data-width", 400)))
                    if datetime_time_el <= self.get_datetime(days, years):
                        repeat = False
                    image_dict = {
                        "remote_image_url": img_el['src'],
                        "posted_at": datetime_time_el,
                        "height": height,
                        "width": width
                    }
                    images.append(image_dict)
            sleep(random.choice(self.get_sleep_values()))
            print(images)
            return images