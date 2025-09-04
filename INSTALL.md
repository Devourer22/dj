# Инструкция по установке

## 📋 Содержание

- [Системные требования](#системные-требования)
- [Установка зависимостей](#установка-зависимостей)
- [Настройка проекта](#настройка-проекта)
- [Настройка базы данных](#настройка-базы-данных)
- [Запуск проекта](#запуск-проекта)
- [Проверка установки](#проверка-установки)
- [Устранение неполадок](#устранение-неполадок)

## 💻 Системные требования

### Минимальные требования
- **Операционная система:** Windows 10, macOS 10.14, Ubuntu 18.04 LTS
- **Python:** версия 3.8 или выше
- **ОЗУ:** минимум 4 ГБ
- **Свободное место:** минимум 1 ГБ

### Рекомендуемые требования
- **Операционная система:** Windows 11, macOS 12, Ubuntu 20.04 LTS
- **Python:** версия 3.9 или выше
- **ОЗУ:** 8 ГБ или больше
- **Свободное место:** 2 ГБ или больше

## 🔧 Установка зависимостей

### 1. Установка Python

#### Windows
1. Скачайте Python с официального сайта: https://www.python.org/downloads/
2. Запустите установщик
3. **Важно:** Отметьте галочку "Add Python to PATH"
4. Выберите "Install Now"

#### macOS
```bash
# Используя Homebrew
brew install python@3.9

# Или скачайте с официального сайта
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.9 python3.9-venv python3.9-pip
```

### 2. Проверка установки Python
```bash
python --version
# или
python3 --version
```

### 3. Установка Git
```bash
# Windows: скачайте с https://git-scm.com/
# macOS
brew install git

# Linux
sudo apt install git
```

## 🚀 Настройка проекта

### 1. Клонирование репозитория
```bash
git clone https://github.com/Devourer22/dj.git
cd dj
```

### 2. Создание виртуального окружения

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Обновление pip
```bash
python -m pip install --upgrade pip
```

### 4. Установка зависимостей
```bash
pip install -r requirements.txt
```

## 🗄️ Настройка базы данных

### Для разработки (SQLite)
SQLite настраивается автоматически и не требует дополнительной конфигурации.

### Для продакшена (PostgreSQL)

#### 1. Установка PostgreSQL
```bash
# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib

# macOS
brew install postgresql

# Windows: скачайте с https://www.postgresql.org/download/windows/
```

#### 2. Создание базы данных
```bash
sudo -u postgres psql
CREATE DATABASE edu_platform;
CREATE USER edu_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE edu_platform TO edu_user;
\q
```

#### 3. Настройка Django
Создайте файл `.env` в корне проекта:
```env
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://edu_user:your_password@localhost/edu_platform
```

## ▶️ Запуск проекта

### 1. Переход в папку Django проекта
```bash
cd dj/yusha144
```

### 2. Применение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Создание суперпользователя
```bash
python manage.py createsuperuser
```
Введите данные для администратора:
- Username: admin
- Email: admin@example.com
- Password: [создайте надежный пароль]

### 4. Сбор статических файлов
```bash
python manage.py collectstatic
```

### 5. Запуск сервера разработки
```bash
python manage.py runserver
```

### 6. Открытие в браузере
Перейдите по адресу: http://127.0.0.1:8000/

## ✅ Проверка установки

### 1. Проверка доступности сайта
- Откройте http://127.0.0.1:8000/
- Должна загрузиться главная страница

### 2. Проверка административной панели
- Перейдите на http://127.0.0.1:8000/admin/
- Войдите с данными суперпользователя
- Должна открыться административная панель

### 3. Проверка API
```bash
# Проверка доступности API
curl http://127.0.0.1:8000/api/
```

## 🔧 Устранение неполадок

### Ошибка "Python not found"
```bash
# Проверьте установку Python
python --version

# Если не работает, попробуйте
python3 --version

# Добавьте Python в PATH (Windows)
```

### Ошибка "pip not found"
```bash
# Установите pip
python -m ensurepip --upgrade

# Или скачайте get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Ошибка "Django not found"
```bash
# Убедитесь, что виртуальное окружение активировано
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Переустановите зависимости
pip install -r requirements.txt
```

### Ошибка "Database connection failed"
```bash
# Проверьте настройки базы данных в settings.py
# Убедитесь, что PostgreSQL запущен
sudo systemctl start postgresql  # Linux
brew services start postgresql   # macOS
```

### Ошибка "Static files not found"
```bash
# Соберите статические файлы
python manage.py collectstatic

# Проверьте настройки STATIC_URL в settings.py
```

### Ошибка "Permission denied"
```bash
# Linux/macOS: измените права доступа
chmod +x manage.py

# Windows: запустите командную строку от имени администратора
```

## 📞 Поддержка

Если у вас возникли проблемы с установкой:

1. Проверьте раздел [Устранение неполадок](#устранение-неполадок)
2. Убедитесь, что все системные требования выполнены
3. Проверьте версии Python и pip
4. Создайте issue в репозитории проекта

## 📚 Дополнительные ресурсы

- [Документация Django](https://docs.djangoproject.com/)
- [Руководство по Python](https://docs.python.org/3/)
- [Документация PostgreSQL](https://www.postgresql.org/docs/)
- [Руководство по Git](https://git-scm.com/doc)