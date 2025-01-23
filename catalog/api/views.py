from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from catalog.models import Product
from .serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
