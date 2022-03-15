# Generated by Django 4.0.3 on 2022-03-15 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('c_tab', models.TextField()),
            ],
            bases=('header.abs',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('name', models.CharField(max_length=50)),
            ],
            bases=('header.abs',),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/img/product/'),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('picture', models.ImageField(upload_to='media/img/images')),
                ('haqq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='header.about')),
            ],
            bases=('header.abs',),
        ),
        migrations.AddField(
            model_name='about',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='header.product'),
        ),
        migrations.AddField(
            model_name='about',
            name='tag',
            field=models.ManyToManyField(blank=True, to='header.tag'),
        ),
    ]
