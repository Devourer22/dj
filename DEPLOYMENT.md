# Руководство по развертыванию

## 📋 Содержание

- [Подготовка к развертыванию](#подготовка-к-развертыванию)
- [Настройка сервера](#настройка-сервера)
- [Настройка базы данных](#настройка-базы-данных)
- [Настройка веб-сервера](#настройка-веб-сервера)
- [Настройка SSL](#настройка-ssl)
- [Мониторинг и логирование](#мониторинг-и-логирование)
- [Автоматическое развертывание](#автоматическое-развертывание)
- [Резервное копирование](#резервное-копирование)

## 🚀 Подготовка к развертыванию

### Требования к серверу
- **ОС:** Ubuntu 20.04 LTS или выше
- **ОЗУ:** минимум 2 ГБ, рекомендуется 4 ГБ
- **Процессор:** 2 ядра, рекомендуется 4 ядра
- **Диск:** минимум 20 ГБ свободного места
- **Сеть:** статический IP-адрес

### Подготовка проекта
1. **Настройка переменных окружения:**
```bash
# Создайте файл .env в корне проекта
DEBUG=False
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

2. **Настройка статических файлов:**
```python
# В settings.py
STATIC_ROOT = '/var/www/edu_platform/static/'
MEDIA_ROOT = '/var/www/edu_platform/media/'
```

## 🖥️ Настройка сервера

### 1. Обновление системы
```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Установка Python и зависимостей
```bash
sudo apt install python3.9 python3.9-venv python3.9-dev python3-pip
sudo apt install build-essential libpq-dev
```

### 3. Создание пользователя для приложения
```bash
sudo adduser --system --group --shell /bin/bash edu_platform
sudo mkdir -p /var/www/edu_platform
sudo chown edu_platform:edu_platform /var/www/edu_platform
```

### 4. Клонирование проекта
```bash
sudo -u edu_platform git clone https://github.com/Devourer22/dj.git /var/www/edu_platform
cd /var/www/edu_platform
```

### 5. Настройка виртуального окружения
```bash
sudo -u edu_platform python3.9 -m venv venv
sudo -u edu_platform venv/bin/pip install --upgrade pip
sudo -u edu_platform venv/bin/pip install -r requirements.txt
```

## 🗄️ Настройка базы данных

### 1. Установка PostgreSQL
```bash
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2. Создание базы данных
```bash
sudo -u postgres psql
CREATE DATABASE edu_platform;
CREATE USER edu_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE edu_platform TO edu_user;
ALTER USER edu_user CREATEDB;
\q
```

### 3. Настройка Django
```bash
cd /var/www/edu_platform/dj/yusha144
sudo -u edu_platform venv/bin/python manage.py makemigrations
sudo -u edu_platform venv/bin/python manage.py migrate
sudo -u edu_platform venv/bin/python manage.py createsuperuser
sudo -u edu_platform venv/bin/python manage.py collectstatic --noinput
```

## 🌐 Настройка веб-сервера

### 1. Установка Nginx
```bash
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

### 2. Конфигурация Nginx
Создайте файл `/etc/nginx/sites-available/edu_platform`:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/edu_platform;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    location /media/ {
        root /var/www/edu_platform;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/edu_platform/edu_platform.sock;
    }
}
```

### 3. Активация сайта
```bash
sudo ln -s /etc/nginx/sites-available/edu_platform /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl reload nginx
```

### 4. Установка Gunicorn
```bash
sudo -u edu_platform venv/bin/pip install gunicorn
```

### 5. Создание systemd сервиса
Создайте файл `/etc/systemd/system/edu_platform.service`:
```ini
[Unit]
Description=Gunicorn instance to serve edu_platform
After=network.target

[Service]
User=edu_platform
Group=www-data
WorkingDirectory=/var/www/edu_platform/dj/yusha144
Environment="PATH=/var/www/edu_platform/venv/bin"
ExecStart=/var/www/edu_platform/venv/bin/gunicorn --workers 3 --bind unix:/var/www/edu_platform/edu_platform.sock yusha144.wsgi:application

[Install]
WantedBy=multi-user.target
```

### 6. Запуск сервиса
```bash
sudo systemctl daemon-reload
sudo systemctl start edu_platform
sudo systemctl enable edu_platform
```

## 🔒 Настройка SSL

### 1. Установка Certbot
```bash
sudo apt install certbot python3-certbot-nginx
```

### 2. Получение SSL сертификата
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 3. Автоматическое обновление
```bash
sudo crontab -e
# Добавьте строку:
0 12 * * * /usr/bin/certbot renew --quiet
```

## 📊 Мониторинг и логирование

### 1. Настройка логирования
Создайте файл `/var/www/edu_platform/logs/`:
```bash
sudo mkdir -p /var/www/edu_platform/logs
sudo chown edu_platform:edu_platform /var/www/edu_platform/logs
```

### 2. Конфигурация логирования Django
```python
# В settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/www/edu_platform/logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### 3. Мониторинг системы
```bash
# Установка htop для мониторинга
sudo apt install htop

# Мониторинг логов
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/www/edu_platform/logs/django.log
```

## 🔄 Автоматическое развертывание

### 1. Создание скрипта развертывания
Создайте файл `/var/www/edu_platform/deploy.sh`:
```bash
#!/bin/bash
cd /var/www/edu_platform
sudo -u edu_platform git pull origin master
sudo -u edu_platform venv/bin/pip install -r requirements.txt
sudo -u edu_platform venv/bin/python dj/yusha144/manage.py migrate
sudo -u edu_platform venv/bin/python dj/yusha144/manage.py collectstatic --noinput
sudo systemctl restart edu_platform
sudo systemctl reload nginx
```

### 2. Настройка прав доступа
```bash
sudo chmod +x /var/www/edu_platform/deploy.sh
```

### 3. Webhook для автоматического развертывания
Создайте файл `/var/www/edu_platform/webhook.py`:
```python
#!/usr/bin/env python3
import subprocess
import sys

def deploy():
    try:
        subprocess.run(['/var/www/edu_platform/deploy.sh'], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == '__main__':
    if deploy():
        print("Deployment successful")
        sys.exit(0)
    else:
        print("Deployment failed")
        sys.exit(1)
```

## 💾 Резервное копирование

### 1. Скрипт резервного копирования
Создайте файл `/var/www/edu_platform/backup.sh`:
```bash
#!/bin/bash
BACKUP_DIR="/var/backups/edu_platform"
DATE=$(date +%Y%m%d_%H%M%S)

# Создание директории для бэкапов
mkdir -p $BACKUP_DIR

# Бэкап базы данных
sudo -u postgres pg_dump edu_platform > $BACKUP_DIR/db_$DATE.sql

# Бэкап медиа файлов
tar -czf $BACKUP_DIR/media_$DATE.tar.gz /var/www/edu_platform/media/

# Бэкап кода
tar -czf $BACKUP_DIR/code_$DATE.tar.gz /var/www/edu_platform/ --exclude=venv --exclude=logs

# Удаление старых бэкапов (старше 30 дней)
find $BACKUP_DIR -name "*.sql" -mtime +30 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete
```

### 2. Автоматическое резервное копирование
```bash
sudo crontab -e
# Добавьте строку для ежедневного бэкапа в 2:00:
0 2 * * * /var/www/edu_platform/backup.sh
```

## 🔧 Полезные команды

### Управление сервисами
```bash
# Перезапуск приложения
sudo systemctl restart edu_platform

# Перезагрузка Nginx
sudo systemctl reload nginx

# Проверка статуса
sudo systemctl status edu_platform
sudo systemctl status nginx
```

### Просмотр логов
```bash
# Логи приложения
sudo journalctl -u edu_platform -f

# Логи Nginx
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Логи Django
sudo tail -f /var/www/edu_platform/logs/django.log
```

### Обновление приложения
```bash
# Ручное обновление
cd /var/www/edu_platform
sudo -u edu_platform git pull
sudo -u edu_platform venv/bin/pip install -r requirements.txt
sudo -u edu_platform venv/bin/python dj/yusha144/manage.py migrate
sudo -u edu_platform venv/bin/python dj/yusha144/manage.py collectstatic --noinput
sudo systemctl restart edu_platform
```

## 🚨 Устранение неполадок

### Проблемы с правами доступа
```bash
# Исправление прав доступа
sudo chown -R edu_platform:www-data /var/www/edu_platform
sudo chmod -R 755 /var/www/edu_platform
```

### Проблемы с базой данных
```bash
# Проверка подключения к БД
sudo -u postgres psql -c "SELECT version();"

# Проверка пользователя БД
sudo -u postgres psql -c "\du"
```

### Проблемы с Nginx
```bash
# Проверка конфигурации
sudo nginx -t

# Перезапуск Nginx
sudo systemctl restart nginx
```

## 📞 Поддержка

При возникновении проблем:
1. Проверьте логи приложения и веб-сервера
2. Убедитесь, что все сервисы запущены
3. Проверьте права доступа к файлам
4. Создайте issue в репозитории проекта