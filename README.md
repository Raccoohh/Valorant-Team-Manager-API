# Valorant Team Manager API 🎮



![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

![Alembic](https://img.shields.io/badge/Alembic_Migrations-FCC624?style=for-the-badge)

![Pydantic](https://img.shields.io/badge/Pydantic_V2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

![Groq](https://img.shields.io/badge/AI-Groq_Llama_3.1-f55036?style=for-the-badge)



An asynchronous RESTful API built with FastAPI to manage esports teams (like "no talent" and others), players, tournaments, and advanced match statistics. Fully dockerized for seamless deployment, featuring live game data fetching and AI-powered match analysis.



## 🚀 Tech Stack



* **Framework:** FastAPI

* **Database:** PostgreSQL (Asynchronous via `asyncpg`)

* **ORM & Migrations:** SQLAlchemy 2.0 + Alembic

* **Data Validation:** Pydantic V2

* **External APIs:** Riot Games Account API, HenrikDev Valorant API

* **AI Integration:** Groq Python SDK (Llama-3.1-8b-instant)

* **Containerization:** Docker & Docker Compose

* **Testing:** Pytest + HTTPX



## ✨ Features



* **Team Management:** Create and manage esports rosters, assigning captains and organizing players.

* **Player Tracking:** Register players using their Riot ID (Name#Tag), automatically fetching and storing their unique `puuid` via the official Riot API.

* **Advanced Match Statistics:** Fetch clean, lightweight match history and detailed individual performance metrics (K/D/A, Agents, Map, Win/Loss) using a dual-verification system (PUUID + Riot ID fallback).

* **AI Coach Analysis:** Generate instant, professional, and personalized esports coaching feedback for specific matches using the Groq AI model based on flat performance stats.

* **Tournament & Payments:** Track match results, tournament brackets, entry fees, and payment statuses.



## 🛠 Prerequisites



Before you begin, ensure you have met the following requirements:



* **Git** installed

* **Docker** and **Docker Compose** installed



## 🚦 Quick Start (Docker)



The easiest way to run the API and the PostgreSQL database is via Docker.



**1. Clone the repository:**

```bash

git clone [https://github.com/Raccoohh/Valorant-Team-Manager-API.git](https://github.com/Raccoohh/Valorant-Team-Manager-API.git)

cd Valorant-Team-Manager-API

```

**2. Configure Environment Variables:** Create a .env file in the root directory and configure your database and API credentials:

```bash

# Database

DATABASE_URL=postgresql+asyncpg://postgres:password@db:5432/postgres



# External APIs

RIOT_API_KEY=RGAPI-your-official-riot-key

HENRIK_API_KEY=your-henrik-api-key

GROQ_API_KEY=gsk_your-groq-api-key

```

**3. Build and start the containers:**

```bash

docker compose up --build -d

```

**4. Run Database Migrations:** Generate the tables in your PostgreSQL database using Alembic:

```Bash

docker compose exec web alembic upgrade head

```

**5. Access the Application:**

* **Backend API Swagger UI:**  `http://localhost:8000/docs`

* **Alternative API ReDoc:**  `http://localhost:8000/redoc`



## 🧪 Running Tests



The project includes automated tests using ```pytest```. You can run the test suite directly inside the Docker container without installing dependencies locally.



To execute all tests, run:

```Bash

docker compose exec web python -m pytest

```



## 🛑 Stopping the Application

To stop the running containers and free up resources, run:

```Bash

docker compose down

```



## 📖 API Documentation



The REST API is fully documented using OpenAPI (Swagger). Once the application is running, navigate to `/docs` to interact with the endpoints. Key endpoints include:



* `POST /players/` - Register a new player and fetch PUUID

* `GET /players/{id}/matches` - Fetch player's recent matches

* `GET /players/{id}/matches/{match_id}/analyze` - Generate AI coach feedback for a specific match

* `POST /teams/` - Register a new esports team

* `POST /payments/` - Process tournament entry fee payment



*Developed by [raccoohh](https://github.com/Raccoohh)*

