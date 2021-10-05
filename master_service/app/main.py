import logging

import httpx
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi_pagination import add_pagination
from fastapi_utils.tasks import repeat_every
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware

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

"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in get_settings().BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""


app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("startup")
@repeat_every(seconds=3600, raise_exceptions=True, logger=logging.getLogger(__name__))
async def scrap_sites():
    async with httpx.AsyncClient() as client:
        await client.post("http://192.168.1.102:8501/scrap/")




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


app.include_router(process_images_router, prefix="/process_images", tags=['process_images'])
app.include_router(images_router, prefix="/images", tags=['images'])

add_pagination(app)
