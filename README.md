# Тестове завдання Checkbox
Для запуску проекту потрібно мати встановлений Docker та Docker Compose.

Проект побудований на базі PostgreSQL версії 16 та Python 3.10. Основні бібліотеки Python, використані для реалізації цього завдання: FastAPI, Tortoise-ORM, Jinja2, Aerich.

**Для запуску проекту введіть команду:**

```bash
docker-compose up --build
```

Відкрийте ``` 0.0.0.0:8000 ```

# Примітки:

- Не було написано тести через брак часу, пов'язаний із основною роботою.
- Деякий функціонал реалізовано мінімально, особливо механіка фільтрів у списку.
- Помилка у використанні бібліотеки - в описі вакансії вказано використання SQLAlchemy, але в проекті використано Tortoise-ORM. Приношу вибачення за це непорозуміння.
