from src.config.logger.logging_module import PTLogger
from src.entities.bl.compare_product import CompareProduct
from src.entities.enum.products import Products
from src.gateway.database.beleza_product import BelezaProduct
from src.entities.enum.converter import Converter
from src.gateway.providers.converter_selector import \
    ConverterSelector
from src.entities.enum.product import Product
from src.entities.enum.provider import Provider
from src.gateway.providers.provider_selector import ProviderSelector

logger = PTLogger(name=__name__)


class GetShampoo:

    def execute(self):
        # self.ikesaki()
        self.beleza_na_web()

    def ikesaki(self):
        for product in ProviderSelector(
                Provider.IKESAKI.value).parse(Product.SHAMPOO_IKESAKI):
            if product:
                product = ConverterSelector(
                    Converter.SHAMPOO_IKESAKI.value
                ).convert(product)
                logger.info(product)
                logger.info('Converted successfully')
                products = BelezaProduct.find_product(Products.SHAMPOO.value, product.brand)
                result = []
                for prod in products:
                    result.append(f'{CompareProduct.compare(prod["name"], product.name)} - {prod["code"][0]["code"]}')
                result.sort(reverse=True)
                logger.info(f'\n\n\n\n\n\n{result}')
            else:
                logger.info('Error retriving product, going to the next one')

    def beleza_na_web(self):
        for product in ProviderSelector(
                Provider.BELEZA_NA_WEB.value).parse(Product.SHAMPOO_BELEZA):

            logger.info('Converting request')
            if product:
                product = ConverterSelector(
                    Converter.SHAMPOO_BELEZA.value).convert(product)
                logger.info(product)
                logger.info('Converted successfully')
                BelezaProduct.insert_product(product, Products.SHAMPOO.value)
            else:
                logger.info('Error retriving product, going to the next one')
