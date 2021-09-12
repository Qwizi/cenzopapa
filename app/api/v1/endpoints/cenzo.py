import datetime
import random

from fastapi import APIRouter, Response
from firebase_admin import firestore
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List, Optional

from scrapp.site import get_last_image
from firebase.firebase import db

router = APIRouter()


class Image(BaseModel):
    image_url: str
    created_at: datetime.datetime


@router.get("/cenzo/", response_model=list[Image], response_model_exclude_none=True)
def last_cenzo_images():
    query = db.collection('images').order_by(u"id", direction=firestore.Query.DESCENDING).limit(10)
    results = query.stream()
    images = []

    for r in results:
        result = r.to_dict()
        image = Image(image_url=result['local_image_url'], created_at=result['created_at'])
        images.append(image)

    return images


@router.get('/cenzo/random', response_model=Image, response_model_exclude_none=True)
def random_cenzo_image():
    last_image_id = get_last_image()['id']
    random_id = random.randint(1, last_image_id)
    query = db.collection(u'images').where(u'id', u'==', random_id).limit(1).stream()
    image = None
    for r in query:
        result = r.to_dict()
        image = Image(image_url=result['local_image_url'], created_at=result['created_at'])
    return image
