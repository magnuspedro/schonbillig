from bs4 import BeautifulSoup

from src.config.exceptions.page_not_found_exception \
    import PageNotFoundException
from src.config.logger.logging_module import PTLogger
from src.gateway.providers.bases.item_request import ItemRequest
from src.gateway.providers.bases.request import Request

logger = PTLogger(name=__name__)


class BelezaNaWebRequestItems(ItemRequest):

    def __init__(self, source: str, params: str, product: str):
        self.source = source
        self.params = params
        self.product = product

    def get_next_url(self, source_page: str) -> str:
        soup = BeautifulSoup(source_page, 'html.parser')
        for button in soup.find_all("button", class_='lazyload'):
            return button.get('data-ajax')

    def get_list_url(self, source_page: str) -> list:
        soup = BeautifulSoup(source_page, 'html.parser')
        return [
            product['href']
            for product in soup.find_all("a", class_='showcase-item-image')
        ]

    def request_itens(self) -> list:
        logger.info("Requesting items")
        try:
            response = Request(
                url=f'{self.source}{self.product}{self.params}').request()
        except PageNotFoundException as e:
            logger.info('The page was not find', extra={
                'mdc': {'status_code': e.status_code, 'url': e.url}})
            response = None
            yield

        while response:

            next_url = self.get_next_url(response.content)

            yield self.get_list_url(response.content)

            if next_url is None:
                break
            try:
                response = Request(url=f'{self.source}{next_url}').request()
            except PageNotFoundException as e:
                logger.info('The page was not find', extra={
                    'mdc': {'status_code': e.status_code, 'url': e.url}})
                break
