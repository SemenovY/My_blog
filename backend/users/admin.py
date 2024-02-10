"""
Класс администратора для модели CustomUser.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Этот класс расширяет встроенный UserAdmin для дополнительной настройки в административном интерфейсе Django.
    """

    list_display = ("id", "username", "role", "is_superuser", "is_staff", "is_active")
    search_fields = ("username",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
