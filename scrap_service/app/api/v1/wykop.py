from time import sleep
import datetime

from bs4 import BeautifulSoup

from .models import ImageModel
from .site import Site


class Wykop(Site):
    site_name = "wykop"
    site_url = "https://www.wykop.pl"
    cenzo_tag = "multimedia-tag/cenzopapa"

    def scrap_images(self, initial_scrap=False):
        page_number = 0
        repeat = True
        images_list = []
        while repeat:
            page_number += 1
            response = self.session.get(f'{self.site_url}/{self.cenzo_tag}/strona/{page_number}')
            print(response.status_code)
            if response.status_code == 503:
                repeat = False

            bs = BeautifulSoup(response.content, 'html.parser')

            rel_images = bs.find_all("div", class_="rel image")
            two_years_ago = datetime.datetime.now() - datetime.timedelta(days=2 * 365)
            week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
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

                #image_model = ImageModel(remote_image_url=image['src'], created_at=datetime_time)
                images_list.append({
                    "remote_image_url": image['src'],
                    "created_at": datetime_time
                })
            sleep(2)
        print(f"Ilosc cenzopap: {len(images_list)}")

        return images_list