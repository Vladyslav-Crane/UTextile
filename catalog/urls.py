from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'), 
    # path('categories', views.catalog, name='catalog'), 
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'), 
    path('product/detail/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')

]