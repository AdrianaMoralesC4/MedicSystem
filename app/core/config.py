from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Sistema de Citas Médicas"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 días
    
    # Database
    DB_URL: str = "postgresql+asyncpg://postgres:amorales@localhost:5432/citas_medicas"
    
    # Email
    SMTP_HOST: str = "smtp.example.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "user@example.com"
    SMTP_PASSWORD: str = "password"
    EMAILS_FROM_EMAIL: str = "no-reply@citasmedicas.com"
    EMAILS_FROM_NAME: str = "Sistema de Citas Médicas"
    
    class Config:
        case_sensitive = True

settings = Settings()