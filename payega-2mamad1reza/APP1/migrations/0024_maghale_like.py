# Generated by Django 3.1.4 on 2021-02-24 20:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP1', '0023_auto_20210222_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='maghale',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Blogliks', to=settings.AUTH_USER_MODEL),
        ),
    ]