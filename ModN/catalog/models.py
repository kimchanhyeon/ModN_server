from django.db import models
from treebeard.ns_tree import NS_Node

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()
    key = models.CharField(max_length=40)

class Seller(models.Model):
    name = models.CharField(max_length=40)
    contact_fax = models.CharField(max_length=20, blank=True)
    primary_contact_phone = models.CharField(max_length=20, blank=False)
    sendary_contact_phone = models.CharField(max_length=20, blank=True)
    #address = models.ForeignKey(Address)

class Category(NS_Node):
    name = models.CharField(max_length=40)

class Sku(models.Model):
    order_item = models.ForeignKey('orders.OrderItem', on_delete=models.PROTECT)
    product = models.ForeignKey('catalog.Product', related_name='skus')
    description = models.CharField(max_length=80, blank=True)
    option_value = models.CharField(max_length=80, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField()

class Product(models.Model):
    market = models.ForeignKey(Market, on_delete= models.PROTECT, related_name='market_products')
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, related_name='products')

    title = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=250, blank=True)
    url_key = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
