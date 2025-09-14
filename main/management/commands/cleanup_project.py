"""
Команда для полной очистки проекта от ненужных файлов
Запускать: python manage.py cleanup_project
"""

from django.core.management.base import BaseCommand
import os
import shutil
from pathlib import Path

class Command(BaseCommand):
    help = 'Очищает проект от ненужных файлов'

    def handle(self, *args, **options):
        self.stdout.write('🧹 Начинаем полную очистку проекта...')
        
        # Очищаем ненужные файлы
        self.cleanup_files()
        
        # Очищаем папки
        self.cleanup_directories()
        
        # Очищаем кэш Python
        self.cleanup_python_cache()
        
        self.stdout.write(self.style.SUCCESS('✅ Очистка проекта завершена!'))

    def cleanup_files(self):
        """Удаляет ненужные файлы"""
        self.stdout.write('📁 Удаляем ненужные файлы...')
        
        # Список файлов для удаления
        files_to_delete = [
            # Старые инструкции и отчеты
            'DEPLOYMENT_GUIDE.md',
            'ZIP_DEPLOY_INSTRUCTIONS.md',
            'АВТОМАТИЧЕСКИЙ_ДЕПЛОЙ.md',
            'АНАЛИЗ_МЕДИАФАЙЛОВ.md',
            'АНАЛИЗ_ПРОБЛЕМ_VPS.md',
            'АНАЛИЗ_ПУТЕЙ_ИЗОБРАЖЕНИЙ.md',
            'ДАННЫЕ_САЙТА.md',
            'ИНСТРУКЦИЯ_ДЛЯ_ЗАКАЗЧИКА.md',
            'ИНСТРУКЦИЯ_ЗАПОЛНЕНИЯ_ДАННЫХ.md',
            'ОТЧЕТ_АДМИНКИ.md',
            'ОТЧЕТ_УДАЛЕНИЯ_CONSOLE_LOG.md',
            
            # Старые файлы деплоя
            'deploy.sh',
            'production_settings.py',
            'modelix_project_backup.tar.gz',
            'modelix.png',  # Дубликат в корне
            
            # Логи
            'django_errors.log',
            
            # Старые CSS файлы
            'static/css/styles_backup.css',
        ]
        
        deleted_count = 0
        for file_path in files_to_delete:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    self.stdout.write(f'  ✅ Удален: {file_path}')
                    deleted_count += 1
                except Exception as e:
                    self.stdout.write(f'  ❌ Ошибка удаления {file_path}: {e}')
            else:
                self.stdout.write(f'  ℹ️ Не найден: {file_path}')
        
        self.stdout.write(f'📊 Удалено файлов: {deleted_count}')

    def cleanup_directories(self):
        """Удаляет ненужные папки"""
        self.stdout.write('📂 Удаляем ненужные папки...')
        
        # Список папок для удаления
        dirs_to_delete = [
            'backups',  # Старые бэкапы
        ]
        
        deleted_count = 0
        for dir_path in dirs_to_delete:
            if os.path.exists(dir_path):
                try:
                    shutil.rmtree(dir_path)
                    self.stdout.write(f'  ✅ Удалена папка: {dir_path}')
                    deleted_count += 1
                except Exception as e:
                    self.stdout.write(f'  ❌ Ошибка удаления папки {dir_path}: {e}')
            else:
                self.stdout.write(f'  ℹ️ Папка не найдена: {dir_path}')
        
        self.stdout.write(f'📊 Удалено папок: {deleted_count}')

    def cleanup_python_cache(self):
        """Очищает кэш Python"""
        self.stdout.write('🐍 Очищаем кэш Python...')
        
        # Ищем все папки __pycache__
        cache_dirs = []
        for root, dirs, files in os.walk('.'):
            for dir_name in dirs:
                if dir_name == '__pycache__':
                    cache_dirs.append(os.path.join(root, dir_name))
        
        deleted_count = 0
        for cache_dir in cache_dirs:
            try:
                shutil.rmtree(cache_dir)
                self.stdout.write(f'  ✅ Удален кэш: {cache_dir}')
                deleted_count += 1
            except Exception as e:
                self.stdout.write(f'  ❌ Ошибка удаления кэша {cache_dir}: {e}')
        
        self.stdout.write(f'📊 Удалено кэш-папок: {deleted_count}')


