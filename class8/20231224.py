import firebase_admin
from firebase_admin import credentials, storage
cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'fir-test-492e5.appspot.com'}) # connecting to firebase

file_path = "Firebase_project/image/bed1.jpg"
bucket = storage.bucket() # storage bucket
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)
