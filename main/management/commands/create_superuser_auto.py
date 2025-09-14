"""
Команда для автоматического создания суперпользователя
Запускать: python manage.py create_superuser_auto
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Автоматически создает суперпользователя'

    def handle(self, *args, **options):
        self.stdout.write('👤 Создаем суперпользователя...')
        
        # Данные для суперпользователя
        username = 'admin'
        email = 'admin@modelix.ru'
        password = 'admin123'  # В продакшене нужно изменить!
        
        # Проверяем, существует ли уже суперпользователь
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.WARNING('⚠️ Суперпользователь уже существует'))
            return
        
        # Создаем суперпользователя
        try:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            
            self.stdout.write(self.style.SUCCESS('✅ Суперпользователь создан!'))
            self.stdout.write(f'  👤 Логин: {username}')
            self.stdout.write(f'  🔑 Пароль: {password}')
            self.stdout.write(f'  📧 Email: {email}')
            self.stdout.write('')
            self.stdout.write('⚠️ ВАЖНО: Смените пароль после первого входа!')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Ошибка при создании суперпользователя: {e}'))


