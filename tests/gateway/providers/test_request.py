from unittest.mock import patch
from unittest import TestCase
from src.gateway.providers.request import Request
from src.config.exceptions.page_not_found_exception \
    import PageNotFoundException
from tenacity import RetryError


class TestRequest(TestCase):

    @patch('src.gateway.providers.request.requests.request')
    def test_request(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200

        response = Request('url').request()

        print(response.__dict__)

        self.assertIsNotNone(response, 'Request cannot be null')
        self.assertEqual(response.ok, True, 'Request has to be successfull')
        self.assertEqual(response.status_code, 200,
                         'Request has to be successfull')

    @patch('src.gateway.providers.request.requests.request')
    def test_request_fail(self, mock_get):
        request = Request('url')
        request.request.retry.wait = None
        mock_get.return_value.ok = False
        mock_get.return_value.status_code = 404

        self.assertRaises(RetryError, request.request)
