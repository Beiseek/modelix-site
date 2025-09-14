"""
Команда для проверки функционала админки
Запускать: python manage.py check_admin
"""

from django.core.management.base import BaseCommand
from django.contrib.admin.sites import site
from django.contrib.auth.models import User
from main.models import *

class Command(BaseCommand):
    help = 'Проверяет функционал админки Django'

    def handle(self, *args, **options):
        self.stdout.write('🔍 Проверяем функционал админки...')
        
        # Проверяем регистрацию моделей
        self.check_model_registration()
        
        # Проверяем данные в базе
        self.check_database_data()
        
        # Проверяем права доступа
        self.check_permissions()
        
        self.stdout.write(self.style.SUCCESS('✅ Проверка админки завершена!'))

    def check_model_registration(self):
        """Проверяет регистрацию моделей в админке"""
        self.stdout.write('📋 Проверяем регистрацию моделей в админке...')
        
        # Список всех моделей
        models_to_check = [
            ('PrintOrder', 'Заявки на печать'),
            ('CallRequest', 'Заявки на звонок'),
            ('PortfolioItem', 'Портфолио'),
            ('Service', 'Услуги'),
            ('SocialLink', 'Социальные ссылки'),
            ('ContactInfo', 'Контактная информация'),
            ('FAQ', 'Часто задаваемые вопросы'),
        ]
        
        registered_models = [model.__name__ for model in site._registry.keys()]
        
        for model_name, description in models_to_check:
            if model_name in registered_models:
                self.stdout.write(f'  ✅ {model_name} - {description}')
            else:
                self.stdout.write(f'  ❌ {model_name} - {description} - НЕ ЗАРЕГИСТРИРОВАН!')

    def check_database_data(self):
        """Проверяет данные в базе"""
        self.stdout.write('🗄️ Проверяем данные в базе...')
        
        # Проверяем количество записей
        data_checks = [
            (Service, 'Услуги', 6),
            (PortfolioItem, 'Портфолио', 8),
            (FAQ, 'FAQ', 6),
            (SocialLink, 'Социальные ссылки', 4),
            (ContactInfo, 'Контактная информация', 1),
        ]
        
        for model, name, expected_count in data_checks:
            count = model.objects.count()
            if count >= expected_count:
                self.stdout.write(f'  ✅ {name}: {count} записей')
            else:
                self.stdout.write(f'  ⚠️ {name}: {count} записей (ожидалось {expected_count})')

    def check_permissions(self):
        """Проверяет права доступа"""
        self.stdout.write('🔐 Проверяем права доступа...')
        
        # Проверяем наличие суперпользователя
        superusers = User.objects.filter(is_superuser=True)
        if superusers.exists():
            self.stdout.write(f'  ✅ Суперпользователи: {superusers.count()} штук')
            for user in superusers:
                self.stdout.write(f'    - {user.username} ({user.email})')
        else:
            self.stdout.write('  ❌ Суперпользователи не найдены!')
        
        # Проверяем обычных пользователей
        regular_users = User.objects.filter(is_superuser=False)
        if regular_users.exists():
            self.stdout.write(f'  ℹ️ Обычные пользователи: {regular_users.count()} штук')


