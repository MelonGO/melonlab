#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient

# MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
# MONGO_DB_NAME = 'flaskdb'
# MONGO_COLLECTION_NAME = 'wedding'

# client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
# db = client['flaskdb']
# db.authenticate(name="melon", password="melon666")
# collection = db['wedding']

app = Flask(__name__)

client = MongoClient("mongo:27017")

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"

@app.route('/write')
def write():
    db = client['school']
    collection = db.students
    student = {
        "id": "1234",
        "name": "sky",
        "gender": "male",
    }
    result = collection.insert_one(student)
    return 'Write : ' + str(result)

@app.route('/read')
def read():
    db = client['wedding']
    collection = db.wedding
    
    students = collection.find()
    result = ''
    for s in students:
        result = s['name']
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
