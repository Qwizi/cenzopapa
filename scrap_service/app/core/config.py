from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    MASTER_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()