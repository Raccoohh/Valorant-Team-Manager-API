# Використовуємо офіційний легкий образ Python 3.10
FROM python:3.10-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Забороняємо Python створювати .pyc файли та буферизувати вивід (корисно для логів)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копіюємо файл із залежностями та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь інший код проєкту
COPY . .

# Команда для запуску нашого сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]