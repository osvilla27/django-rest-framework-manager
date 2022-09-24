from rest_framework.serializers import ModelSerializer
from customer.models import Customer

class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'email', 'phone', 'city',
                'address', 'neighborhood', 'created_at', 'updated_at']

