# Generated by Django 5.1.4 on 2025-01-13 17:04

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='fabric',
            options={'verbose_name_plural': 'fabrics'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=catalog.models.category_image_upload_to),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=catalog.models.product_image_upload_to),
        ),
    ]