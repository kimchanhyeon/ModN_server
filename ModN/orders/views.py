from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework import viewsets


from ModN.order.models import OrderGroup
from ModN.order.models import Order
from ModN.order.models import OrderItem
from ModN.order.models import Sku
from ModN.order.models import FulfillmentGroup

from ModN.order.serializers import OrderGroupSerializer
from ModN.order.serializers import OrderSerializer
from ModN.order.serializers import OrderItemSerializer
from ModN.order.serializers import SkuSerializer
from ModN.order.serializers import FulfillmentGroupSerializer

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
