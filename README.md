<p align="center">
  <img src="docs/banner.png" width="900">
</p>

<h1 align="center">🎮 Valorant Team Manager API</h1>

<p align="center">
Backend for managing Valorant esports teams and tournaments.
</p>

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 📑 Contents

- Features
- Tech Stack
- Installation
- API
- Project Structure
- Screenshots
- License

## 📂 Project Structure

```text
project/
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── main.py
├── migrations/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## ⚙️ Environment Variables

Create `.env`

```env
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/esports_db
SECRET_KEY=your_secret_key
REDIS_URL=redis://redis:6379/0
```

## 🚀 Example Request

```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "admin@example.com",
  "password": "password123"
}
```

## 📷 API Documentation

<img src="docs/swagger.png">

## 📄 License

MIT License

## 👤 Author

**Raccoon**

GitHub: https://github.com/твій-нік