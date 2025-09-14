"""
Команда для проверки всех путей к изображениям перед деплоем
Запускать: python manage.py check_images
"""

from django.core.management.base import BaseCommand
import os
import re
from pathlib import Path

class Command(BaseCommand):
    help = 'Проверяет все пути к изображениям перед деплоем'

    def handle(self, *args, **options):
        self.stdout.write('🔍 Проверяем все пути к изображениям...')
        
        # Проверяем все изображения
        self.check_all_images()
        
        # Проверяем пути в шаблонах
        self.check_template_paths()
        
        # Проверяем пути в CSS
        self.check_css_paths()
        
        self.stdout.write(self.style.SUCCESS('✅ Проверка изображений завершена!'))

    def check_all_images(self):
        """Проверяет все изображения"""
        self.stdout.write('📁 Проверяем существование изображений...')
        
        # Список всех изображений из кода
        all_images = [
            # Services
            'media/services/modelix.png',
            'media/services/hero_block.png',
            'media/services/printer.jpg',
            'media/services/3d_modeling.jpg',
            'media/services/3d_printing.jpg',
            'media/services/3d_scanning.jpg',
            'media/services/reverse_engineering.jpg',
            'media/services/engineering.jpg',
            'media/services/post_processing.jpg',
            
            # Portfolio
            'media/portfolio/portfl1.jpg',
            'media/portfolio/portfl2.jpg',
            'media/portfolio/portfl3.jpg',
            'media/portfolio/portfl4.jpg',
            'media/portfolio/portfl5.jpg',
            'media/portfolio/portfl6.jpg',
            'media/portfolio/portfl7.jpeg',
            'media/portfolio/portfl8.jpg',
        ]
        
        missing_count = 0
        total_count = len(all_images)
        
        for image_path in all_images:
            if os.path.exists(image_path):
                self.stdout.write(f'  ✅ {image_path}')
            else:
                self.stdout.write(f'  ❌ {image_path} - ОТСУТСТВУЕТ!')
                missing_count += 1
        
        self.stdout.write(f'📊 Результат: {total_count - missing_count}/{total_count} изображений найдено')
        
        if missing_count > 0:
            self.stdout.write(self.style.ERROR(f'❌ Найдено {missing_count} отсутствующих изображений!'))
        else:
            self.stdout.write(self.style.SUCCESS('✅ Все изображения на месте!'))

    def check_template_paths(self):
        """Проверяет пути в шаблонах"""
        self.stdout.write('📝 Проверяем пути в шаблонах...')
        
        template_path = 'main/templates/main/index.html'
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ищем все пути к изображениям
            image_paths = re.findall(r'src="([^"]*\.(?:jpg|jpeg|png|gif|webp))"', content)
            
            for path in image_paths:
                if path.startswith('/media/'):
                    # Убираем ведущий слеш для проверки
                    file_path = path[1:]  # Убираем первый символ '/'
                    if os.path.exists(file_path):
                        self.stdout.write(f'  ✅ {path}')
                    else:
                        self.stdout.write(f'  ❌ {path} - ФАЙЛ НЕ НАЙДЕН!')
                elif path.startswith('{{'):
                    self.stdout.write(f'  ⚠️ {path} - динамический путь (проверить в базе данных)')
                else:
                    self.stdout.write(f'  ℹ️ {path} - внешний путь')

    def check_css_paths(self):
        """Проверяет пути в CSS"""
        self.stdout.write('🎨 Проверяем пути в CSS...')
        
        css_files = [
            'static/css/styles.css',
            'static/css/mobile.css',
            'static/css/hero-responsive.css',
        ]
        
        for css_file in css_files:
            if os.path.exists(css_file):
                with open(css_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Ищем пути к изображениям в CSS
                image_paths = re.findall(r'url\(["\']?([^"\']*\.(?:jpg|jpeg|png|gif|webp))["\']?\)', content)
                
                for path in image_paths:
                    if path.startswith('/media/'):
                        file_path = path[1:]  # Убираем ведущий слеш
                        if os.path.exists(file_path):
                            self.stdout.write(f'  ✅ {css_file}: {path}')
                        else:
                            self.stdout.write(f'  ❌ {css_file}: {path} - ФАЙЛ НЕ НАЙДЕН!')
                    else:
                        self.stdout.write(f'  ℹ️ {css_file}: {path} - внешний путь')


