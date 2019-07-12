#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
    product_count = len(products)
    unique_product_names = len(set([p.name for p in products]))
    mean_price = sum([p.price for p in products])/product_count
    mean_flammability = sum([p.flammability for p in products])/product_count
    mean_weight = sum([p.weight for p in products])/product_count
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {unique_product_names}')
    print(f'Average price: {mean_price}')
    print(f'Average weight: {mean_weight}')
    print(f'Average flammability: {mean_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())
