import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware

from .services.watermark import WatermarkService
from .utils.request_exceptions import http_exception_handler
from .utils.request_exceptions import request_validation_exception_handler
from .core import config
from .core.db import database
from .routers.image import images_router
from .routers.process_images import process_images_router
from .utils.app_exceptions import app_exception_handler, AppExceptionCase

logging.config.fileConfig('./logger.ini', disable_existing_loggers=False)


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

app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(process_images_router, prefix="/api/v1/process_images", tags=['process_images'])
app.include_router(images_router, prefix="/api/v1/cenzo", tags=['cenzo'])
