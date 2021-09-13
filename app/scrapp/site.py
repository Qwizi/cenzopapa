import abc
import os
import requests
import uuid
import datetime
from time import sleep

from bs4 import BeautifulSoup
from abc import abstractmethod, ABC

from firebase_admin import firestore

from app.firebase.firebase import db, bucket


def remove_image_from_temp(path):
    if os.path.exists(path):
        os.remove(path)


def download_image_from_url(remote_image_url, filename):
    response = requests.get(remote_image_url)
    if response.status_code == 200:
        path = f"temp/{filename}"
        file = open(path, "wb")
        file.write(response.content)
        file.close()
        return path


def add_image_to_storage(remote_image_url, filename):
    path = download_image_from_url(remote_image_url, filename)

    blob = bucket.blob(filename)
    blob.upload_from_filename(path)
    blob.make_public()

    print(filename)
    print(path)
    print(blob.public_url)
    remove_image_from_temp(path)

    return blob.public_url


def get_last_image():
    last_img_ref = db.collection(u"images")
    query = last_img_ref.order_by(u"id", direction=firestore.Query.DESCENDING).limit(1)
    result = query.stream()
    for r in result:
        return r.to_dict()


def check_image_exists(remote_image_url):
    img = None
    query = db.collection(u'images').where(u'remote_image_url', u'==', remote_image_url).limit(1).stream()
    for r in query:
        img = r.to_dict()
    return img


def add_image_to_database(image, local_image_url):
    last_img = get_last_image()
    new_img = db.collection('images').add({
        "id": last_img['id'] + 1 if last_img is not None else 1,
        "remote_image_url": image['remote_image_url'],
        "created_at": image['created_at'],
        "local_image_url": local_image_url
    })
    return new_img


class Site(abc.ABC):
    site_name: str
    site_url: str
    session: any

    def run(self):
        images = self.scrap_images(initial_scrap=True)
        # add_image_to_storage("https://www.wykop.pl/cdn/c3201142/comment_16314771800U23OBKTiokrKxQeEd90Ap,w300.jpg")
        for img in images:
            if not check_image_exists(img['remote_image_url']):
                filename = f"{uuid.uuid4()}.jpg"
                local_image_url = add_image_to_storage(img['remote_image_url'], filename)
                print(local_image_url)
                if local_image_url:
                    new_img = add_image_to_database(img, local_image_url)
                    print(new_img)

    @abstractmethod
    def scrap_images(self, initial_scrap=False):
        pass


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
                images_list.append({
                    'remote_image_url': image['src'],
                    'created_at': datetime_time
                })
            sleep(2)
        print(f"Ilosc cenzopap: {len(images_list)}")

        return images_list
