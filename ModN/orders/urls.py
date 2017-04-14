from django.conf.urls import include, url
from rest_framework import routers
from orders import views

# router = routers.DefaultRouter()
# router.register(r'order', views.OrderViewSet)
# router.register(r'ordergrups', views.OrderGroupViewSet)

urlpatterns = [
    # url(r'^$', views.OrderViewSet),
    # url(r'^$', views.OrderItemViewSet),
    # url(r'^$', views.OrderGroupViewSet),
    # url(r'^$', views.SkuViewSet),
    # url(r'^$', views.FulfillmentGroupViewSet),

    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
