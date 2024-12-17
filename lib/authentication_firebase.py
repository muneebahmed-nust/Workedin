import firebase_admin
from firebase_admin import credentials,auth,firestore
import firebase_admin.auth
import firebase

cred = credentials.Certificate("D:/ICT/Workedin/CODE/workedin-d5a9f-firebase-adminsdk-zvjk7-5621df463f.json")
firebase_admin.initialize_app(cred)

firebase_database=firebase_admin.firestore.client()

# dict=firebase_database.collection("user").document("user").get().to_dict()
# dict['new']=14523

# firebase_database.collection("user").document("user").set(dict)