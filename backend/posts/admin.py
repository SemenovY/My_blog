from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Конфигурация администратора для модели BlogPost.

    Атрибуты:
        list_display (tuple): Поля, отображаемые в списке изменений.
        list_filter (tuple): Поля, используемые для фильтрации в боковой панели.
        search_fields (tuple): Поля, используемые для поиска в верхней части страницы списка изменений.
    """

    list_display = ("id", "title", "user", "created_at", "is_published")
    list_filter = ("created_at", "is_published")
    search_fields = ("title", "text", "user__username")
