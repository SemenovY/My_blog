from typing import Any

from django.http import HttpRequest
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Право доступа, позволяющее только администраторам выполнять запрос.

    Методы:
        has_permission(self, request: HttpRequest, view: Any) -> bool:
            Проверяет, имеет ли пользователь административные права.

    Атрибуты:
        message (str): Сообщение об ошибке, которое будет возвращено в случае отсутствия прав доступа.
    """

    message = "Only administrators have access."

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        """
        Проверяет, имеет ли пользователь административные права.

        Аргументы:
            request (HttpRequest): Запрос.
            view (Any): Представление.

        Возвращает:
            bool: True, если пользователь является администратором, в противном случае - False.
        """
        return request.user.is_authenticated and request.user.is_admin
