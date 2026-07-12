from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.player import PlayerCreate, PlayerResponse
from app.crud import player as crud_player
from app.services.riot_client import riot_service
from app.services.ai_client import ai_service

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/", response_model=PlayerResponse)
async def create_new_player(player: PlayerCreate, db: AsyncSession = Depends(get_db)):
    # 1. Розбиваємо riot_id, який прислав клієнт, на game_name та tag_line
    try:
        game_name, tag_line = player.riot_id.split("#")
    except ValueError:
        raise HTTPException(
            status_code=400, 
            detail="Неправильний формат riot_id. Використовуйте формат 'Name#Tag'."
        )

    # 2. Робимо запит до Riot API. Якщо гравця немає, сервіс сам викине 404 помилку.
    player_data = await riot_service.get_player_puuid(game_name, tag_line)
    puuid = player_data.get("puuid")

    # 3. Зберігаємо гравця в БД, передаючи отриманий puuid
    new_player = await crud_player.create_player(db, player, puuid=puuid)
    
    return new_player


@router.get("/{player_id}", response_model=PlayerResponse)
async def read_player(player_id: int, db: AsyncSession = Depends(get_db)):
    db_player = await crud_player.get_player(db, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


@router.get("/{player_id}/matches")
async def get_player_matches(player_id: int, db: AsyncSession = Depends(get_db)):
    """
    Отримати останні матчі гравця за його внутрішнім ID у нашій базі даних.
    """
    db_player = await crud_player.get_player(db, player_id)
    
    if not db_player:
        raise HTTPException(status_code=404, detail="Гравця не знайдено у базі даних")
    
    try:
        game_name, tag_line = db_player.riot_id.split("#")
    except ValueError:
        raise HTTPException(status_code=400, detail="У гравця неправильно збережений riot_id")

    # 1. Отримуємо гігантський масив (повні дані матчів) від стороннього API
    raw_matches = await riot_service.get_player_matchlist(game_name, tag_line)
    
    # 2. Робимо коротку вижимку, щоб Swagger (і фронтенд у майбутньому) не зависав
    short_matches = []
    for match in raw_matches:
        meta = match.get("metadata", {})
        short_matches.append({
            "match_id": meta.get("matchid"),
            "map": meta.get("map"),
            "mode": meta.get("mode"),
            "server": meta.get("cluster"),
            "rounds_played": meta.get("rounds_played"),
            "start_time": meta.get("game_start_patched")
        })
    
    return {
        "status": "success",
        "player": {
            "id": db_player.id,
            "nickname": db_player.nickname,
            "riot_id": db_player.riot_id
        },
        # Віддаємо тільки акуратний відфільтрований список
        "matches": short_matches      
    }


# === ОНОВЛЕНИЙ ЕНДПОІНТ З ПЕРЕДАЧЕЮ РЕЗЕРВНИХ ДАНИХ ===
@router.get("/{player_id}/matches/{match_id}")
async def get_player_match_details(player_id: int, match_id: str, db: AsyncSession = Depends(get_db)):
    """
    Отримати коротку відфільтровану статистику конкретного матчу для одного гравця.
    Шукає гравця всередині матчу за PUUID або за Нікнеймом#Тегом.
    """
    # 1. Дістаємо гравця з PostgreSQL
    db_player = await crud_player.get_player(db, player_id)
    
    if not db_player:
        raise HTTPException(status_code=404, detail="Гравця не знайдено у базі даних")
    
    # 2. Розбиваємо riot_id на дві частини для резервного пошуку в сервісі
    try:
        game_name, tag_line = db_player.riot_id.split("#")
    except ValueError:
        raise HTTPException(status_code=400, detail="У гравця неправильно збережений riot_id")
    
    # 3. Викликаємо сервіс, передаючи і PUUID, і текстовий Riot ID
    match_stats = await riot_service.get_match_details(
        match_id=match_id, 
        puuid=db_player.puuid, 
        game_name=game_name, 
        tag_line=tag_line
    )
    
    return {
        "status": "success",
        "player": {
            "id": db_player.id,
            "nickname": db_player.nickname,
            "riot_id": db_player.riot_id
        },
        "match_details": match_stats
    }


@router.get("/{player_id}/matches/{match_id}/analyze")
async def analyze_player_match(player_id: int, match_id: str, db: AsyncSession = Depends(get_db)):
    """
    Отримати автоматичний аналіз конкретного матчу від ШІ-тренера.
    Ендпоінт поєднує дані PostgreSQL, статистику ігрового API та аналітику Groq.
    """
    # 1. Перевіряємо наявність гравця в базі даних
    db_player = await crud_player.get_player(db, player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail="Гравця не знайдено у базі даних")

    # 2. Витягуємо чисту статистику матчу, яку ми реалізували раніше
    # (Вона вже містить захист від помилок та подвійний пошук за PUUID/Нікнеймом)
    match_stats = await riot_service.get_match_details(
        match_id=match_id,
        puuid=db_player.puuid,
        game_name=db_player.riot_id.split("#")[0],
        tag_line=db_player.riot_id.split("#")[1]
    )

    # 3. Передаємо структуровані цифри у Groq API для генерації фідбеку
    coach_commentary = await ai_service.generate_match_analysis(match_stats)

    # 4. Повертаємо гарну відповідь клієнту
    return {
        "status": "success",
        "player": {
            "id": db_player.id,             # 👈 Змінено player на db_player
            "nickname": db_player.nickname  # 👈 Змінено player на db_player
        },
        "match_id": match_id,
        "stats": match_stats,
        "coach_analysis": coach_commentary
    }