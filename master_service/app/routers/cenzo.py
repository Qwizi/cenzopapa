import random
from typing import List

from fastapi import APIRouter
from firebase_admin import firestore

from ..schemas.images import ImageDBModel, ImageDBOut
from ..services.main import FireStoreService
from ..utils.firebase import db

cenzo_router = APIRouter()


@cenzo_router.get("/", response_model=list[ImageDBOut])
def cenzo_last_10_images():
    firestore_service = FireStoreService(db)
    query = db.collection('images').order_by(u"id", direction=firestore.Query.DESCENDING).limit(10).stream()
    images = []
    for r in query:
        result = r.to_dict()
        image = ImageDBOut(url=result["public_url"])
        images.append(image)
    return images

@cenzo_router.get("/random", response_model=ImageDBOut)
def cenzo_random():
    firestore_service = FireStoreService(db)
    last_cenzo = firestore_service.get_last("images")
    random_id = random.randint(1, last_cenzo['id'])
    query = db.collection(u'images').where(u'id', u'==', random_id).limit(1).stream()
    image = None
    for r in query:
        result = r.to_dict()
        image = ImageDBOut(url=result["public_url"])
    return image
