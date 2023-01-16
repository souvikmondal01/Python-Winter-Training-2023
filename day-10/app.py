from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    print("I am in the /hello endpoint")
    return "hello"

users = [
    {
        "user_id": 1,
        "username": "user1"
    },
    {
        "user_id": 2,
        "username": "user2"
    }
]

# create an endpoint to featch all the user ids
@app.route('/fetch_user_id')
def fetchUserId():
    user_id = {"ids":[]}
    for user in users:
        user_id["ids"].append(user["user_id"])
    return user_id

# create an endpoint to featch all the username
@app.route('/fetch_user_name')
def fetchUserName():
    user_name = {"username":[]}
    for user in users:
        user_name["username"].append(user["username"])
    return user_name

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
