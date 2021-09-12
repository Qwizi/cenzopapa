from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from core import config
from api.v1.api import api_router
from firebase.firebase import db, bucket


def get_settings():
    return config.Settings()


def get_application():
    _app = FastAPI(title=get_settings().PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in get_settings().BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(api_router, prefix="/v1")

    return _app


app = get_application()
