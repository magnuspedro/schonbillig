from bs4 import BeautifulSoup
from config.logger.logging_module import PTLogger

from gateway.providers.item_request import ItemRequest
from gateway.providers.request import Request
from config.exceptions.page_not_found_exception \
    import PageNotFoundException

logger = PTLogger(name=__name__)


class BelezaNaWebRequestItens(ItemRequest):

    def __init__(self, source, params, product):
        self.source = source
        self.params = params
        self.product = product

    def get_next_url(self, source_page):
        soup = BeautifulSoup(source_page, 'html.parser')
        for button in soup.find_all("button", class_='lazyload'):
            return button.get('data-ajax')

    def get_list_url(self, source_page):
        soup = BeautifulSoup(source_page, 'html.parser')
        return [
            product['href']
            for product in soup.find_all("a", class_='showcase-item-image')
        ]

    def request_itens(self):
        logger.info("Requesting items")
        # try:
        response = Request(
            url=self.source + self.product + self.params).request()
        # except PageNotFoundException as e:
        #     logger.info('The page was not find', extra={
        #         'mdc': {'status_code': e.status_code, 'url': e.url}})
        #     return

        while response:

            next_url = self.get_next_url(response.content)

            yield self.get_list_url(response.content)

            if next_url is None:
                break
            # try:
            response = Request(url=self.source + next_url).request()
            # except PageNotFoundException as e:
            #     logger.info('The page was not find', extra={
            #         'mdc': {'status_code': e.status_code, 'url': e.url}})
            #     return
