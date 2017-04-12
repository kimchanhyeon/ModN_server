# Djnago Restframework Modules
from rest_framework import viewsets
from rest_framework.response import Response

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
