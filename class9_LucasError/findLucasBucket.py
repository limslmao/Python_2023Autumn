# 最後發現Lucas的資料夾有一個隱藏檔案
# 這個隱藏檔案會直接讓操作失誤
# 解方是直接砍掉整個資料夾，重新upload所有檔案
# 懷疑是.DS.Store這個檔案

import pyrebase
import os

dir_name = "nature"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

config = {
  "apiKey": "AIzaSyAAtnfE9hLYnjttc6lMpas_4pyNIVPwDck",
  "authDomain": "yayay-e2c6c.firebaseapp.com",
  "projectId": "yayay-e2c6c",
  "storageBucket": "yayay-e2c6c.appspot.com",
  "messagingSenderId": "967513318932",
  "appId": "1:967513318932:web:0c32f47abe59c93deee901",
  "databaseURL": "",
  "serviceAccount":"yayay-e2c6c-firebase-adminsdk-1gbl4-204c585238.json"
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