import uuid
from django.db import models


class Image(models.Model):
    filename = models.UUIDField(default=uuid.uuid4, editable=True)
    extension = models.CharField(max_length=255, null=False, default='.png')
    remote_image_url = models.URLField(default='http://localhost.pl/image.png')
    public_url = models.URLField(default='https://localhost.pl/image.png')
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField()
    height = models.IntegerField(default=600)
    width = models.IntegerField(default=400)

    def __str__(self):
        return f"[{self.id}] | {self.remote_image_url} | {self.public_url}"