#python

##import firebase packages
import firebase_admin
from firebase_admin import credentials
 
##connect python with firebase private service key.
cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred)
