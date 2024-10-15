from django.urls import path
from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
)
from comment.apps import CommentConfig

app_name = CommentConfig.name

urlpatterns = [
    path(
        "comments/create/", CommentCreateAPIView.as_view(), name="comment-create"
    ),  # Создание комментария
    path(
        "comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment-detail"
    ),  # Просмотр комментария
    path(
        "comments/update/<int:pk>/",
        CommentUpdateAPIView.as_view(),
        name="comment-update",
    ),  # Обновление комментария
    path(
        "comments/delete/<int:pk>/",
        CommentDeleteAPIView.as_view(),
        name="comment-delete",
    ),  # Удаление комментария
]
