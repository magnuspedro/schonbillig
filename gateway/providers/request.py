import requests
from config.logger.logging_module import PTLogger
from config.exceptions.page_not_found_exception import PageNotFoundException
from tenacity import retry, stop_after_attempt, wait_fixed
from config.config import Config

logger = PTLogger(name=__name__)


class Request:

    def __init__(self, url: str, method: str = 'GET', headers: str = None,
                 body: str = None, cookies: str = None):
        self.method = method.upper()
        self.url = url
        self.body = body
        self.cookies = cookies or {}
        self.headers = headers or {}

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str) -> str:
        if not isinstance(url, str):
            raise TypeError(
                f'Url must be str or unicode, got {type(url).__name__}')
        self.__url = url

    @retry(stop=stop_after_attempt(Config.REQUEST_RETRY.value),
           wait=wait_fixed(Config.WAITING_TIME.value))
    def request(self) -> requests.Response:

        response = requests.request(
            self.method, self.url, headers=self.headers, cookies=self.cookies)
        logger.info(f'[{response.status_code}] --> Status Code',
                    extra={'mdc': {'status_code': response.status_code,
                                   'url': self.url}})

        if response.status_code != 200:
            raise PageNotFoundException(
                url=response.url, status_code=response.status_code)

        logger.debug('Setting response body')

        self.body = response.content

        logger.info('Request finished with success')

        return response
