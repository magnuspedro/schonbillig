from config.config import Config
from config.logger.logging_module import PTLogger

from ..request import Request
from ..spyder import Spyder
from .beleza_na_web_page import BelezaNaWebPage
from .enum.product import Product
from .strategy.product_selector import ProductSelector
from config.exceptions.page_not_found_exception \
    import PageNotFoundException

logger = PTLogger(name=__name__)


class BelezaNaWebSpyder(Spyder):

    source = Config.BELEZA_BASE_URL.value

    def start_request(self):
        product = ProductSelector(Product.SHAMPOO.value).choose_product()
        for requests in BelezaNaWebPage(product, self.source).start_request():
            for request in requests:
                # try:

                response = Request(self.source+request).request()

                # except PageNotFoundException as e:

                #     logger.info('The page was not find', extra={
                #         'mdc': {'status_code': e.status_code, 'url': e.url}})
                #     continue

                if response.ok:
                    yield response
