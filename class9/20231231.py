import firebase_admin
from firebase_admin import credentials, storage
cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'fir-test-492e5.appspot.com'}) # connecting to firebase

## Its your turn 1.1
# file_path = "sea.webp"
# bucket = storage.bucket()
# blob = bucket.blob(file_path)
# blob.upload_from_filename(file_path)

## Its your turn 1.2
# bucket = storage.bucket() # storage bucket
# def upload_blob(bucket, source_file_name, destination_blob_name):
#     blob = bucket.blob(destination_blob_name)
#     blob.upload_from_filename(source_file_name)
#     print(f"File {source_file_name} uploaded to {destination_blob_name}.")
# upload_blob(bucket, 'sea.webp', 'nature/beautiful_sea.webp') 

## Its your turn 1.3
# import os

# dir_path = "./taipei"
# filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg")]
# print(filelist) # 先run確定有抓到檔案

# bucket = storage.bucket()
# for file in filelist:
#     file_path = dir_path+"/"+file
#     blob_path = "photo/"+file
#     print("Now is uploading file {}.".format(file_path))
#     blob = bucket.blob(blob_path)
#     blob.upload_from_filename(file_path)

## Its your turn 1.4
bucket = storage.bucket()
blob = bucket.blob("nature/beautiful_sea.webp")
blob.download_to_filename('my_love.webp')





