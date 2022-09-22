import datetime as dt
import json
import os
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
    filterset_fields = ['store_id', 'customer_id', 'date']
    ordering = ['-id']


def read_file():
    with open(os.path.join('data.json')) as file:
        object = json.load(file)
        return object
    
    
def create_sales():
    object = read_file()
    return object


def get_date(data):
    date = list(data)
    year = "".join(date[0:4])
    month = "".join(date[4:6])
    day = "".join(date[6:8])
    date = dt.date(int(year), int(month), int(day))
    return date


class CreateSalesApiViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        sales = json.loads(request.data["data"])
        #sales = create_sales()
        
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

            print(is_sale_exists)
            if not is_sale_exists:
                object = Sale()
                object.id = sale["id_registro"]
                object.store_id = store
                object.customer_id = customer
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


    # start_date =  dt.date(2022, 8, 1)
    # end_date = dt.date(2022, 8, 17)
    # query=Sale.objects.filter(date__gte=start_date,date__lte=end_date)
    # for q in query:
    #  print(q.date)
    # query=Sale.objects.filter(store_id__name="OSVILL")
    # for q in query:
    #  print(q.date)
    # x = os.path.join('data.csv')
    