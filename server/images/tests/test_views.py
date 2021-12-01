from datetime import datetime

import pytest
from django.test import Client
from django.utils.timezone import make_aware

from images.models import Image
from server.tests.utils import create_image, TEST_URL, create_user


@pytest.mark.django_db
def test_list_images_empty():
    c = Client()
    response = c.get("/images/")
    print(response.json())
    assert response.status_code == 200
    assert response.json()['count'] == 0
    assert response.json()['next'] is None
    assert response.json()['previous'] is None
    assert response.json()['results'] == []


@pytest.mark.django_db
def test_unvalidated_images_empty():
    create_image(TEST_URL)
    c = Client()
    response = c.get("/images/")
    assert response.status_code == 200
    assert "results" in response.json()
    assert "count" in response.json()
    assert "next" in response.json()
    assert "previous" in response.json()
    assert response.json()['count'] == 0


@pytest.mark.django_db
def test_list_image():
    image, author = create_image(TEST_URL)
    Image.objects.create(
        posted_at=make_aware(datetime.now()),
        is_validated=True,
        author=author
    )
    c = Client()
    response = c.get("/images/")
    assert response.status_code == 200
    assert "results" in response.json()
    assert "count" in response.json()
    assert "next" in response.json()
    assert "previous" in response.json()
    assert response.json()['count'] == 1


@pytest.mark.django_db
def test_retrieve_image():
    author = create_user()
    image = Image.objects.create(
        posted_at=make_aware(datetime.now()),
        is_validated=True,
        author=author
    )
    c = Client()
    response = c.get(f"/images/{image.pk}/")
    assert response.status_code == 200
    assert response.json()['id'] == image.pk
    assert "id" in response.json()
    assert "url" in response.json()
    assert "author" in response.json()
    assert "width" in response.json()
    assert "height" in response.json()
    assert "likes" in response.json()
    assert "likes_count" in response.json()
    assert "file" not in response.json()
    assert "is_validated" not in response.json()


@pytest.mark.django_db
def test_random_empty_image():
    c = Client()
    response = c.get("/images/random/")
    assert response.status_code == 404
