from request.request import Request
from logger.logging_module import PTLogger
from lxml import html

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

    def follow_link(self, body):
        # TODO: IMPLEMENT
        page = html.fromstring(body)
        page = page.xpath('//a/@href')
        return self.start_request(page)
