import re
from django.core.exceptions import ValidationError


# Валидатор для пароля
def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Пароль должен содержать не менее 8 символов.")
    if not re.search(r"\d", value):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру.")


# Валидатор для email
def validate_email_domain(value):
    allowed_domains = ["mail.ru", "yandex.ru"]
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError(
            f"Разрешены только следующие домены: {', '.join(allowed_domains)}."
        )
