import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred)
