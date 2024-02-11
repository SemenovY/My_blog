from api.views.posts import BlogPostDetailAPIView, BlogPostListCreateAPIView
from api.views.users import CustomUserDetailAPIView, CustomUserListCreateAPIView
from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("users/", CustomUserListCreateAPIView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", CustomUserDetailAPIView.as_view(), name="user-detail"),
    path("posts/", BlogPostListCreateAPIView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", BlogPostDetailAPIView.as_view(), name="post-detail"),
]
