import unittest

from unittest.mock import patch, Mock
from src.usecase.get_conditioner import GetConditioner


class TestGetConditioner(unittest.TestCase):

    @patch('src.usecase.get_conditioner.ProviderSelector.parse')
    def test_get_conditioner_fail(self, mock_get):
        mock_get.return_value = [None]
        conditioner = GetConditioner().execute()
        self.assertIsNone(conditioner)

    @patch('src.usecase.get_conditioner.ProviderSelector.parse')
    def test_get_conditioner(self, mock_get):

        with open('tests/fixtures/html/beleza.html') as file:
            html = file.read()
        mock_request = Mock()
        mock_request.ok = True
        mock_request.status_code = 200
        mock_request.url = 'www.belezanaweb.com.br'
        mock_request.content = str(html)
        mock_request.text = str(html)

        mock_get.return_value = [mock_request]

        conditioner = GetConditioner().execute()
        self.assertIsNone(conditioner)
