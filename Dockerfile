FROM ubuntu:latest
LABEL authors="funnydevelopment"

FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y mongodb-tools mongodb-clients

# Копируем файлы из текущего каталога в контейнер
WORKDIR /app
COPY . .

# Устанавливаем пакеты из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем MongoDB и восстанавливаем базу данных
RUN apt-get install -y mongodb
RUN mkdir /data/db  # Создаем каталог для хранения данных MongoDB
RUN mongorestore --db mydatabase /app/sampleDB

# Задаем переменные окружения для MongoDB
ENV MONGO_INITDB_ROOT_USERNAME=username
ENV MONGO_INITDB_ROOT_PASSWORD=password
ENV MONGO_INITDB_DATABASE=mydatabase

# Команда для запуска вашего приложения
CMD ["python", "bot.py"]