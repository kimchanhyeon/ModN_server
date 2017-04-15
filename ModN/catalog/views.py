# Djnago Restframework Modules
from django.http.response import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Models
from .models import (
    Market,
    Seller,
    Category,
    Product,
    Sku
)

# Serializers
from .serializers import (
    MarketSerializer,
    SellerSerializer,
    CategorySerializer,
    ProductSerializer,
    SkuSerializer
)

#catalog API

class Product_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# Create your views here.
class MarketViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SkuViewSet(viewsets.ModelViewSet):
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer
