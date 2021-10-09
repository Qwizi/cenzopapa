from datetime import datetime
from uuid import UUID

import databases
import ormar
import sqlalchemy

from .config import get_settings

database = databases.Database(
    f"postgresql://{get_settings().DATABASE_USER}:{get_settings().DATABASE_PASS}@{get_settings().DATABASE_HOST}/{get_settings().DATABASE_DB}")
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


class Image(ormar.Model):
    class Meta(BaseMeta):
        tablename = "images"

    id: int = ormar.Integer(primary_key=True)
    filename: UUID = ormar.UUID(nullable=True)
    extension: str = ormar.String(max_length=255, nullable=True)
    remote_image_url: str = ormar.String(max_length=255, nullable=True)
    public_url: str = ormar.String(max_length=255, nullable=True)
    created_at: datetime = ormar.DateTime(default=datetime.now)


engine = sqlalchemy.create_engine(
    f"postgresql://{get_settings().DATABASE_USER}:{get_settings().DATABASE_PASS}@{get_settings().DATABASE_HOST}/{get_settings().DATABASE_DB}")
metadata.create_all(engine)
