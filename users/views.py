from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.generics import CreateAPIView


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для обработки всех операций CRUD для модели User.
    """

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        elif self.action in ["partial_update", "update"]:
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        """
        Возвращает список разрешений для каждого действия.
        """
        permission_classes = {
            "create": [AllowAny],  # Разрешаем всем доступ к регистрации
            "retrieve": [
                IsAuthenticated,
                IsOwnerOrAdmin,
            ],  # Пользователь может читать себя, админ — всех
            "update": [
                IsAuthenticated,
                IsOwnerOrAdmin,
            ],  # Пользователь может редактировать себя, админ — всех
            "partial_update": [
                IsAuthenticated,
                IsOwnerOrAdmin,
            ],  # Пользователь может редактировать себя, админ — всех
            "destroy": [
                IsAdminUser
            ],  # Только администратор может удалять пользователей
            "list": [
                IsAdminUser,
            ],  # Только администратор может видеть список всех пользователей
        }.get(
            self.action, [IsAuthenticated, IsAdminUser]
        )  # По умолчанию только администратор и авторизованные пользователи

        return [permission() for permission in permission_classes]
