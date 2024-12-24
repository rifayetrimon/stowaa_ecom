from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_HOST: str
    REDIS_PORT: int
    SECRET_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"  

settings = Settings()


