from src.config.logger.logging_module import PTLogger
from src.entities.enum.products import Products
from src.gateway.database.beleza_product import BelezaProduct
from src.entities.enum.converter import Converter
from src.gateway.providers.converter_selector import \
    ConverterSelector
from src.entities.enum.product import Product
from src.entities.enum.provider import Provider
from src.gateway.providers.provider_selector import ProviderSelector

logger = PTLogger(name=__name__)


class GetTreatment:

    @staticmethod
    def execute():
        for product in ProviderSelector(
                Provider.BELEZA_NA_WEB.value).parse(Product.TREATMENT_BELEZA):

            logger.info('Converting request')
            if product:
                product = ConverterSelector(
                    Converter.FINISHER_BELEZA.value).convert(product)
                logger.info(product)
                logger.info('Converted successfully')
                BelezaProduct.insert_product(product, Products.TREATMENT.value)
            else:
                logger.info('Error retriving product, going to the next one')
