from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Fabric


# Create your views here.
def catalog(request):
    return render(
        request,
        "catalog/catalog.jinja2",
        {"categories": Category.objects.all()},
        using="jinja2",
    )
