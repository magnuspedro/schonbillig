from src.gateway.providers.bases.request import Request
from tenacity import RetryError
import pytest


def test_successful_request(requests_mock):
    url = 'https://httpstat.us/200'
    requests_mock.get(url, status_code=200)
    request = Request(method='GET', url=url).request()
    assert request.status_code == 200


def test_fail_request(requests_mock):
    with pytest.raises(RetryError):
        url = 'https://httpstat.us/500'
        requests_mock.get(url, status_code=500)
        request = Request(method='GET', url=url)
        request.request.retry.wait = None
        request.request()
