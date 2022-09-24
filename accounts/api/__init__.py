from rest_framework import serializers
from accounts.models import Account


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", 'email', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_date):
        password = validated_date.pop('password', None)
        instance = self.Meta.model(**validated_date)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'date_joined']