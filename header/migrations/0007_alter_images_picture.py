# Generated by Django 4.0.3 on 2022-03-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0006_alter_images_haqq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.ImageField(upload_to='img/images/'),
        ),
    ]