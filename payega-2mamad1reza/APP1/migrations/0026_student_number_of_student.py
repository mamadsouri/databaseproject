# Generated by Django 3.1.4 on 2021-02-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0025_maghale_vaziat'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='number_of_student',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
