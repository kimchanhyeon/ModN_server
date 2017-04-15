from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.User_api.as_view()),
    url(r'^address/$', views.CustomerAddress_api.as_view()),
]