# Generated by Django 3.1.4 on 2021-02-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0010_auto_20210215_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_A', models.CharField(max_length=100)),
                ('conrext_A', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='maghale',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]