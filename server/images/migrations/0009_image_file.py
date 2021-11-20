# Generated by Django 3.2.9 on 2021-11-20 16:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_remove_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
    ]
