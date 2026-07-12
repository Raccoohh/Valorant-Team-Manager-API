# Valorant Team Manager API 🎯

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AI](https://img.shields.io/badge/AI_Coach-Llama_3-purple.svg)

An asynchronous RESTful API and Interactive Dashboard built to manage esports rosters (like "no talent"), track player statistics, and provide instant AI-driven coaching feedback using live match data.

## ✨ Features

* **🧠 AI Coach Analysis:** Generates personalized, professional esports coaching feedback for specific matches using the Groq API (Llama 3.1) based on raw gameplay statistics.
* **📈 Streamlit Analytics Dashboard:** A clean, gamer-oriented web interface to easily register players, view match history, and request AI analysis without touching API endpoints manually.
* **👥 Team & Player Management:** Register players using their Riot ID (Name#Tag), automatically fetching and storing their unique PUUID via the official Riot API.
* **🔄 Advanced Match Tracking:** Fetch clean, lightweight match history and detailed individual performance metrics (K/D/A, Agents, Map, Win/Loss).
* **🐳 Fully Dockerized:** Seamless one-click deployment for the database, backend, and frontend via Docker Compose.

## 🛠 Tech Stack

* **Backend Framework:** FastAPI (Asynchronous)
* **Frontend UI:** Streamlit, Pandas
* **Database:** PostgreSQL (Asyncpg) + SQLAlchemy 2.0
* **Migrations:** Alembic
* **External APIs:** Riot Games Account API, HenrikDev Valorant API
* **AI Integration:** Groq Python SDK (Llama-3.1-8b-instant)
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitHub Actions (Automated pytest pipeline)

## 🚀 Quick Start (Docker)

The easiest way to run the complete stack is via Docker. Ensure you have Git and Docker installed on your machine.

**1. Clone the repository:**
```bash
git clone [https://github.com/Raccoohh/Valorant-Team-Manager-API.git](https://github.com/Raccoohh/Valorant-Team-Manager-API.git)
cd Valorant-Team-Manager-API
```

**2. Configure Environment Variables:**
Create a ```.env``` file in the root directory (you can safely copy ```.env.example```) and configure your secure credentials:
```bash
# Database Credentials
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=valorant_db

# Backend Database URL
DATABASE_URL=postgresql+asyncpg://postgres:your_secure_password@db:5432/valorant_db

# External APIs
RIOT_API_KEY=RGAPI-your-official-riot-key
HENRIK_API_KEY=your-henrik-api-key
GROQ_API_KEY=gsk_your-groq-api-key
```

**3. Build and start the containers:**
```bash
docker compose up --build -d
```
Note: The FastAPI backend container will automatically run the Alembic database migrations on startup.

## 🌐 Accessing the Application

Once the containers are successfully running, you can access the services locally:
* **🎮 Streamlit Dashboard (Frontend):**  `http://localhost:8501`
* **📖 Interactive API Docs (Swagger UI):**  `http://localhost:8000/docs`
* **📄 Alternative API Docs (ReDoc):**  `http://localhost:8000/redoc`

## 🧪 Testing

This project uses `pytest` for testing. The testing pipeline is fully automated via **GitHub Actions** and runs on every push or pull request to the `main` branch.
To run the test suite locally on your machine:

**1. Install testing dependencies (if not already installed):**
```bash
pip install pytest httpx pytest-asyncio
```

2. Execute the tests:
```Bash
pytest -v
```

## 🛑 Stopping the Application

To stop the running containers and free up resources, run:
```Bash
docker compose down
```

## 📖 API Documentation (Key Endpoints)

The REST API is fully documented using OpenAPI (Swagger). Once the application is running, navigate to `/docs` to interact with all endpoints. Some of the core routes include:

* **`POST /players/`** - Register a new player and automatically fetch their Riot PUUID.
* **`GET /players/{player_id}/matches`** - Fetch a lightweight summary of the player's recent matches.
* **`GET /players/{player_id}/matches/{match_id}/analyze`** - Generate automated AI coach feedback (Groq Llama 3) for a specific match.
* **`POST /teams/`** - Register a new esports team and assign a captain.
* **`POST /payments/`** - Process tournament entry fee payments for the team.

*Developed by [raccoohh](https://github.com/Raccoohh)*

