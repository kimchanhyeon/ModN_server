#Djnago Restframework Modules
from rest_framework import viewsets
from rest_framework.response import Response

#Models
from .models import (
    User,
    CustomerAddress
)

#Serializers
from .serializers import (
    UserSerializer,
    CustomerAddressSerializer
)

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.users.all()
    serializer_class = UserSerializer

class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
