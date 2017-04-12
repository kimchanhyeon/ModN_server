from rest_framework import serializers, mixins

from catalog.serializers import (
    MarketSerializer,
    SellerSerializer
)

from .models import (
    OrderGroup,
    Order,
    OrderItem,
    FulfillmentGroup,
    FulfillmentOption
)
from catalog.serializers import  SkuSerializer
from catalog.models import Sku
#from ModN.order.models import SkuOptions

class OrderItemSerializer(serializers.ModelSerializer):
#    order = OrderSerializer(many=True)
    sku = SkuSerializer(many=True)
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'sku',
            'url',
            'url_key',
            #'base_retail_price'
            'base_sale_price',
            'quantity'
            'status'
        )

class FulfillmentGroupSerializer(serializers.ModelSerializer):
#    order = OrderItemSerializer(many = True)
    order_item = OrderItemSerializer(many=True)
    class Meta:
        model = FulfillmentGroup
        fields = (
            'id',
            'sale_price',
            'status',
            'total',
            'type',
            'seller',
            'order_item'
        )

class OrderSerializer(serializers.ModelSerializer):
#    order_item = OrderItemSerializer(many=True)
    fulfillment_group = FulfillmentGroupSerializer(many=True)
    market = MarketSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            'id',
            'fulfillment_group',
            'market',
            'date_created',
            'date_updated',
            'order_number',
            #'order_subtotal',
            'order_total',
            'total_shipping',
            'created_by',
            'updated_by'
        )

class OrderGroupSerializer(serializers.ModelSerializer):
    orders =OrderSerializer(many=True)
    class Meta:
        model = OrderGroup
        fields = (
            'id',
            'orders',
            'order_group_number',
            'order_group_status',
            'total_shipping',
            'toatl_price',
#            'created_by',
#            'updated_by',
            'date_created',
            'date_updated'
        )


# class OrderSerializer(serializers.ModelSerializer):
# #    order_item = OrderItemSerializer(many=True)
#     fulfillment_group = FulfillmentGroupSerializer(many=True)
#     market = MarketSerializer(many=True)
#     class Meta:
#         model = Order
#         fields = (
#             'id',
#             'fulfillment_group',
#             'market',
#             'date_created',
#             'date_updated',
#             'order_number',
#             #'order_subtotal',
#             'order_total',
#             'total_shipping',
#             'created_by',
#             'updated_by'
#         )

# class OrderItemSerializer(serializers.ModelSerializer):
# #    order = OrderSerializer(many=True)
#     sku = SkuSerializer(many=True)
#     class Meta:
#         model = OrderItem
#         fields = (
#             'id',
#             'sku',
#             'url',
#             'url_key',
#             #'base_retail_price'
#             'base_sale_price',
#             'quantity'
#             'status'
#         )
"""
class SkuSerializer(serializers.ModelSerializer):
#    order_item = OrderItemSerializer(many=True)
    sku_options=SkuOptionsSerializer(many=True)
    class Meta:
        model = Sku
        fields = (
            'id',
            'description',
            'option_value',
            'sale_price',
            'amount'
        )

class SkuOptionsSerializer(serializers.ModelSerializer):
#    sku = SkuSerializer(many=True)
    class Meta:
        model = SkuOptions
        fields = (
            'id',
            'value',
            'description'
            )
"""

# class FulfillmentGroupSerializer(serializers.ModelSerializer):
# #    order = OrderItemSerializer(many = True)
#     order_item = OrderItemSerializer(many=True)
#     class Meta:
#         model = FulfillmentGroup
#         fields = (
#             'id',
#             'sale_price',
#             'status',
#             'total',
#             'type',
#             'seller',
#             'order_item'
#         )
