from flask import Flask, request
from uuid import uuid1,uuid4
import os,json,pytz
from datetime import date,datetime

db = {}
db_filename = "db.json"

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
            "password": password,
            "username": username,
            "purchases": {}
        }

        emailList =[]
        for email in db["users"]:
            emailList.append(email["email"])
        # print(emailList)  

        if len(db["users"]) == 0 or userDict["email"] not in emailList:
            db["users"].append(userDict)
            with open(db_filename,"r+") as f:
                f.seek(0)
                json.dump(db,f,indent=4)
                
            return "User added successfully"
        else:
            return "User already exists"    
    return "Error: Trying to access endpoint with wrong method"    

# User login
@app.route('/login',methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    userIndex = None
    for user in db["users"]:
        if user["email"] == email and user["password"] == password:
            userIndex = db["users"].index(user)

            response = {
                "message" : "Logged in successfully",
                "user_index": userIndex
            }
            return response
        else:
            continue
    return "Wrong email or password!"           

# Add purchase
@app.route('/add_purchase',methods=['POST'])
def add_purchase():
    if request.method == 'POST':
        user_index = int(request.form["user_index"])
        item_name = request.form["item_name"]
        item_type = request.form["item_type"]
        item_price = request.form["item_price"]

        curr_date = str(date.today())
        curr_time = str(datetime.now(pytz.timezone("Asia/Kolkata")))

        itemDict = {
            "item_name":item_name,
            "item_type":item_type,
            "item_price":item_price,
            "purchase_time":curr_time
        }

        existing_dates = list(db["users"][user_index]["purchases"].keys())
        if len(db["users"][user_index]["purchases"]) == 0 or curr_date not in existing_dates:
            # if there are no purchases user has done for the day
            db["users"][user_index]["purchases"][curr_date] = []
            db["users"][user_index]["purchases"][curr_date].append(itemDict)
            with open(db_filename,"r+") as f:
                f.seek(0)
                json.dump(db,f,indent=4)
            return "Item added successfully"
        else:
            db["users"][user_index]["purchases"][curr_date].append(itemDict)
            with open(db_filename,"r+") as f:
                f.seek(0)
                json.dump(db,f,indent=4)
            return "Item added successfully"
        return "Some error occured"
        
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)