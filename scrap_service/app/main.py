import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .core import config
from .routers.scrap import scrap_router
from .utils.app_exceptions import AppExceptionCase, app_exception_handler
from .utils.request_exceptions import request_validation_exception_handler, http_exception_handler

logging.config.fileConfig('logger.ini', disable_existing_loggers=False)

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


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(scrap_router, prefix="/api/v1", tags=['scrap'])
