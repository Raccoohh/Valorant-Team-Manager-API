import uuid
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_create_team():
    # Генеруємо унікальну назву для кожного запуску тесту
    unique_team_name = f"no talent test {uuid.uuid4()}"
    
    response = client.post(
        "/teams/",
        json={"name": unique_team_name, "captain_id": 1} # Передаємо унікальну назву
    )
    
    assert response.status_code == 200
    
    data = response.json()
    # Перевіряємо, чи сервер повернув саме ту унікальну назву
    assert data["name"] == unique_team_name
    assert "id" in data