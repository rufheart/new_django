# Generated by Django 4.0.3 on 2022-04-05 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0014_images_delete_photos_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='cont_info',
            name='s_2addres',
            field=models.CharField(default=datetime.datetime(2022, 4, 5, 10, 57, 37, 829741, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cont_info',
            name='s_address',
            field=models.CharField(max_length=50),
        ),
    ]