import unittest
from datetime import datetime

from entities.shampoo import Shampoo
from entities.price import Price


class TestShampoo(unittest.TestCase):

    shampoo = Shampoo(
        name='Shampoo',
        brand='Seda',
        brand_line='Seda crespo',
        price=[Price(**{'price': 20.1})],
        vegan=False,
        size='200ML',
        utility='Hidratante',
        size_unit='Small',
        hair_type='Crespo',
        hair_shaft_condition='Ressecado',
        url='http://beleza.com.br',
        sku="1123",
    )

    def test_name_type(self):
        self.assertEqual(type(self.shampoo.name), str, "Should be Str")

    def test_brand_line_type(self):
        self.assertEqual(type(self.shampoo.brand_line), str, "Should be Str")

    def test_size_type(self):
        self.assertEqual(type(self.shampoo.size), str, "Should be Str")

    def test_vegan_type(self):
        self.assertEqual(type(self.shampoo.vegan), bool, "Should be bool")

    def test_utility_type(self):
        self.assertEqual(type(self.shampoo.utility), str, "Should be Str")

    def test_size_unit_type(self):
        self.assertEqual(type(self.shampoo.size_unit), str, "Should be Str")

    def test_hair_type_type(self):
        self.assertEqual(type(self.shampoo.hair_type), str, "Should be Str")

    def test_hair_shaft_condition_type(self):
        self.assertEqual(
            type(self.shampoo.hair_shaft_condition), str, "Should be Str")

    def test_url_type(self):
        self.assertEqual(type(self.shampoo.url), str, "Should be Str")

    def test_sku_type(self):
        self.assertEqual(type(self.shampoo.sku), str, "Should be Str")

    def test_price_type(self):
        self.assertEqual(type(self.shampoo.price), list, "Should be list")

    def test_datetime(self):
        self.assertEqual(type(self.shampoo.create_at), datetime,
                         'Should be datetime Type')
