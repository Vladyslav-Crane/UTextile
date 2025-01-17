from django.contrib import admin
from .models import Category, ProductType, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("slug", "name")
    search_fields = ("name", "slug")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    search_fields = ("name", "category__name")
    list_filter = ("category",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
