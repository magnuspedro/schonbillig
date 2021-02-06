import unittest
from unittest.mock import patch

from src.config.exceptions.page_not_found_exception import PageNotFoundException
from src.gateway.providers.beleza_na_web.beleza_na_web_request_items import \
    BelezaNaWebRequestItems


class TestBelezaNaWebRequestItens(unittest.TestCase):

    @patch(
        'src.gateway.providers.ikesaki.ikesaki_request_itens.Request.request')
    def create_request(self, mock_get):
        with open('tests/fixtures/html/ikesaki_list.html', 'r') as f:
            content = f.read()
            mock_get.return_value.text = content
            mock_get.return_value.content = content
            mock_get.return_value.ok = True
            return next(BelezaNaWebRequestItems('s', 'p', 'p').request_itens())

    @patch(
        'src.gateway.providers.ikesaki.ikesaki_request_itens.Request.request')
    def create_fail_request(self, mock_get):
        mock_get.side_effect = PageNotFoundException(
            url='url',
            status_code=404)
        return next(BelezaNaWebRequestItems('s', 'p', 'p').request_itens())

    def test_request_itens(self):
        response = self.create_request()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)

    def test_request_fail(self):
        response = self.create_fail_request()

        self.assertIsNone(response)
