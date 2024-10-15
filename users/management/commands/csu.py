from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Создание учётки админа"

    def handle(self, *args, **options):
        user = User.objects.create(
            username="admin2",
            email="admin2@mail.ru",
            birth_date="1991-05-19",
            phone="+79992345679",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password("Admin1234")
        user.save()
