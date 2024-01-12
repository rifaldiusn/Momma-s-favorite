from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/login", methods=["POST"]) #127.0.0.1:5000/user
def user_login():
    user_id = request.get_json()
    if user_id.get("istri") and user_id.get("istri") == 1: #di postman ditulis {"istri":1}
        name = "Xrene"
        gender = "female"
        age = 54
    elif  user_id.get("suami") and user_id.get("suami") == 2: #di postman ditulis {"suami":2}
        name = "Max"
        gender = "male"
        age = 60
    elif user_id.get("anak-1") and user_id.get("anak-1") == 3: #di postman ditulis {"anak-1":3}
        name = "Avgene Maxrene"
        gender = "male"
        age = 26
    elif user_id.get("anak-2") and user_id.get("anak-2") == 4: #di postman ditulis {"anak-2":4}
        name = "Cullilan Maxrene"
        gender = "male"
        age = 28
    else :
        name = None
        gender = None
        age = None
    
    data = {
        "name": name,
        "gender" : gender,
        "age" : age} 

    return jsonify (data), 201

if __name__ == "__main__":
    app.run(debug=True)