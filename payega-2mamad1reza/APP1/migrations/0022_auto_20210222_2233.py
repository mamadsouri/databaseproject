# Generated by Django 3.1.4 on 2021-02-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0021_auto_20210221_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='Degree_of_education_p',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
