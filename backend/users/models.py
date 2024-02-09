from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    user = ("user", _("User"))
    admin = ("admin", _("Administrator"))


class CustomUser(AbstractUser):
    role = models.SlugField(
        _("user role"),
        choices=UserRole.choices,
        default=UserRole.user,
    )

    @property
    def is_admin(self) -> bool:
        return self.role == UserRole.admin or self.is_superuser
