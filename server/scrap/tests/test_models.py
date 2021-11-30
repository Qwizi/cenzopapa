from datetime import datetime

import pytest
from django.contrib.auth import get_user_model

from images.models import Image


@pytest.mark.django_db
def test_create_image():
    Image.objects.create(
        posted_at=datetime.now(),
        author_id=1
    )

    assert Image.objects.count() == 1
