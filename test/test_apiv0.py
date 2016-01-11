#!/usr/bin/env python

import unittest
from api.ordering.version0 import API

api = API()

class TestAPI(unittest.TestCase):

    def setUp(self):
       pass

    def test_api_info_type(self):
       self.assertIsInstance( api.api_info(), dict ) 

    def test_api_info_key_val(self):
        self.assertEqual( api.api_info().keys(), ['version_0'] )

    def test_get_available_products_type(self):
        product_id = 'LT50150401987120XXX02'
        self.assertIsInstance( api.available_products(product_id), dict )

    def test_get_available_products_key_val(self):
        product_id = 'LT50150401987120XXX02'
        self.assertEqual( api.available_products(product_id).keys()[0], "tm" )

class TestValidation(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()


