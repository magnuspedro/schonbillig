from requests import Session
from bs4 import BeautifulSoup
from logger.logging_module import PTLogger
from ..item_request import ItemRequest
from ..request import Request


logger = PTLogger(name=__name__)


class BelezaNaWebRequestItens(ItemRequest):

    def __init__(self, base_url, params, sub_item, sub_url):
        self.sub_item = sub_item
        self.sub_url = sub_url
        self.base_url = base_url
        self.params = params

    def get_next_url(self, source_page):
        soup = BeautifulSoup(source_page, 'html.parser')
        for button in soup.find_all("button", class_='lazyload'):
            return button.get('data-ajax')

    def get_list_url(self, source_page):
        soup = BeautifulSoup(source_page, 'html.parser')
        urls = []
        for sub_url in soup.find_all("a", class_='showcase-item-image'):
            urls.append(sub_url['href'])

        return urls

    def request_itens(self):
        logger.info("Requesting items")
        urls = []
        # visit item page and scrape button
        response = Request(
            url=self.base_url + self.sub_url + self.params).request()
        while response.ok:
            next_url = self.get_next_url(response.content)

            if next_url is None:
                break

            urls.extend(self.get_list_url(response.content))

            # add item to watch list

            response = Request(url=self.base_url + next_url).request()

            yield urls
