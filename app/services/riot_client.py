import httpx
from app.core.config import settings

class RiotGamesClient:
    def __init__(self):
        # Налаштовуємо базові параметри для всіх запитів
        self.api_key = settings.RIOT_API_KEY
        self.headers = {"X-Riot-Token": self.api_key}
        self.base_url = "https://europe.api.riotgames.com" # Кластер для Valorant (Європа)

    async def get_player_puuid(self, game_name: str, tag_line: str):
        """
        Метод для отримання унікального ідентифікатора гравця (PUUID).
        Приклад: game_name="TenZ", tag_line="NA1"
        """
        # Спеціальний URL згідно з документацією Riot API
        url = f"{self.base_url}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()
                return data.get("puuid") # Повертаємо унікальний ID гравця
            
            # Якщо гравця не знайдено або ключ недійсний
            return None

# Створюємо готовий об'єкт, який зможемо імпортувати в інші файли
riot_service = RiotGamesClient()