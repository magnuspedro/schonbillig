import unittest

from unittest.mock import patch
from src.entities.conditioner import Conditioner
from src.gateway.providers.beleza_na_web.converter.get_conditioner_beleza_conevert import \
    GetConditionerBelezaConverter
import requests


class TestConditionerConverter(unittest.TestCase):

    @patch('requests.get')
    def mock_request(self, mock_get):
        with open(
            'tests/fixtures/html/beleza.html',
                'r') as f:

            mock_get.return_value.text = f.read()
            mock_get.return_value.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-conditioner-50ml/'
            return requests.get()

    def test_converter(self):

        product = GetConditionerBelezaConverter().to_entity(self.mock_request())
        self.assertEqual(type(product), Conditioner,
                         'Converter is conditioner type')
        self.assertIsNotNone(product.name)
        self.assertIsNotNone(product.brand)
        self.assertIsNotNone(product.brand_line)
        self.assertIsNotNone(product.price)
        self.assertIsNotNone(product.price[0].price)
        self.assertIsNotNone(product.price[0].create_at)
        self.assertIsNotNone(product.vegan)
        self.assertIsNotNone(product.size)
        self.assertIsNotNone(product.utility)
        self.assertIsNotNone(product.size_unit)
        self.assertIsNotNone(product.hair_type)
        self.assertIsNotNone(product.hair_shaft_condition)
        self.assertIsNotNone(product.url)
        self.assertIsNotNone(product.code)
        self.assertIsNotNone(product.create_at)