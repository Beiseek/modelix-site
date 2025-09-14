"""
Команда для сброса и пересоздания всех данных
Запускать: python manage.py reset_data
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command
from main.models import Service, PortfolioItem, FAQ, SocialLink, ContactInfo

class Command(BaseCommand):
    help = 'Сбрасывает и пересоздает все данные сайта'

    def handle(self, *args, **options):
        self.stdout.write('🗑️ Сбрасываем все данные...')
        
        # Удаляем все данные
        Service.objects.all().delete()
        PortfolioItem.objects.all().delete()
        FAQ.objects.all().delete()
        SocialLink.objects.all().delete()
        ContactInfo.objects.all().delete()
        
        self.stdout.write('✅ Все данные удалены')
        
        # Пересоздаем данные
        self.stdout.write('🔄 Пересоздаем данные...')
        call_command('migrate_data')
        
        self.stdout.write(self.style.SUCCESS('✅ Все данные успешно пересозданы!'))
