"""
Команда для исправления проблем с изображениями
Запускать: python manage.py fix_images
"""

from django.core.management.base import BaseCommand
import os
import shutil
from pathlib import Path

class Command(BaseCommand):
    help = 'Исправляет проблемы с изображениями'

    def handle(self, *args, **options):
        self.stdout.write('🖼️ Исправляем проблемы с изображениями...')
        
        # Проверяем и исправляем отсутствующие изображения
        self.fix_missing_images()
        
        # Проверяем пути в шаблоне
        self.check_template_paths()
        
        self.stdout.write(self.style.SUCCESS('✅ Проверка изображений завершена!'))

    def fix_missing_images(self):
        """Исправляет отсутствующие изображения"""
        self.stdout.write('🔍 Проверяем отсутствующие изображения...')
        
        # Список изображений, которые должны существовать
        required_images = [
            'media/portfolio/portfl8.jpg',  # Отсутствует!
        ]
        
        for image_path in required_images:
            if not os.path.exists(image_path):
                self.stdout.write(f'  ❌ Отсутствует: {image_path}')
                
                # Пытаемся создать из существующего изображения
                if 'portfl8.jpg' in image_path:
                    source = 'media/portfolio/portfl1.jpg'
                    if os.path.exists(source):
                        shutil.copy2(source, image_path)
                        self.stdout.write(f'  ✅ Создан: {image_path} (копия {source})')
                    else:
                        self.stdout.write(f'  ⚠️ Не удалось создать: {image_path}')
            else:
                self.stdout.write(f'  ✅ Существует: {image_path}')

    def check_template_paths(self):
        """Проверяет пути в шаблоне"""
        self.stdout.write('📝 Проверяем пути в шаблоне...')
        
        template_path = 'main/templates/main/index.html'
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ищем проблемные пути
            problematic_paths = [
                '/media/portfolio/portfl8.jpg',  # Отсутствует
            ]
            
            for path in problematic_paths:
                if path in content:
                    self.stdout.write(f'  ⚠️ Проблемный путь в шаблоне: {path}')
                else:
                    self.stdout.write(f'  ✅ Путь не найден в шаблоне: {path}')
        else:
            self.stdout.write('  ❌ Шаблон не найден!')


