from api.permissions import IsAuthorOrReadOnly
from api.serializers.posts import BlogPostSerializer
from drf_spectacular.utils import extend_schema
from posts.models import BlogPost
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogPostListCreateAPIView(APIView):
    """
    API-вью для получения списка и создания постов.

    Атрибуты:
    - permission_classes: Список классов разрешений, управляющих доступом к вью.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostSerializer

    @extend_schema(tags=["Посты"], summary="Получить список всех постов", operation_id="get_all_posts")
    def get(self, request):
        """
        Получить список всех постов.

        Возвращает:
        Response: Сериализованный список постов.
        """
        posts = BlogPost.objects.all().order_by("-created_at")
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(posts, request)
        serializer = BlogPostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(tags=["Посты"], summary="Создать новый пост", operation_id="create_post")
    def post(self, request):
        """
        Создать новый пост.

        Аргументы:
        - request: Объект HTTP-запроса с данными для нового поста.

        Возвращает:
        Response: Сериализованное представление созданного поста.
        """
        serializer = BlogPostSerializer(data=request.data)
        serializer.fields["user"].read_only = True
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user"] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BlogPostDetailAPIView(APIView):
    """
    API-вью для просмотра, обновления и удаления конкретного поста.

    Атрибуты:
    - permission_classes: Список классов разрешений, управляющих доступом к вью.
    """

    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = BlogPostSerializer

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

    @extend_schema(tags=["Посты"], summary="Получить конкретный пост", operation_id="get_post_detail")
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
        post = self.get_object(pk)
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)

    @extend_schema(tags=["Посты"], summary="Обновить конкретный пост", operation_id="update_post")
    def put(self, request, pk):
        """
        Обновить конкретный пост.
        """
        instance = self.get_object(pk)
        self.check_object_permissions(request, instance)

        serializer = BlogPostSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @extend_schema(tags=["Посты"], summary="Удалить конкретный пост", operation_id="delete_post")
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
        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
