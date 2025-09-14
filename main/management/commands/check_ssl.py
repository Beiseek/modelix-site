"""
Команда для проверки совместимости с SSL
Запускать: python manage.py check_ssl
"""

from django.core.management.base import BaseCommand
from django.conf import settings
import os
import re
from pathlib import Path

class Command(BaseCommand):
    help = 'Проверяет совместимость проекта с SSL'

    def handle(self, *args, **options):
        self.stdout.write('🔒 Проверяем совместимость с SSL...')
        
        # Проверяем настройки Django
        self.check_django_settings()
        
        # Проверяем шаблоны
        self.check_templates()
        
        # Проверяем статические файлы
        self.check_static_files()
        
        # Проверяем JavaScript
        self.check_javascript()
        
        self.stdout.write(self.style.SUCCESS('✅ Проверка SSL завершена!'))

    def check_django_settings(self):
        """Проверяет настройки Django для SSL"""
        self.stdout.write('⚙️ Проверяем настройки Django...')
        
        # Проверяем безопасные настройки
        security_settings = [
            ('SECURE_HSTS_SECONDS', 'HSTS включен'),
            ('SECURE_HSTS_INCLUDE_SUBDOMAINS', 'HSTS для поддоменов'),
            ('SECURE_HSTS_PRELOAD', 'HSTS preload'),
            ('SECURE_BROWSER_XSS_FILTER', 'XSS защита'),
            ('SECURE_CONTENT_TYPE_NOSNIFF', 'MIME sniffing защита'),
            ('X_FRAME_OPTIONS', 'Clickjacking защита'),
        ]
        
        for setting, description in security_settings:
            if hasattr(settings, setting):
                value = getattr(settings, setting)
                if value:
                    self.stdout.write(f'  ✅ {setting}: {description}')
                else:
                    self.stdout.write(f'  ⚠️ {setting}: {description} - отключено')
            else:
                self.stdout.write(f'  ❌ {setting}: {description} - не настроено')
        
        # Проверяем SSL настройки
        ssl_settings = [
            ('SECURE_SSL_REDIRECT', 'SSL редирект'),
            ('SESSION_COOKIE_SECURE', 'Безопасные сессии'),
            ('CSRF_COOKIE_SECURE', 'Безопасные CSRF'),
        ]
        
        for setting, description in ssl_settings:
            if hasattr(settings, setting):
                value = getattr(settings, setting)
                if value:
                    self.stdout.write(f'  ✅ {setting}: {description} - включено')
                else:
                    self.stdout.write(f'  ⚠️ {setting}: {description} - отключено (нужно для SSL)')
            else:
                self.stdout.write(f'  ⚠️ {setting}: {description} - не настроено (нужно для SSL)')

    def check_templates(self):
        """Проверяет шаблоны на проблемы с SSL"""
        self.stdout.write('📝 Проверяем шаблоны...')
        
        template_path = 'main/templates/main/index.html'
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ищем HTTP ссылки
            http_links = re.findall(r'href="(http://[^"]*)"', content)
            http_srcs = re.findall(r'src="(http://[^"]*)"', content)
            
            if http_links:
                self.stdout.write(f'  ❌ Найдены HTTP ссылки: {len(http_links)}')
                for link in http_links:
                    self.stdout.write(f'    - {link}')
            else:
                self.stdout.write('  ✅ HTTP ссылки не найдены')
            
            if http_srcs:
                self.stdout.write(f'  ❌ Найдены HTTP src: {len(http_srcs)}')
                for src in http_srcs:
                    self.stdout.write(f'    - {src}')
            else:
                self.stdout.write('  ✅ HTTP src не найдены')
            
            # Проверяем HTTPS ссылки
            https_links = re.findall(r'href="(https://[^"]*)"', content)
            if https_links:
                self.stdout.write(f'  ✅ HTTPS ссылки: {len(https_links)}')
        else:
            self.stdout.write('  ❌ Шаблон не найден!')

    def check_static_files(self):
        """Проверяет статические файлы"""
        self.stdout.write('📁 Проверяем статические файлы...')
        
        # Проверяем WhiteNoise
        if 'whitenoise.middleware.WhiteNoiseMiddleware' in settings.MIDDLEWARE:
            self.stdout.write('  ✅ WhiteNoise настроен')
        else:
            self.stdout.write('  ⚠️ WhiteNoise не настроен')
        
        # Проверяем STATICFILES_STORAGE
        if hasattr(settings, 'STATICFILES_STORAGE'):
            storage = settings.STATICFILES_STORAGE
            if 'whitenoise' in storage.lower():
                self.stdout.write('  ✅ WhiteNoise storage настроен')
            else:
                self.stdout.write('  ⚠️ WhiteNoise storage не настроен')

    def check_javascript(self):
        """Проверяет JavaScript файлы"""
        self.stdout.write('📜 Проверяем JavaScript...')
        
        js_files = [
            'static/js/main.js',
            'static/js/hero-responsive.js',
        ]
        
        for js_file in js_files:
            if os.path.exists(js_file):
                with open(js_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Ищем проблемные паттерны
                http_patterns = re.findall(r'http://', content)
                location_patterns = re.findall(r'location\.href\s*=', content)
                
                if http_patterns:
                    self.stdout.write(f'  ⚠️ {js_file}: найдены HTTP ссылки')
                else:
                    self.stdout.write(f'  ✅ {js_file}: HTTP ссылки не найдены')
                
                if location_patterns:
                    self.stdout.write(f'  ℹ️ {js_file}: найдены location.href (проверить вручную)')
            else:
                self.stdout.write(f'  ❌ {js_file}: файл не найден')


