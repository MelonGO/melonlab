#!/usr/bin/env python
import os

from flask import Flask
from flask import render_template
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("mongo:27017")
db = client["wedding"]
collection = db["shops"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wedding')
def wedding():
    shops = collection.find()
    return render_template('wedding.html', shops=shops)

@app.route('/shops/<shopname>')
def shop(shopname):
    shop = collection.find_one({'name':shopname})
    if shop:
        reviews = shop['comments']
    return render_template('shop.html', reviews=reviews)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
