# Generated by Django 3.2.9 on 2021-11-30 15:51

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('file', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('posted_at', models.DateTimeField()),
                ('height', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('is_validated', models.BooleanField(default=False)),
            ],
        ),
    ]
