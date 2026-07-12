FROM python:3.10-slim

WORKDIR /app

# Встановлюємо залежності для Streamlit
RUN pip install --no-cache-dir streamlit requests pandas

# Копіюємо код фронтенду в контейнер
COPY app.py .

EXPOSE 8501

# Запуск дашборду (зверни увагу, що тепер ми запускаємо app.py)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]