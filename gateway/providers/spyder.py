from config.logger.logging_module import PTLogger

from .request import Request

logger = PTLogger(name=__name__)


class Spyder:
    urls: list

    def start_request(self, urls=None):
        if urls is None:
            urls = self.urls
        for url in urls:
            logger.debug(f'[StartRequest]', extra={'mdc': {'url': url}})
            yield Request(url).make_request()

    def parse(self):
        raise NotImplementedError(
            f'{self.__class__.__name__}.parse callback is not defined')
