# Valorant Team Manager API 🎮

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange)

An asynchronous backend API designed to manage esports teams, dynamic player rosters, tournament participation, and financial tracking for Valorant.

## 🚀 Features

* **Player Management:** Register players, store Riot IDs, and manage individual profiles.
* **Dynamic Team Rosters:** Create teams, assign captains, and seamlessly link multiple players to active rosters.
* **Tournament Tracking:** Record competitive events, set entry fees, and track match results (automated win/loss calculation).
* **Financial Dashboard:** Process team entry payments and track financial statuses for tournaments.
* *(Planned)* **External API Integration:** Synchronize player stats directly via the official Riot Games API.

## 🏗️ Architecture & Best Practices Highlights

As a backend-focused project, special attention was given to modern API standards and performance:

* **Asynchronous I/O:** Utilized `asyncpg` with FastAPI to ensure non-blocking, high-performance database operations.
* **Data Validation:** Implemented strict schema validation and serialization using `Pydantic` models.
* **Database Migrations:** Fully version-controlled database schema using `Alembic`, allowing safe and trackable structural changes.
* **Modular Design:** Separated the application into distinct layers (API Routers, CRUD operations, Database Models, and Schemas) for maximum scalability.

## 🛠 Tech Stack

* **Backend:** Python 3.10+, FastAPI, Pydantic
* **Database & ORM:** PostgreSQL, SQLAlchemy (Async)
* **Migrations:** Alembic
* **External Clients:** HTTPX (for asynchronous API calls)

## ⚙️ Local Setup & Installation

The project is configured for a standard local Python environment.

### Prerequisites
* Python 3.10+
* PostgreSQL server running locally

### Quick Start

**1. Clone the repository:**
```bash
git clone [https://github.com/Raccoohh/Valorant-Team-Manager-API.git](https://github.com/Raccoohh/Valorant-Team-Manager-API.git)
cd Valorant-Team-Manager-API

2. Create a virtual environment & install dependencies: 
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

3. Configure Environment Variables:
Create a .env file in the root directory and configure your database credentials:
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost/esports_db
RIOT_API_KEY=your_riot_api_key_here

4. Apply Migrations & Run the Server:
alembic upgrade head
uvicorn main:app --reload

5. Access the Application:
Backend API Swagger UI: http://localhost:8000/docs

Alternative ReDoc UI: http://localhost:8000/redoc

📖 API Documentation
The REST API is fully documented using OpenAPI (Swagger). Once the application is running, navigate to /docs to interact with the endpoints. Key endpoints include:

POST /players/ - Register a new esports player

POST /teams/ - Create a new team with a designated captain

POST /teams/{team_id}/players/{player_id} - Add a player to a team roster

POST /tournaments/ - Create a new tournament

POST /matches/ - Record match results between teams

POST /payments/ - Process tournament entry fees