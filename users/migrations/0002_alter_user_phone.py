# Generated by Django 5.1.2 on 2024-10-15 18:24

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                help_text="Введите номер телефона, в формате 999 123 45 67, +7 подставится автоматически",
                max_length=17,
                unique=True,
                validators=[users.validators.validate_phone],
                verbose_name="Номер телефона",
            ),
        ),
    ]
