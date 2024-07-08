#!/usr/bin/env python3
'''how to implement Basic Auth in a Flask API'''
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Dennis": generate_password_hash("Hello"),
    "Irene": generate_password_hash("Bye")
    }

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username),
                                                 password):
        return username


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % auth.current_user()})

if __name__ == '__main__':
    app.run()
