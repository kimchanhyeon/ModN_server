from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/$', views.Product_api.as_view()),
    # url(r'^address/$', views.CustomerAddress_api.as_view()),
]