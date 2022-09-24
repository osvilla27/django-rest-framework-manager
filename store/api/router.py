from django.urls import path
from rest_framework.routers import DefaultRouter
from store.api.views import (SaleApiViewSet, 
                             SpentApiViewSet, 
                             StoreApiViewSet, 
                             CreateSalesApiViewSet, 
                             DateSaleApiViewSet,
                             StatisticsApiViewSet
                            )


router_store = DefaultRouter()

router_store.register(prefix='store', basename='store',
                      viewset=StoreApiViewSet)

router_store.register(prefix='spent', basename='spent',
                      viewset=SpentApiViewSet)

router_store.register(prefix='sale', basename='sale',
                      viewset=SaleApiViewSet)

urlpatterns = [
    path('create-sales/', CreateSalesApiViewSet.as_view()),
    path('date-sale/', DateSaleApiViewSet.as_view()),
    path('statistics/', StatisticsApiViewSet.as_view()),
]
