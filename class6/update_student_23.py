import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../firebase_token.json")
# Initiate firebase
firebase_admin.initialize_app(cred)
# Initiate firestore
db = firestore.client()


# Its your turn 2.3
path = "Autumn2023_Students/student02"
doc_ref = db.document(path)
doc = {
    'email': 'niceday@gmail.com'
}
doc_ref.update(doc)