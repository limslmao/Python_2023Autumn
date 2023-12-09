import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../firebase_token.json")
# Initiate firebase
firebase_admin.initialize_app(cred)
# Initiate firestore
db = firestore.client()


# Its your turn 2.1
doc = {
    'name':'Jaclyn', 
    'email':'jaclyn@gmail.com'
}
doc_ref = db.collection("Autumn2023_Students").document("student02")
doc_ref.set(doc)
