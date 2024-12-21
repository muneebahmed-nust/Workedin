import firebase_admin
from firebase_admin import credentials,auth,firestore
import firebase_admin.auth
import firebase

cred = credentials.Certificate("D:/ICT/Workedin/CODE/workedin-d5a9f-firebase-adminsdk-zvjk7-5621df463f.json")
firebase_admin.initialize_app(cred)

firebase_database=firebase_admin.firestore.client()

# dict=firebase_database.collection("user").document("user").get().to_dict()
# dict['new']=14523
# firebase_database.collection("city2").document("cname").collection("addresses").document("gfdg").set({
#   "street": "123 Main St",
#   "city": "Anytown",
#   "state": "CA",
#   "zip": "12345"
# });

# docs=firebase_database.collection("City wise Labour data").document("Karachi").collection("Electrician").get()
# # Print each document's data
# print(docs)
# print(type(docs))
# for doc in docs:
#     data = doc.to_dict()
#     print(data)
#     print(type(data))

docs = firebase_database.collection("City wise Labour data").document("Karachi").collection("Electrician").get()

for doc in docs:
    doc_id = doc.id  # Get document identifier
    data = doc.to_dict()  # Get document data
    data["email"] = doc.id
    print(data)
    print("-" * 50) 