# pip install requests
# https://fakeapi.net/

import requests
from pprint import pp


API_ENDPOINT = 'https://fakeapi.net/'
# PRODUCTS
products_ep = 'products/'
orders_ep = 'orders/'

def list_query(endpoint, **params):

    def check_params(param, val):
        allowed_params = {
            'page': int,
            'limit': int,
            'search': str,
            'searchFields': str,
            'sort': str,
            'order': str,
        }
        if param in allowed_params.keys() and type(val) == allowed_params[param]:
            return True
        return False
    
    def build_params(params):
        query = ''
        if params:
            query = '?'
            for prm, val in params.items():
                if check_params(prm, val):
                    query += f'{prm}={val}&'
            query = query[:-1]
        return query

    query = build_params(params)

    with requests.get(f'{API_ENDPOINT}{endpoint}{query if query else ""}') as response:

        if response.ok:
            data = response.json()
            return data.get('data')
        else:
            return {'error': response.status_code}
        
pp(list_query('/products', search='phone', searchFields='title'))


def item_query(endpoint, id):
    with requests.get(f'{API_ENDPOINT}{endpoint}{id}') as response:

        if response.ok:
            data = response.json()
            return data
        else:
            return {'error': response.status_code}


def not_delivered_orders():
    in_progress = filter(lambda ord: ord['status'] == 'processing', orders)
    return list(in_progress)

products = list_query(products_ep)
orders = list_query(orders_ep)

the_order = item_query(orders_ep, 1)



def collect_products(order_list):

    products_collection = []

    
    for ord in order_list:
        products_collection.append(*ord['products'])
    
    result = []
    for prod in products_collection:
        result += filter(lambda p: p['id'] == prod['productId'], products)
    return result


pp(list(map(lambda p: {'title': p['title'], 'price': p['price']}, collect_products(not_delivered_orders()))))