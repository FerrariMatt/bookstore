from django.contrib.auth.models import Group, User
from rest_framework import serializers

from product.serializers.product_serializer import ProductSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, isntance):
        total = sum([product.price for product in isntance.product.all()])
        return total

    class Meta:
        model = Product
        field = ['product', 'total']