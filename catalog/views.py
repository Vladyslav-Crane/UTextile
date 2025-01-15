from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Fabric

# Create your views here.
def catalog(request):
    return render(request, 'catalog.html', {'categories': Category.objects.all()})