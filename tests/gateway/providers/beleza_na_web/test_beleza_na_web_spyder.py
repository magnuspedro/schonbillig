import unittest
from unittest.mock import patch, Mock

from config.exceptions.page_not_found_exception import PageNotFoundException
from gateway.providers.beleza_na_web.beleza_na_web_spyder import \
    BelezaNaWebSpyder


class TestBelezaNaWebSpyder(unittest.TestCase):

    @patch('gateway.providers.beleza_na_web.beleza_na_web_spyder.BelezaNaWebRequestItens.request_itens')
    @patch('gateway.providers.beleza_na_web.beleza_na_web_spyder.Request.request')
    def test_fail_product(self, mock_itens, mock_get):
        mock_get.return_value = ['http://www.belezanaweb.com.br', 'url']

        mock_itens.side_effect = PageNotFoundException()
        response = next(BelezaNaWebSpyder().start_request())
        self.assertIsNone(response)

    @patch('gateway.providers.beleza_na_web.beleza_na_web_spyder.BelezaNaWebRequestItens.request_itens')
    @patch('gateway.providers.beleza_na_web.beleza_na_web_spyder.Request.request')
    def test_individual_product(self, mock_request, mock_get):

        mock_get.return_value = ['http://www.belezanaweb.com.br', 'url']

        mock_request.return_value = Mock()
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.content = "content"

        response = next(BelezaNaWebSpyder().start_request())

        self.assertEqual(response.ok, True)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.content, str)