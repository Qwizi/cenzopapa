# Generated by Django 3.2.9 on 2021-12-01 20:50
from django.db import migrations


def create_task(apps, schema_editor):
    from django_q.tasks import schedule
    func = 'scrap.tasks.scrap_images'
    schedule(func, 7, schedule_type='H')


class Migration(migrations.Migration):
    dependencies = [
        ('django_q', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_task),
    ]