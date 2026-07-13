# 🎯 no talent | Valorant Team Manager & AI Coach

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A resilient, micro-service oriented platform engineered for the **no talent** competitive Valorant roster. This system automates roster management, ingests real-time match data via the Riot API, and leverages LLM-driven inference to provide actionable tactical VOD analysis.



---

## ✨ Core Features

* **Esports Roster Engine:** Centralized management for players, team roles, and historical match logs.
* **Resilient Data Ingestion:** Asynchronous interaction with the HenrikDev API (Unofficial Riot API) with fault-tolerant parsing for non-standard match types (Deathmatch, Custom Lobbies).
* **AI Tactical Coach:** Real-time analysis of player stats via Groq Llama 3.1, providing objective feedback on performance patterns.
* **CI/CD Pipeline:** Fully automated testing and linting via GitHub Actions, ensuring code quality before merge.
* **Containerized Orchestration:** Production-ready multi-container architecture using `docker-compose`.

## 🏗️ Architecture & Project Structure

The project follows a **Service-Oriented Architecture (SOA)**, decoupling business logic from external API integration and UI concerns.

```text
├── app/
│   ├── api/            # FastAPI routers (players, teams, tournaments, matches)
│   ├── core/           # Database engine, SQLAlchemy session, and app settings
│   ├── crud/           # Data access layer (CRUD operations)
│   ├── models/         # Database models (SQLAlchemy)
│   ├── schemas/        # Data validation models (Pydantic)
│   └── services/       # External service adapters (Riot/Groq)
├── frontend/           # Streamlit-based interactive dashboard
├── alembic/            # Automated database migration versions
├── tests/              # Asynchronous test suite (pytest + sqlite)
└── docker-compose.yml  # Infrastructure as code
```

## 🛠️ Tech Stack

* **Backend:** FastAPI, Uvicorn, SQLAlchemy (async), Alembic
* **Frontend:** Streamlit, Pandas
* **Database:** PostgreSQL
* **AI/ML:** Groq API (Llama 3.1)
* **DevOps:** Docker, Docker Compose, GitHub Actions

## 🚀 Quick Start (Docker)

Ensure Docker Desktop is running, then execute the following:

1.**Configure Environment:**
Copy the template and provide your API keys:
```Bash
cp .env.example .env
# Edit .env with your RIOT_API_KEY, GROQ_API_KEY, and DB credentials
```

2.**Initialize & Launch:**
```Bash
docker compose up --build -d
```

3.**Access Services:** 
* **Dashboard:** `http://localhost:8501`
* **API Docs (Swagger):** `http://localhost:8000/docs`

## 🧪 Testing Strategy

Quality is enforced through an asynchronous, isolated testing environment.

* **Isolated Databases:** Tests utilize in-memory ```aiosqlite```, ensuring the production PostgreSQL database remains pristine.

* **Mocked Infrastructure:** External API dependencies (HenrikDev/Groq) are mocked using ```unittest.mock``` for fast, deterministic, and cost-free test runs.

**Run the suite locally within the container:**
```Bash
docker compose exec web pytest -v
```
Developed for performance, scalability, and esports excellence.

*Developed by [raccoohh](https://github.com/Raccoohh)*