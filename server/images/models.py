from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    url = models.URLField(default='http://localhost.pl/image.png')
    file = CloudinaryField('file', null=True, blank=True)
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
        return f"[{self.id}] | {self.url}"

    def save(self, *args, **kwargs):
        if self.file:
            self.url = self.file.url
        super(Image, self).save(*args, **kwargs)
