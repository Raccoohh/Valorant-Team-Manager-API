from groq import AsyncGroq
from app.core.config import settings

class AIGamesAnalyst:
    def __init__(self):
        # Ініціалізуємо асинхронний клієнт Groq
        self.client = AsyncGroq(api_key=settings.GROQ_API_KEY)
        # ЗАМІНИ НА ЦЕЙ РЯДОК:
        self.model = "llama-3.1-8b-instant"

    async def generate_match_analysis(self, match_stats: dict) -> str:
        """
        Генерує короткий аналітичний відгук на основі статистики матчу від імені тренера.
        """
        
        # Формуємо зрозумілий для ШІ текстовий опис отриманого словника статистики
        game_data_summary = (
            f"Агент: {match_stats.get('agent')}\n"
            f"Карта: {match_stats.get('map')}\n"
            f"Вбивства (Kills): {match_stats.get('kills')}\n"
            f"Смерті (Deaths): {match_stats.get('deaths')}\n"
            f"Асисти (Assists): {match_stats.get('assists')}\n"
            f"Результат матчу: {'Перемога' if match_stats.get('won') else 'Поразка'}"
        )

        # Системний промпт, який задає поведінку, тон та правила для моделі
        system_prompt = (
            "Ти — професійний кіберспортивний тренер та аналітик у грі Valorant. "
            "Твоє завдання — проаналізувати суху статистику матчу гравця та дати йому коротку, "
            "точну, конструктивну та професійну пораду. "
            "Відповідь має бути виключно українською мовою, обсягом до 3-5 речень. "
            "Звертай увагу на співвідношення KDA (Kills/Deaths/Assists). Наприклад, якщо смертей більше ніж убивств, "
            "порадь грати обережніше чи змінити позиційку. Якщо статистика крута, похвали за імпакт. "
            "Уникай загальних фраз, пиши так, ніби проводиш швидкий розбір матчу (VOD review) для гравця високого рівня."
        )

        # Надсилаємо асинхронний запит до Groq API
        chat_completion = await self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f"Проаналізуй цей матч:\n{game_data_summary}"
                }
            ],
            model=self.model,
            temperature=0.7,  # Додає помірну креативність у підбір слів тренера
            max_tokens=256    # Обмежуємо довжину відповіді для економії та лаконічності
        )

        # Повертаємо чистий згенерований текст
        return chat_completion.choices[0].message.content

# Створюємо готовий сервіс для імпорту в роутери
ai_service = AIGamesAnalyst()