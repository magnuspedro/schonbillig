import unittest
from gateway.providers.beleza_na_web.converter.get_shampoo_converter \
    import GetShampooConverter
from entities.shampoo import Shampoo


class TestShampooConverter(unittest.TestCase):

    def test_converter(self):
        with open('tests/gateway/providers/beleza_na_web/converter/beleza.html', 'r') as f:
            html = f.read()

            product = GetShampooConverter().to_entity(html)

            self.assertEqual(type(product), Shampoo)

# TODO : finish test
