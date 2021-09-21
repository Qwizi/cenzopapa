import firebase_admin
from firebase_admin import credentials, firestore, storage

from app.core.config import settings

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'storageBucket': settings.FIREBASE_STORAGE_BUCKET})

db = firestore.client()
bucket = storage.bucket()