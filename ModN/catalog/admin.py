from django.contrib import admin
from .models import (
    Market,
    Seller,
    Category,
    Product,
    Sku,
)
# Register your models here.
admin.site.register(Market)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sku)
