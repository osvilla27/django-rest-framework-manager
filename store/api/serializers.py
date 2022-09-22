from rest_framework.serializers import ModelSerializer
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
        fields = ['id', 'store', 'year', 'month', 'total', 'description']

class SaleSerializer(ModelSerializer):

    class Meta:
        model = Sale
        fields = ['id', 
                'store_id',
                'customer_id',
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
                'updated_at']
    