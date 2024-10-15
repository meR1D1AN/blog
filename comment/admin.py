from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fileds = ["author", "text", "created_at", "updated_at"]
