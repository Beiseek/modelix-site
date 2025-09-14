#!/usr/bin/env python3
"""
Автоматический скрипт деплоя для VPS
Запускать: python auto_deploy.py
"""

import os
import sys
import subprocess
import django
from pathlib import Path

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelix_site.settings')
django.setup()

def run_command(command, description):
    """Выполняет команду и выводит результат"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - успешно")
        if result.stdout:
            print(f"   Вывод: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - ошибка")
        print(f"   Ошибка: {e.stderr.strip()}")
        return False

def main():
    print("🚀 АВТОМАТИЧЕСКИЙ ДЕПЛОЙ MODELIX САЙТА")
    print("=" * 50)
    
    # Проверяем, что мы в правильной директории
    if not os.path.exists('manage.py'):
        print("❌ Ошибка: manage.py не найден. Запустите скрипт из корня проекта.")
        sys.exit(1)
    
    # 1. Установка зависимостей
    print("\n📦 УСТАНОВКА ЗАВИСИМОСТЕЙ")
    print("-" * 30)
    
    if not run_command("pip install -r requirements_production.txt", "Установка зависимостей"):
        print("❌ Не удалось установить зависимости")
        sys.exit(1)
    
    # 2. Сбор статических файлов
    print("\n📁 СБОР СТАТИЧЕСКИХ ФАЙЛОВ")
    print("-" * 30)
    
    if not run_command("python manage.py collectstatic --noinput --settings=modelix_site.settings_production", 
                      "Сбор статических файлов"):
        print("❌ Не удалось собрать статические файлы")
        sys.exit(1)
    
    # 3. Выполнение миграций
    print("\n🗄️ МИГРАЦИИ БАЗЫ ДАННЫХ")
    print("-" * 30)
    
    if not run_command("python manage.py migrate --settings=modelix_site.settings_production", 
                      "Выполнение миграций"):
        print("❌ Не удалось выполнить миграции")
        sys.exit(1)
    
    # 4. Создание данных
    print("\n📋 СОЗДАНИЕ ДАННЫХ")
    print("-" * 30)
    
    if not run_command("python manage.py reset_data --settings=modelix_site.settings_production", 
                      "Создание данных сайта"):
        print("❌ Не удалось создать данные")
        sys.exit(1)
    
    
    # Очищаем ненужные медиафайлы
    if not run_command("python manage.py cleanup_media --settings=modelix_site.settings_production", 
                      "Очистка медиафайлов"):
        print("❌ Не удалось очистить медиафайлы")
        sys.exit(1)
    
    # Проверяем изображения
    if not run_command("python manage.py check_images --settings=modelix_site.settings_production", 
                      "Проверка изображений"):
        print("❌ Обнаружены проблемы с изображениями")
        sys.exit(1)
    
    # Проверяем админку
    if not run_command("python manage.py check_admin --settings=modelix_site.settings_production", 
                      "Проверка админки"):
        print("❌ Обнаружены проблемы с админкой")
        sys.exit(1)
    
    # Очищаем проект от ненужных файлов
    if not run_command("python manage.py cleanup_project --settings=modelix_site.settings_production", 
                      "Очистка проекта"):
        print("❌ Не удалось очистить проект")
        sys.exit(1)
    
    # Проверяем совместимость с SSL
    if not run_command("python manage.py check_ssl --settings=modelix_site.settings_production", 
                      "Проверка SSL совместимости"):
        print("❌ Обнаружены проблемы с SSL")
        sys.exit(1)
    
    # 5. Создание суперпользователя
    print("\n👤 СОЗДАНИЕ СУПЕРПОЛЬЗОВАТЕЛЯ")
    print("-" * 30)
    
    if not run_command("python manage.py create_superuser_auto --settings=modelix_site.settings_production", 
                      "Создание суперпользователя"):
        print("❌ Не удалось создать суперпользователя")
        sys.exit(1)
    
    # 6. Проверка сайта
    print("\n🔍 ПРОВЕРКА САЙТА")
    print("-" * 30)
    
    if not run_command("python manage.py check --settings=modelix_site.settings_production", 
                      "Проверка конфигурации"):
        print("❌ Обнаружены ошибки в конфигурации")
        sys.exit(1)
    
    # 7. Запуск тестового сервера
    print("\n🌐 ЗАПУСК СЕРВЕРА")
    print("-" * 30)
    
    print("✅ Деплой завершен успешно!")
    print("")
    print("📋 ИНФОРМАЦИЯ ДЛЯ ДОСТУПА:")
    print("  🌐 Сайт: http://ваш-ip-адрес:8000")
    print("  👤 Админка: http://ваш-ip-адрес:8000/admin/")
    print("  🔑 Логин: admin")
    print("  🔑 Пароль: admin123")
    print("")
    print("⚠️ ВАЖНО:")
    print("  1. Смените пароль админа после первого входа")
    print("  2. Настройте домен в ALLOWED_HOSTS")
    print("  3. Настройте HTTPS для продакшена")
    print("  4. Настройте веб-сервер (nginx/apache)")
    print("")
    print("🚀 Для запуска сервера выполните:")
    print("  python manage.py runserver 0.0.0.0:8000 --settings=modelix_site.settings_production")

if __name__ == "__main__":
    main()
