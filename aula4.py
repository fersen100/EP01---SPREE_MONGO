import requests
import json

session = requests.Session()

r = session.post('http://localhost:3000/api/v1/products?token=e0c91507ca69781a03c62aabd83246ed75e8ed0f498a4652')
print(r.text)

r = session.get('http://localhost:3000/api/v1/products?token=e0c91507ca69781a03c62aabd83246ed75e8ed0f498a4652')

produtos = r.json()
print(json.dumps(produtos, indent=2))

posicoes = r.json()
print(json.dumps(posicoes, indent=2))