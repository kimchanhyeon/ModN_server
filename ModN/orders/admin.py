from django.contrib import admin
from .models import (
    OrderGroup,
    Order,
    OrderItem,
    FulfillmentGroup,
    FulfillmentOption
)
# Register your models here.
admin.site.register(OrderGroup)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(FulfillmentGroup)
admin.site.register(FulfillmentOption)
