from enum import Enum

from pydantic import BaseModel


class EventType(str, Enum):
    SCRAP_IMAGES_SUCCESSFULLY = "scrap.images_successfully"


class EventModel(BaseModel):
    event_type: EventType
    data: dict
