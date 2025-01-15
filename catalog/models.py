from datetime import date
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_extensions.db.models import TimeStampedModel

def category_image_upload_to(instance, filename):
    return f'media/images/category/{date.today()}/{filename}'

def product_image_upload_to(instance, filename):
    return f'media/images/product/{date.today()}/{filename}'

class Category(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=category_image_upload_to, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


# Create your models here.
class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=product_image_upload_to, null=True, blank=True)
    price = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Fabric(Product):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fabrics')

    class Meta:
        verbose_name_plural = _('fabric')
        verbose_name_plural = _('fabrics')

