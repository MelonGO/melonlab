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
    shops_list = []
    for item in shops:
        tmp = int(item['total'])
        item['total'] = tmp
        shops_list.append(item)
    shops_list.sort(key=lambda x: (x['total']), reverse=True)
    return render_template('wedding.html', shops=shops_list)

@app.route('/shop/<shopname>')
def shop(shopname):
    shop = collection.find_one({'name':shopname})
    if shop:
        reviews = shop['comments']
    return render_template('shop.html', reviews=reviews)

@app.route('/vpn')
def vpn():
    return render_template('vpn.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
