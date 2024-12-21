import firebase_admin
from firebase_admin import credentials,auth,firestore
import firebase_admin.auth
import firebase

cred = credentials.Certificate("D:/ICT/Workedin/CODE/workedin-d5a9f-firebase-adminsdk-zvjk7-5621df463f.json")
firebase_admin.initialize_app(cred)

firebase_database=firebase_admin.firestore.client()

# dict=firebase_database.collection("Employer").document("123").get().to_dict()
# dict["already"]=[1,2,3]
# firebase_database.collection("Employer").document("123").set(dict)
# print(dict)



# firebase_database.collection("City wise Job data").document("Karachi").collection().document(user_name).set(
#         {
#             "description":job_description
#         }
#         )
# doc_ref = firebase_database.collection("City wise Job data").document("Karachi").collection("jobs").document()
# firebase_database.collection("sdfsd").document("Karachi").set(
#         {
#             "description":"sdfsd",
#             "job_id":"sdfsd"
#         }
#         )

# # Get the auto-generated ID
# unique_id = doc_ref.id
# print(unique_id)
# # Set the document data
# doc_ref.set({
#     "description": "job_description",
#     "job_id": "unique_id"  # Store ID in document itself
# })
# docs=firebase_database.collection("City wise Labour data").document("Karachi").collection("Electrician").get()
# # Print each document's data
# print(docs)
# print(type(docs))
# for doc in docs:
#     data = doc.to_dict()
#     print(data)
#     print(type(data))

# docs=firebase_database.collection("City wise Job data").document("Karachi").collection("Carpenter").get()

# for doc in docs:
#   print(doc)  # Get document identifier
#   data = doc.to_dict()  # Get
#   print(data)
# docs = firebase_database.collection("City wise Tradesperson data").document("Karachi").collection("Electrician").get()

# for doc in docs:
#     doc_id = doc.id  # Get document identifier
#     data = doc.to_dict()  # Get document data
#     data["email"] = doc.id
#     print(data)
#     print("-" * 50) 