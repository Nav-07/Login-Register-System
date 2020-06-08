from flask import Flask, request, jsonify, redirect
import json
import os
from User import User

# Create Flask Object
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

users_list = []

# Create the Endpoints
@app.route('/')
def index():
    return 'Login Register System by Nav 2020'

@app.route('/user', methods=['POST'])
def user():
    name = request.json['name']
    mail = request.json['mail']
    password = request.json['password']

    if (mail != '' and name != '' and password != '') :
        new_user = User(name, mail, password)
        users_list.append(new_user)

        return jsonify(new_user.json()), 201
    else:
        return jsonify({'message': 'Supplied Credentials had Missing Values.'}), 400

# Run the App
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=50)
