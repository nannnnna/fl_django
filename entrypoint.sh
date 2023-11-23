#!/bin/bash

# Ожидание полного запуска базы данных
# Это полезно, если ваше приложение зависит от базы данных
echo "Waiting for database to start..."
sleep 10  # Настройте это время в соответствии с вашим окружением

# Выполнение миграций
echo "Running migrations..."
python manage.py migrate

# Загрузка данных
echo "Loading data..."
python manage.py load_data

# Запуск Django-приложения
echo "Starting Django application..."
exec "$@"
