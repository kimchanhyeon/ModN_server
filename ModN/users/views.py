#Djnago Restframework Modules
from django.http.response import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

#Models
from users.models import (
    User,
    CustomerAddress
)

#Serializers
from users.serializers import (
    UserSerializer,
    CustomerAddressSerializer
)

#users API

class User_api(GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is POST request')
        # reqFirstName = request.GET['first_name']
        # reqLastName = request.GET['last_name']
        # books = User(first_name=reqFirstName, last_name=reqLastName)
        # books.save()
        # return self.list(books, *args, **kwargs)

class CustomerAddress_api(GenericAPIView, mixins.ListModelMixin):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.users.all()
#     serializer_class = UserSerializer
#
# class CustomerAddressViewSet(viewsets.ModelViewSet):
#     queryset = CustomerAddress.objects.all()
#     serializer_class = CustomerAddressSerializer
