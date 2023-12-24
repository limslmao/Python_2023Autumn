import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred) # connecting to firebase
db = firestore.client()

def getProductInfo(product_id): # Use product id to differenciate which product's info we want to.
    # Get path to the product info
    collection_name = "Autumn2023_Class7_Products" 
    document_name = "product{}".format(product_id)
    doc_ref = db.collection(collection_name).document(document_name)

    # Get info from the path. Remember to use try/except to avoid failing.
    try:
        doc = doc_ref.get()
        doc_dict = doc.to_dict()
        print("The content of the document is：{}".format(doc_dict))
    except:
        print("The reference of document is not exist, please check the path is correct or not.")

    # Transfer product info dictionary to display string.
    display_text = "{}, {} {}/{}".format(doc_dict['category'], doc_dict['origin'], doc_dict['color'], doc_dict['material'])
    display_price = "NT.{}".format(doc_dict['price'])

    return display_text, display_price

getProductInfo("02")