# Generated by Django 4.0.3 on 2022-03-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0003_about_tag_alter_product_image_images_about_prod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.ImageField(upload_to='img/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='img/product/'),
        ),
    ]
