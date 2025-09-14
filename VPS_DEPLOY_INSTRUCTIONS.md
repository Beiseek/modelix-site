# 🚀 Инструкция по деплою Modelix на VPS

## 📋 Подготовка VPS

### 1. Обновление системы
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Установка необходимых пакетов
```bash
sudo apt install -y python3 python3-pip python3-venv nginx postgresql postgresql-contrib git
```

### 3. Создание пользователя для проекта
```bash
sudo adduser modelix
sudo usermod -aG sudo modelix
su - modelix
```

## 🗄️ Настройка PostgreSQL

### 1. Создание базы данных
```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE modelix_db;
CREATE USER modelix_user WITH PASSWORD 'ваш_пароль_бд';
GRANT ALL PRIVILEGES ON DATABASE modelix_db TO modelix_user;
\q
```

## 📁 Загрузка проекта

### 1. Клонирование репозитория
```bash
cd /home/modelix
git clone https://github.com/Beiseek/modelix-site.git
cd modelix-site
```

### 2. Создание виртуального окружения
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements_production.txt
```

## ⚙️ Настройка Django

### 1. Обновление настроек
```bash
nano modelix_site/settings_production.py
```

**Обязательно изменить:**
- `SECRET_KEY` - сгенерировать новый
- `ALLOWED_HOSTS` - добавить ваш домен и IP
- `DATABASES` - настройки PostgreSQL

### 2. Выполнение миграций
```bash
python manage.py migrate --settings=modelix_site.settings_production
```

### 3. Сбор статических файлов
```bash
python manage.py collectstatic --settings=modelix_site.settings_production --noinput
```

### 4. Автоматическая настройка данных
```bash
python auto_deploy.py
```

## 🌐 Настройка Nginx

### 1. Создание конфигурации
```bash
sudo nano /etc/nginx/sites-available/modelix
```

```nginx
server {
    listen 80;
    server_name ваш-домен.ru www.ваш-домен.ru;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /home/modelix/modelix-site/staticfiles/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    location /media/ {
        alias /home/modelix/modelix-site/media/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### 2. Активация сайта
```bash
sudo ln -s /etc/nginx/sites-available/modelix /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## 🔒 Настройка SSL (Let's Encrypt)

### 1. Установка Certbot
```bash
sudo apt install certbot python3-certbot-nginx
```

### 2. Получение SSL сертификата
```bash
sudo certbot --nginx -d ваш-домен.ru -d www.ваш-домен.ru
```

### 3. Обновление настроек Django
```bash
nano modelix_site/settings_production.py
```

**Раскомментировать:**
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## 🚀 Запуск проекта

### 1. Создание systemd сервиса
```bash
sudo nano /etc/systemd/system/modelix.service
```

```ini
[Unit]
Description=Modelix Django App
After=network.target

[Service]
User=modelix
Group=modelix
WorkingDirectory=/home/modelix/modelix-site
Environment="PATH=/home/modelix/modelix-site/venv/bin"
ExecStart=/home/modelix/modelix-site/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 modelix_site.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

### 2. Запуск сервиса
```bash
sudo systemctl daemon-reload
sudo systemctl enable modelix
sudo systemctl start modelix
sudo systemctl status modelix
```

## ✅ Проверка работы

### 1. Проверка сервисов
```bash
sudo systemctl status modelix
sudo systemctl status nginx
sudo systemctl status postgresql
```

### 2. Проверка логов
```bash
sudo journalctl -u modelix -f
sudo tail -f /var/log/nginx/error.log
```

### 3. Тестирование сайта
- Откройте ваш домен в браузере
- Проверьте HTTPS редирект
- Проверьте все страницы и функции

## 🔧 Полезные команды

### Перезапуск сервисов
```bash
sudo systemctl restart modelix
sudo systemctl restart nginx
```

### Обновление проекта
```bash
cd /home/modelix/modelix-site
git pull
source venv/bin/activate
pip install -r requirements_production.txt
python manage.py migrate --settings=modelix_site.settings_production
python manage.py collectstatic --settings=modelix_site.settings_production --noinput
sudo systemctl restart modelix
```

### Проверка SSL
```bash
sudo certbot certificates
sudo certbot renew --dry-run
```

## 📊 Мониторинг

### Логи Django
```bash
sudo journalctl -u modelix -f
```

### Логи Nginx
```bash
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Использование ресурсов
```bash
htop
df -h
free -h
```

## 🆘 Решение проблем

### Если сайт не загружается
1. Проверьте статус сервисов: `sudo systemctl status modelix nginx`
2. Проверьте логи: `sudo journalctl -u modelix -f`
3. Проверьте конфигурацию Nginx: `sudo nginx -t`

### Если SSL не работает
1. Проверьте сертификаты: `sudo certbot certificates`
2. Проверьте конфигурацию Nginx
3. Убедитесь, что порты 80 и 443 открыты

### Если база данных не подключается
1. Проверьте статус PostgreSQL: `sudo systemctl status postgresql`
2. Проверьте настройки в `settings_production.py`
3. Проверьте права пользователя базы данных

## 🎯 Финальная проверка

После деплоя убедитесь, что:
- ✅ Сайт открывается по HTTPS
- ✅ Все страницы загружаются
- ✅ Формы работают
- ✅ Админка доступна
- ✅ Статические файлы загружаются
- ✅ Медиафайлы отображаются
- ✅ SSL сертификат действителен

**Проект готов к работе! 🚀**


