import unittest
from unittest.mock import patch
from gateway.providers.beleza_na_web.beleza_na_web_spyder\
    import BelezaNaWebSpyder
from config.exceptions.page_not_found_exception import PageNotFoundException


class TestBelezaNaWebSpyder(unittest.TestCase):

    @patch('gateway.providers.beleza_na_web.beleza_na_web_spyder')
    def test_fail_product(self, mock_exception):
        mock_exception.side_effect = PageNotFoundException(
            url='url', status_code=404)

        response = BelezaNaWebSpyder().start_request()

        self.assertIsNone(response)

    # @patch('gateway.providers.request.requests.request')
    # def test_individual_product(self, mock_get):
    #     mock_get.return_value.ok = True
    #     mock_get.return_value.status_code = 200

    #     response = BelezaNaWebSpyder().start_request()

    #     self.assertIsNone(response)
