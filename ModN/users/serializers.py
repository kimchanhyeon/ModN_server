from rest_framework import serializer
from ModN.customer.models import Address, CustomAddress

class CustomAddressSerializer(serializer.ModelSerializer):
    class Meta:
        model = CustomAddress

class AddressSerializer(serializer.ModelSerializer):
    class Meta:
        model = Address