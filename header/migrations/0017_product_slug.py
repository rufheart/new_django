# Generated by Django 4.0.3 on 2022-04-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0016_rename_s_2addres_cont_info_s_2address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
