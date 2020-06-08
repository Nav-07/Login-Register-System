from flask import Flask, request, jsonify, redirect
import json
import os

# Create Flask Object
app = Flask(__name__)

# Create the Endpoints
@app.route('/')
def index():
    return 'Login Register System by Nav 2020'
# Run the App
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=50)
