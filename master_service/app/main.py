from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .api.v1.process_images import process_images_router
from .core import config


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

    _app.include_router(process_images_router, prefix="/api/v1/process_images", tags=['process_images'])

    return _app


app = get_application()
