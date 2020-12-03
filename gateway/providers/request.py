import requests
from config.logger.logging_module import PTLogger

logger = PTLogger(name=__name__)


class Request:

    def __init__(self, url, method='GET', headers=None, body=None, cookies=None):
        self.method = method.upper()
        self.url = url
        self.body = body
        self.cookies = cookies or {}
        self.headers = headers or {}

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        if not isinstance(url, str):
            raise TypeError(
                f'Request url must be str or unicode, got {type(url).__name__}')
        self.__url = url

    def request(self):

        response = requests.request(
            self.method, self.url, headers=self.headers, cookies=self.cookies)
        logger.info(f'[{response.status_code}] --> Status Code',
                    extra={'mdc': {'status_code': response.status_code, 'url': self.url}})

        if response.status_code != 200:
            raise Exception(response.status_code)

        logger.debug('Setting response body')

        self.body = response.content

        logger.info('Request finished with success')

        return response
