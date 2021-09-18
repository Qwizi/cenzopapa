from fastapi import APIRouter
import httpx

from .models import EventModel, EventType
from ...core.config import settings

webhook_router = APIRouter()


@webhook_router.get('/health/')
async def check_health():
    return True


@webhook_router.post("/", response_model=EventModel)
async def send_event(event: EventModel):
    async with httpx.AsyncClient() as client:
        try:
            await client.post(settings.MASTER_WEBHOOK, data=event.dict())
        except Exception as e:
            print(e)
    return event
