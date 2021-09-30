from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    FIREBASE_STORAGE_BUCKET: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASS: str
    DATABASE_DB: str


    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()


def get_settings():
    return Settings()
