import unittest

from unittest.mock import patch
from usecase.get_shampoo import GetShampoo


class TestGetShampoo(unittest.TestCase):

    @patch('gateway.providers.request.requests.request')
    def test_get_shampoo(self, mock_get):
        mock_get.return_value.ok = False
        mock_get.return_value.status_code = 404

        shampoo = GetShampoo().execute()
        print(shampoo)

        return shampoo
