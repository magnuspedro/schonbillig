from unittest.mock import patch
from unittest import TestCase
from gateway.providers.request import Request


class TestRequest(TestCase):

    @patch('gateway.providers.request.requests.get')
    def test_request(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200

        response = Request('url').request()

        self.assertIsNotNone(response, 'Request cannot be null')
        self.assertEqual(response.ok, 200, 'Request has to be successfull')
        self.assertEqual(response.status_code, 200,
                         'Request has to be successfull')
