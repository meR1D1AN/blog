from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_email_domain, validate_password, validate_phone


class User(AbstractUser):
    username = models.CharField(
        max_length=50, unique=True, verbose_name="Логин", help_text="Введите логин"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите электронную почту, разрешены домены: mail.ru, yandex.ru",
        validators=[validate_email_domain],
    )
    password = models.CharField(
        verbose_name="Пароль",
        help_text="Введите пароль, должен быть не менее 8 символов, должен включать цифры",
        validators=[validate_password],
    )
    phone = models.CharField(
        max_length=17,
        unique=True,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона, в формате 999 123 45 67, +7 подставится автоматически",
        validators=[validate_phone],
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения", help_text="Выберите дату рождения"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания аккаунта",
        help_text="Дата создания аккаунта",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования аккаунта",
        help_text="Дата редактирования аккаунта",
    )

    def __str__(self):
        return f"{self.username} - ({self.email})"

    def clean_phone(self):
        # Убираем пробелы
        phone = self.phone.replace(" ", "")
        # Добавляем код +7, если не введен
        if not phone.startswith("+7"):
            phone = "+7" + phone
        return phone

    def save(self, *args, **kwargs):
        # Перед сохранением форматируем номер телефона
        self.phone = self.clean_phone()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
