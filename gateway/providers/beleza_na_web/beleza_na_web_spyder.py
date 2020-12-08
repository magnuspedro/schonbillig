from config.config import Config
from config.exceptions.page_not_found_exception import PageNotFoundException
from config.logger.logging_module import PTLogger
from gateway.providers.beleza_na_web.beleza_na_web_request_itens import \
    BelezaNaWebRequestItens
from gateway.providers.beleza_na_web.enum.product import Product
from gateway.providers.beleza_na_web.strategy.product_selector import \
    ProductSelector
from gateway.providers.request import Request
from gateway.providers.spyder import Spyder
from requests import Response

logger = PTLogger(name=__name__)


class BelezaNaWebSpyder(Spyder):

    source = Config.BELEZA_BASE_URL.value

    def start_request(self) -> Response:
        product = ProductSelector(Product.SHAMPOO.value).choose_product()
        logger.debug('[BelezaNaWeb] ', extra={'mdc': {'url': product}})

        for requests in BelezaNaWebRequestItens(
                params=Config.BELEZA_PARAMAS.value,
                product=product, source=self.source,).request_itens():
            yield from self.request_prodcut(requests)

    def request_prodcut(self, requests: list) -> Response:
        for request in requests:
            try:
                response = Request(self.source+request).request()
            except PageNotFoundException as e:

                logger.info('The page was not find', extra={
                    'mdc': {'status_code': e.status_code, 'url': e.url}})
                yield
                continue
            if response.ok:
                yield response
