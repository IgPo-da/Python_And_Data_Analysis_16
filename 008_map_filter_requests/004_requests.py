# pip install requests
# https://fakeapi.net/

import requests
from pprint import pp


# PRODUCTS
get_all_products_ep = 'products'
products_search_ep = 'products?search=blender&searchFields=title'
products_sort_ep = 'products?sort=price&order=desc'  # order - desc/asc
get_one_product_ep = 'products/12'  # Where 12 is an id of a product

# ORDERS
orders_ep = 'orders'
one_order_ep = 'orders/1'

# ERRORS
error_ep = 'math'

def data_query(api_endpoint, id=0):
    # Create connection and get the response
    # Endpoint accepts:
    #       'api_endpoint' - URL to a fakeapi.net endpoint
    #       'id' - optional (for single queries)
    with requests.get(f'https://fakeapi.net/{api_endpoint}{f"/{str(id)}" if id else ""}') as res:
        # res.ok - returns boolean for statuses 200 and 300
        if res.ok:
            # convert response to dictionary
            data = res.json()
            # check what type is returned (there's 'data' key for lists)
            if data.get('data'):
                return data.get('data')
            else:
                return data
        else:
            return {'error': f'Failed to connect: {res.status_code}'}


products = data_query(get_all_products_ep)
orders = data_query(orders_ep)

order = data_query(orders_ep, 2)
prod = data_query(get_all_products_ep, 1)


def cart_builder(order):
    pp(order)
    product_list = order.get('products')
    pp(f'PROD_LIST:{product_list}')
    cart = []
    for product in product_list:
        cart += list(filter(lambda p: p['id'] == product['productId'], products)) * product['quantity']
    return cart


def count_cart(cart):
    total_price = 0
    for p in cart:
        total_price += p.get('price')
    return total_price


order1_cart = cart_builder(order)
pp(count_cart(order1_cart))


# # pp(data_query(error_ep))



# def builder(product_list):
#     products = data_query(get_all_products_ep)
#     result = []
#     for product_data in product_list:
#         result += filter(lambda product: product['id'] == product_data['productId'], products)
#     return result

# pp(builder(order['products']))
