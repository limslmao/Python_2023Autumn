import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../firebase_token.json")
# Initiate firebase
firebase_admin.initialize_app(cred)
# Initiate firestore
db = firestore.client()


# Its your turn 2.2
path = "Autumn2023_Students"
collection_ref = db.collection(path)
docs = collection_ref.where('name','==','Jaclyn').get()
for doc in docs:
    print("The content of document is ：{}".format(doc.to_dict()))
