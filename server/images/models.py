from django.conf import settings
from django.db import models


class Image(models.Model):
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField()
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    is_validated = models.BooleanField(default=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"[{self.id}] | {self.url}"