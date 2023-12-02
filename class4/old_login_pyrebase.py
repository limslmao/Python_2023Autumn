import pyrebase

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

def login():
    print("Log in...")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print(login['localId'])
        print("Successfully logged in!")
    except:
        print("Invalid email or password!")

login()