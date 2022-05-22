# Generated by Django 4.0.3 on 2022-05-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_detail_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail_product',
            name='desc_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='detail_product',
            name='desc_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='detail_product',
            name='slug_az',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='detail_product',
            name='slug_en',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
