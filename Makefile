# Makefile for Django project using pyproject.toml

# Переменные
PYTHON = python
PIP = pip
DJANGO_MANAGE = $(PYTHON) manage.py

# Определение команд по умолчанию
.DEFAULT_GOAL := help

# Список команд и их описания
help:
	@echo "Используйте следующие команды:"
	@echo "  make runserver       - Запустить сервер разработки"
	@echo "  make migrate         - Применить миграции"
	@echo "  make createsuperuser - Создать суперпользователя"
	@echo "  make test            - Запустить тесты"
	@echo "  make install         - Установить зависимости"
	@echo "  make clean           - Очистить миграции и базу данных"

# Команды
runserver:
	$(DJANGO_MANAGE) runserver

migrate:
	$(DJANGO_MANAGE) migrate

createsuperuser:
	$(DJANGO_MANAGE) createsuperuser

test:
	$(DJANGO_MANAGE) test

install:
	$(PIP) install --upgrade pip
	$(PIP) install poetry
	poetry install

clean:
	rm -rf db.sqlite3
	find . -name "migrations" -type d -exec rm -r {} +

.PHONY: help runserver migrate createsuperuser test install clean
