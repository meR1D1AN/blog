from django.contrib import admin

from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # отображаемые поля
    list_display = ("title", "author", "created_at", "updated_at")
    # фильтр по дате создания
    list_filter = ("created_at",)
    # поиск по названию поста
    search_fields = ("title",)
    # ссылка на автора поста
    list_display_links = ("title", "author",)
