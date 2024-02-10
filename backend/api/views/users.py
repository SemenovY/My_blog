from typing import Union

from api.serializers.users import UserSerializer
from django.http import Http404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser


@extend_schema(
    tags=["Пользователи"],
    methods=["GET", "POST"],
    description="Все пользователи",
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить список всех пользователей",
    ),
    post=extend_schema(
        summary="Создать нового пользователя",
    ),
)
class UserListCreateAPIView(APIView):
    """
    Представление для операций чтения и создания пользователей.

    Методы:
        get(self, request) -> Response:
            Получает список всех пользователей.

        post(self, request) -> Response:
            Создает нового пользователя.
    """

    serializer_class = UserSerializer

    def get(self, request) -> Response:
        """
        Получает список всех пользователей.

        Аргументы:
            request: Запрос.

        Возвращает:
            Response: Ответ с данными пользователями.
        """
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        """
        Создает нового пользователя.

        Аргументы:
            request: Запрос.

        Возвращает:
            Response: Ответ с данными созданного пользователя.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=["Пользователи"],
    methods=["GET", "PUT", "DELETE"],
    description="Чтение, обновление и удаления пользователя",
)
@extend_schema_view(
    get=extend_schema(
        summary="Получает данные конкретного пользователя",
    ),
    put=extend_schema(
        summary="Обновляет данные конкретного пользователя",
    ),
    delete=extend_schema(
        summary="Удаляет конкретного пользователя",
    ),
)
class UserDetailAPIView(APIView):
    """
    Представление для операций чтения, обновления и удаления пользователя.

    Методы:
        get(self, request, pk) -> Response:
            Получает данные конкретного пользователя.

        put(self, request, pk) -> Response:
            Обновляет данные конкретного пользователя.

        delete(self, request, pk) -> Response:
            Удаляет конкретного пользователя.
    """

    serializer_class = UserSerializer

    def get_object(self, pk: int) -> Union[CustomUser, Http404]:
        """
        Получает объект пользователя по его идентификатору.

        Аргументы:
            pk (int): Идентификатор пользователя.

        Возвращает:
            Union[CustomUser, Http404]: Объект пользователя или Http404, если пользователь не найден.
        """
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk: int) -> Response:
        """
        Получает данные конкретного пользователя.

        Аргументы:
            request: Запрос.
            pk (int): Идентификатор пользователя.

        Возвращает:
            Response: Ответ с данными пользователя.
        """
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk: int) -> Response:
        """
        Обновляет данные конкретного пользователя.

        Аргументы:
            request: Запрос.
            pk (int): Идентификатор пользователя.

        Возвращает:
            Response: Ответ с обновленными данными пользователя.
        """
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        """
        Удаляет конкретного пользователя.

        Аргументы:
            request: Запрос.
            pk (int): Идентификатор пользователя.

        Возвращает:
            Response: Ответ об успешном удалении пользователя.
        """
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
