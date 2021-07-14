from rest_framework import serializers
from product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity', 'product_category')


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'category', 'product')