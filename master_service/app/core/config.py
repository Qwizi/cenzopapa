from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    FIREBASE_STORAGE_BUCKET: str
    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASS: str
    DATABASE_DB: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()


def get_settings():
    return Settings()
