import firebase_admin
from firebase_admin import credentials, firestore, storage

from core.config import settings

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'storageBucket': settings.FIREBASE_STORAGE_BUCKET})

db = firestore.client()
bucket = storage.bucket()

"""
blob = bucket.blob("2.jpg")
blob.upload_from_filename(filename='./temp/1.jpg')
blob.make_public()
"""
