from django.contrib.auth.models import AbstractUser
from django.db import models

from images.models import Image


class CUser(AbstractUser):
    favorite_images = models.ManyToManyField(Image, related_name='favorite_images')
