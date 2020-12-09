from src.config.exceptions.page_not_found_exception import PageNotFoundException
from src.config.logger.logging_module import PTLogger
from src.entities.enum.products import Products
from src.gateway.database.beleza_product import BelezaProduct
from src.gateway.providers.converter.strategy.converter import Converter
from src.gateway.providers.converter.strategy.converter_selector import \
    ConverterSelector
from src.gateway.providers.product import Product
from src.gateway.providers.strategy.provider import Provider
from src.gateway.providers.strategy.provider_selector import ProviderSelector

logger = PTLogger(name=__name__)


class GetShampoo:

    @staticmethod
    def execute():
        for product in ProviderSelector(
                Provider.BELEZA_NA_WEB.value).parse(Product.SHAMPOO_BELEZA):

            logger.info('Converting request')
            if(product):
                product = ConverterSelector(
                    Converter.SHAMPOO_BELEZA.value).convert(product)
                logger.info(product)
                logger.info('Converted successfully')
                BelezaProduct.insert_product(product, Products.SHAMPOO.value)
            else:
                logger.info('Error retriving product, going to the next one')
