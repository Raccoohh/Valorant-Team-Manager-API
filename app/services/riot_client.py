import httpx
from fastapi import HTTPException
from app.core.config import settings

class RiotGamesClient:
    def __init__(self):
        # Налаштовуємо базові параметри для офіційного Riot API
        self.api_key = settings.RIOT_API_KEY
        self.headers = {"X-Riot-Token": self.api_key}
        
        # Офіційний сервер для отримання PUUID (Account API)
        self.account_url = "https://europe.api.riotgames.com"
        
        # Публічний сервер для матчів Valorant (HenrikDev API)
        self.henrik_url = "https://api.henrikdev.xyz"
        
        # Ключ авторизації для HenrikDev
        self.henrik_api_key = settings.HENRIK_API_KEY

    async def get_player_puuid(self, game_name: str, tag_line: str) -> dict:
        """
        Метод для отримання даних гравця (PUUID) через офіційний Riot API.
        """
        url = f"{self.account_url}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)

            if response.status_code == 200:
                return response.json()
            
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail=f"Гравця {game_name}#{tag_line} не знайдено.")
            
            elif response.status_code in (401, 403):
                raise HTTPException(status_code=403, detail="Помилка авторизації: перевірте ваш RIOT_API_KEY.")
            
            else:
                raise HTTPException(
                    status_code=response.status_code, 
                    detail=f"Помилка від Riot API: {response.text}"
                )

    async def get_player_matchlist(self, game_name: str, tag_line: str) -> list:
        """
        Отримує список останніх матчів гравця через стабільний ендпоінт HenrikDev 
        за нікнеймом та тегом (щоб уникнути їхнього багу з перевіркою PUUID).
        """
        url = f"{self.henrik_url}/valorant/v3/matches/eu/{game_name}/{tag_line}"

        henrik_headers = {
            "Authorization": self.henrik_api_key
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=henrik_headers)

            if response.status_code == 200:
                data = response.json()
                return data.get("data", [])
            
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail="Матчів для цього гравця не знайдено.")
            
            elif response.status_code in (401, 403):
                raise HTTPException(status_code=401, detail="Помилка авторизації HenrikDev: перевірте HENRIK_API_KEY.")
                
            elif response.status_code == 429:
                raise HTTPException(status_code=429, detail="Перевищено ліміт запитів. Спробуйте пізніше.")
            
            else:
                raise HTTPException(
                    status_code=response.status_code, 
                    detail=f"Помилка від стороннього API: {response.text}"
                )

    # === ОНОВЛЕНИЙ МЕТОД З ПОДВІЙНИМ ПОШУКОМ ===
    async def get_match_details(self, match_id: str, puuid: str, game_name: str, tag_line: str) -> dict:
        """
        Отримує детальну статистику конкретного матчу через HenrikDev API.
        Шукає гравця спочатку за PUUID, а якщо не знаходить — за нікнеймом та тегом (резервний варіант).
        """
        url = f"{self.henrik_url}/valorant/v2/match/{match_id}"
        
        henrik_headers = {
            "Authorization": self.henrik_api_key
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=henrik_headers)

            if response.status_code == 200:
                data = response.json().get("data", {})
                meta = data.get("metadata", {})
                players = data.get("players", {}).get("all_players", [])
                teams = data.get("teams", {})

                # КРОК 1: Спроба знайти гравця за PUUID
                target_player = next((p for p in players if p.get("puuid") == puuid), None)

                # КРОК 2: РЕЗЕРВНИЙ ВАРІАНТ (якщо за PUUID не знайшли, шукаємо за ніком та тегом)
                if not target_player:
                    target_player = next(
                        (p for p in players if p.get("name", "").lower() == game_name.lower() 
                         and p.get("tag", "").lower() == tag_line.lower()), 
                        None
                    )

                if not target_player:
                    raise HTTPException(
                        status_code=404, 
                        detail=f"Гравець {game_name}#{tag_line} не брав участі в цьому матчі."
                    )

                # Витягуємо метрики
                stats = target_player.get("stats", {})
                team_color = target_player.get("team", "").lower()  # "red" або "blue"
                has_won = teams.get(team_color, {}).get("has_won", False)

                return {
                    "match_id": match_id,
                    "map": meta.get("map"),
                    "agent": target_player.get("character"),
                    "kills": stats.get("kills"),
                    "deaths": stats.get("deaths"),
                    "assists": stats.get("assists"),
                    "won": has_won
                }
            
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail="Матч не знайдено.")
            elif response.status_code in (401, 403):
                raise HTTPException(status_code=401, detail="Помилка авторизації HenrikDev: перевірте HENRIK_API_KEY.")
            elif response.status_code == 429:
                raise HTTPException(status_code=429, detail="Перевищено ліміт запитів до стороннього API. Спробуйте пізніше.")
            else:
                raise HTTPException(
                    status_code=response.status_code, 
                    detail=f"Помилка від стороннього API: {response.text}"
                )

# Створюємо готовий об'єкт, який зможемо імпортувати в інші файли
riot_service = RiotGamesClient()