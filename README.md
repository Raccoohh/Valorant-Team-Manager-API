# 🎯 no talent | Valorant Team Manager & AI Coach

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

A full-stack, containerized application designed to manage the **no talent** competitive Valorant roster. It tracks match histories via the Riot API, manages tournament entries and payments, and provides automated VOD reviews using AI (Groq Llama 3.1).

## ✨ Core Features

* **Esports Roster Management:** Register players with their Riot IDs, assign roles (Duelist, Initiator, etc.), and manage Discord integrations.
* **Resilient Riot API Integration:** Fetches player PUUIDs and match statistics from the HenrikDev API. Built with fault tolerance to handle missing metadata (e.g., custom lobbies, deathmatches).
* **AI Match Coach:** Deep integration with Groq LLM to analyze raw match metrics (KDA, agent, map) and generate actionable tactical feedback.
* **Automated Migrations:** Alembic migrations run automatically on container startup to ensure database schemas are always strictly in sync.
* **Interactive HQ Dashboard:** Built with Streamlit, offering a dual-column layout for immediate player registration and historical match analysis.

## 🏗️ Architecture & Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | FastAPI (Python 3.10+) | Asynchronous REST API with CORS enabled for public/commercial access. |
| **Database** | PostgreSQL + asyncpg | Relational database handling teams, players, tournaments, and payments. |
| **ORM & Migrations** | SQLAlchemy + Alembic | Asynchronous database interactions and version control. |
| **Frontend** | Streamlit | Responsive UI directly communicating with the backend API. |
| **AI / LLM** | Groq API | High-speed inference for the tactical AI coach feature. |
| **DevOps** | Docker + Compose | Multi-container orchestration (`db`, `web`, `frontend`). |

## 🚀 Quick Start (Docker)

The recommended way to launch the application is via Docker. The setup is fully self-contained.

### 1. Environment Setup
Create a `.env` file in the root directory and add your secret keys:
```env
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=valorant_db

RIOT_API_KEY=your_riot_api_key_here
HENRIK_API_KEY=your_henrikdev_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

**2. Launch the Cluster**
Start the containers using Docker Compose:
```Bash
docker compose up --build -d
```
Note: The ```web``` container is configured to run ```alembic upgrade head``` automatically before starting the Uvicorn server, ensuring your database is instantly ready.


**3. Access the Services**
* **no talent HQ Dashboard (Streamlit):**  `http://localhost:8501`
* **API Swagger Documentation:**  `http://localhost:8000/docs`

## 💻 Local Development (Optional)

If you need to develop locally or leverage IDE IntelliSense, set up your Python environment.
```Bash
# 1. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate   # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## 🧪 Testing Strategy

* **Absolute Database Isolation:** Tests bypass PostgreSQL entirely, utilizing an in-memory ```SQLite``` (```aiosqlite```) database via dependency overrides. Tables are generated and dropped natively within the fixture lifecycle.

* **Zero-Network Mocking:** Third-party API calls (Riot API) are aggressively mocked using ```unittest.mock.patch``` to prevent rate-limiting and ensure deterministic, sub-second test execution.

**Run the test suite inside the active backend container:**
```Bash
docker compose exec web pytest -v
```

## 📁 Project Structure

├── app/
│   ├── api/            # API Routers (players, teams, tournaments, matches, payments)
│   ├── core/           # Database engine and session configuration
│   ├── crud/           # Database CRUD operations
│   ├── models/         # SQLAlchemy schemas
│   ├── schemas/        # Pydantic validation models
│   └── main.py         # FastAPI application entry point & CORS configuration
├── frontend/
│   └── app.py          # Streamlit UI dashboard
├── alembic/            # Database migration scripts
├── tests/              # Pytest async test suite and conftest.py
├── docker-compose.yml  # Service orchestration (Postgres, API, Frontend)
├── Dockerfile          # Python backend image recipe
└── requirements.txt    # Project dependencies

*Developed by [raccoohh](https://github.com/Raccoohh)*

