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
    return render_template('wedding.html')

@app.route('/wedding/analysis')
def weddingAnalysis():
    return render_template('weddingAnalysis.html')

@app.route('/wedding/data')
def weddingData():
    shops = collection.find()
    shops_list = []
    for item in shops:
        tmp = int(item['total'])
        item['total'] = tmp
        shops_list.append(item)
    shops_list.sort(key=lambda x: (x['total']), reverse=True)
    return render_template('weddingData.html', shops=shops_list)

@app.route('/wedding/shop/<shopname>')
def shop(shopname):
    shop = collection.find_one({'name':shopname})
    if shop:
        reviews = shop['comments']
    return render_template('shop.html', reviews=reviews)

@app.route('/vpn')
def vpn():
    return render_template('vpn.html')

@app.route('/proxy')
def proxy():
    return render_template('proxy.html')

@app.route('/cicd')
def cicd():
    return render_template('cicd.html')

@app.route('/imgrating')
def imgrating():
    return render_template('imgrating.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
