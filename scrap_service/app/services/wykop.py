import datetime
import logging
from abc import ABC
from time import sleep

from bs4 import BeautifulSoup
from fastapi.encoders import jsonable_encoder

from app.schemas.images import Image, ImageList
from app.services.main import SiteMixin, send_to_master

logger = logging.getLogger(__name__)


class WykopScrapService(SiteMixin, ABC):
    cenzo_tag = "multimedia-tag/cenzopapa"

    def scrap(self, initial_scrap=False):
        page_number = 0
        repeat = True
        while repeat:
            images_list = []
            page_number += 1
            url = f'{self.site_url}/{self.cenzo_tag}/strona/{page_number}'
            response = self.client.get(url)
            logger.info(f"Zaczynam pobierac dane ze strony {url}")
            if response.status_code == 503:
                repeat = False
                logger.error("Wystąpil problem z zapytaniem")

            bs = BeautifulSoup(response.content, 'html.parser')

            rel_images = bs.find_all("div", class_="rel image")
            two_years_ago = datetime.datetime.now() - datetime.timedelta(days=2 * 365)
            week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
            if not rel_images:
                logger.error("Nie znaleziono zdjec z papajem")

            for rel_image in rel_images:
                image = rel_image.find("img")
                time = rel_image.find("time")
                datetime_time = time.attrs["datetime"]
                datetime_time = datetime.datetime.strptime(datetime_time[:-6], '%Y-%m-%dT%H:%M:%S')

                if initial_scrap:
                    if datetime_time < two_years_ago:
                        repeat = False
                else:
                    if datetime_time < week_ago:
                        repeat = False
                logger.info(f"[cenzopapa] -> {image['src']} | {datetime_time}")
                image = Image(remote_image_url=image['src'], created_at=datetime_time)
                images_list.append(image)
                """"
                images_list.append({
                    "remote_image_url": image['src'],
                    "created_at": datetime_time
                })
                """
            sleep(2)
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
