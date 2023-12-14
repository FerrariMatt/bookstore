from rest_framework import serializers

from product.serializers.product_serializer import ProductSerializer
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in isntance.product.all()])
        return total

    class Meta:
        model = Product
        field = ['product', 'total', 'user', 'products_id']
        extra_kwargs = {'product': {'required': False}}

    def create(self, validated_data):
        product_data = validated_date.pop('products_id')
        user_data = validates_data.pop('user')

        order = order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)

        return order