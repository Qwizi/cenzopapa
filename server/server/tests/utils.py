from datetime import datetime

from django.contrib.auth import get_user_model
from django.utils.timezone import make_aware

from images.models import Image

USER_DATA = {
    "username": "Test",
    "email": "test@test.pl",
    "password": "test123456"
}

TEST_URL = "http://www.example.com/images/123.png"

def create_user():
    User = get_user_model()
    user = User.objects.create_user(**USER_DATA)
    return user


def create_image(url=None):
    author = create_user()
    if url:
        return Image.objects.create(
            url=url,
            posted_at=make_aware(datetime.now()),
            author=author
        ), author
    return Image.objects.create(
        posted_at=make_aware(datetime.now()),
        author=author
    ), author
