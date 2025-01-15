from django.contrib import admin
from .models import Category, Fabric

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class FabricAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Fabric, FabricAdmin)
