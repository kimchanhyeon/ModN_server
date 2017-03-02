from django.db import models

class User(models.Model):
    SEX_CHOICES = (
        ('FEMALE', 'FEMALE'),
        ('MALE', 'MALE')
    )
    address = models.OneToOneField("CustomerAddress")

    type = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank= True)
    last_name = models.CharField(max_length=50, blank= True)
    name = models.CharField(max_length=100)
    cell_phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    authenticated = models.BooleanField(default = False)
    account_lock = models.BooleanField(default = False)


# Create your models here.
class Address(models.Model):
    address1 = models.CharField(max_length = 80)
    address2 = models.CharField(max_length = 40)
    city = models.CharField(max_length = 80)
    company_name = models.CharField(max_length = 100)
    email_address = models.CharField(max_length = 254)
    fax = models.CharField(max_length = 20)
    is_active = models.BooleanField()
    is_default = models.BooleanField()
    postal_code = models.CharField(max_length= 10)
    primary_phone = models.CharField(max_length= 20)
    secondary_phone = models.CharField(max_length= 20)
    state = models.CharField(max_length= 20)
    building_address = models.CharField(max_length=80)
    road_address = models.CharField(max_length=80)
    customer_address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, related_name='addresses')


class CustomerAddress(Address):
    TYPE_CHOICES=(
        ('MAIN', 'MAIN'),
        ('SUB', 'SUB')
    )
    address_name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

