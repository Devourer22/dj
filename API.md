# API Документация

## 📋 Содержание

- [Обзор API](#обзор-api)
- [Аутентификация](#аутентификация)
- [Пользователи](#пользователи)
- [Курсы](#курсы)
- [Уроки](#уроки)
- [Коды ответов](#коды-ответов)
- [Примеры запросов](#примеры-запросов)
- [Обработка ошибок](#обработка-ошибок)

## 🌐 Обзор API

Образовательная платформа предоставляет RESTful API для взаимодействия с системой. API построен на основе Django REST Framework и поддерживает стандартные HTTP методы.

### Базовый URL
```
http://yourdomain.com/api/
```

### Формат данных
- **Входные данные:** JSON
- **Выходные данные:** JSON
- **Кодировка:** UTF-8

### Версионирование
API использует версионирование через URL:
```
http://yourdomain.com/api/v1/
```

## 🔐 Аутентификация

### Регистрация пользователя
```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword123",
    "first_name": "Иван",
    "last_name": "Иванов"
}
```

**Ответ:**
```json
{
    "id": 1,
    "username": "newuser",
    "email": "user@example.com",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_joined": "2024-01-01T12:00:00Z"
}
```

### Авторизация
```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "newuser",
    "password": "securepassword123"
}
```

**Ответ:**
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
        "id": 1,
        "username": "newuser",
        "email": "user@example.com",
        "first_name": "Иван",
        "last_name": "Иванов"
    }
}
```

### Выход из системы
```http
POST /api/auth/logout/
Authorization: Token your-token-here
```

**Ответ:**
```json
{
    "message": "Successfully logged out"
}
```

## 👥 Пользователи

### Получение профиля текущего пользователя
```http
GET /api/users/profile/
Authorization: Token your-token-here
```

**Ответ:**
```json
{
    "id": 1,
    "username": "newuser",
    "email": "user@example.com",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_joined": "2024-01-01T12:00:00Z",
    "is_staff": false,
    "courses_created": 2,
    "courses_enrolled": 5
}
```

### Обновление профиля
```http
PUT /api/users/profile/
Authorization: Token your-token-here
Content-Type: application/json

{
    "first_name": "Иван",
    "last_name": "Петров",
    "email": "newemail@example.com"
}
```

### Получение списка пользователей (только для админов)
```http
GET /api/users/
Authorization: Token admin-token-here
```

**Ответ:**
```json
{
    "count": 25,
    "next": "http://yourdomain.com/api/users/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "first_name": "Иван",
            "last_name": "Иванов",
            "date_joined": "2024-01-01T12:00:00Z",
            "is_staff": false
        }
    ]
}
```

## 📚 Курсы

### Получение списка курсов
```http
GET /api/courses/
```

**Параметры запроса:**
- `page` - номер страницы (по умолчанию 1)
- `search` - поиск по названию курса
- `author` - фильтр по автору
- `is_published` - фильтр по статусу публикации

**Ответ:**
```json
{
    "count": 50,
    "next": "http://yourdomain.com/api/courses/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Введение в Python",
            "description": "Базовый курс по программированию на Python",
            "author": {
                "id": 1,
                "username": "teacher1",
                "first_name": "Алексей",
                "last_name": "Учитель"
            },
            "created_at": "2024-01-01T12:00:00Z",
            "updated_at": "2024-01-15T10:30:00Z",
            "is_published": true,
            "lessons_count": 10,
            "enrolled_students": 25
        }
    ]
}
```

### Получение детальной информации о курсе
```http
GET /api/courses/1/
```

**Ответ:**
```json
{
    "id": 1,
    "title": "Введение в Python",
    "description": "Базовый курс по программированию на Python",
    "content": "Подробное описание курса...",
    "author": {
        "id": 1,
        "username": "teacher1",
        "first_name": "Алексей",
        "last_name": "Учитель"
    },
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-15T10:30:00Z",
    "is_published": true,
    "lessons": [
        {
            "id": 1,
            "title": "Переменные и типы данных",
            "order": 1,
            "created_at": "2024-01-01T12:00:00Z"
        }
    ],
    "enrolled_students": 25
}
```

### Создание нового курса
```http
POST /api/courses/
Authorization: Token your-token-here
Content-Type: application/json

{
    "title": "Новый курс",
    "description": "Описание нового курса",
    "content": "Подробное содержание курса",
    "is_published": false
}
```

### Обновление курса
```http
PUT /api/courses/1/
Authorization: Token your-token-here
Content-Type: application/json

{
    "title": "Обновленное название курса",
    "description": "Обновленное описание",
    "content": "Обновленное содержание",
    "is_published": true
}
```

### Удаление курса
```http
DELETE /api/courses/1/
Authorization: Token your-token-here
```

## 📖 Уроки

### Получение списка уроков курса
```http
GET /api/courses/1/lessons/
```

**Ответ:**
```json
[
    {
        "id": 1,
        "title": "Переменные и типы данных",
        "content": "Содержание урока...",
        "order": 1,
        "course": 1,
        "created_at": "2024-01-01T12:00:00Z",
        "updated_at": "2024-01-01T12:00:00Z"
    }
]
```

### Получение детальной информации об уроке
```http
GET /api/lessons/1/
```

**Ответ:**
```json
{
    "id": 1,
    "title": "Переменные и типы данных",
    "content": "Подробное содержание урока...",
    "order": 1,
    "course": {
        "id": 1,
        "title": "Введение в Python"
    },
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}
```

### Создание нового урока
```http
POST /api/courses/1/lessons/
Authorization: Token your-token-here
Content-Type: application/json

{
    "title": "Новый урок",
    "content": "Содержание нового урока",
    "order": 2
}
```

### Обновление урока
```http
PUT /api/lessons/1/
Authorization: Token your-token-here
Content-Type: application/json

{
    "title": "Обновленное название урока",
    "content": "Обновленное содержание урока",
    "order": 1
}
```

### Удаление урока
```http
DELETE /api/lessons/1/
Authorization: Token your-token-here
```

## 📊 Коды ответов

| Код | Описание |
|-----|----------|
| 200 | OK - запрос выполнен успешно |
| 201 | Created - ресурс создан успешно |
| 400 | Bad Request - неверный запрос |
| 401 | Unauthorized - требуется авторизация |
| 403 | Forbidden - недостаточно прав |
| 404 | Not Found - ресурс не найден |
| 405 | Method Not Allowed - метод не поддерживается |
| 500 | Internal Server Error - внутренняя ошибка сервера |

## 💡 Примеры запросов

### JavaScript (Fetch API)
```javascript
// Авторизация
const login = async (username, password) => {
    const response = await fetch('/api/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password })
    });
    
    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.token);
        return data;
    }
    throw new Error('Login failed');
};

// Получение курсов
const getCourses = async () => {
    const token = localStorage.getItem('token');
    const response = await fetch('/api/courses/', {
        headers: {
            'Authorization': `Token ${token}`
        }
    });
    
    return response.json();
};

// Создание курса
const createCourse = async (courseData) => {
    const token = localStorage.getItem('token');
    const response = await fetch('/api/courses/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
        },
        body: JSON.stringify(courseData)
    });
    
    return response.json();
};
```

### Python (requests)
```python
import requests

# Авторизация
def login(username, password):
    response = requests.post('http://yourdomain.com/api/auth/login/', 
                           json={'username': username, 'password': password})
    if response.status_code == 200:
        data = response.json()
        return data['token']
    return None

# Получение курсов
def get_courses(token):
    headers = {'Authorization': f'Token {token}'}
    response = requests.get('http://yourdomain.com/api/courses/', headers=headers)
    return response.json()

# Создание курса
def create_course(token, course_data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {token}'
    }
    response = requests.post('http://yourdomain.com/api/courses/', 
                           json=course_data, headers=headers)
    return response.json()
```

### cURL
```bash
# Авторизация
curl -X POST http://yourdomain.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "password"}'

# Получение курсов
curl -X GET http://yourdomain.com/api/courses/ \
  -H "Authorization: Token your-token-here"

# Создание курса
curl -X POST http://yourdomain.com/api/courses/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your-token-here" \
  -d '{"title": "Новый курс", "description": "Описание"}'
```

## ⚠️ Обработка ошибок

### Формат ошибок
```json
{
    "error": "error_code",
    "message": "Человеко-читаемое описание ошибки",
    "details": {
        "field_name": ["Список ошибок для поля"]
    }
}
```

### Примеры ошибок

#### Ошибка валидации
```json
{
    "error": "validation_error",
    "message": "Данные не прошли валидацию",
    "details": {
        "title": ["Это поле обязательно для заполнения"],
        "email": ["Введите корректный email адрес"]
    }
}
```

#### Ошибка авторизации
```json
{
    "error": "authentication_failed",
    "message": "Неверные учетные данные"
}
```

#### Ошибка доступа
```json
{
    "error": "permission_denied",
    "message": "У вас нет прав для выполнения этого действия"
}
```

#### Ошибка "не найдено"
```json
{
    "error": "not_found",
    "message": "Запрашиваемый ресурс не найден"
}
```

## 🔧 Настройка API

### Пагинация
API поддерживает пагинацию для списков ресурсов:

```json
{
    "count": 100,
    "next": "http://yourdomain.com/api/courses/?page=3",
    "previous": "http://yourdomain.com/api/courses/?page=1",
    "results": [...]
}
```

### Фильтрация
Поддерживаются следующие параметры фильтрации:
- `search` - поиск по тексту
- `ordering` - сортировка результатов
- `page_size` - количество элементов на странице

### Rate Limiting
API имеет ограничения на количество запросов:
- **Анонимные пользователи:** 100 запросов в час
- **Авторизованные пользователи:** 1000 запросов в час
- **Администраторы:** без ограничений

## 📞 Поддержка

При возникновении проблем с API:
1. Проверьте правильность URL и параметров
2. Убедитесь в корректности токена авторизации
3. Проверьте формат отправляемых данных
4. Обратитесь к кодам ошибок для диагностики
5. Создайте issue в репозитории проекта