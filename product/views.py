from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from product.serializers import ProductSerializer, CategorySerializer
from product.models import Product, Category
from product.permissions import IsAdminUserOrReadOnly


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() #prefetch_related('product_category')
    lookup_field = 'pk'
    permission_classes = (IsAdminUserOrReadOnly, )


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsAdminUserOrReadOnly, )
