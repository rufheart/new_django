# Generated by Django 4.0.3 on 2022-05-10 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cont_info',
            name='abs_ptr',
        ),
        migrations.RemoveField(
            model_name='images',
            name='abs_ptr',
        ),
        migrations.RemoveField(
            model_name='images',
            name='products',
        ),
        migrations.RemoveField(
            model_name='product',
            name='abs_ptr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_pro',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='abs_ptr',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product_review',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user_pro',
        ),
        migrations.DeleteModel(
            name='Add_To_Card',
        ),
        migrations.DeleteModel(
            name='Cont_Info',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]