from flask import Flask, request, jsonify, redirect
import json
import os
from User import User
from Mail import Mail
from SMS import SMS
from functools import wraps

import jwt
import datetime

# Create Flask Object
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = os.environ['SECRET_KEY']

users_list = []

# JWT 
def jwt_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        # Missing Token
        if not token:
            return jsonify({'message': 'Missing Token'}), 400
        
        try:
            data = jwt.decode(token, os.environ['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid Token Supplied'}), 400

        return func(*args, **kwargs)

    return decorated

# Create the Endpoints
@app.route('/')
def index():
    return 'Login Register System by Nav 2020'

@app.route('/user', methods=['POST'])
def user():
    name = request.json['name']
    phone = request.json['phone']
    mail = request.json['mail']
    password = request.json['password']

    if (mail != '' and name != '' and password != '') :
        new_user = User(name, phone, mail, password)
        users_list.append(new_user)

        return jsonify(new_user.json()), 201
    else:
        return jsonify({'message': 'Supplied Credentials had Missing Values.'}), 400

@app.route('/login')
def login():
    auth = request.authorization
    if not auth:
        return jsonify({'message': 'Authotization Not Provided!'}), 400
    else:
        username = auth.username
        password = auth.password

        for user in users_list:
            if username == user.name and password == user.password:
                token = jwt.encode({'name': user.name, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=15)}, os.environ['SECRET_KEY'])

                mail = Mail(user.mail, 'Login', 'http://0.0.0.0:50/user-login?token={}'.format(token.decode('utf-8')))
                mail.send()
                sms = SMS(user.phone, 'Someone Logged into your account')
                sms.send()
                return jsonify({'token': token.decode('utf-8')}), 200
            else:
                return jsonify({'message': 'Username or Password is Invalid'}), 400
        return jsonify({'message': 'Username or Password is Invalid'}), 400      

@app.route('/user-login')
@jwt_required
def user_login():
    return jsonify({
        'message': 'System is Completed'
    }), 200

# Run the App
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=50)
