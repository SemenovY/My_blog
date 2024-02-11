#  Проект «Мой блог»
### Работа с постами:
 - Получение, Создание, Обновление, Удаление публикаций.
### Аутентификация:
 - Получить, Обновить, Проверить JWT Токен.
 -  Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SemenovY/My_blog
cd My_blog
```
Cоздать и активировать виртуальное окружение:
```
poetry init
poetry shell
```
Установить зависимости:
```
poetry install
```
Выполнить миграции:
```
python3 manage.py migrate
```
При необходимости создать суперпользователя:
```
python manage.py createsuperuser
```
Запустить проект:
```
python3 manage.py runserver
```
### Использованные технологии:
- python = "^3.11"
- django = "^5.0.2"
- djangorestframework = "^3.14.0"
- pre-commit = "^3.6.0"
- python-dotenv = "^1.0.1"
- drf-spectacular = "^0.27.1"
- drf-spectacular-sidecar = "^2024.2.1"
- djoser = "^2.2.2"
- djangorestframework-simplejwt = "^5.3.1"
### Автор:
Семёнов Юрий
GitHub: https://github.com/SemenovY
e-mail: info@juriys.ru
