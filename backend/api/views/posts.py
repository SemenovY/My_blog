from api.serializers.posts import BlogPostSerializer
from posts.models import BlogPost
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogPostListCreateAPIView(APIView):
    """
    API-вью для получения списка и создания блог-постов.

    Атрибуты:
    - permission_classes: Список классов разрешений, управляющих доступом к вью.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Получить список всех постов.

        Возвращает:
        Response: Сериализованный список постов.
        """
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Создать новый пост.

        Аргументы:
        - request: Объект HTTP-запроса с данными для нового поста.

        Возвращает:
        Response: Сериализованное представление созданного поста.
        """
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetailAPIView(APIView):
    """
    API-вью для просмотра, обновления и удаления конкретного поста.

    Атрибуты:
    - permission_classes: Список классов разрешений, управляющих доступом к вью.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Получить объект поста по его идентификатору.

        Аргументы:
        - pk (int): Идентификатор поста.

        Возвращает:
        BlogPost: Объект поста.

        Выбрасывает:
        Http404: Если пост с указанным идентификатором не найден.
        """
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        """
        Получить конкретный пост.

        Аргументы:
        - request (Any): Объект HTTP-запроса.
        - pk (int): Идентификатор поста.

        Возвращает:
        Response: Сериализованное представление поста.

        Выбрасывает:
        Http404: Если пост с указанным идентификатором не найден.
        """
        blog_post = self.get_object(pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Обновить конкретный пост.

        Аргументы:
        - request (Any): Объект HTTP-запроса.
        - pk (int): Идентификатор поста.

        Возвращает:
        Response: Сериализованное представление обновленного поста.

        Выбрасывает:
        Http404: Если пост с указанным идентификатором не найден.
        """
        blog_post = self.get_object(pk)
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Удалить конкретный пост.

        Аргументы:
        - request (Any): Объект HTTP-запроса.
        - pk (int): Идентификатор поста.

        Возвращает:
        Response: Пустой ответ с кодом 204 No Content.

        Выбрасывает:
        Http404: Если пост с указанным идентификатором не найден.
        """
        blog_post = self.get_object(pk)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
