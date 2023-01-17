from flask import Flask, request
from uuid import uuid1,uuid4
import os,json,pytz
from datetime import date,datetime

db = {}
db_filename = "D:\\Python_Winter_Training_2023\\day-11\\expense_tracker\\db.json"

# Check whether db.json exists in the directory or not
if os.path.exists(db_filename):
    print("db exists")
    with open(db_filename,'r') as f:
        db = json.load(f)
else:
    print("db does not exists")
    accessKey = str(uuid1())
    secretKey = str(uuid4())

    item_type = ["Food","Beverages","Clothing","Stationaries","Wearables","Electronics Accessories"]

    db = {
        "accessKey": accessKey,
        "secretKey": secretKey,
        "item_type": item_type,
        "users":[]
    }
    with open(db_filename,"w+") as f:
        json.dump(db,f,indent=4)

app = Flask(__name__)

# User sign up
@app.route('/signup',methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        userDict = {
            "name": name,
            "email": email,
            "pawword": password,
            "username": username,
            "purchases": {}
        }

        if len(db["users"]) == 0 or userDict not in db["users"]:
            db["users"].append(userDict)
            with open(db_filename,"r+") as f:
                f.seek(0)
                json.dump(db,f,indent=4)
                
            return "User added successfully"
        else:
            return "User already exists"    
    return "Error: Trying to access endpoint with wrong method"    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)