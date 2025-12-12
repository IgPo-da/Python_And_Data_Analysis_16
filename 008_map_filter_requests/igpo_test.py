# pip install requests
# https://fakeapi.net/
from pprint import pp
import requests


API = "https://fakeapi.net"

products_ep = '/products'

with requests.get(f'{API}{products_ep}') as response:
    print(response)
    data = response.json()

for product in data['data']: # time 28 minute of the 2-nd video
    print(f'{product['title']} - {product['description']}')