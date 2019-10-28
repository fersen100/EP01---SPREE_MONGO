import requests
import json
import os
from datetime import datetime
from pymongo  import MongoClient
from flask    import request

cliente             = MongoClient('localhost:27017')
banco               = cliente['config']
posicoes_collection = banco['spree_collection']

session = requests.Session()

url = "http://localhost:3000/api/v1/products?token=e0c91507ca69781a03c62aabd83246ed75e8ed0f498a4652"

r = session.get(url)

posicoes = r.json()

x= json.loads(r.text)

for k in x["products"]:
    item_doc = {
        'id': k['id'],
        'name': k['name'],
        'price': k['price'],
        'data': datetime.utcnow()
    }

posicoes_collection.insert_one(item_doc)

