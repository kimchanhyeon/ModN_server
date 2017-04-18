from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>\w{0,50})/$', views.User_api.as_view()),
    url(r'^(?P<username>\w{0,50})/address/$', views.CustomerAddress_api.as_view()),
    # url(r'^address/(?P<data>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.CustomerAddress_api.as_view()),
]