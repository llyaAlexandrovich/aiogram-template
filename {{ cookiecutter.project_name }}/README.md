# Telegram Bot

Телеграм-бот на базе `aiogram` с использованием:
- **SQLAlchemy** — работа с базой данных
- **Alembic** — миграции


## 📦 Требования

- Python 3.10+
- PostgreSQL / SQLite


Создание миграций - ```alembic revision --autogenerate -m "comment"```

Применение миграций - ```alembic upgrade head```