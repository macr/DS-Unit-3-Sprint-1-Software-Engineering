#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, inventory_report, ADJECTIVES, NOUNS
from unittest.mock import patch


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_explode(self):
        """test Product.explode results"""
        prod1 = Product('Product fizzle', flammability=2, weight=3)
        prod2 = Product('Product boom!', flammability=5, weight=4)
        prod3 = Product('Product BABOOM!', flammability=7, weight=8)
        self.assertEqual(prod1.explode(), '...fizzle.')
        self.assertEqual(prod2.explode(), '...boom!')
        self.assertEqual(prod3.explode(), '...BABOOM!!')

    def test_product_stealability(self):
        """test Product.stealability results"""
        prod1 = Product('Not so', price=5, weight=15)
        prod2 = Product('Kinda', price=5, weight=10)
        prod3 = Product('Very', price=100, weight=8)
        self.assertEqual(prod1.stealability(), 'Not so stealable...')
        self.assertEqual(prod2.stealability(), 'Kinda stealable.')
        self.assertEqual(prod3.stealability(), 'Very stealable!')


class AcmeReportTests(unittest.TestCase):
    """Make sure ACME reports are correct"""
    def setUp(self):
        self.products = generate_products()

    def test_default_num_products(self):
        self.assertEqual(len(self.products), 30)

    def test_legal_names(self):
        products = generate_products()
        for product in products:
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

    # mock print function so we can check args passed to print
    @patch('acme_report.print')
    def test_report_results(self, mock_print):
        # to keep the test output clean
        mock_print.return_value = ''
        products = generate_products()
        # calculate results to check agains printed
        product_count = len(products)
        unique_product_names = len(set([p.name for p in products]))
        mean_price = sum([p.price for p in products])/product_count
        mean_flammability = sum(
            [p.flammability for p in products])/product_count
        mean_weight = sum([p.weight for p in products])/product_count
        inventory_report(products)

        # add print parameters to a list
        args = [arg[0][0] for arg in mock_print.call_args_list]

        # Check that we pass the calculated values above to `print`
        # Check each line if it contains the value we are checking for and
        # a matching keyword to make sure it is on the same line.
        price_match = [(str(mean_price) in arg and 'price' in arg.lower())
                       for arg in args]
        unique_names = [
            (str(unique_product_names) in arg and 'unique' in arg.lower()) for arg in args]
        flammability_match = [
            (str(mean_flammability) in arg and 'flammability' in arg.lower()) for arg in args]
        weight_match = [
            (str(mean_weight) in arg and 'weight' in arg.lower()) for arg in args]
        self.assertTrue(any(price_match))
        self.assertTrue(any(unique_names))
        self.assertTrue(any(flammability_match))
        self.assertTrue(any(weight_match))


if __name__ == '__main__':
    unittest.main()
