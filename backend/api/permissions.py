from posts.models import BlogPost
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользователи могут редактировать или удалять свои собственные посты.

    Не могут редактировать или удалять посты других пользователей.
    """

    def has_permission(self, request, view):
        """Автор или только смотреть, или создать."""
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Проверяем совпадает ли автор поста с пользователем из запроса, если да, то даём все права."""
        if isinstance(obj, BlogPost):
            return request.method in permissions.SAFE_METHODS or obj.user == request.user
        return False
