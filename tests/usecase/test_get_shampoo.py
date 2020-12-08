import unittest

from unittest.mock import patch, Mock
from usecase.get_shampoo import GetShampoo


class TestGetShampoo(unittest.TestCase):

    @patch('usecase.get_shampoo.ProviderSelector.parse')
    def test_get_shampoo_fail(self, mock_get):
        mock_get.return_value = [None]
        shampoo = GetShampoo().execute()
        self.assertIsNone(shampoo)

    @patch('usecase.get_shampoo.ProviderSelector.parse')
    def test_get_shampoo(self, mock_get):

        with open('tests/fixtures/html/beleza.html') as file:
            html = file.read()
        mock_request = Mock()
        mock_request.ok = True
        mock_request.status_code = 200
        mock_request.url = 'www.belezanaweb.com.br'
        mock_request.content = str(html)
        mock_request.text = str(html)

        mock_get.return_value = [mock_request]

        shampoo = GetShampoo().execute()
        self.assertIsNone(shampoo)
