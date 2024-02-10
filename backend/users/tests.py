# from typing import Any, Dict
#
# from api.serializers.users import UserSerializer
# from rest_framework import status
# from rest_framework.test import APIClient
#
# from .models import CustomUser
#
#
# class TestUserAPI:
#     """
#     Тесты для API представлений пользователей.
#
#     Атрибуты:
#         client (APIClient): Клиент для отправки запросов к API.
#         list_url (str): URL для получения списка пользователей.
#     """
#
#     client = APIClient()
#     list_url = "/users/"
#
#     def test_get_users_list(self):
#         """
#         Тестирование получения списка пользователей.
#
#         Методы:
#             get(self, request) -> Response:
#                 Получает список всех пользователей.
#         """
#         response = self.client.get(self.list_url)
#         assert response.status_code == status.HTTP_200_OK
#         serialized_data = UserSerializer(CustomUser.objects.all(), many=True).data
#         assert response.data == serialized_data
#
#     def test_create_user(self):
#         """
#         Тестирование создания обычного пользователя.
#
#         Методы:
#             post(self, request) -> Response:
#                 Создает нового пользователя.
#         """
#         user_data: Dict[str, Any] = {
#             "username": "testuser",
#             "email": "testuser@example.com",
#             "password": "testpassword",
#             "role": "user",
#         }
#         response = self.client.post(self.list_url, user_data, format="json")
#         assert response.status_code == status.HTTP_201_CREATED
#         assert CustomUser.objects.filter(username=user_data["username"]).exists()
#
#     def test_create_user_invalid_data(self):
#         """
#         Тестирование создания пользователя с недопустимыми данными.
#
#         Методы:
#             post(self, request) -> Response:
#                 Создает нового пользователя.
#         """
#         invalid_data: Dict[str, Any] = {
#             "username": "invaliduser",
#             "email": "invaliduser@example.com",
#             "password": "",  # Invalid, as password is required
#             "role": "user",
#         }
#         response = self.client.post(self.list_url, invalid_data, format="json")
#         assert response.status_code == status.HTTP_400_BAD_REQUEST
#         assert not CustomUser.objects.filter(username=invalid_data["username"]).exists()
#
#
# # Аналогичные тесты для UserDetailAPIView
# class TestUserDetailAPI:
#     """
#     Тесты для API представлений деталей пользователя.
#
#     Атрибуты:
#         client (APIClient): Клиент для отправки запросов к API.
#     """
#
#     client = APIClient()
#
#     def test_get_user_details(self):
#         """
#         Тестирование получения деталей пользователя.
#
#         Методы:
#             get(self, request, pk) -> Response:
#                 Получает данные конкретного пользователя.
#         """
#         user = CustomUser.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             role="user",
#         )
#         detail_url = f"/users/{user.id}/"
#         response = self.client.get(detail_url)
#         assert response.status_code == status.HTTP_200_OK
#         serialized_data = UserSerializer(user).data
#         assert response.data == serialized_data
#
#     def test_update_user_details(self):
#         """
#         Тестирование обновления деталей пользователя.
#
#         Методы:
#             put(self, request, pk) -> Response:
#                 Обновляет данные конкретного пользователя.
#         """
#         user = CustomUser.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             role="user",
#         )
#         detail_url = f"/users/{user.id}/"
#         updated_data = {
#             "username": "updateduser",
#             "email": "updateduser@example.com",
#             "role": "admin",
#         }
#         response = self.client.put(detail_url, updated_data, format="json")
#         assert response.status_code == status.HTTP_200_OK
#         user.refresh_from_db()
#         assert user.username == updated_data["username"]
#         assert user.email == updated_data["email"]
#         assert user.role == updated_data["role"]
#
#     def test_delete_user(self):
#         """
#         Тестирование удаления пользователя.
#
#         Методы:
#             delete(self, request, pk) -> Response:
#                 Удаляет конкретного пользователя.
#         """
#         user = CustomUser.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             role="user",
#         )
#         detail_url = f"/users/{user.id}/"
#         response = self.client.delete(detail_url)
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not CustomUser.objects.filter(id=user.id).exists()
import pytest
from api.views.users import UserListCreateAPIView
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


def test_get_user_list(api_client, django_user_model):
    # Create some test users
    user1 = django_user_model.objects.create(username="user1", email="user1@example.com", password="password1")
    user2 = django_user_model.objects.create(username="user2", email="user2@example.com", password="password2")

    # Authenticate the client if needed
    api_client.force_authenticate(user=user1)

    # Make the API request to get the user list
    url = reverse("api:user-list")
    response = api_client.get(url)

    # Check that the request was successful (status code 200)
    assert response.status_code == status.HTTP_200_OK

    # Check the response data
    assert len(response.data) == 2  # Assuming two users were created
    assert response.data[0]["username"] == user1.username
    assert response.data[1]["username"] == user2.username
