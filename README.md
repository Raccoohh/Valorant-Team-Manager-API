# Valorant Team Manager API 🎮

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange)

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