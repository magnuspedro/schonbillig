import unittest
from unittest.mock import patch

from gateway.providers.beleza_na_web.beleza_na_web_request_itens \
    import BelezaNaWebRequestItens


class TestBelezaNaWebRequestItens(unittest.TestCase):

    @patch(
        'gateway.providers.beleza_na_web.beleza_na_web_request_itens.BelezaNaWebRequestItens.request_itens')
    def create_request(self, mock_get):
        with open('tests/fixtures/html/beleza_list.html', 'r') as f:
            content = f.read()
            mock_get.return_value.text = content
            mock_get.return_value.content = content
            mock_get.return_value.ok = True
            return BelezaNaWebRequestItens('s', 'p', 'p').request_itens()

    def test_request_itens(self):
        response = self.create_request()
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.text)
        self.assertIsNotNone(response.content)
        self.assertIsNotNone(response.url)
