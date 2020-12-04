import unittest
from datetime import datetime

from entities.price import Price


class TestPrice(unittest.TestCase):
    price = Price(49.01)

    def test_price_equals(self):
        self.assertEqual(self.price.price, 49.01,
                         'Price should be equals')
        self.assertNotEqual(self.price.price, 49,
                            'Price should not be equals')

    def test_price_type(self):
        self.assertEqual(type(self.price.price), float,
                         'Price should be float')

    def test_price_nan_type(self):
        self.price = Price(
            float('nan'), 'NAN should be float, I know i doesn`t make sense')

        self.assertEqual(type(self.price.price), float,
                         'Price should be float')

    def test_datetime_type(self):
        self.assertEqual(type(self.price.create_at), datetime,
                         'Date time should be datetime Type')
