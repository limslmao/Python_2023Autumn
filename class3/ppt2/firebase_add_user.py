#python

##import firebase packages
import firebase_admin
from firebase_admin import credentials
# Import the Firebase service
from firebase_admin import auth

##connect python with firebase private service key.
cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred)

email = "python_autumn_2023@gmail.com"
password = "123456"
user = auth.create_user(email=email, password=password)
print("User create successfully! {}".format(user.uid))
