from api.serializers.users import UserSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from users.models import CustomUser


class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    """
    Класс представления для списка и создания пользователей.

    Атрибуты:
    - queryset: QuerySet модели CustomUser
    - serializer_class: Класс сериализатора для модели CustomUser
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @extend_schema(tags=["Пользователи"], summary="Получить список всех пользователей", operation_id="get_all_users")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=["Пользователи"], summary="Создать нового пользователя", operation_id="create_user")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Класс представления для получения, обновления и удаления пользователей.

    Атрибуты:
    - queryset: QuerySet модели CustomUser
    - serializer_class: Класс сериализатора для модели CustomUser
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @extend_schema(tags=["Пользователи"], summary="Получить конкретного пользователя", operation_id="get_user_detail")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=["Пользователи"], summary="Обновить конкретного пользователя", operation_id="update_user")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(tags=["Пользователи"], summary="Удалить конкретного пользователя", operation_id="delete_user")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
