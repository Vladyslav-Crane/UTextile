from django.urls import path, include
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("api/", include("catalog.api.urls")),
    # path('categories', views.catalog, name='catalog'),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/detail/<slug:slug>",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
]
