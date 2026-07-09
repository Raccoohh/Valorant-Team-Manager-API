# Valorant Team Manager API 🎮

An asynchronous RESTful API built with FastAPI to manage esports teams, players, tournaments, and match statistics. Fully dockerized for seamless deployment and testing.

## 🚀 Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database:** PostgreSQL (Asynchronous via `asyncpg`)
* **ORM & Migrations:** SQLAlchemy 2.0 + Alembic
* **Data Validation:** Pydantic V2
* **Containerization:** Docker & Docker Compose
* **Testing:** Pytest + HTTPX

## ✨ Features

* **Team Management:** Create and manage esports rosters (e.g., assigning captains and players).
* **Player Tracking:** Register players with their unique Riot IDs and link them to teams.
* **Tournament & Matches:** Record match results, track scores, and manage tournament brackets.
* **Payment Tracking:** Monitor tournament entry fees and payment statuses.
* **Automated Testing:** Fully isolated test environment integrated with Docker.

## 🛠️ Prerequisites

Before you begin, ensure you have met the following requirements:
* [Git](https://git-scm.com/) installed
* [Docker](https://www.docker.com/) and Docker Compose installed

## 🚦 Quick Start (Docker)

The easiest way to run the API and the PostgreSQL database is via Docker.

**1. Clone the repository:**
```bash
git clone [https://github.com/Raccoohh/Valorant-Team-Manager-API.git](https://github.com/Raccoohh/Valorant-Team-Manager-API.git)
cd Valorant-Team-Manager-API
```
2. **Configure Environment Variables:**
   Create a `.env` file in the root directory and configure your database credentials:
   ```env
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres
   ```

**3. Build and start the containers:**
```Bash
docker compose up --build -d
```

**4. Run Database Migrations:**
Generate the tables in your PostgreSQL database using Alembic:
```Bash
docker compose exec web alembic upgrade head
```

**5. Access the Application:**

* Backend API Swagger UI: `http://localhost:8000/docs`
* Alternative API ReDoc: `http://localhost:8000/redoc`

## 🧪 Running Tests

The project includes automated tests using `pytest`. You can run the test suite directly inside the Docker container without installing dependencies locally.

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

The REST API is fully documented using OpenAPI (Swagger). Once the application is running, navigate to /docs to interact with the endpoints. Key endpoints include:
* `POST /teams/` - Register a new esports team
* `POST /payments/` - Process tournament entry fee payment
* `POST /matches/` - Record match results and scores

*Developed by [Raccoohh](https://github.com/Raccoohh)*
