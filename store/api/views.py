import datetime as dt
import json
from accounts.models import Account
from customer.models import Customer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from store.models import Sale, Store, Spent
from store.api.serializers import SpentSerializer, StoreSerializer, SaleSerializer
from rest_framework import generics


def get_date(data):
    date = list(data)
    year = "".join(date[0:4])
    month = "".join(date[4:6])
    day = "".join(date[6:8])
    date = dt.date(int(year), int(month), int(day))
    return date


class StoreApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user']
    ordering = ['-created_at']


class SpentApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SpentSerializer
    queryset = Spent.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['store','year', 'month']
    ordering = ['-id']
    

class SaleApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['store', 'customer']
    ordering = ['-id']

    
class CreateSalesApiViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        sales = json.loads(request.data["data"])

        for sale in sales:
            phone = sale["telefono_destinatario"]
            date = get_date(sale["fecha_creacion"])
            store = Store.objects.get(name=sale["generado_por"].lower())
            is_customer_exists = Customer.objects.filter(phone=phone).exists()

            if is_customer_exists:
                customer = Customer.objects.get(phone=phone)
                customer.name = sale["nombre_destinatario"]
                customer.phone = sale["telefono_destinatario"]
                customer.save()
            else:
                user = Account.objects.get(id=store.user.id)
                customer = Customer()
                customer.user = user
                customer.name = sale["nombre_destinatario"]
                customer.phone = sale["telefono_destinatario"]
                customer.save()

            is_sale_exists = Sale.objects.filter(guide=sale["guia"]).exists()

            if not is_sale_exists:
                object = Sale()
                object.store = store
                object.customer = customer
                object.sale = sale["venta"]
                object.collection = int(sale["recaudo"])
                object.cost = int(sale["costo"])
                object.date = date
                object.carrier = sale["transportadora"]
                object.guide = sale["guia"]
                object.freight = int(sale["flete"])
                object.delivery_status = sale["estado_transportadora"]
                object.save()

        return Response({"message": "created"})


class DateSaleApiViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SaleSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user')
        store_id = self.request.query_params.get('store_id')
        start_date = self.request.query_params.get('start_date')
        start_date = get_date(start_date)
        end_date = self.request.query_params.get('end_date')
        end_date = get_date(end_date)
        queryset = Sale.objects.all()

        if user_id is not None:
           queryset = queryset.filter(store__user=user_id, date__gte=start_date, date__lte=end_date)

        if store_id is not None:
           queryset = queryset.filter(store=store_id, date__gte=start_date, date__lte=end_date)

        return queryset


class StatisticsApiViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data["user"]
        start_date = get_date(request.data["start_date"])
        end_date = get_date(request.data["end_date"])
        sales = Sale.objects.filter(store__user=user_id, date__gte=start_date, date__lte=end_date)
        
        total_collection = 0
        total_cost = 0
        total_freight = 0
        num_sale = 0

        for sale in sales:
            total_collection += sale.collection
            total_cost += sale.cost
            num_sale += 1
            total_freight += sale.freight
        
       
        return Response({"total_collection" : total_collection,
                         "total_cost" : total_cost, 
                         "total_freight" : total_freight, 
                         "num_sale" : num_sale,
                         })
