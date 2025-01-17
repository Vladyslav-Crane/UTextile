from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView
from .models import Category, Product
from .forms import ProductForm


# Create your views here.
def catalog(request):
    return render(
        request,
        "catalog/catalog.html",
        {"categories": Category.objects.all()},
    )


# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()  # Сохранение объекта модели в базу данных
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'product_form.html', {'form': form})


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    # success_url = reverse_lazy('article_success')  # Если не указывать - get_absolute_url модели

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


# def product_update(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()  # Обновление объекта модели
#             return redirect('product_detail', slug=product.slug)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'product_form.html', {'form': form})
