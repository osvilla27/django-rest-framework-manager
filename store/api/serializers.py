from rest_framework.serializers import ModelSerializer
from customer.api.serializers import CustomerSerializer
from store.models import Store, Spent, Sale
from accounts.api.serializers import UserSerializer


class StoreSerializer(ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'slug', 'name', 'image', 'user', 'user_data',
                  'created_at', 'updated_at']


class SpentSerializer(ModelSerializer):

    class Meta:
        model = Spent
        fields = ['id', 'store', 'date', 'total', 'description']


class SaleSerializer(ModelSerializer):
    customer_data = CustomerSerializer(source='customer', read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 
                'store',
                'customer',
                'sale',
                'amount',
                'collection',
                'cost',
                'date',
                'carrier',
                'guide',
                'freight',
                'status',
                'delivery_status',
                'created_at',
                'updated_at',
                'customer_data'
                ]
    