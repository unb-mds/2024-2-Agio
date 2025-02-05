from rest_framework import serializers

from .models import ProductTable


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTable
        fields = ['product_name', 'amount', 'category', 'description', 'price']