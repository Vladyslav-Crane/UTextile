import os
from django.conf import settings
from datetime import date
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_extensions.db.models import TimeStampedModel

def category_image_upload_to(instance, filename):
    return f'images/category/{date.today()}/{filename}'

def product_image_upload_to(instance, filename):
    return f'images/product/{date.today()}/{filename}'

class Category(TimeStampedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=category_image_upload_to, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    # def get_absolute_url(self):
    #     return reverse('catalog:category_detail', kwargs={'slug': self.slug})

class ProductType(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.slug

# Create your models here.
class Product(TimeStampedModel):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=product_image_upload_to, null=True, blank=True)
    price = models.PositiveIntegerField()

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name="products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})

