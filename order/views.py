from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from order.serializers import OrderSerializer, SubOrderSerializer
from order.models import Order, SubOrder
# from product.permissions import IsAdminUserOrReadOnly


class SubOrderView(ModelViewSet):
    serializer_class = SubOrderSerializer
    queryset = SubOrder.objects.all()
    lookup_field = 'pk'
    # permission_classes = (IsAdminUserOrReadOnly, )

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)


class CartView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'
    # permission_classes = (IsAdminUserOrReadOnly, )

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
