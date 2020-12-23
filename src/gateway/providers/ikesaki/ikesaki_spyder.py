from enum import Enum

from requests import Response

from src.config.config import Config
from src.config.exceptions.page_not_found_exception import \
    PageNotFoundException
from src.config.logger.logging_module import PTLogger
from src.gateway.providers.ikesaki.ikesaki_request_itens import \
    IkesakiRequestItems
from src.gateway.providers.ikesaki.strategy.product_selector import \
    ProductSelector
from src.gateway.providers.request import Request
from src.gateway.providers.spyder import Spyder

logger = PTLogger(name=__name__)


class IkesakiSpyder(Spyder):
    source = Config.IKESAKI_BASE_URL.value

    def start_request(self, ref_product: Enum) -> Response:
        product = ProductSelector(ref_product.value).choose_product()
        logger.debug(f'[BelezaNaWeb] Requesting {ref_product.name} ', extra={
            'mdc': {'url': product, 'product': ref_product.name}})

        for requests in IkesakiRequestItems(
                params=Config.IKESAKI_PARAMS.value,
                product=product, source=self.source, ).request_itens():
            yield from self.request_product(requests)

    @staticmethod
    def request_product(requests: list) -> Response:
        for request in requests:
            try:
                response = Request(request).request()
            except PageNotFoundException as e:

                logger.info('The page was not find', extra={
                    'mdc': {'status_code': e.status_code, 'url': e.url}})
                yield
                continue
            if response.ok:
                yield response
