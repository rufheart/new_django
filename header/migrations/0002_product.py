# Generated by Django 4.0.3 on 2022-03-13 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('name', models.CharField(max_length=35)),
                ('image', models.ImageField(upload_to='img/product/')),
                ('desc', models.TextField()),
                ('new_pr', models.CharField(max_length=10)),
                ('old_pr', models.CharField(max_length=10)),
            ],
            bases=('header.abs',),
        ),
    ]