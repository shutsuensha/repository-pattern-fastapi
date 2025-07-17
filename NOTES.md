## Start 24.06.2025 ~ 1 month maximum

## TO DO


дальше https://chatgpt.com/c/6859d413-8434-800b-94f4-252b99e4f44f
паттерны проектирования
микросервисы + event-driven + масштабирование

artemshumeiko + весь курс пересмотреть на доп технологии / приемы
https://artemshumeiko.zenclass.ru/student/courses/937c3a35-998d-4420-bd3d-9f64db23be23/lessons/18c89b4f-19e3-481f-be49-b9eda822a430
https://github.com/artemonsh/backend-course/

2. tests
(unnit / integrational)
pytest - pytest-xdist
factory_boy или faker
hypothesis
locust
pyroject.toml
make test
make coverage

3. lint / format / static
pyroject.toml
ruff
ruff.lint
ruff.format
mypy
make lint
make format
make typecheck

4. security
make security-bandit
make security-safety
make security-audit
make security-check

5. pre-commit
.pre-commit-config.yaml

6. github ci/cd
req - lock
make lock
make sync (ci/cd)

6.1 - gitflow + pr

7. docs
markdown
mkdocs.yml
make docs
make docs-build
gh page
make docs-publish

8. Readme example + проверить установку и запуск + contribute guyide

9. agile/scrum, Kanban / Scrum - Jira/Confluence

10. hotfix + release branches

11. Next  

## Steps
pyenv install 3.12.3
pyenv local 3.12.3

pip install uv
uv venv

pre-commit install
make commands



## Git Flow Feature / BugFix

git checkout develop
git pull origin develop
git checkout -b feature/repository-pattern

    git add app/models/user.py
    git commit -m "feat: добавлена модель User"

    git add app/schemas/user.py
    git commit -m "feat: добавлены схемы UserCreate и UserResponse"

    git add app/services/user_service.py
    git commit -m "feat: логика регистрации с валидацией email"

    git add tests/test_user_register.py
    git commit -m "test: регистрация с валидными и невалидными данными"

    git add app/api/routes/user.py
    git commit -m "feat: реализован роут POST /register"

    git add README.md
    git commit -m "docs: добавлен пример запроса /register"

    git add .
    git commit -m "feat: реализован паттерн репозиториев"

git push origin feature/repository-pattern

- Создаёшь Pull Request из feature/repository-pattern в develop.
- Проводишь код-ревью, правки.
- После одобрения — мержишь PR через веб-интерфейс.

git checkout develop
git pull origin develop
git branch -d feature/repository-pattern


## Git naming
feat:	новая фича
fix:	багфикс
chore:	инфраструктура: Makefile, CI, pre-commit
docs:	README, swagger
test:	тесты
style:	black, ruff, без логики
perf:	улучшение производительности


3. Подготовка релиза
Создаёшь ветку release/vX.Y.Z от develop
В этой ветке исправляешь баги, обновляешь документацию, собираешь changelog
Тестируешь стабильно
Мержишь в main и тегируешь релиз (например, git tag vX.Y.Z)
Мержишь обратно в develop (если были исправления)

4. Срочный хотфикс
Создаёшь ветку hotfix/<описание> от main
Исправляешь критический баг на продакшене
Мержишь в main и создаёшь тег
Мержишь обратно в develop, чтобы исправление не потерялось

Дополнительные рекомендации
Мерж с --no-ff, чтобы сохранить историю веток
Используй semantic commits (Conventional Commits) для автоматизации changelog
Настраивай защиту веток в репозитории (например, запрет пуша напрямую в main и develop, обязательный код-ревью)
Внедри CI/CD для тестирования, линтинга и деплоя



## Next
fastapi-users + OAuth2 (Authlib) +  OAuth 2.0 / Google / Github Login
fastapi-pagination
sqladmin / tortoise-orm – для административных панелей.

Хочешь — могу прислать шаблон идеального FastAPI-проекта, который можно использовать как скелет под любой проект.

DynamoDB, ElasticSearch, ClickHouse

Kafka
FastStream, Taskiq
Aioamqp

artemshumeiko + весь курс пересмотреть на доп технологии / приемы
https://artemshumeiko.zenclass.ru/student/courses/937c3a35-998d-4420-bd3d-9f64db23be23/lessons/18c89b4f-19e3-481f-be49-b9eda822a430
https://github.com/artemonsh/backend-course/


https://github.com/zhanymkanov/fastapi-best-practices
https://github.com/beagreatengineer/how-to-develop-perfect-crud
https://github.com/mjhea0/awesome-fastapi
+ chatgpt


Code Review Practices — как давать/принимать полезный фидбэк
Team Collaboration Tools — Git workflow, GitHub Projects, issue-tracking
Tech Leadership Skills — как планировать спринты, вести документацию, принимать архитектурные решения


## Directions

1. ai/ml, ai agents, ai editors, prompt engineering

2. fastapi, aiogram, parsing, drf, python

3. react, next, js, ts

4. go backend

5. devops