# Generated by Django 3.1.4 on 2021-02-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0011_auto_20210216_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='conrext_A',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title_A',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
