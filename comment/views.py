from .models import Comment
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from post.permissions import IsAuthorOrAdmin
from .serializers import CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    """
    Создание комментария. Доступно для авторизованных пользователей.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated
    ]  # Только авторизованные пользователи могут создавать комментарии

    def perform_create(self, serializer):
        # Автоматически устанавливаем автора текущим пользователем
        serializer.save(author=self.request.user)


class CommentDetailAPIView(generics.RetrieveAPIView):
    """
    Просмотр комментария. Доступно всем пользователям.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]  # Доступ к просмотру для всех


class CommentUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление комментария. Пользователь может редактировать только свои комментарии, администратор
    может редактировать все.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrAdmin,
    ]  # Только автор или администратор могут редактировать


class CommentDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление комментария. Пользователь может удалять только свои комментарии, администратор может удалять все.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrAdmin,
    ]  # Только автор или администратор могут удалять
