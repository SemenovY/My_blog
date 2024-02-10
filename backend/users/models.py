from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    """
    Роли пользователей.

    Атрибуты:
        user (str): Роль обычного пользователя.
        admin (str): Роль администратора.
    """

    user = ("user", _("User"))
    admin = ("admin", _("Administrator"))


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя.

    Атрибуты:
        role (str): Роль пользователя, используя UserRole.choices.
        is_admin (bool): Свойство, определяющее, является ли пользователь администратором.
    """

    role: str = models.SlugField(
        _("user role"),
        choices=UserRole.choices,
        default=UserRole.user,
    )

    @property
    def is_admin(self) -> bool:
        """
        Проверяет, является ли пользователь администратором.

        Возвращает:
            bool: True, если пользователь является администратором, в противном случае - False.
        """
        return self.role == UserRole.admin or self.is_superuser
