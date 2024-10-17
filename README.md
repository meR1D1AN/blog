# Описание проекта
Приложение, в котором пользователи могут писать посты и комментировать их.

## Требования

- Python 3.12.6
- Django 5.1.2
- DRF 3.15.2
- PostgreSQL 17

## Установка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/meR1D1AN/blog.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd blog
    ```

3. Установите зависимости с помощью Poetry:
    ```bash
    poetry install
    ```

4. Скопируйте .env.sample в .env и настройте переменные окружения в файле .env.
    ```bash
    cp .env.sample .env
    ```

5. Выполните миграции базы данных:
    ```bash
    poetry run python manage.py migrate
    ```

6. Создайте суперпользователя для доступа к админке:
    ```bash
    poetry run python manage.py createsuperuser
    ```
   или же можете воспользоваться командой `csu`, обязательно указав в файле .env ADMIN_PASSWORD:
    ```bash
    poetry run python manage.py csu
    ```

7. Запустите сервер:
    ```bash
    poetry run python manage.py runserver
    ```
   
## Документация API

Автогенерируемая документация доступна по следующим URL:

- Swagger: http://localhost:8000/docs/
- ReDoc: http://localhost:8000/redoc/
