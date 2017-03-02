from django.db import models

# Create your models here.

class OrderGroup(models.Model):
    STATUS_CHOISCES=(
        ('Open', 'Open'),
        ('Processed', 'Processed'),
        ('Completed', 'Completed'),
        ('Declined', 'Declined'),
        ('Cancelled', 'Cancelled'),
        ('Failed', 'Failed')
    )
    create_by = models.ForeignField('users.User', on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignField('users.User', on_delete=models.SET_NULL, null=True)

    number = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, blank=True, choices=STATUS_CHOISCES, default=STATUS_CHOISCES('Open'))

    #total = shipping + subtotal + tax
    total = models.DecimalField(max_digits=15, decimal_places=2)
    shipping = models.DecimalField(max_digits=15, decimal_places=2)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    date_submitted = models.DateTimeField('date order group created', auto_now_add=True)
    date_updated = models.DateTimeField('date order group created', auto_now=True)

    @classmethod
    def addOrderItem(cls, user, order_group_id, sku, quantity):
        quantity = int(quantity)
        product= sku.product
        order_item = OrderItem.objects.create(
            description = sku.description,
            price = sku.price,
            quantity = quantity,
            product = product,
            sku = sku
        )
        if order_group_id == None:
            order_group=OrderGroup.objects.create(
                created_by = user,
                updated_by = user,
                status = 'Open'
            )
            order = Order.objects.create(
                order_group = order_group,
                market = product.market,
            )
            fulfillment_group=FulfillmentGroup.objects.create(
                fulfillment_option = product.fulfillment_option,
                order = order,
                seller = product.seller,
                address = user.address.filter(type='MAIN').addresses,
                status = FulfillmentGroup.STATUS_CHOICES('Preparing')
            )
        else :
            order_group=OrderGroup.filter(id=order_group_id)
            order = order_group.orders.objects.filter(market=product.market)
            fulfillment_group = order.objects.fulfillment_groups.filter(seller=product.seller)

        order.add(order_item)
        fulfillment_group.add(order_item)

        FulfillmentGroup.calcShipping(fulfillment_group)
        Order.calcTotal(order)
        OrderGroup.calcTotal(order_group)

    @classmethod
    def removeOrderItem(cls, order_group_id, order_item):
        product = order_item.product

        order_group = OrderGroup.filter(id=order_group_id)
        order = order_group.orders.filter(market=product.market)
        fulfillment_group = order.fulfillment_groups.filter(seller=product.seller)

        order.remove(order_item)
        fulfillment_group.remove(order_item)
        if fulfillment_group.fulfillment_items.count() == 0:
            fulfillment_group.delete()
        else :
            FulfillmentGroup.calShipping(fulfillment_group)

        if order.order_items.count() == 0 :
            order.delete()
        else :
            Order.calcTotal(order)

        OrderGroup.calcTotal(order_group)
        order_item.delete()

    @classmethod
    def updateOrderItem(cls, order_group_id, order_item):
        quantity = int(order_item.quantity)
        product = order_item.product

        order_group = OrderGroup.filter(id=order_group_id)
        order = order_group.orders.filter(market=product.market)
        fulfillment_group = order.fulfillment_groups.filter(seller=product.seller)

        order.order_items.filter(id=order_item.id).update(quantity=quantity)

        FulfillmentGroup.calcShipping(fulfillment_group)
        Order.calcTotal(order)
        OrderGroup.calcTotal(order_group)

    @classmethod
    def calcTotal(cls, order_group):
        subtotal = 0
        tax = 0
        shipping = 0
        for order in order_group.orders:
            subtotal += order.subtotal
            shipping += order.shipping

        total = subtotal + tax + shipping
        order_group.update(subtotal= subtotal, tax=tax, shipping=shipping, total=total)

class Order(models.Model):
    STATUS_CHOISCES = (
        ('Open', 'Open'),
        ('Processed', 'Processed'),
        ('Completed', 'Completed'),
        ('Declined', 'Declined'),
        ('Cancelled', 'Cancelled'),
        ('Failed', 'Failed')
    )
    order_group = models.ForeignKey(OrderGroup, on_delete=models.CASCADE, related_name='orders')
    market = models.ForeignKey('catalog.Market', on_delete=models.PROTECT, related_name='market_orders+')

    number = models.CharField(max_length=20, blank=True)
    #status = models.CharField(max_length=20, blank=True)

    # total = shipping + subtotal + tax
    total = models.DecimalField(max_digits=15, decimal_places=2)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    shipping = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2, default=0)

class FulfillmentGroup(models.Model):
    STATUS_CHOICES = (
        ('Fufilled', 'Fulfilled'),
        ('Unfufilled', 'Unfufilled'),
        ('Shipping', 'Shipping'),
        ('Preparing', 'Preparing')
    )

    fulfillment_option = models.ForeignKey(FulfillmentOption, on_delete=models.PROTECT, related_name="options_fulfillment_group+")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='fulfillment_groups')
    address = models.ForeignKey('customer.CustomerAddress', on_delete=models.PROTECT, related_name="address_fulfillment_groups+")
    seller =  models.ForeignKey('catalog.Market', on_delete=models.PROTECT, related_name="seller_fulfillment_groups+")
    #personal_message = models.ForeignKey()

    number = models.CharField(max_length=15, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=20, blank=True)

class OrderItem(models.Model):
    STATUS_CHOICES = (
        ('PAYED', 'PAYED'),
        ('REFUNDED', 'REFUNDED'),
        ('DENIED', 'DENIED'),
        ('CANCELLED', 'CANCELLED'),
        ('COMPLETED', 'COMPLETED')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    fulfillment_group = models.ForeignKey('FulfillmentGroup', on_delete=models.NULL, null=True, related_name='fulfillment_items')
    product = models.ForeignKey('catalog.Product', on_delete=models.SET_NULL, null=True, related_name='product_order_items')
    sku = models.ForeignKey('catalog.sku', related_name='sku_order_items')
    #personel_message = models.ForeignKey(PersonelMessage)
    description = models.harField(max_length=100)
    status = models.CharField(max_length=20, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField()

class FulfillmentOption(models.Model):
    TYPE_CHOICES=(
        ('WEIGHT', 'WEIGHT'),
        ('FIXED', 'FIXED'),
        ('PRICE', 'PRICE')
    )
    price = models.DecimalField(max_digits=15, decimal_places=2)
    type=models.CharField(max_length=20, choices=TYPE_CHOICES, default='FIXED')
    value = models.PositiveIntegerField()
