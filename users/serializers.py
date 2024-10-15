from datetime import datetime
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User
import re


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "birth_date",
            "created_at",
            "updated_at",
            "password",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Изменяем формат времени для created_at
        if representation.get("created_at"):
            created_at = datetime.strptime(
                representation["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z"
            )
            representation["created_at"] = created_at.strftime("%Y.%m.%d %H:%M:%S")
        # Изменяем формат времени для updated_at
        if representation.get("updated_at"):
            updated_at = datetime.strptime(
                representation["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z"
            )
            representation["updated_at"] = updated_at.strftime("%Y.%m.%d %H:%M:%S")
        return representation

    def validate_phone(self, value):
        # Если пользователь ввёл номер телефона с пробелами, то убирать их
        value = value.replace(" ", "")
        # К номеру телефона автоматически добавляется код +7, если пользователь не ввёл +7
        if not value.startswith("+7"):
            value = "+7" + value
        # Проверяем, кол-во цифр в номере телефона должно быть не больше 11, код не учитывается, так как он добавляется автоматически
        if len(value) != 12:
            raise ValidationError(
                "Номер телефона должен состоять из 11 цифр, код +7 не учитывается, и подставляется автоматически."
            )
        # Проверяем, что номер телефона содержит только цифры после +7
        if not value[1:].isdigit():
            raise ValidationError(
                "Номер телефона должен содержать только цифры после +7"
            )
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Пароль должен содержать не менее 8 символов.")
        if not re.search(r"\d", value):
            raise ValidationError("Пароль должен содержать хотя бы одну цифру.")
        return value

    def validate_email(self, value):
        allowed_domains = ["mail.ru", "yandex.ru"]
        domain = value.split("@")[-1]
        if domain not in allowed_domains:
            raise ValidationError(
                f"Разрешены только следующие домены: {', '.join(allowed_domains)}."
            )
        return value


class UserCreateSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(UserSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields

    def get_fields(self):
        fields = super().get_fields()
        fields.pop("created_at", None)  # Убирает поле created_at
        return fields

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
