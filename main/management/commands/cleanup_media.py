"""
Команда для очистки ненужных медиафайлов
Запускать: python manage.py cleanup_media
"""

from django.core.management.base import BaseCommand
import os
from pathlib import Path

class Command(BaseCommand):
    help = 'Удаляет ненужные медиафайлы'

    def handle(self, *args, **options):
        self.stdout.write('🧹 Очищаем ненужные медиафайлы...')
        
        # Список файлов для удаления
        files_to_delete = [
            'media/services/reverse_engineering_KFJWLVI.jpg',
            'media/portfolio/Снимок_экрана_2025-09-13_093954.png'
        ]
        
        total_saved = 0
        
        for file_path in files_to_delete:
            if os.path.exists(file_path):
                # Получаем размер файла
                file_size = os.path.getsize(file_path)
                total_saved += file_size
                
                # Удаляем файл
                os.remove(file_path)
                
                self.stdout.write(f'  ✅ Удален: {file_path} ({file_size:,} байт)')
            else:
                self.stdout.write(f'  ⚠️ Файл не найден: {file_path}')
        
        # Конвертируем байты в KB/MB
        if total_saved > 1024 * 1024:
            saved_str = f'{total_saved / (1024 * 1024):.1f} MB'
        elif total_saved > 1024:
            saved_str = f'{total_saved / 1024:.1f} KB'
        else:
            saved_str = f'{total_saved} байт'
        
        self.stdout.write(self.style.SUCCESS(f'✅ Очистка завершена! Сэкономлено: {saved_str}'))


