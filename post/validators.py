import re
from datetime import date
from django.core.exceptions import ValidationError


# Валидатор возраста (не менее 18 лет)
def validate_author_age(author):
    if not author.birth_date:
        raise ValidationError("У автора должна быть указана дата рождения.")

    today = date.today()
    age = (
        today.year
        - author.birth_date.year
        - ((today.month, today.day) < (author.birth_date.month, author.birth_date.day))
    )

    if age < 18:
        raise ValidationError("Автор должен быть старше 18 лет для публикации постов.")


# Валидатор для запрещенных слов в заголовке поста
def validate_post_title(value):
    forbidden_words = ["ерунда", "глупость", "чепуха"]

    for word in forbidden_words:
        if re.search(rf"\b{word}\b", value, re.IGNORECASE):
            raise ValidationError(
                f"Заголовок не должен содержать запрещенные слова: {', '.join(forbidden_words)}."
            )
