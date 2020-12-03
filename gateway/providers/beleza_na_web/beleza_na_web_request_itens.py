from bs4 import BeautifulSoup
from config.logger.logging_module import PTLogger

from ..item_request import ItemRequest
from ..request import Request

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
        response = Request(
            url=self.source + self.product + self.params).request()
        while response.ok:
            next_url = self.get_next_url(response.content)

            if next_url is None:
                break

            yield self.get_list_url(response.content)

            response = Request(url=self.source + next_url).request()
