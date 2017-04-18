#Djnago Restframework Modules
from django.http.response import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import unicodedata
from users.form import (
    UserForm,
    CustomerAddressForm,
)
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

    def get(self, request, username, *args, **kwargs):
        user = User.objects.all().filter(username=username).values()
        # user = User.objects.all().filter(username=username).get()
        return JsonResponse({'results': list(user)})
        # return self.list(request, *args, **kwargs)
        # return HttpResponse(user.email)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return HttpResponse('This is POST request')


class CustomerAddress_api(GenericAPIView, mixins.ListModelMixin):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer

    def get(self, request, username, *args, **kwargs):
        # user = User.objects.all().filter(username=username).get()
        # customeraddress = CustomerAddress.objects.filter(email_address=user.email).values()
        # return JsonResponse({'results': list(customeraddress)})
        return self.list(request, *args, **kwargs)
        # return HttpResponse(user.email)

    def post(self, request, *args, **kwargs):
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            # form.address1 = form.address1.encode('utf-8')
            # form.address2 = form.address2.encode('utf-8')
            post = form.save(commit=False)
            post.save()

        return HttpResponse('good')


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.users.all()
#     serializer_class = UserSerializer
#
# class CustomerAddressViewSet(viewsets.ModelViewSet):
#     queryset = CustomerAddress.objects.all()
#     serializer_class = CustomerAddressSerializer
