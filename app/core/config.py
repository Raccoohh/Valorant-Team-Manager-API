from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    RIOT_API_KEY: str = ""
    DATABASE_URL: str = "DATABASE_URL=postgresql+asyncpg://postgres:Artur12345@db:5432/esports_db"  

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()