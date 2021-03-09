# Generated by Django 3.1.4 on 2021-02-13 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP1', '0003_maghale_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressuny',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.university'),
        ),
        migrations.AlterField(
            model_name='maghale',
            name='Professor_Maghale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.professor'),
        ),
        migrations.AlterField(
            model_name='maghale',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.student'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='uni',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.university'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.professor'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uni',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP1.university'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]