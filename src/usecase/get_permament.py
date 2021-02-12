from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Pool

from src.config.config import Config
from src.config.logger.logging_module import PTLogger
from src.entities.enum.products import Products
from src.gateway.database.beleza_product import BelezaProduct
from src.entities.enum.converter import Converter
from src.gateway.providers.converter_selector import \
    ConverterSelector
from src.entities.enum.products_strategy import ProductsStrategy
from src.entities.enum.provider import Provider
from src.gateway.providers.provider_selector import ProviderSelector

logger = PTLogger(name=__name__)


class GetPermanent:

    @staticmethod
    def execute():
        converter = ConverterSelector(Converter.PERMANENT_BELEZA.value)
        products = ProviderSelector(
            Provider.BELEZA_NA_WEB.value).parse(ProductsStrategy.PERMANENT_BELEZA)
        logger.info(f'Number of Products {len(products)}')
        try:
            pool = Pool()
            products = pool.map(converter.convert, products)
        finally:
            logger.info('Products Converted successfully')
            pool.close()
            pool.join()
        with ThreadPoolExecutor(max_workers=Config.REQUEST_MAX_WORKERS.value) as executor:
            process = [executor.submit(
                BelezaProduct.insert_product, product, Products.PERMANENT.value) for product in products]
        logger.info('Sending product to database')
        for task in process:
            task.result()

