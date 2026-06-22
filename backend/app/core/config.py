from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Knowledge Assistant"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ai_knowledge_assistant"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
