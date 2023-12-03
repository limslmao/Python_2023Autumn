import pyrebase
from tkinter import *

# // Your web app's Firebase configuration
config = {
    "apiKey": "AIzaSyBTjmE7P6drIjs3D4fqthZtRKBxqKMWfU0",
    "authDomain": "fir-test-492e5.firebaseapp.com",
    "projectId": "fir-test-492e5",
    "storageBucket": "fir-test-492e5.appspot.com",
    "messagingSenderId": "596036791015",
    "appId": "1:596036791015:web:b5d06e757cb7771ccb1042",
    "databaseURL" : "" #記得手動新增
    }

# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()