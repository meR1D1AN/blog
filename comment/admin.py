from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ["id", "author", "text", "created_at", "updated_at"]
    list_display_links = ["id", "text"]