from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers.process_images import process_images_router
from .core import config


def get_settings():
    return config.Settings()


app = FastAPI(title=get_settings().PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in get_settings().BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(process_images_router, prefix="/api/v1/process_images", tags=['process_images'])
