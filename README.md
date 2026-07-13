# 🎮 Valorant Team Manager & AI Coach API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

A full-stack, containerized application designed to manage competitive Valorant rosters (like *no talent*), track match histories via the Riot API, and provide automated VOD reviews and tactical feedback using AI (Groq Llama 3.1).

## ✨ Features

* **Roster Management:** Register players, assign roles, and form competitive teams.
* **Riot API Integration:** Automatically fetches player PUUIDs and recent match statistics (handles custom lobbies and deathmatches safely).
* **AI Coach:** Analyzes post-match statistics using LLMs to provide actionable feedback and tactical advice.
* **Robust Testing:** Asynchronous test suite using an isolated in-memory SQLite database and mocked external API calls.
* **Interactive Dashboard:** Built with Streamlit for a seamless user experience.

## 🏗️ Tech Stack

* **Backend:** FastAPI (Python 3.10+)
* **Database:** PostgreSQL (asyncpg), SQLAlchemy ORM
* **Migrations:** Alembic
* **Frontend:** Streamlit
* **External Services:** HenrikDev API (Unofficial Riot API), Groq API (LLM)
* **DevOps:** Docker, Docker Compose
* **Testing:** Pytest, pytest-asyncio, aiosqlite, unittest.mock

---

## 🚀 Quick Start (Docker)

The easiest way to run the application is using Docker. This ensures a consistent environment without polluting your local machine.

### 1. Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
RIOT_API_KEY=your_henrikdev_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

**2. Build and Run**
Start the containers using Docker Compose:
```bash
docker compose up --build -d
```
Docker will automatically provision the PostgreSQL database, run Alembic migrations, and start the backend and frontend servers.

**3. Access the Application**
* **Interactive Dashboard (Frontend):**  `http://localhost:8501`
* **API Swagger Documentation:**  `http://localhost:8000/docs`

💻 Local Development (Optional)
If you wish to contribute to the code, use IDE features like IntelliSense, or run scripts locally, set up a virtual environment.

**1. Setup Virtual Environment**
```Bash
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
```

**2. Install Dependencies**
```Bash
pip install -r requirements.txt
pip install pytest pytest-asyncio aiosqlite httpx
```
(Note: The application still requires a running PostgreSQL instance. You can keep the db container running via Docker while developing the backend locally).

## 🧪 Testing

The project features a robust, isolated asynchronous testing environment.

* **Database Isolation:** Tests run against an in-memory ```SQLite``` database (```aiosqlite```), ensuring the production PostgreSQL database remains untouched.
* **Network Isolation:** All third-party API calls (e.g., Riot API) are mocked using ```@patch``` to ensure fast, reliable, and offline testing without hitting rate limits.

To run the test suite inside the Docker container:
```Bash
docker compose exec web pytest -v
```

##  📁 Project Structure
├── app/
│   ├── api/            # FastAPI routers (players, teams, matches)
│   ├── core/           # Database configuration and app settings
│   ├── crud/           # Create, Read, Update, Delete operations
│   ├── models/         # SQLAlchemy database models
│   ├── schemas/        # Pydantic validation schemas
│   └── services/       # External API clients (Riot Service, AI Service)
├── frontend/           # Streamlit application UI
├── alembic/            # Database migration scripts
├── tests/              # Asynchronous unit and integration tests
├── docker-compose.yml  # Container orchestration
├── Dockerfile          # Backend image configuration
└── requirements.txt    # Python dependencies

*Developed by [raccoohh](https://github.com/Raccoohh)*

