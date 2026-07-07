# Valorant Team Manager API 🎮

A robust Backend API built with **FastAPI** and **PostgreSQL** to manage esports teams, player rosters, tournament participation, and financial tracking.

## 🚀 Features

- **Player Management:** Register players, assign in-game roles (Duelist, Controller, IGL), and store Discord/Riot IDs.
- **Team Rosters:** Create and manage teams, assign captains, and track active rosters.
- **Tournament Tracking:** Record tournament entries, store match results, and track team performance.
- **Financial Accounting:** Manage tournament entry fees and payment statuses.
- _(Planned)_ **Riot Games API Integration:** Automatically fetch player statistics and match history.

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.10+
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (Async)
- **Migrations:** Alembic

## ⚙️ Local Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/Raccoohh/Valorant-Team-Manager-API.git](https://github.com/Raccoohh/Valorant-Team-Manager-API.git)

1. Create and activate a virtual environment.

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
uvicorn app.main:app --reload