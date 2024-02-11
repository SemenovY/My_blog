from api.serializers.users import UserSerializer
from posts.models import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели BlogPost.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ("id", "user", "title", "text", "created_at", "is_published")
        read_only_fields = ["user"]
