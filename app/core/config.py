from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    IMGUR_CLIENT_ID: str
    IMGUR_CLIENT_SECRET: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    FIREBASE_API_KEY: str
    FIREBASE_AUTH_DOMAIN: str
    FIREBASE_PROJECT_ID: str
    FIREBASE_STORAGE_BUCKET: str
    FIREBASE_MSG_SENDER_ID: str
    FIREBASE_APP_ID: str
    FIREBASE_MEASUREMENT_ID: str
    FIREBASE_DATABASE_URL: str

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
