# Generated by Django 4.0.3 on 2022-04-20 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ABS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cont_Info',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('fname', models.CharField(max_length=35)),
                ('lname', models.CharField(max_length=35)),
                ('company', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=13)),
                ('fax', models.CharField(max_length=30)),
                ('s_address', models.CharField(max_length=50)),
                ('s_2address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=35)),
                ('state', models.SmallIntegerField(choices=[(1, 'Alabama'), (2, 'Alaska'), (3, 'Arizona')])),
                ('zip', models.CharField(max_length=25)),
                ('country', models.SmallIntegerField(choices=[(1, 'Azerbaijan'), (2, 'Afganistan')])),
                ('bil_addr', models.BooleanField()),
                ('ship_addr', models.BooleanField()),
            ],
            bases=('header.abs',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('company', models.CharField(max_length=40)),
                ('tel', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=50)),
                ('comment', models.TextField()),
            ],
            bases=('header.abs',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('name', models.CharField(max_length=35)),
                ('image', models.ImageField(upload_to='img/product')),
                ('desc', models.TextField()),
                ('new_pr', models.CharField(max_length=10)),
                ('old_pr', models.CharField(max_length=10)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('header.abs',),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('value_review', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='Value')),
                ('quality_review', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='Quality')),
                ('price_review', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='Price')),
                ('summary', models.CharField(max_length=40, verbose_name='Summary')),
                ('comment', models.TextField()),
                ('product_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review', to='header.product')),
                ('user_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('header.abs',),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('images_tb', models.ImageField(upload_to='img/images ')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='header.product')),
            ],
            bases=('header.abs',),
        ),
        migrations.CreateModel(
            name='Add_To_Card',
            fields=[
                ('abs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='header.abs')),
                ('add_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_to_card', to='header.product')),
                ('add_usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_to_card', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('header.abs',),
        ),
    ]
