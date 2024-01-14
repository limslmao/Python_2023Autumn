import pyrebase
import os
dir_name = "project_images"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
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

# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
storage = firebase.storage()
# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
storage = firebase.storage()
all_files = storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name): # Only need the file starts with directory we want.
        print("Now is downloading file {}.".format(file.name))
        file.download_to_filename(file.name)


# import firebase
import firebase_admin
from firebase_admin import credentials, storage
import os
# import secret key
cred = credentials.Certificate("./yayay-e2c6c-firebase-adminsdk-1gbl4-204c585238.json")


#---
# initiate firebase
firebase_admin.initialize_app(cred, {"storageBucket" : "yayay-e2c6c.appspot.com"})
bucket = storage.bucket()
def upload_blob(bucket, source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File{source_file_name} up load to {destination_blob_name}")
#upload_blob(bucket, "下載 (7).jpg", "Taipei-101/101-3.png")
#---
# dir_path = "./taipei"
# filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg")]
# print(filelist)
# #---
# bucket = storage.bucket()
# for file in filelist:
#     file_path = dir_path+"/"+file
#     blob_path = "Taipei-101/"+file
#     print("Now is uploading file {}." .format(file_path))
#     blob = bucket.blob(blob_path)
#     blob.upload_from_filename(file_path)
#---
bucket = storage.bucket()
blob = bucket.blob("nature/beautiful_sea.png")
blob.download_to_filename("my_love.png")