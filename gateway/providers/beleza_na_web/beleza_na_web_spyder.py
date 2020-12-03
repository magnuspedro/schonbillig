from config.config import Config
from config.logger.logging_module import PTLogger

from ..request import Request
from ..spyder import Spyder
from .beleza_na_web_page import BelezaNaWebPage
from .converter.get_shampoo_converter import GetShampooConverter
from .strategy.product_selector import ProductSelector
from .enum.product import Product

logger = PTLogger(name=__name__)


class BelezaNaWebSpyder(Spyder):

    source = Config.BELEZA_BASE_URL.value

    def start_request(self):
        product = ProductSelector(Product.SHAMPOO.value).choose_product()
        for requests in BelezaNaWebPage(product, self.source).start_request():
            for request in requests:
                response = Request(self.source+request).request()
                if response.ok:
                    yield response

    def parse(self):
        for request in self.start_request():
            logger.info('Converting request')
            # TODO: CreateStrategy to choose products
            product = GetShampooConverter().to_entity(request)
            logger.info(product)
            logger.info('Converted successfully')
            yield product
