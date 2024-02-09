from typing import Any
from django.http import HttpRequest
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, request_view: Any) -> bool:
        return request.user.is_authenticated and request.user.is_admin
