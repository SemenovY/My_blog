from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя.

    Атрибуты:
        role (str): Роль пользователя, используя UserRole.choices.
        is_admin (bool): Свойство, определяющее, является ли пользователь администратором.
    """

    pass

    def __str__(self):
        return self.username
