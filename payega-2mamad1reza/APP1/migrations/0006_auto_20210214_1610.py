# Generated by Django 3.1.4 on 2021-02-14 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0005_auto_20210214_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='Email',
            new_name='Email_p',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='Email_s',
        ),
    ]