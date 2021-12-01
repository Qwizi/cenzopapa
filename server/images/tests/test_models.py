from datetime import datetime

import pytest
from django.utils.timezone import make_aware

from images.models import Image

from server.tests.utils import create_image, TEST_URL


@pytest.mark.django_db
def test_create_image_without_url_file():
    create_image()
    assert Image.objects.count() == 1


@pytest.mark.django_db
def test_create_image_with_url():
    image, author = create_image(TEST_URL)
    assert Image.objects.count() == 1
    assert image.url == TEST_URL
    assert image.author == author
    assert image.is_validated is False


@pytest.mark.django_db
def test_list_image():
    image, author = create_image(TEST_URL)
    assert Image.objects.count() == 1
    assert Image.objects.all()[0].author == author


@pytest.mark.django_db
def test_retrieve_image():
    _, _ = create_image(TEST_URL)
    image = Image.objects.get(url=TEST_URL)
    assert image.url == TEST_URL


@pytest.mark.django_db
def test_update_image():
    image, _ = create_image(TEST_URL)
    assert image.is_validated is False
    image.is_validated = True
    image.save()
    assert image.is_validated is True


@pytest.mark.django_db
def test_delete_image():
    image, author = create_image(TEST_URL)
    image.delete()
    assert Image.objects.count() == 0
