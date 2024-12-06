import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Ensure the path is correct and properly formatted
cred = credentials.Certificate("DOWNLOAD JSON FILE FROM FIREBASE AND COPY IT TO YOU LOCAL MACHINE THEN PASTE THE LOCATION HERE")
firebase_admin.initialize_app(cred, {'databaseURL': "//ADD YOUR FIREBASE DATABASE URL"})

ref = db.reference('Students')

data = {
   


    "231030308": {
        "Name": "Shivam Sharma",
        "faculty": "Vikas Baghel",
        "Subject": "Python Lab",
        "Standing": "G",
    },



    "231030229": {
        "Name": "Priyanshu Prajapati",
        "faculty": "Vikas Baghel",
        "Subject": "Python Lab",
        "Standing": "G",
    },

    "vikasbaghel": {
        "Name": "Viaks Baghel",
        "faculty": "Vikas Baghel",
        "Subject": "Python Lab",
        
    },
 
 

    
}

for key, value in data.items():
    ref.child(key).set(value)
