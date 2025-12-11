from pprint import pp
import requests

# 200 - success
# 300 - success redirect
# 400 - error (client)
# 500 - error (server)

API = 'https://fakeapi.net'

products_ep = '/products'

# response = requests.get(f'{API}{products_ep}')
# # print(response.ok)
# # print(response.status_code)

# data = response.json()
# response.close()

products_search_ep = '/products?search=watch&searchFields=title,description'

single_product_ep = '/products/1'

def list_query(endpoint):

    with requests.get(f'{API}{endpoint}') as response:
        if response.ok:
            data = response.json()
            return data['data']
        else:
            return {'error': f'{response.status_code}'}


def single_item_query(endpoint, id):
    with requests.get(f'{API}{endpoint}/{id}') as response:
        if response.ok:
            data = response.json()
            return data
        else:
            return {'error': f'{response.status_code}'}

# pp(list_query('/orders'))
# pp(single_item_query('/products', 3))

orders = list_query('/orders')
products = list_query('/products')

processing = filter(lambda order: order['status'] == 'processing', orders)

products_list = []
for order in processing:
    products_list.append(order['products'][0]['productId'])
pp(products_list)

required = filter(lambda p: p['id'] in products_list, products)
pp(list(required))