# Generated by Django 5.1.2 on 2024-10-15 07:42

import django.contrib.auth.models
import django.utils.timezone
import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        help_text="Введите логин",
                        max_length=50,
                        unique=True,
                        verbose_name="Логин",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите электронную почту, разрешены домены: mail.ru, yandex.ru",
                        max_length=254,
                        unique=True,
                        validators=[users.validators.validate_email_domain],
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        help_text="Введите пароль, должен быть не менее 8 символов, должен включать цифры",
                        validators=[users.validators.validate_password],
                        verbose_name="Пароль",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Введите номер телефона, в формате 999 123 45 67, +7 подставится автоматически",
                        max_length=17,
                        unique=True,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        help_text="Выберите дату рождения", verbose_name="Дата рождения"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Дата создания аккаунта",
                        verbose_name="Дата создания аккаунта",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Дата редактирования аккаунта",
                        verbose_name="Дата редактирования аккаунта",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
