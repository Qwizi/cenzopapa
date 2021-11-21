import cloudinary.uploader
from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Image(models.Model):
    url = models.URLField(null=True, blank=True)
    file = CloudinaryField('file', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField()
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    is_validated = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")

    def __str__(self):
        return f"[{self.id}] | {self.url}"


def on_create_image(sender, **kwargs):
    if kwargs['created']:
        image = kwargs['instance']
        if image.file:
            image.url = image.file.url
            image.height = image.file.metadata.get("height")
            image.width = image.file.metadata.get("width")
            image.save()


post_save.connect(on_create_image, sender=Image)


@receiver(post_delete, sender=Image)
def delete_image_in_cloudinary(sender, instance, **kwargs):
    if instance.file:
        file_name = instance.file
        cloudinary.uploader.destroy(file_name.public_id, invalidate=True)
