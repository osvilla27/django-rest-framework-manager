from django.urls import path
from rest_framework.routers import DefaultRouter
from customer.api.views import CustomerApiViewSet


router_customer = DefaultRouter()

router_customer.register(prefix='customer', basename='customer',
                      viewset=CustomerApiViewSet)

