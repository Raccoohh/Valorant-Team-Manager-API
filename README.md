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