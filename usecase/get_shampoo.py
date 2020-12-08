import pipey

from config.exceptions.page_not_found_exception import PageNotFoundException
from config.logger.logging_module import PTLogger
from gateway.database.beleza_product import BelezaProduct
from gateway.providers.beleza_na_web.converter.strategy.converter import \
    Converter
from gateway.providers.beleza_na_web.converter.strategy.converter_selector import \
    ConverterSelector
from gateway.providers.strategy.provider import Provider
from gateway.providers.strategy.provider_selector import ProviderSelector

logger = PTLogger(name=__name__)


class GetShampoo:

    @staticmethod
    def execute():
        for product in ProviderSelector(
                Provider.BELEZA_NA_WEB.value).parse():

            logger.info('Converting request')
            if(product):
                product = ConverterSelector(
                    Converter.SHAMPOO.value).convert(product)
                logger.info(product)
                logger.info('Converted successfully')
                BelezaProduct.insert_product(product)
            else:
                logger.info('Error retriving product, going to the next one')
