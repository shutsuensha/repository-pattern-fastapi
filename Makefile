.PHONY: help install sync lock run test coverage lint format typecheck \
        security-bandit security-safety security-audit security-check \
        docs docs-build docs-publish

help: ## Показать список доступных команд
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

install: ## Установить все зависимости (prod + dev)
	uv pip install -r requirements.txt -r requirements-dev.txt

sync: ## Синхронизировать окружение по lock-файлу (ci/cd)
	uv pip sync requirements.lock.txt

lock: ## Сгенерировать requirements.lock.txt
	uv pip freeze > requirements.lock.txt

run: ## Запустить FastAPI dev-сервер
	uv run uvicorn app.main:app --reload

test: ## Запустить все unit-тесты
	pytest

coverage: ## Тесты с покрытием (pytest-cov)
	pytest --cov=app --cov-report=term-missing

lint: ## Линтинг через Ruff
	ruff check app/ tests/

format: ## Форматирование кода Ruff Format
	ruff format app/ tests/

typecheck: ## Проверка типов через Mypy
	mypy app/

security-bandit: ## Поиск уязвимостей в коде (Bandit)
	bandit -r app -ll -q

security-safety: ## Проверка зависимостей по CVE (Safety)
	safety check --full-report

security-audit: ## Альтернатива Safety — pip-audit
	pip-audit

security-check: security-bandit security-safety security-audit ## Запустить все проверки безопасности

docs: ## Запустить локальный сервер документации MkDocs
	mkdocs serve

docs-build: ## Собрать HTML-документацию в папку ./site
	mkdocs build

docs-publish: ## Залить документацию на GitHub Pages
	mkdocs gh-deploy
