from rest_framework import serializers
from order.models import SubOrder, Order


class SubOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubOrder
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'