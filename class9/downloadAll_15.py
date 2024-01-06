import pyrebase
import os

config = {
    "apiKey": "AIzaSyBTjmE7P6drIjs3D4fqthZtRKBxqKMWfU0",
    "authDomain": "fir-test-492e5.firebaseapp.com",
    "projectId": "fir-test-492e5",
    "storageBucket": "fir-test-492e5.appspot.com",
    "messagingSenderId": "596036791015",
    "appId": "1:596036791015:web:b5d06e757cb7771ccb1042",
    "databaseURL" : "" ,
    "serviceAccount":"../firebase_token.json" ## authenticate with Firebase as an admin and disregard any security rules. from https://github.com/thisbejim/Pyrebase
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

## Its your turn 1.5
dir_name = "nature"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
storage = firebase.storage()
all_files = storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name): # Only need the file starts with directory we want.
        file.download_to_filename(file.name)