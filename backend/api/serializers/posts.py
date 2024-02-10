from rest_framework import serializers


class BlogPostSerializer(serializers.Serializer):
    """
    Сериализатор для модели BlogPost.

    Атрибуты:
    - user (str): Пользователь, связанный с записью в блоге.
    - title (str): Заголовок записи в блоге.
    - text (str): Текстовое содержимое записи в блоге.
    - created_at (DateTime): Временная метка создания записи в блоге.
    - published (bool): Указывает, опубликована ли запись в блоге.
    """

    user = serializers.CharField()
    title = serializers.CharField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField()
    published = serializers.BooleanField()
