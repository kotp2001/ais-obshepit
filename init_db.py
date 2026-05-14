#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

User = get_user_model()

print("Выполняем миграции...")
call_command('migrate', '--noinput')
print("Миграции выполнены.")

print("Создаём суперпользователя...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    print("Суперпользователь admin/admin123 создан")
else:
    print("Суперпользователь уже существует")

print("Собираем статику...")
call_command('collectstatic', '--noinput')
print("Готово!")
