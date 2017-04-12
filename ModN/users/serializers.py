from rest_framework import serializer
from .models import (
    User,
    CustomerAddress
)

class CustomerAddressSerializer(serializer.ModelSerializer):
    class Meta:
        model = CustomerAddress

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
