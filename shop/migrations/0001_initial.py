# Generated by Django 3.1.5 on 2021-01-14 21:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('sku', models.CharField(max_length=30, unique=True)),
                ('stock', models.PositiveSmallIntegerField()),
                ('price', models.PositiveSmallIntegerField()),
                ('images', models.ManyToManyField(blank=True, to='shop.ProductImage')),
            ],
        ),
    ]
