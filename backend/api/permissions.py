from typing import Any

from django.http import HttpRequest
from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее только администраторам или владельцу объекта изменять или удалять его.
    """

    message = "Only administrators or the owner have access."

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: HttpRequest, view: Any, obj: Any) -> bool:
        return request.user.is_admin or (obj.user == request.user and request.method in permissions.SAFE_METHODS)
