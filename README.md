# Valorant Team Manager API 🎮

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange)

<<<<<<< HEAD
A high-performance asynchronous web application designed to manage competitive Valorant esports teams, synchronize player rosters, and track financial/tournament performance.

## 🚀 Features

* **Player Management:** Register professional players, store unique Riot IDs, and manage individual profiles.
* **Dynamic Team Rosters:** Create teams, assign captains, and manage multi-player rosters with efficient relationship handling.
* **Tournament Tracking:** Record competitive events, track entry fees, and calculate match results (automated win/loss evaluation).
* **Financial Accounting:** Manage tournament entry payments and track financial compliance for team organizations.
* **Extensible Architecture:** Designed with future Riot Games API integration in mind.

## 🏗️ Architecture & Best Practices Highlights

As a backend-focused project, special attention was given to performance, maintainability, and stability:

* **Asynchronous I/O:** Utilized `asyncpg` with FastAPI to ensure non-blocking, high-performance database interactions.
* **Data Validation:** Implemented strict request validation and object serialization using `Pydantic` models.
* **Database Migrations:** Fully version-controlled database schema using `Alembic`, allowing safe and trackable structural changes.
* **Modular Design:** Separated the application into distinct layers (API Routers, CRUD operations, Database Models, and Schemas) for maximum scalability.

## 🛠 Tech Stack

* **Backend:** Python 3.10+, FastAPI, Pydantic
* **Database & ORM:** PostgreSQL, SQLAlchemy (Async)
* **Migrations:** Alembic
* **HTTP Client:** HTTPX (for asynchronous API requests)

## ⚙️ Local Setup & Installation

### Prerequisites
* Python 3.10+
* PostgreSQL server

### Quick Start

**1. Clone the repository:**
```bash
git clone [https://github.com/Raccoohh/Valorant-Team-Manager-API.git](https://github.com/Raccoohh/Valorant-Team-Manager-API.git)
cd Valorant-Team-Manager-API

2. Create a virtual environment & install dependencies:
=======
A robust asynchronous backend web application designed to track Valorant esports teams, manage dynamic player rosters, and handle tournament financials.

## 🚀 Features

* **Pro Directory:** Register professional players, store unique Riot IDs, and manage individual profiles.
* **Dynamic Team Rosters:** Create teams, assign captains, and seamlessly link multiple players to active rosters using Many-to-Many relationships.
* **Tournament Tracking:** Record competitive events, set entry fees, and track match results with automated win/loss calculation.
* **Financial Accounting:** Manage tournament entry payments and track financial compliance for team organizations.

## 🏗️ Architecture & Best Practices Highlights

As a backend-focused project, special attention was given to performance and stability:

* **Asynchronous I/O:** Utilized strict `asyncpg` configurations with FastAPI to ensure non-blocking, high-performance database interactions.
* **Data Validation:** Implemented strict schema validation and serialization using `Pydantic` models.
* **Database Migrations:** Solved schema versioning using `Alembic`, allowing safe and trackable structural changes.
* **Modular Design:** Separated the application into distinct layers (API Routers, CRUD operations, Database Models, and Schemas).

## 🛠 Tech Stack

* **Backend:** Python 3.10+, FastAPI, SQLAlchemy (Async), Pydantic
* **Database:** PostgreSQL
* **Migrations:** Alembic
* **Infrastructure:** Uvicorn, HTTPX

## ⚙️ Local Setup & Installation

The project is fully configured for easy local setup.

### Prerequisites
* Python 3.10+
* PostgreSQL server running locally
* Git

### Quick Start

**1. Clone the repository:**
```bash
git clone https://github.com/Raccoohh/Valorant-Team-Manager-API.git
cd Valorant-Team-Manager-API
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**2. Configure Environment Variables:** Create a `.env` file in the root directory and configure your database credentials:

```env
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost/esports_db
RIOT_API_KEY=your_riot_api_key_here
```
**3. Build and Run the Server:** 
```Bash
alembic upgrade head
uvicorn main:app --reload
```
**4. Access the Application:**

* **Backend API Swagger UI:** `http://localhost:8000/docs`

## 📖 API Documentation

The REST API is fully documented using OpenAPI (Swagger). Once the application is running, navigate to `/docs` to interact with the endpoints. Key endpoints include:

* `POST /players/` - Register a new esports player
* `POST /teams/` - Create a new esports team
* `POST /teams/{team_id}/players/{player_id}` - Add a player to an active team roster
* `POST /tournaments/` - Create a new tournament
* `POST /matches/` - Record match results
* `POST /payments/` - Process tournament entry fees

---
*Developed by [Raccoohh](https://github.com/Raccoohh)*
>>>>>>> c3eac86876e28cd6b7b08062c6c8e98c5e9a6726
