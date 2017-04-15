#Djnago Restframework Modules
from django.http.response import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import (
    OrderGroup,
    Order,
    OrderItem,
    FulfillmentGroup,
    FulfillmentOption
)

from catalog.models import Sku

from .serializers import (
    OrderGroupSerializer,
    OrderSerializer,
    OrderItemSerializer,
    FulfillmentGroupSerializer
)

from catalog.serializers import SkuSerializer

#Orders API

class Order_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Create your views here.
class OrderGroupViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = OrderGroup.objects.all()
    serializer_class = OrderGroupSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class SkuViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer

class FulfillmentGroupViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = FulfillmentGroup.objects.all()
    serializer_class = FulfillmentGroupSerializer
