import uuid
import pytest
from unittest.mock import patch

@pytest.mark.asyncio
# 🧙‍♂️ МАГІЯ: Перехоплюємо виклик до Riot API
@patch("app.api.players.riot_service.get_player_puuid")
async def test_create_team(mock_get_puuid, client):
    # Кажемо моку: "Просто поверни цей словник, ніби ти справжній Riot API"
    mock_get_puuid.return_value = {"puuid": "fake-puuid-for-testing-123"}

    # ==========================================
    # КРОК 1: Створюємо гравця (майбутнього капітана)
    # ==========================================
    player_payload = {
        "nickname": "TestCaptain",
        "riot_id": "Captain#TEST",
        "game_role": "Duelist",
        "discord_tag": "captain#0000"
    }
    
    player_response = await client.post("/players/", json=player_payload)
    
    # Тепер Riot API не відхилить запит, і гравець успішно збережеться в SQLite
    assert player_response.status_code == 200, f"Помилка створення гравця: {player_response.text}"
    captain_id = player_response.json()["id"]

    # ==========================================
    # КРОК 2: Створюємо команду з цим капітаном
    # ==========================================
    unique_team_name = f"no talent test {uuid.uuid4()}"
    
    team_response = await client.post(
        "/teams/",
        json={"name": unique_team_name, "captain_id": captain_id}
    )
    
    assert team_response.status_code == 200, f"Помилка створення команди: {team_response.text}"
    
    data = team_response.json()
    assert data["name"] == unique_team_name
    assert "id" in data
    assert data["captain_id"] == captain_id