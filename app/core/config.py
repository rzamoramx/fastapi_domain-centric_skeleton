# Applications configs like env variables, settings, etc.
# Logging configuration is also done here.
# Scope: global
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Application"
    DATABASE_URL: str = "sqlite:///./sql_app.db"


settings = Settings()
