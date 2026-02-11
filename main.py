import requests as rq
import json
import csv


def fields_extractor(product):
    """ Extract only useful fields """
    edited_product = {}
    for key, val in product.items():
        if key in ['id', 'title', 'category', 'price', 'rating', 'availabilityStatus']:
            if key == 'availabilityStatus':
                if val == 'In Stock':
                    edited_product['inStock'] = True
                else:
                    edited_product['inStock'] = False
            elif key == 'title':
                edited_product['name'] = val
            else:
                edited_product[key] = val
    return edited_product

def sort_price(products, rev = False):
    """ Sort products based on price """
    return sorted(products, key= lambda p : p['price'], reverse=rev)

def sort_rating(products, rev = False):
    """ Sort products based on rating """
    return sorted(products, key= lambda p : p['rating'], reverse=rev)

def filter_in_stock(products):
    """ Return only available products in stock """
    in_stock_products = list(filter(lambda p : p['inStock'], products))
    return in_stock_products

def top_expensive(products, n = 5):
    """ Return top n expensive products """
    return sort_price(products, rev = True)[:n]


res = rq.get('https://dummyjson.com/products?limit=0')
res.raise_for_status()
parsed_res = res.json()
products = parsed_res['products']

edited_products = []
keys = []
new_products = []

for product in products:
    new_product = fields_extractor(product)
    edited_products.append(new_product)

for key in edited_products[0]:
    keys.append(key)

opt1 = input('Choose operation:\n'+
            '1- Sort by price.\n'+
            '2- Sort by rating.\n'+
            '3- Filter in-stock.\n'+
            '4- Top N expensive.\n'+
            '0- None.\n')
if opt1 == '1':
    opt2 = input('Sort by price:\n'+
                 '1- Ascendingly.\n'+
                 '2- Descendingly.\n')
    if opt2 == '1':
        new_products = sort_price(edited_products)
    elif opt2 == '2':
        new_products = sort_price(edited_products, True)
    else:
        print('Invalid input!')
elif opt1 == '2':
    opt2 = input('Sort by rating:\n'+
                 '1- Ascendingly.\n'+
                 '2- Descendingly.\n')
    if opt2 == '1':
        new_products = sort_rating(edited_products)
    elif opt2 == '2':
        new_products = sort_rating(edited_products, True)
    else:
        print('Invalid input!')
elif opt1 == '3':
    new_products = filter_in_stock(edited_products)
elif opt1 == '4':
    try:
        opt2 = int(input('Enter value of N: '))
    except ValueError:
        print('Invalid input!')
    else:
        new_products = top_expensive(edited_products, opt2)
elif opt1 == '0':
    new_products = edited_products
else:
    print('Invalid input!')

if new_products:
    with open('products.json', 'w') as f_obj:
        json.dump(new_products, f_obj, indent=4)

    with open('products.csv', 'w') as f_obj:
        writer = csv.DictWriter(f_obj, fieldnames=keys)
        writer.writeheader()
        writer.writerows(new_products)

    with open('products.txt', 'w') as f_obj:
        f_obj.write('\n'.join(str(p) for p in new_products)) 