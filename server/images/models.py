import uuid

from django.conf import settings
from django.db import models


class Image(models.Model):
    filename = models.UUIDField(default=uuid.uuid4, editable=True)
    extension = models.CharField(max_length=255, null=False, default='.png')
    remote_image_url = models.URLField(default='http://localhost.pl/image.png')
    public_url = models.URLField(default='https://localhost.pl/image.png')
    file = models.ImageField(upload_to="images", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField()
    height = models.IntegerField(default=600)
    width = models.IntegerField(default=400)
    is_validated = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"[{self.id}] | {self.remote_image_url}"
