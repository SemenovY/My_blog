from api.views.posts import BlogPostDetailAPIView, BlogPostListCreateAPIView
from api.views.users import UserDetailAPIView, UserListCreateAPIView
from django.urls import path

app_name = "api"

urlpatterns = [
    # Эндпоинты для пользователей, если возникнет необходимость в дальнейшем.
    path("users/", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    # Эндпоинты для постов
    path("posts/", BlogPostListCreateAPIView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", BlogPostDetailAPIView.as_view(), name="post-detail"),
]
