import cloudinary.uploader
from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


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


def on_create_image(sender, **kwargs):
    if kwargs['created']:
        image = kwargs['instance']
        if image.file:
            image.url = image.file.url
            image.save()


post_save.connect(on_create_image, sender=Image)


@receiver(post_delete, sender=Image)
def save_profile(sender, instance, **kwargs):
    if instance.file:
        file_name = instance.file
        cloudinary.uploader.destroy(file_name.public_id, invalidate=True)
        print(file_name.public_id)
