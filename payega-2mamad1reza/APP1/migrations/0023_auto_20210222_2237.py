# Generated by Django 3.1.4 on 2021-02-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0022_auto_20210222_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree_of_education_p',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
