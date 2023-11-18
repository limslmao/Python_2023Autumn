#python

##import firebase packages
import firebase_admin
from firebase_admin import credentials
# Import the Firebase service
from firebase_admin import auth


##connect python with firebase private service key. 
cred = credentials.Certificate("../../firebase_token.json")
firebase_admin.initialize_app(cred)

email = "test@gmail.com"
password = "2023autumn"
phone_number = "+886912345678"
user = auth.create_user(email=email, password=password, phone_number = phone_number)
print("User create successfully! {}".format(user.uid))
