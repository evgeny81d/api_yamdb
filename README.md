# Веб-приложение по сбору отзывов пользователей на произведения

Цель проекта - получить опыт командной работы.


## Стек технологий
- Python 3.7
- Django 2.2.16
- Django Filter 21.1
- Django REST Framework 3.12.4
- Simple JWT 5.2.0


## Описание проекта

Веб-приложение **YaMDb** собирает отзывы пользователей на произведения. 

Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Произведению может быть присвоен жанр из списка предустановленных.
Список категорий и жанров может быть расширен администратором.

Пользователи могут оставлять к произведениям текстовые отзывы и ставить оценку от одного до десяти.

Из пользовательских оценок формируется рейтинг произведения (средняя величина всех его оценок).
На одно произведение пользователь может оставить только один отзыв.

Произведение представляет собой его название, год и описание, хранение самих произведений не предусмотрено. 


## Модели ORM
В веб-приложении используются следующие модели:
- User - кастомная модель пользователя
- Title - модель произведения
- Genre - модель жанра произведения
- Category - модель категории произведения
- Review - модель отзыва к произведению
- Comment - модель комментария к отзывам


## Пользовательские роли и права доступа
- Анонимный пользователь:
    - может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь:
    - имеет те же права что и анонимный пользователь.
    - может публиковать отзывы и ставить оценки произведениям.
    - может комментировать отзывы.
    - может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений.
    - эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор:
    - имеет те же права, что и аутентифицированный пользователь.
    - имеет право удалять и редактировать любые отзывы и комментарии.
- Администратор: 
    - полные права на управление всем контентом проекта.
    - может создавать и удалять произведения, категории и жанры.
    - может назначать роли пользователям.
- Суперпользователь:
    - имеет те же права, что и администратор.
    - может создавать, блокировать и удалять пользователей.
    - имеет неограниченные права управления проектом.


## Ресурсы API
- `http://127.0.0.1:8000/api/v1/auth/` - аутентификация и регистрация.
- `http://127.0.0.1:8000/api/v1/users/` - пользователи.
- `http://127.0.0.1:8000/api/v1/titles/` - произведения.
- `http://127.0.0.1:8000/api/v1/categories/` - категории произведений.
- `http://127.0.0.1:8000/api/v1/genres/` - жанры произведений.
- `http://127.0.0.1:8000/api/v1/reviews/` - отзывы на произведения.
- `http://127.0.0.1:8000/api/v1/comments/` - комментарии к отзывам.


## Настройка и запуск веб-приложения
```
# Клонируем репозиторий
git clone https://github.com/evgeny81d/api_yamdb.git

# Переходим в директорию с проектом 
cd api_yamdb

# Создаем виртуальное окружение Python версии 3.7
python3.7 -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt --upgrade pip

# Применяем миграции
python3 api_yamdb/manage.py migrate

# Создаем суперпользователя
python3 api_yamdb/manage.py createsuperuser

# Запускаем сервер разработки django
python3 api_yamdb/manage.py runserver
```

 - [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) - полная документация API
 - [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) - админ панель веб-приложения


## Примеры API запросов
Для создания пользователя через API, необходимо: 
- сначала отправить запрос с адресом электронной почты и именем нового пользователя. После этого на указанный
адрес электронной почты придет письмо с кодом подтверждения.
- после этого отправить запрос на получение токена указав имя пользователя и код подтверждения из письма.

В учебной версии веб-приложения, отправка письма происходит в файл, который сохраняется в
директории `api_yamdb/sent_emails/`. Это реализовано с помощью почтового
бэкэнда Django - `django.core.mail.backends.filebased.EmailBackend`.

### Создание нового пользователя
#### Запрос
```sh
curl --location --request POST 'http://127.0.0.1:8000/api/v1/auth/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "newuseremail@example.com",
    "username": "newuser"
}'
```
#### Ответ
```sh
{
    "email": "newuseremail@example.com",
    "username": "newuser"
}
```

### Получение токена
#### Запрос
```sh
curl --location --request POST 'http://127.0.0.1:8000/api/v1/auth/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "newuser",
    "confirmation_code": "newuser-confirmation-code"
}'
```
#### Ответ
```sh
{
    "token": "jwt_access_token"
}
```

### Обращение к данным своей учетной записи
#### Запрос
```sh
curl --location --request GET 'http://127.0.0.1:8000/api/v1/users/me/' \
--header 'Authorization: Bearer jwt_access_token'
```
#### Ответ
```sh
{
    "username": "newuser",
    "email": "newuseremail@example.com",
    "first_name": "",
    "last_name": "",
    "bio": "",
    "role": "user"
}
```

## Разработчики
[Евгений Дериглазов](https://github.com/evgeny81d) |
Тимлид. Кастомная модель User, регистрация и аутентификация пользователей.

[Александр Гетманов](https://github.com/SelfGenius) | Разработчик, контент администратора.

[Герман Кабачков](https://github.com/tinkofoxil) | Разработчик, контент пользователей.
