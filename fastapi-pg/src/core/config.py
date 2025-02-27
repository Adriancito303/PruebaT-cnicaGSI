from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI GSI"
    PROJECT_VERSION: str = "0.1.0"
    DATABASE_URL: str
    
    class config:
        env_file = ".env"
    
settings = Settings()