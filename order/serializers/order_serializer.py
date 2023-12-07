from rest_framework import serializers

from product.serializers.product_serializer import ProductSerializer
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, isntance):
        total = sum([product.price for product in isntance.product.all()])
        return total

    class Meta:
        model = Product
        field = ['product', 'total']