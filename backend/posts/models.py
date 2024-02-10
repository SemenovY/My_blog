from datetime import datetime
from typing import Text

from django.db import models
from users.models import CustomUser


class BlogPost(models.Model):
    """
    Модель для представления постов.

    Поля:
        user (CustomUser): Связь с пользователем, создавшим пост.
        title (str): Заголовок поста (максимум 255 символов).
        text (Text): Текст поста.
        created_at (DateTime): Дата и время создания поста (устанавливается автоматически).
        is_published (bool): Флаг публикации поста (по умолчанию False).

    Методы:
        __str__(): Возвращает строковое представление объекта, используя заголовок поста.
    """

    user: CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title: str = models.CharField(max_length=255)
    text: Text = models.TextField()
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    is_published: bool = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self) -> str:
        return self.title
