import re
from django.core.exceptions import ValidationError



def validate_password(value):
    """
    # Валидатор для пароля при создании пользователя с помощью API или в админ панели Django
    """
    if len(value) < 8:
        raise ValidationError("Пароль должен содержать не менее 8 символов.")
    if not re.search(r"\d", value):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру.")



def validate_email_domain(value):
    """
    Валидатор для домена электронной почты при создании пользователя с помощью API или в админ панели Django
    """
    allowed_domains = ["mail.ru", "yandex.ru"]
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError(
            f"Разрешены только следующие домены: {', '.join(allowed_domains)}."
        )


def validate_phone(value):
    """
    Валидатор для номера телефона при создании пользователя с помощью API или в админ панели Django
    """
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
        raise ValidationError("Номер телефона должен содержать только цифры после +7")
    return value
