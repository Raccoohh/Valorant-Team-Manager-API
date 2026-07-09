from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    RIOT_API_KEY: str = ""
    
    DATABASE_URL: str 
    
    # Реєструємо ці змінні, щоб Pydantic не видавав помилку "Extra inputs are not permitted"
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_DB: str | None = None

    # extra="ignore" захистить тебе в майбутньому: якщо ти додаш у .env щось нове, проєкт не впаде
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()