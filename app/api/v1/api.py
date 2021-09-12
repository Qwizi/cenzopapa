from fastapi import APIRouter

from .endpoints import scrap, cenzo

api_router = APIRouter()
api_router.include_router(scrap.router, tags=['scrap'])
api_router.include_router(cenzo.router, tags=['cenzo'])