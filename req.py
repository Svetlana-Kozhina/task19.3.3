import json

import requests

# GET запрос
status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.json())

petId = 9223372036854775231

res1 = requests.get(f'https://petstore.swagger.io/v2/pet/{petId}', headers={'accept': 'application/json'})

print(res1.status_code)
print(res1.json())

# POST запрос

res2 = requests.post(f'https://petstore.swagger.io/v2/pet/{petId}', headers={'accept': 'application/json'}, data={'name': 'bound crocodilia new'})

print(res2.status_code)
print(res2.json())

# DELETE запрос

res3 = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}')

print(res3.status_code)
print(res3.json())

# PUT запрос

body = {'id': 9223372036854775231, 'category': {'id': 0, 'name': 'string'}, 'name': 'fish_new123', 'photoUrls': ['string'], 'tags': [{'id': 0, 'name': 'string'}], 'status': 'available'}

res4 = requests.put('https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(body))

print(res4.status_code)
print(res4.json())

