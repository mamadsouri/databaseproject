# Generated by Django 3.1.4 on 2021-02-27 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0027_auto_20210226_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='maghale',
            name='Short_explanation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
