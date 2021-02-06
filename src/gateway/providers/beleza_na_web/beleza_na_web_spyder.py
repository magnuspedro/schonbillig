from enum import Enum

from requests import Response

from src.config.config import Config
from src.config.exceptions.page_not_found_exception import PageNotFoundException
from src.config.logger.logging_module import PTLogger
from src.gateway.providers.beleza_na_web.beleza_na_web_request_items import \
    BelezaNaWebRequestItems
from src.gateway.providers.beleza_na_web.products.product_selector import \
    ProductSelector
from src.gateway.providers.bases.request import Request
from src.gateway.providers.bases.spyder import Spyder

logger = PTLogger(name=__name__)


class BelezaNaWebSpyder(Spyder):
    source = Config.BELEZA_BASE_URL.value

    def start_request(self, ref_product: Enum) -> Response:
        product = ProductSelector(ref_product.value).choose_product()
        logger.debug(f'[BelezaNaWeb] Requesting {ref_product.name} ', extra={
            'mdc': {'url': product, 'product': ref_product.name}})

        for requests in BelezaNaWebRequestItems(
                params=Config.BELEZA_PARAMAS.value,
                product=product, source=self.source, ).request_itens():
            yield from self.request_product(requests)

    def request_product(self, requests: list) -> Response:
        for request in requests:
            try:
                response = Request(self.source + request).request()
            except PageNotFoundException as e:

                logger.info('The page was not find', extra={
                    'mdc': {'status_code': e.status_code, 'url': e.url}})
                yield
                continue
            if response.ok:
                yield response
