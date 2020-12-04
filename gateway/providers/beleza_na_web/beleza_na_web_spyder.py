from config.config import Config
from config.logger.logging_module import PTLogger

from ..request import Request
from ..spyder import Spyder
from .beleza_na_web_page import BelezaNaWebPage
from .converter.strategy.converter import Converter
from .converter.strategy.converter_selector import ConverterSelector
from .enum.product import Product
from .strategy.product_selector import ProductSelector

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
            product = ConverterSelector(
                Converter.SHAMPOO.value).convert(request)
            logger.info(product)
            logger.info('Converted successfully')
            yield product
