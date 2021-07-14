from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_staff or request.user.is_superuser                                                                                                                                        