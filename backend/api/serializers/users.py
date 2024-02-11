from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользовательских данных.
    """

    class Meta:
        """
        Метакласс для определения настроек сериализатора.

        Атрибуты:
            model (CustomUser): Модель пользователя для сериализации.
            fields (tuple): Поля модели, которые будут сериализованы.
        """

        model = CustomUser
        fields = ("id", "username", "email", "password")
