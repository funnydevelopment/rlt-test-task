FROM ubuntu:latest
LABEL authors="funnydevelopment"

FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY . .

# Устанавливаем MongoDB и восстанавливаем базу данных
RUN apt-get update && apt-get install -y mongodb-tools
WORKDIR /app
RUN mongorestore --db mydatabase /app/sampleDB

# Устанавливаем MongoDB-клиент с паролем
RUN apt-get install -y mongodb-tools
RUN echo "mongodb://username:password@mongodb:27017/mydatabase" > /app/mongodb_uri.txt

# Команда для запуска вашего приложения
CMD ["python", "bot.py"]
