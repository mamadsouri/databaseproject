# Generated by Django 3.1.4 on 2021-02-27 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0028_maghale_short_explanation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maghale',
            old_name='Short_explanation',
            new_name='ShortExplanation',
        ),
    ]
