#МОСКОВСКИЙ ГОСУДАРСТВЕННЫЙ ТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ им. Н.Э. Баумана

#Факультет “Информатика и системы управления” Кафедра “Системы обработки информации и управления”

#Дисциплина “Парадигмы и конструкции языков программирования”

Отчет по ДЗ

Выполнил: Студент группы ИУ5-33Б Гудис А.В. Преподаватель: Нардид А.Н.



# 🤖 GPT Telegram Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

</div>

## 📖 Описание

Умный Telegram бот с интеграцией различных AI(генерация фото, текстов и голоса, обработка фотографий и многое другое) для интеллектуального общения и решения различных задач. Бот использует асинхронную архитектуру для высокой производительности и поддерживает контекст диалога.

## 🚀 Возможности

- ✅ **Интеграция с различными AI** - общение с современными AI моделями
- ✅ **Контекст диалога** - бот помнит историю сообщений
- ✅ **Асинхронная архитектура** - высокая производительность
- ✅ **Webhook поддержка** - быстрый отклик на сообщения
- ✅ **Кэширование в Redis** - оптимизация запросов
- ✅ **Контейнеризация** - легкий деплой через Docker
- ✅ **Логирование** - детальный мониторинг работы

## 🛠 Технологии

- **Bot Framework**: Aiogram 3.x (асинхронный)
- **AI**: differtn AI APIs
- **Cache**: Redis
- **DevOps**: Docker, Docker Compose
- **Async**: asyncio, aiohttp

## 📦 Быстрый старт

### Предварительные требования
- Docker и Docker Compose
- Telegram Bot Token от [@BotFather](https://t.me/BotFather)

### Запуск проекта

```bash
# Клонирование репозитория
git clone https://github.com/GudAlex61/GPT-telegabot

# Запуск бота
docker-compose up --build
```


## 👨‍💻 Разработка

### Установка для разработки

```bash
# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Установка зависимостей
pip install -r requirements.txt

# Запуск бота
python -m app
```

## 📊 Мониторинг

- Логирование всех запросов и ошибок
- Метрики производительности
- Статистика использования
