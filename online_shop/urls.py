from django.contrib import admin
from django.urls import path
from product.views import ProductView, CategoryView
from user.views import UserView
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('product/', ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>', ProductView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('category/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('category/<int:pk>', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
