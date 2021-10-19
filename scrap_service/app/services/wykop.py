import datetime
import logging
from abc import ABC
from time import sleep

from bs4 import BeautifulSoup
from fastapi.encoders import jsonable_encoder

from ..schemas.images import Image, ImageList
from ..services.main import SiteMixin, send_to_master

logger = logging.getLogger(__name__)


class WykopScrapService(SiteMixin, ABC):
    cenzo_tag = "multimedia-tag/cenzopapa"

    def scrap(self, days: int = 1, years: int = None):
        page_number = 0
        repeat = True
        try:
            while repeat:
                images_list = []
                page_number += 1
                url = f'{self.site_url}/{self.cenzo_tag}/strona/{page_number}/'
                response = self.client.get(url)
                logger.info(f"Zaczynam pobierac dane ze strony {url}")
                if response.status_code == 503:
                    repeat = False
                    logger.error("Wystąpil problem z zapytaniem")

                bs = BeautifulSoup(response.content, 'html.parser')

                rel_images = bs.find_all("div", class_="rel image")
                if not rel_images:
                    logger.error("Nie znaleziono zdjec z papajem")
                    repeat = None
                else:
                    for rel_image in rel_images:
                        logger.info(rel_image)
                        image = rel_image.find("img")
                        time = rel_image.find("time")
                        datetime_time = time.attrs["datetime"]
                        datetime_time = datetime.datetime.strptime(datetime_time[:-6], '%Y-%m-%dT%H:%M:%S')
                        height = int(float(image.get("data-height", 600)))
                        width = int(float(image.get("data-width", 400)))
                        logger.info(f"Wysokosc: {height}, szerokosc: {width}")

                        if datetime_time <= self.get_datetime(days, years):
                            repeat = False
                        """
                        if initial_scrap:
                            if datetime_time < two_years_ago:
                                repeat = False
                        else:
                            if datetime_time < week_ago:
                                repeat = False
                        """
                        logger.info(f"[cenzopapa] -> {image['src']} | {datetime_time}")
                        image = Image(
                            remote_image_url=image['src'],
                            created_at=datetime_time,
                            height=height,
                            width=width
                        )
                        images_list.append(image)
                sleep(2)

                if len(images_list) > 0:
                    images_list_ = ImageList(images=images_list)
                    images_list_json = images_list_.dict()
                    images_list_json_data = jsonable_encoder(images_list_json)
                    logger.info(f"Ilosc zdjec: {len(images_list)}")
                    callback_response = send_to_master(images_list_json_data)
                    logger.info(f"Wynik zapytania do callbacka -> {callback_response.status_code}")
                    if callback_response.status_code != 200:
                        logger.error("Nie udalo się przeslac zdjec")
                    else:
                        logger.info(f"Przesłano {len(images_list)}")
        except Exception as e:
            logger.error(e)
            repeat = False
