from src.config.logger.logging_module import PTLogger
from src.entities.enum.products import Products
from src.gateway.database.beleza_product import BelezaProduct
from src.gateway.providers.converter.strategy.converter import Converter
from src.gateway.providers.converter.strategy.converter_selector import \
    ConverterSelector
from src.gateway.providers.product import Product
from src.gateway.providers.strategy.provider import Provider
from src.gateway.providers.strategy.provider_selector import ProviderSelector

from src.gateway.providers.ikesaki.ikesaki_spyder import IkesakiSpyder

logger = PTLogger(name=__name__)


class GetShampoo:

    def execute(self):
        self.ikesaki()
        # self.beleza_na_web()

    def ikesaki(self):
        for product in ProviderSelector(
                Provider.IKESAKI.value).parse(Product.SHAMPOO_IKESAKI):
            if product:
                product = ConverterSelector(
                    Converter.SHAMPOO_IKESAKI.value
                ).convert(product)
                logger.info(product)
                logger.info('Converted successfully')
            else:
                logger.info('Error retriving product, going to the next one')

    def beleza_na_web(self):
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
