FROM ubuntu:latest
LABEL authors="funnydevelopment"

FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY . .

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y wget gnupg

# Устанавливаем ключ GPG MongoDB
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -

# Добавляем репозиторий MongoDB
RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Устанавливаем MongoDB Tools
RUN apt-get update && apt-get install -y mongodb-database-tools

# Остальной код Dockerfile оставляем без изменений
# Команда для запуска вашего приложения
CMD ["python", "bot.py"]
